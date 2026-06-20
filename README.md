# python-intro
Repositorio para estudiar Python

[Inicio del plan de estudio: 21/06/2025]

Este repositorio está clonado en los siguientes equipos: 
- Notebook/trabajo: ARG-PF33XZ9F - SO: Ubuntu 24.04 (WSL)
- Servidor/LAB: doc-srv-gen-01 - SO: Fedora 44 (Server Edition) 
- Servidor/LAB: doc-srv-gen-02 - SO: Debian 13 (trixie)
- Servidor/LAB: doc-srv-gen-03 - SO: Debian 13 (trixie)

Se ha reorganizado el código, creando el directorio: python-intro/code.
Se ha configurado el entorno virtual python-intro/venv, en cada equipo.
Se ha cambiado la conexión a SSH mediante clave privada/pública.
Se ha configurado git eliminando la opción "credential.helper -> store" en todos los equipos.

[Reoganización del entorno virtual en python-intro/venv: 18/05/2026]
Se reorganiza el entorno virtual en el directorio python-intro/venv.

[Clonación mediante SSH del repositorio en todos los equipos: 24/05/2026] 
Se ha clonado el repositorio en: doc-srv-gen-01, doc-srv-gen-02, doc-srv-gen-03 y ARG-PF33XZ9F.

[Migración del segmento de red en el Laboratorio: 12/06/2026]
Se ha migrado el segmento de red del laboratorio de 192.168.100.0/24 a 192.168.1.0/24:
doc-srv-gen-01: 192.168.100.30 -> 192.168.1.30
doc-srv-gen-02: 192.168.100.31 -> 192.168.1.31
doc-srv-gen-03: 192.168.100.36 -> 192.168.1.36
