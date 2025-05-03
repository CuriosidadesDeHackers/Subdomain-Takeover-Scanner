
<a href='https://ko-fi.com/O4O3W3IIA' target='_blank'>
  <img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi5.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' />
</a>

# 🔍 Subdomain Takeover Scanner

## 📝 Descripción

Subdomain Takeover Scanner es una herramienta de línea de comandos escrita en Python diseñada para identificar y verificar posibles vulnerabilidades de subdomain takeover en un dominio específico. Utiliza herramientas de terceros como `subfinder` y `subzy` para realizar estas tareas. La herramienta está diseñada para ser fácil de usar y se encarga de la instalación de dependencias necesarias, como Go, si no están presentes en el sistema.

## ✨ Características

- **Detección de Subdominios:** Utiliza `subfinder` para encontrar subdominios de un dominio dado.
- **Verificación de Subdominios:** Utiliza `subzy` para verificar la disponibilidad de los subdominios encontrados y detectar posibles vulnerabilidades de subdomain takeover.
- **Extracción de URLs:** Utiliza `waybackurls` para extraer URLs de los subdominios encontrados.
- **Instalación Automática de Dependencias:** Instala automáticamente Go y las herramientas necesarias si no están presentes en el sistema.
- **Compatibilidad Multiplataforma:** Soporta sistemas operativos Windows y Linux.
- **Interfaz de Usuario Amigable:** Proporciona una interfaz de línea de comandos sencilla y guiada.
- **Opciones Avanzadas:** Permite al usuario decidir si desea extraer subdominios del dominio principal o directamente extraer URLs del dominio principal.
- **Limpieza de URLs:** Si el usuario no desea escanear subdominios, la herramienta elimina todo lo que hay entre `://` y el punto antes del dominio dado en el archivo de URLs.

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
5. La herramienta preguntará si deseas extraer subdominios del dominio principal o directamente extraer URLs del dominio principal.

## 🎯 Público Objetivo

- **Profesionales de Ciberseguridad:** Para identificar y verificar subdominios como parte de auditorías de seguridad.
- **Administradores de Sistemas:** Para gestionar y asegurar los subdominios de sus dominios.
- **Investigadores de Seguridad:** Para realizar análisis de seguridad en dominios específicos.

## 📸 Demo

Búsqueda de Subdominios y URLs junto con prueba de posible subdomain takeover.
![image](https://github.com/user-attachments/assets/39f3a4c6-0483-4126-a2f1-ad37e33cec3e)

Búsqueda de solo URLs junto con prueba de posible subdomain takeover.
![image](https://github.com/user-attachments/assets/2dd487b3-c685-42f8-bca8-976607502682)

Búsqueda de solo Subdominios junto con prueba de posible subdomain takeover.
![image](https://github.com/user-attachments/assets/2468d307-008f-45a5-8a2b-669fc58160cf)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejoras o correcciones.

## 📜 Licencia

Este proyecto está bajo la Licencia GNU GPL v3.0. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por usar Subdomain Takeover Scanner! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos. 😊

---

**Nota:** Esta herramienta es compatible tanto para Windows como para Linux.
