1/26/2025

1) When you boot jetson, select ubuntu as user
2) Set datetime with
    sudo date --set "20 Jan 2025 20:15"
3) Become tim
    sudo su - tim
    cd /home/tim/github/stargazing/production
4) sudo python2.7 -O morse_gui.py

And youre off

The -O puts it in debugging mode and in the code it will use the GPIO when in debugging mode

Also set the printer to 5.5 inches for page length and cut length
 
Also I found these commands that root did once

   15  echo 57 > /sys/class/gpio/export
   16  echo out > /sys/class/gpio/gpio57/direction
   17  echo 1 > /sys/class/gpio/gpio57/value
   18  echo 0 > /sys/class/gpio/gpio57/value
   19  echo 57 > /sys/class/gpio/unexport

they look like someway to send signals to GPIO from the CL

