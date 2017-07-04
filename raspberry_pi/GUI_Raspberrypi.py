###############################################
####         Apuntes 2017/06/27             ###
####    IoT linux Modo Grafico parte 2      ###

1. Sistema con modo gráfico (linux)
2. Desactivar modo gráfico
# Administrar los servicios, deshabilitar modo gráfico para que no se active cuando inicia en modo 5.
sudo systemctl disable lightdm
sudo systemctl stop lightdm

3. Agregar script para ejecutar juego

vi ~/.bashrc
# modo X,  en background "&"
sudo X &
Export display=:0
# cambiar a directorio
cd /home/pi/test
# Ejecutar programa
python test.py

###############################################
####         Solución Alternativa           ###

1. Sistema con modo gráfico (linux)
# pi (automatic login)

2. Desactivar modo gráfico

# alternativa 5 (ok) - default-display-manager 
##############################################
 vi  /etc/X11/default-display-manager 
 /usr/bin/lightdm stop 

# Si presenta error al guardar, usar :w !sudo tee % > /dev/null
# Nota: para iniciar modo gráfico lightdm start 
 
3. Agregar linea para ejecutar juego

# Editar Archivo
cd /home/
vi ~/.bashrc

# Agregar línea
python /home/pi/python_games/wormy.py

4. Ambiente

Probado en: 
Imagen: https://www.raspberrypi.org/downloads/raspbian/
Emulador: http://qemu.weilnetz.de/w32/2017/
Kernel: https://github.com/dhruvvyas90/qemu-rpi-kernel/blob/master/kernel-qemu-4.4.34-jessie

#############################################
Otros Apuntes:

# Ver archivos ocultos
ls -la ~/ | more

# Modo texto
sudo init 3

# cambiar pantalla
Alt + f1 

# log nuevos eventos
tail -f /var/log/syslog 

# rc analogó a las x init.
ls -l | grep rc

# Escritorios Ctrl + Alt + F#
# Envíar a escritorio 
Export DISPLAY=:0

# Envia programa a background
nombrePrograma &

# ver archivos ejecutandose
jobs 

# matar primer job
kill %1

# Escritorio remoto
# VNC 

# ver numeración vi
Set nu

# matar procesos
kill -9 

#####################################
# Siguiente paso Esconder el booteo #
#####################################

#####################################
# Otros intentos
# Editar

vi ~/.bashrc
# inicie, modo #& en background
sudo X &
# exportar display
Export display=:0
# cambiar a directorio
cd /home/pi/test
python /home/pi/python_games/wormy.py
# Ejecutar programa
python test.py
python wormy.py

# Error, el sistema deja de reconoce el teclado

2. Desactivar modo gráfico

# alternativa 1 - (error)
# Administrar los servicios, deshabilitar modo gráfico para que no se active cuando inicia en modo 5.
sudo systemctl disable lightdm
sudo systemctl stop lightdm

##############################################
# en init 3, configurar inicio, para que pida login

# alternativa 3, modificar Grub Archivo no encontrado
##############################################
# vi /etc/default/grub
DEFAULT = "text"

# alternativa 4 () Archivo no encontrado
##############################################
# vi /etc/default/grub


#####################################
# Refencias: 
# Ejecutar .bashrc? https://askubuntu.com/a/127059
# Guardar default-display-manager  https://stackoverflow.com/a/8253435/4564845