<a href='https://ko-fi.com/O4O3W3IIA' target='_blank'>
  <img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi5.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' />
</a>

# 🔍 Subdomain Takeover Scanner

## 📝 Descripción

Subdomain Takeover Scanner es una herramienta de línea de comandos escrita en Python diseñada para identificar y verificar posibles vulnerabilidades de subdomain takeover en un dominio específico. Utiliza herramientas de terceros como `subfinder` y `subzy` para realizar estas tareas. La herramienta está diseñada para ser fácil de usar y se encarga de la instalación de dependencias necesarias, como Go, si no están presentes en el sistema.

## ✨ Características

- **Detección de Subdominios:** Utiliza `subfinder` para encontrar subdominios de un dominio dado.
- **Verificación de Subdominios:** Utiliza `subzy` para verificar la disponibilidad de los subdominios encontrados y detectar posibles vulnerabilidades de subdomain takeover.
- **Instalación Automática de Dependencias:** Instala automáticamente Go y las herramientas necesarias si no están presentes en el sistema.
- **Compatibilidad Multiplataforma:** Soporta sistemas operativos Windows y Linux.
- **Interfaz de Usuario Amigable:** Proporciona una interfaz de línea de comandos sencilla y guiada.

## 🛠️ Requisitos

- Python 3.x
- Conexión a Internet para la instalación de dependencias

## 📥 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/subdomain-takeover-scanner.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd subdomain-takeover-scanner
   ```
3. Ejecuta el script:
   ```bash
   python3 subdomain_takeover_scanner.py
   ```

## 🔧 Uso

1. Ejecuta el script:
   ```bash
   python3 subdomain_takeover_scanner.py
   ```
2. Sigue las instrucciones en pantalla para instalar Go y las herramientas necesarias si no están presentes.
3. Introduce el dominio que deseas escanear cuando se te solicite.
4. La herramienta buscará y verificará los subdominios automáticamente, identificando posibles vulnerabilidades de subdomain takeover.

## 🎯 Público Objetivo

- **Profesionales de Ciberseguridad:** Para identificar y verificar subdominios como parte de auditorías de seguridad.
- **Administradores de Sistemas:** Para gestionar y asegurar los subdominios de sus dominios.
- **Investigadores de Seguridad:** Para realizar análisis de seguridad en dominios específicos.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejoras o correcciones.

## 📜 Licencia

Este proyecto está bajo la Licencia GNU GPL v3.0. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por usar Subdomain Takeover Scanner! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos. 😊

---

**Nota:** Esta herramienta es compatible tanto para Windows como para Linux.
