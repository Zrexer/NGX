#!/usr/bin/env python 

import pyngrok.ngrok
import wget
import os 
import sys 
import time
import json
import platform
import gdown
import rich

os.system("")
commands: dict = {}

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m'
    red = '\033[31m'
    blue = '\033[36m'
    pink = '\033[35m'
    yellow = '\033[93m'
    darkblue = '\033[34m'
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'

class NGX(object):
    def createStreamDL(platformDownload: str = platform.system()):
        if not os.path.exists("./ngrok"):
            if platformDownload == "Linux":
                try:
                    wget.download("https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-s390x.tgz")
                    return {"error" : False}
                except Exception as E:
                    return {"error" : True, "base" : E, "type" : "onDownload"}
            
            elif platformDownload == "Windows":
                try:
                    wget.download("https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip")
                    return {"error" : False}
                except Exception as E:
                    return {"error" : True, "base" : E, "type" : "onDownload"}
            
            elif platformDownload == "Darwin":
                try:
                    wget.download("https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-darwin-amd64.zip")
                    return {"error" : False}
                except Exception as E:
                    return {"error" : True, "base" : E, "type" : "onDownload"}
                
        else:
            return {"error" : True, "base" : "the ngrok file does exists", "type" : "onExistsFile"}

    def createStreamStableConnection(port: int = 8081, connectionMethodProto: str = "http"):
        base = pyngrok.ngrok
        connector = base.connect(port, connectionMethodProto)
        print(log(f"Link Created: {colors.red}'{connector.public_url}'").createInfo)
        while 1:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                exit()

class BufferList(object):
    def __init__(self,
                 List: list = [],
                 ):
        
        self.list = List
        
    def parse(self):
        bfd = {}

        for i in range(len(self.list)):
            bfd["_"+str(i+1)] = self.list[i]

        return bfd
    
    def isexists(self, target):
        if target in self.list:
            return True
        else:return False
    
    def indexexists(self, target):
        if target in self.list:
            return self.list.index(target)
        else:return False

    def isinfrontof(self, target, indexes):
        isit = False

        if target in self.list:
            try:
                indx = self.list.index(target)
                if indx == indexes:
                    isit = True
                else:isit = False
            except Exception as e:return e
        
        return isit

class BufferConsole(object):
    def __init__(self):

        self.data = []

    def __setcommands__(self, __key, __value):
        commands[__key] = __value
        return commands
    
    def getDictArgv(self):
        return BufferList(sys.argv).parse()
    
    def addFlag(self, *flags, mode: str = "in_front_of"):
        flg = list(flags)
        for i in range(len(flg)):
            self.__setcommands__(str(i+1), flg[i])

        if mode == "in_front_of":
            for key, val in BufferConsole().getDictArgv().items():
                if str(val) in flg:
                    keyx = int(str(key).replace("_", ""))
                    keyx += 1
                    if not f"_{keyx}" in BufferConsole().getDictArgv().keys():
                        self.data.append("Null")
                        pass
                    else:
                        self.data.append(BufferConsole().getDictArgv()[f"_{keyx}"])
                        pass
                
                else:
                    pass

            return self.data

class log(object):
    def __init__(self, msg: str = ""):
        self.msg = msg
    
    @property
    def createInfo(self):
        return "{}[{}{}{}] [{}{}{}] {}{}".format(colors.magenta, colors.yellow, time.strftime("%H:%M:%S"), colors.magenta, colors.white+colors.underline+colors.green, "INFO"+colors.white, colors.magenta, colors.white, self.msg)
    
    @property
    def createError(self):
        return "{}[{}{}{}] [{}{}{}] {}{}".format(colors.magenta, colors.yellow, time.strftime("%H:%M:%S"), colors.magenta, colors.white+colors.underline+colors.red, "ERROR"+colors.white, colors.magenta, colors.white, self.msg)
    
    @property
    def createWran(self):
        return "{}[{}{}{}] [{}{}{}] {}{}".format(colors.magenta, colors.yellow, time.strftime("%H:%M:%S"), colors.magenta, colors.white+colors.underline+colors.silver, "WARNING"+colors.white, colors.magenta, colors.white, self.msg)

    def returnBanner():
        s = "{"
        bs = "}"
        print("""
                {}_  _ ____ {}_  _ 
                {}|\ | | __  {}\/  
                {}| \| |__] {}_/\_ 
              
    {}{}{}{}{}{}{}{}{}{}
""".format(colors.yellow, colors.red, colors.yellow, colors.red, colors.yellow, colors.red, colors.yellow, bs, "-"*6, colors.cyan, s, "ᴅᴇᴠ#ʜᴏꜱᴛ1ʟᴇᴛ > 4.5.3", bs, colors.yellow, "-"*6, s+colors.white))

