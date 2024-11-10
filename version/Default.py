## IMPORTS
from dhooks import Webhook, Embed
from pystyle import Write, Colorate, Colors
import os, time
import ctypes

## ART
banner_header_1 = '''
███████╗███████╗██████╗ ███████╗ █████╗ ██╗     
██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██║     
███████╗█████╗  ██████╔╝█████╗  ███████║██║     
╚════██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██║██║     
███████║███████╗██║  ██║███████╗██║  ██║███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝                                                                                      
'''

## INPUTS & CONFIG
print(Colorate.Horizontal(Colors.blue_to_purple, f"{banner_header_1}", 1))
time.sleep(0.4)
usrData = Write.Input(f"{os.getlogin()}$ ", Colors.blue_to_purple, interval=0.025)

## CODE
if usrData == 'ping' or usrData == 'p':
    http_base = "https://"
    pingReq = Write.Input('Ping$ ', Colors.red_to_yellow, interval=0.025)
    time.sleep(1)
    print("Please wait a moment on our end.")
    os.system(f"ping {pingReq}")
    input("Exit main-c.py [!].. ")

elif usrData == 'prompt' or usrData == 'pr':
    PromptChange = Write.Input('Prompt$ ', Colors.red_to_yellow, interval=0.025)
    pr_start = ctypes.windll.kernel32.SetConsoleTitleW(f"{PromptChange}")