# LiSP_0_5-Midas-osc
Simple script to send OSC mesages using python and python-osc 

OSC mesages has been added in linux show player 0.6 but found it not very stable. So made a very simple script to send it using python in Linux Show Player.

Usage:

To use this program first argv  is ip address of the midas
argv 2 is the port (Default 10023 to control)
argv 3 is your osc adr
argv 4 is int of float (i, f)
argv 5 is your msg

a int mesage:
MidasSend.py ip_adress port /ch/01/mix/on i 0
a float mesage:
MidasSend.py ip_adress port /ch/01/mix/fader f 0.5

It is terible writen and should not be used if you don't know how it works.
I use it for a Midas m32, but should be posible to be used for any OSC device.