log.returnBanner()

baseTime = time.time()
print(log(f"Running at {colors.red}[{colors.white}{time.ctime(baseTime)}{colors.red}]{colors.white}\n").createInfo)

bfr = BufferConsole()

pscsi = bfr.addFlag("-csi")
psset = bfr.addFlag("--set")
psport = bfr.addFlag("--port")
psdriveUrl = bfr.addFlag("--down")

if len(sys.argv) <= 1:
    print(log(f"No Arguments Called: Get Infomation with {colors.red}[{colors.white}-h {colors.red}/ {colors.white}--help{colors.red}]{colors.white}").createError)

if "-h" in sys.argv or "--help" in sys.argv:
    helpData = {
        "help" : "Show This Message",
        "-csi ngrok" : "Download Ngrok file with OS Scanner",
        "--set <token>" : "Set the Auth Token of NGROK",
        "--down <url>" : "Download a File From GOOGLE DRIVE",
        "--create" : {
            "worker stream" : "create a link on 8081 port",
            "--port <port number>" : "to set a special port, also should be writed in fron of --create"
        }
    }
    rich.print(json.dumps(helpData, indent=4))

if len(pscsi) == 1 and pscsi[0] != "Null" and pscsi == "ngrok":
    print(log("Try To Get NGROK File").createInfo)
    ngxngrok = NGX.createStreamDL()
    if ngxngrok['error'] == True:
        if ngxngrok['type'] == 'onDownload':
            print(log("Cannot Download").createError)
            print(log(ngxngrok['base']).createError)
            exit()
        else:
            print(log(f"The Ngrok file already exists in {colors.red}'{os.getcwd()}'").createInfo)
            print(log("Passed").createWran)
            pass
    else:
        print(log(f"Ngrok was Downloaded For {colors.red}{platform.system()}").createInfo)
        exit()

if len(pscsi) == 1 and pscsi[0] == "Null":
    print(log("Cannot get the Installer Stream").createError)
    exit()

if len(pscsi) == 1 and pscsi[0] != "Null" and pscsi[0] == "ngrok":
    print(log(f"Unknown Stream {colors.red}'{pscsi[0]}'{colors.white}").createError)
    exit()

if "--set" in sys.argv:
    if not psset[0] == "Null":
        try:
            pyngrok.ngrok.set_auth_token(psset[0])
            print(log(f"The Token {colors.red}'{psset[0]}'{colors.white} is saved").createInfo)
            pass
        except Exception as ET:
            print(log("Cannot set token").createError)
            print(log(ET).createError)
            exit()
    else:
        print(log("Cannot get the Token").createError)
        exit()

if "--create" in sys.argv:
    if "--port" in sys.argv and not psport[0] == "Null":
        print(log(f"Try To create a Stable Connection with port {colors.red}'{psport[0]}'").createInfo)
        NGX.createStreamStableConnection(psport[0])
    else:
        print(log(f"Try To create a Stable Connection with port {colors.red}'8081'").createInfo)
        link = NGX.createStreamStableConnection()

if len(psdriveUrl) == 1:
    if not psdriveUrl[0] == "Null":
        print(log("Please Be Sure About Current Connection").createWran)
        print(log(f"Try to DOWNLOAD File: {colors.red}'{psdriveUrl[0]}'{colors.white} ...").createInfo)
        try:
            gdown.download(psdriveUrl, quiet=False)
            print(log(f"Downloaded File: {colors.red}'{wget.filename_from_url(psdriveUrl[0])}'").createInfo)
            print(log(f"Saved in Path: {colors.red}'{os.getcwd()}'").createInfo)
        except Exception as ERROR_DRIVE_DOWNLOAD:
            print(log(str(ERROR_DRIVE_DOWNLOAD)).createError)
            pass
    else:print(log("Cannot Get the URL For Download").createError)
