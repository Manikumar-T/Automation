#!/usr/bin/python3
from datetime import datetime
from datetime import date
import subprocess as sp
import  psutil,os,json

battery = psutil.sensors_battery()
os.system("journalctl -b --user-unit pulseaudio -g \"Battery Level\" -r -n 1 -o json > info.json")
blue_stat="Not connected"
try:
    f = open("info.json")
    data= json.load(f)
except:
    blue_stat="no bluetooth connect after boot"
blue_con=sp.getoutput("hcitool con").split()

print("\tSystem  info\t\t\t\tBluetooth info ")
print("\t============\t\t\t\t===============")

print("Battery percentage: ",int(battery.percent),"%",end="\t\t",sep="")
#check the bluetooth Devices connection status
if(len(blue_con)!=1):
    print("\t",data['MESSAGE'],end="")
    if("8C:64:A2:6D:25:B3" in blue_con):
        blue_stat="Mani's oneplus"
    else:
        blue_stat="unknow device"
print("\nCharging state: ","Charging" if battery.power_plugged==True else "discharging",end="")
print("\t\t Bluetooth Device: ",blue_stat)
hrs=int(datetime.now().strftime("%H"))%12
print("\n \t\tTime: ",hrs,datetime.now().strftime(":%M:%S"),sep="",end="")
print("\tDate: ",date.today())

print("\t\t\twifi info")
print("\t\t\t=========")
print(sp.getoutput("nmcli dev stat"))
