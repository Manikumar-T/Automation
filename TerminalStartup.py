#!/usr/bin/python3
from datetime import datetime
from datetime import date
import subprocess as sp
import  psutil,os,json

from table2ascii import table2ascii, Merge, PresetStyle
#Get user name
user_name = os.getlogin()
#Get System Battery level
battery = psutil.sensors_battery()
#System call for journalctl to read bluetooth device info
os.system("journalctl -b --user-unit pulseaudio -g \"Battery Level\" -r -n 1 -o json > /home/"+user_name+"/info.json")
#Default Values 
blue_stat="Not connected"
blu_BLevel="-"
blu_DName ="Not connected"

#Read the Bluetooth device info from info.json file
try:
    f = open("/home/"+user_name+"/info.json")
    data= json.load(f)
except:
    data={}
    blue_stat="Not connected"


##Get the bluetooth device deatails using bluetoothctl
blue_con=sp.getoutput("bluetoothctl info").split("\n")

# Device Battery Info data
batteryPercentage =str(int(battery.percent))+"%"
chargingStatus = "Charging" if battery.power_plugged==True else "discharging"

#check the bluetooth Devices connection status and data
if(len(blue_con)!=2 and data!={}):
    blu_BLevel = data["MESSAGE"].split(":")[1]
    blu_DName = blue_con[1].split(": ")[1]

#Get the time
time=str(int(datetime.now().strftime("%H"))%12)+datetime.now().strftime(":%M:%S")

#Get network Device data
wifi = sp.getoutput("nmcli dev status | grep wifi ")
LAN = sp.getoutput("nmcli dev status | grep ethernet")


#Create Table form of data
output = table2ascii(
    header=["System Info",Merge.LEFT,"Bluetooth Info",Merge.LEFT],
    body=[
        ["Battery Level",batteryPercentage,"Battery Level",blu_BLevel],
        ["Charging state",chargingStatus,"Device Name",blu_DName],
        ["Time",time,"",Merge.LEFT],
        ["Data",date.today(),"",Merge.LEFT],
        ["Network Info",Merge.LEFT,Merge.LEFT,Merge.LEFT],
        [wifi,Merge.LEFT,Merge.LEFT,Merge.LEFT],
        [LAN,Merge.LEFT,Merge.LEFT,Merge.LEFT],        
    ],

    style=PresetStyle.double_thin_box,
    first_col_heading=True,
)
#print the tabled data
print(output)
