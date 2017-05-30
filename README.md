# HeyRemember-Python

**English**

Python script for sending notifications with messages stored in a local sqlite database.

**ENG: WARNING: This system  works only on Windows10**

## Requirements
They need to be installed in that order, because `pypiwin32` is used by` win10toast`
```
pip install pypiwin32
pip install win10toast
```
In case you can not install `win10toast` via pip, you can do it manually by downloading or cloning the creator's repository ([Windows 10 toast notifications](https://github.com/jithurjacob/Windows-10-Toast-Notifications)), version 0.8 of this repository at the time I downloaded it had a problem with the `requirements.txt` file, what I did to fix it was to modify `setup.py` and remove the requirements for installation, then I installed it manually with` setup.py install` and I was able to install it correctly.

## Workflow

This script what it does to general features is to take the information from a local database and display it as toast notifications.

### Set up

```
DB_PATH = 'persistence/recordatorios.db'			# Local database path
ICON = 'icon.ico' 						# Path of the icon to be displayed upon notification
NOTIFICATION_DURATION = 5*60 # 5 minutes 			# How long the notification available in the tray will last
NOTIFICATION_INTERVAL = 30*60 # 20 minutes 			# Time between notification and notification
```

> NOTICE: The time `NOTIFICATION_INTERVAL` start counting after the `NOTIFICATION_DURATION` time expires


**Español**

Python script para el envío de notificaciones con mensajes almacenados en una base de datos sqlite.

**ADVERTENCIA: Este sistema sólo funciona en Windows10**

## Requisitos
Es necesario que se instalen en ese orden, debido a que `pypiwin32` es usada por `win10toast`
```
pip install pypiwin32
pip install win10toast
```
En caso de que no se pueda instalar `win10toast` a través de pip, se puede hacer de forma manual descargando o clonando el repositorio del creador ([Windows 10 toast notifications](https://github.com/jithurjacob/Windows-10-Toast-Notifications)), la versión 0.8 de este repositorio en el momento en el que lo descargué tenía un problema con el archivo `requirements.txt`, lo que hice para solucionarlo fue modificar el `setup.py` y quitarle los requerimientos para instalación, luego la instalé manualmente con `setup.py install` y ya pude instalarlo correctamente.

## Flujo de trabajo

Este script lo que hace a rasgos generales es tomar la información de una base de datos locale y mostrarla como notificaciones toast.

### Configurar

```
DB_PATH = 'persistence/recordatorios.db'			# Ruta de la base de datos local
ICON = 'icon.ico' 						# Ruta del ícono que se mostrará al salir la notificación
NOTIFICATION_DURATION = 5*60 # 5 minutes 			# Tiempo que durará la notificación disponible en la bandeja
NOTIFICATION_INTERVAL = 30*60 # 20 minutes 			# Tiempo de espera entre notificación y notificación
```

> NOTA: El tiempo `NOTIFICATION_INTERVAL` empieza a contar luego de que se acabe el tiempo `NOTIFICATION_DURATION`

Icons made by <a href="http://www.flaticon.com/authors/dinosoftlabs" title="DinosoftLabs">DinosoftLabs</a> from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a>
