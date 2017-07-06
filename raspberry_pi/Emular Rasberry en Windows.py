0) Tutorial: https://www.youtube.com/watch?v=xiQX0YXYuqU
1) Emulador: http://qemu.weilnetz.de/w32/2017/
2) Kernel: https://github.com/dhruvvyas90/qemu-rpi-kernel/blob/master/kernel-qemu-4.4.34-jessie
3) Imagen: https://www.raspberrypi.org/downloads/raspbian/

4) start.bat
qemu-system-arm -kernel kernel-qemu-4.4.34-jessie -cpu arm1176 -m 256 -M versatilepb -no-reboot -serial stdio -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw init=/bin/bash" -drive "file=2017-06-21-raspbian-jessie.img,index=0,media=disk,format=raw" -redir tcp:2222::22

5) Kernel
sudo nano /etc/udev/rules.d/90-qemu.rules

KERNEL=="sda", SYMLINK+="mmcblk0"
KERNEL=="sda?", SYMLINK+="mmcblk0p%n"
KERNEL=="sda2", SYMLINK+="root"

Save Ctrl + x

# Restart
sudo shutdown -h

# Error

# remover init=/bin/bash from start.bat to stop the emulator
qemu-system-arm -kernel kernel-qemu-4.4.34-jessie -cpu arm1176 -m 256 -M versatilepb -no-reboot -serial stdio -append "root=/dev/sda2 panic=1 rootfstype=ext4 rw" -drive "file=2017-06-21-raspbian-jessie.img,index=0,media=disk,format=raw" -redir tcp:2222::22

# Agregar 2 GB más de espacio

qemu-img.exe resize 2017-06-21-raspbian-jessie.img +2G

###############################################
# Expandir el disco
sudo fdisk/div/sdi

# Ver particiones
p

# Borrar "Delete"
D

# Elegir paticion
2

# New
N

# Primary
p 

# Start in end first partition + 1
134567

# Write
w


# shotdown

Errororrororooror




###############################################
# 
sudo resize2fs /dev/sda2

# Expandir Swap A CON_SWAPFILE 1024
sudo nano /etc/dphys-swapgile

# Reiniciar servicio
sudo /etc/init.d/dphys-swapgile stop
sudo /etc/init.d/dphys-swapgile start
free -m

###############################################
#
Rasperry py configuration
enable SSH
performance Turbo 1000 meghertz

### ingresar con putty 127.0.0.1:2222