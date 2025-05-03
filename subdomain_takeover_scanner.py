#!/usr/bin/env python3
import os
import subprocess
import sys
import platform
import requests
from colorama import Fore, Style, init
import shutil
import time

# Inicializar colorama
init(autoreset=True)

# Configuración global
GO_INSTALL_PATHS = {
    'Windows': [
        r"C:\Program Files\Go\bin\go.exe",
        r"C:\Go\bin\go.exe",
        os.path.expanduser(r"~\go\bin\go.exe")
    ],
    'Linux': [
        "/usr/local/go/bin/go",
        "/usr/bin/go",
        os.path.expanduser("~/.go/bin/go"),
        os.path.expanduser("~/go/bin/go")
    ]
}

class SubdomainScanner:
    def __init__(self):
        self.system = platform.system()
        self.tools = {
            'subfinder': {
                'install': 'go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest',
                'test_cmd': ['-version']
            },
            'subzy': {
                'install': 'go install -v github.com/PentestPad/subzy@latest',
                'test_cmd': ['version']
            },
            'waybackurls': {
                'install': 'go install github.com/tomnomnom/waybackurls@latest',
                'test_cmd': ['-version']
            }
        }

    def clear_screen(self):
        """Limpia la pantalla según el SO."""
        os.system('cls' if self.system == 'Windows' else 'clear')

    def run_command(self, command, error_msg=None, show_output=True):
        """Ejecuta un comando con manejo de errores."""
        try:
            result = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout.strip() if result.stdout else ""
        except subprocess.CalledProcessError as e:
            if error_msg:
                print(Fore.RED + f"{error_msg}: {e.stderr if e.stderr else str(e)}")
            return None

    def get_go_path(self):
        """Obtiene la ruta de instalación de Go."""
        # Primero verificar si está en PATH
        go_path = shutil.which('go')
        if go_path:
            return go_path

        # Buscar en rutas comunes
        for path in GO_INSTALL_PATHS.get(self.system, []):
            if os.path.exists(path):
                return path

        return None

    def install_go(self):
        """Instala Go en el sistema."""
        print(Fore.YELLOW + "Instalando Go...")

        try:
            if self.system == 'Windows':
                # Instalación para Windows
                version = requests.get("https://go.dev/dl/?mode=json").json()[0]['version'][2:]
                url = f"https://go.dev/dl/go{version}.windows-amd64.msi"
                subprocess.run([
                    "powershell", "-Command",
                    f"Invoke-WebRequest -Uri '{url}' -OutFile go_installer.msi"
                ], check=True)
                subprocess.run(["msiexec", "/i", "go_installer.msi", "/quiet"], check=True)
                os.remove("go_installer.msi")
                print(Fore.GREEN + "Go instalado. Reinicia tu terminal.")
            else:
                # Instalación para Linux
                print(Fore.CYAN + "Instalando dependencias...")
                self.run_command(
                    ['sudo', 'apt-get', 'update'],
                    "Error al actualizar paquetes"
                )
                self.run_command(
                    ['sudo', 'apt-get', 'install', '-y', 'wget', 'tar', 'git'],
                    "Error al instalar dependencias"
                )

                version = requests.get("https://go.dev/dl/?mode=json").json()[0]['version'][2:]
                self.run_command(
                    ['wget', f"https://go.dev/dl/go{version}.linux-amd64.tar.gz"],
                    "Error al descargar Go"
                )
                self.run_command(
                    ['sudo', 'tar', '-C', '/usr/local', '-xzf', f"go{version}.linux-amd64.tar.gz"],
                    "Error al extraer Go"
                )
                os.remove(f"go{version}.linux-amd64.tar.gz")

                # Configurar PATH
                with open(os.path.expanduser("~/.bashrc"), "a") as f:
                    f.write('\nexport PATH=$PATH:/usr/local/go/bin\n')

                print(Fore.GREEN + "Go instalado. Ejecuta 'source ~/.bashrc' o reinicia tu terminal.")

            return True
        except Exception as e:
            print(Fore.RED + f"Error durante la instalación: {str(e)}")
            return False

    def check_tool(self, name):
        """Verifica si una herramienta está instalada."""
        tool_path = shutil.which(name)
        if tool_path:
            return tool_path

        # Verificar en GOPATH/bin
        go_bin = os.path.expanduser("~/go/bin")
        tool_path = os.path.join(go_bin, name)
        if os.path.exists(tool_path):
            return tool_path

        return None

    def install_tool(self, name):
        """Instala una herramienta de Go."""
        print(Fore.YELLOW + f"Instalando {name}...")
        if not self.run_command(
            self.tools[name]['install'].split(),
            f"Error al instalar {name}",
            show_output=False
        ):
            return False

        # Verificar instalación
        tool_path = self.check_tool(name)
        if not tool_path:
            print(Fore.RED + f"{name} no se instaló correctamente")
            return False

        print(Fore.GREEN + f"{name} instalado en: {tool_path}")
        return True

    def run_subfinder(self, domain):
        """Ejecuta subfinder para encontrar subdominios."""
        output_file = f"{domain}_subdomains.txt"
        tool_path = self.check_tool('subfinder')

        print(Fore.CYAN + "\n[+] Subdominios encontrados:\n" + Fore.RESET)

        # Ejecutar subfinder y mostrar resultados en tiempo real
        try:
            process = subprocess.Popen(
                [tool_path, "-d", domain],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            subdomains = set()
            for line in process.stdout:
                subdomain = line.strip()
                if subdomain:  # Solo si no está vacío
                    print(subdomain)
                    subdomains.add(subdomain)

            # Esperar a que termine el proceso
            process.wait()

            if process.returncode != 0:
                error = process.stderr.read()
                print(Fore.RED + f"Error al ejecutar subfinder: {error}")
                return None

            # Guardar resultados en archivo
            with open(output_file, 'w') as f:
                f.write('\n'.join(sorted(subdomains)))

            print(Fore.GREEN + f"\n[+] Total de subdominios encontrados: {len(subdomains)}")
            print(Fore.GREEN + f"[+] Resultados guardados en: {output_file}")

            return output_file

        except Exception as e:
            print(Fore.RED + f"Error al ejecutar subfinder: {str(e)}")
            return None

    def run_waybackurls(self, subdomain):
        """Ejecuta waybackurls para extraer URLs de un subdominio."""
        tool_path = self.check_tool('waybackurls')
        if not tool_path:
            return []

        output = self.run_command([tool_path, subdomain], show_output=False)
        return output.splitlines() if output else []

    def process_subdomains(self, subdomains_file):
        """Procesa cada subdominio con waybackurls y combina los resultados."""
        urls_file = subdomains_file.replace("_subdomains.txt", "_urls.txt")
        with open(subdomains_file, 'r') as file:
            subdomains = [s.strip() for s in file.readlines() if s.strip()]

        all_urls = []
        total = len(subdomains)

        print(Fore.CYAN + f"\n[+] Procesando {total} subdominios...\n")

        for i, subdomain in enumerate(subdomains, 1):
            print(Fore.BLUE + f"[{i}/{total}] Extrayendo URLs para {subdomain}...")
            urls = self.run_waybackurls(subdomain)
            if urls:
                all_urls.extend(urls)
                print(Fore.GREEN + f"  → Encontradas {len(urls)} URLs")

        # Escribir resultados (solo URLs únicas)
        unique_urls = set(all_urls)
        with open(urls_file, 'w') as file:
            file.write("\n".join(unique_urls) + "\n")

        print(Fore.GREEN + f"\n[+] Total de URLs únicas encontradas: {len(unique_urls)}")
        print(Fore.GREEN + f"[+] Resultados guardados en: {urls_file}")

        return urls_file

    def run_waybackurls_for_domain(self, domain):
        """Ejecuta waybackurls para extraer URLs del dominio principal."""
        tool_path = self.check_tool('waybackurls')
        output_file = f"{domain}_urls.txt"
        output = self.run_command([tool_path, domain], show_output=False)
        if output:
            with open(output_file, 'w') as file:
                file.write(output)
            return output_file
        return None

    def clean_urls_file(self, urls_file, domain):
        """Elimina todo lo que hay entre :// y el punto antes del dominio dado en el archivo de URLs."""
        cleaned_urls = []
        with open(urls_file, 'r') as file:
            for line in file:
                url = line.strip()
                if domain in url:
                    prefix, suffix = url.split(f"://", 1)
                    domain_index = suffix.find(f".{domain}")
                    if domain_index != -1:
                        cleaned_url = f"{prefix}://{suffix[domain_index+1:]}"
                        cleaned_urls.append(cleaned_url)
                    else:
                        cleaned_urls.append(url)
                else:
                    cleaned_urls.append(url)

        with open(urls_file, 'w') as file:
            file.write("\n".join(cleaned_urls) + "\n")

        print(Fore.GREEN + f"\n[+] Archivo de URLs limpiado: {urls_file}")

    def run_subzy(self, input_file):
        """Ejecuta subzy para verificar subdominios."""
        tool_path = self.check_tool('subzy')

        try:
            process = subprocess.Popen(
                [tool_path, "run", "--targets", input_file, "--hide_fails"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            for line in process.stdout:
                print(line, end='')  # Imprimir la salida en tiempo real

            # Esperar a que termine el proceso
            process.wait()

            if process.returncode != 0:
                error = process.stderr.read()
                print(Fore.RED + f"Error al ejecutar subzy: {error}")
                return None

            return True

        except Exception as e:
            print(Fore.RED + f"Error al ejecutar subzy: {str(e)}")
            return None

    def main(self):
        self.clear_screen()
        print(Fore.CYAN + r"""
 _____       _         _                       _         _____     _                              _____                                
/  ___|     | |       | |                     (_)       |_   _|   | |                            /  ___|                                
\ `--. _   _| |__   __| | ___  _ __ ___   __ _ _ _ __     | | __ _| | _____  _____   _____ _ __  \ `--.  ___ __ _ _ __  _ __   ___ _ __
 `--. \ | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \    | |/ _` | |/ / _ \/ _ \ \ / / _ \ '__|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
/\__/ / |_| | |_) | (_| | (_) | | | | | | (_| | | | | |   | | (_| |   <  __/ (_) \ V /  __/ |    /\__/ / (_| (_| | | | | | | |  __/ |
\____/ \__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|   \_/\__,_|_|\_\___|\___/ \_/ \___|_|    \____/ \___\__,_|_| |_|_| |_|\___|_|

""")
        print(Fore.BLUE + "creado por CuriosidadesDeHackers\n")

        # Verificar Go
        go_path = self.get_go_path()
        if not go_path:
            print(Fore.RED + "Go no está instalado")
            if input(Fore.YELLOW + "¿Instalar Go? (s/n): ").lower() == 's':
                if not self.install_go():
                    sys.exit(1)
                print(Fore.YELLOW + "Por favor reinicia el script después de instalar Go")
                sys.exit(0)
            else:
                sys.exit(1)
        else:
            print(Fore.GREEN + f"Go encontrado en: {go_path}")

        # Verificar/instalar herramientas
        for tool in self.tools:
            if not self.check_tool(tool):
                print(Fore.RED + f"{tool} no está instalado")
                if input(Fore.YELLOW + f"¿Instalar {tool}? (s/n): ").lower() == 's':
                    if not self.install_tool(tool):
                        sys.exit(1)
                else:
                    sys.exit(1)
            else:
                print(Fore.GREEN + f"{tool} encontrado en: {self.check_tool(tool)}")

        # Obtener dominio
        domain = input(Fore.CYAN + "\nIntroduce el dominio a escanear: ").strip()
        if not domain:
            print(Fore.RED + "Dominio no válido")
            sys.exit(1)

        # Preguntar si se desea extraer subdominios
        if input(Fore.YELLOW + "\n¿Deseas extraer los subdominios del dominio principal? (s/n): ").lower() == 's':
            print(Fore.BLUE + "\n[+] Buscando subdominios...")
            subdomains_file = self.run_subfinder(domain)
            if not subdomains_file:
                sys.exit(1)

            # Mostrar contenido del archivo de subdominios
            with open(subdomains_file, 'r') as f:
                subdomains = f.read().splitlines()

            # Preguntar si se desea extraer URLs
            if input(Fore.YELLOW + "\n¿Deseas extraer todas las URLs de los subdominios encontrados? (s/n): ").lower() == 's':
                urls_file = self.process_subdomains(subdomains_file)
            else:
                urls_file = subdomains_file
        else:
            # Extraer URLs del dominio principal
            print(Fore.BLUE + "\n[+] Extrayendo URLs del dominio principal...")
            urls_file = self.run_waybackurls_for_domain(domain)
            if not urls_file:
                sys.exit(1)

            # Limpiar el archivo de URLs
            self.clean_urls_file(urls_file, domain)

        # Verificar subdominios con subzy
        print(Fore.BLUE + "\n[+] Verificando subdominios en busca de subdomain takeover")
        if not self.run_subzy(urls_file):
            sys.exit(1)

        print(Fore.GREEN + "\n[+] Escaneo completado con éxito")

if __name__ == "__main__":
    scanner = SubdomainScanner()
    scanner.main()
