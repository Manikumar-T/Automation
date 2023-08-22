#To get the platform
import platform
#Execute the command and get it's output
import subprocess as sp
#To do the os relatee operation
import os

import re
#To read and write the configration dictnory
import json
#To display data clearly
import pprint

# Dict to store the configration
configDict={
    "Manjaro_package":[],
    "snap_package":[],
    "config":[],
    "vscode_extenstion":[]

}

#To get the System name
class SystemInfo:

    def __init__(self) -> None:
        self.platformName = "Manjaro" if ("MANJARO" in platform.platform()) else "Debian"

    #call the systemInfo object with print, str,format it's return this string
    def __str__(self) -> str:
        return self.platformName


#Class to do a operation backup config file
class ConfigFile:
    def __init__(self) -> None:
        #Get the user home path
        self.home=os.path.expanduser('~')
        #change the current working path as home
        os.chdir(self.home)
        #Create the backup folder
        self.backup=""
        try:
            os.mkdir(".backup") 
        except:
            print("Backup Folder exist...")
        finally:
            #if backup folder exist the create the backup path
            if(os.path.isdir('.backup')):
                self.backup = self.home+"/.backup"
                print("Search config file...")
                if(os.path.isfile('.backup/config.json')):
                      self.readconfig()
                      print()
        
                
    #Write the json config file
    def writeConfig(self):
        print(self.backup)
        with open(self.backup+"/config.json",'w') as fConfigWrite:
            json.dump(configDict,fConfigWrite)
    #Read the json config file
    def readconfig(self):
        try:
            with open(self.backup+"/config.json",'r') as fConfigRead:
                global configDict
                configDict=json.load(fConfigRead)
        except:
            print("config.json file not found")
        
        #print(configDict)
    def CreateSymLink(self):
        #move the file to backup folder
        print("⚠️!!!!Don't close the script!!!!⚠️ \n\nmoving file to backup folder...🗃️")
        
        for i in configDict['config']:
            try:
                #To the config file to backup folder
                mv_file=sp.Popen(["mv",f"{self.home}/{i}", f"{self.backup}"]) # mv /home/manikumar/info.json /home/manikumar/.backup
                mv_file.wait()
                print(f"{i} moved to {self.backup}")
                

                #create the symlink files in backup folder
                symlink = sp.Popen(['ln','-s',f"{self.backup}/{i}",f"{self.home}"])
                symlink.wait()
                print("symlink Created ...🔗")
                
                  
            except:
                print(f"'{i}'not found..😐")
            
        
    
#Backup the distro package, snap package list
class Backup:

    def __init__(self,platform) -> None:
        self.platformname = str(platform)

        pass
    #function to get the distro package list using it's own package manager
    def getDistroPackage(self):
        if(self.platformname == "Manjaro"):
            '''Get the  manually install application using pacman
                1.pacman -Qqe get the system application as well as installed by user
                2.desktopfs-pkg.txt file has only the system application
                3.grep -v to inverse the match to get the manualy install application 
            '''
            Software_list = sp.getoutput("pacman -Qqe | grep -v \"$(awk '{print $1}' /desktopfs-pkgs.txt)\"")
            if("No such file" not in Software_list):
                configDict["Manjaro_package"] = Software_list.split()
                print("Manjaro Package List Created...👍")
            else:
                configDict["Manjaro_package"]=[]
                print("Unable to Get Distro Package List...😐")
    #function to get the Snap package list 
    def getSnapPackage(self):
        try:
            #capture the output of snap list commmand 
            snapListString = sp.run(["snap",'list'],shell=False,capture_output=True,text=True)
            #Spliting the table head and warning msg for output
            snapListString = [i for i in snapListString.stdout.split('\n') if "Name" not in i and "WARNING:" not in i and "" != i]
            #Split the package name from the output
            snapList =[]
            for i in snapListString:
               snapList.append(i.split()[0])

            configDict['snap_package'] = snapList
            print("Snap Package List Created...👍")
            
        except:
            configDict["snap_package"]=[]
            print("Unable to Get Snap Package List...😐")

    #function to get the config file list
    def getConfigList(self):
        AllDotFileList = []
        BackupDotFileList =[]  
        flag = 1
        if(configDict["config"]==[]):
            while (flag!=0):
                #print the list of config file
                print("------------------------------List Of Configeration File------------------------------")
                AllDotFileList=[i for i in os.listdir() if os.path.isfile(i)]
                for i in range(len(AllDotFileList)):
                    print(f"{i+1}){AllDotFileList[i]}")

                #Get the S.No of list user want to backup
                ConfigIndex = input("Enter the config file S.NO seprated by Space(Ex: 1 3 14 5 2): ").split()

                #change the element type into int and get config file name
                try:

                    ConfigIndex  = list(map(int,ConfigIndex)) #change the type into int
                    for i in ConfigIndex:
                        if(i>0 and i<=len(AllDotFileList)):  #condition to check is valid S.No
                            BackupDotFileList.append(AllDotFileList[i-1]) #add the element for backup

                        configDict["config"]=BackupDotFileList; #add to config dictonary
                    flag = 0
                except:
                    print("invalid input 😐")

    #function to get the vs code extenstion list
    def getVsExtList(self):
        #get the vs code extenstion list 
        vsExtenstionList = sp.getoutput("code --list-extensions").split("\n")
        #store the list into to config dict
        configDict["vscode_extenstion"] = vsExtenstionList
   



            
            
                
                
fconfig =ConfigFile()
obj1 = Backup(SystemInfo())
obj1.getDistroPackage()
obj1.getSnapPackage()
obj1.getConfigList()
obj1.getVsExtList()
fconfig.writeConfig()
fconfig.CreateSymLink()
pprint.pprint(configDict)