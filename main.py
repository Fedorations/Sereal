import os
import time
import ctypes
from pystyle import Write, Colorate, Colors

## ART
banner_header_1 = '''
███████╗███████╗██████╗ ███████╗ █████╗ ██╗     
██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██║     
███████╗█████╗  ██████╔╝█████╗  ███████║██║     
╚════██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██║██║     
███████║███████╗██║  ██║███████╗██║  ██║███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝                                                                                     
'''

## INPUTS & Config
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ping_command():
    clear_console()
    http_base = "https://"
    pingReq = Write.Input('Ping$ ', Colors.red_to_yellow, interval=0.025)
    time.sleep(1)
    print("Please wait a moment on our end.")
    os.system(f"ping {pingReq}")
    input("Return... ")
    clear_console()

def prompt_command():
    clear_console()
    PromptChange = Write.Input('Prompt$ ', Colors.red_to_yellow, interval=0.025)
    ctypes.windll.kernel32.SetConsoleTitleW(f"{PromptChange}")
    input("Return... ")
    clear_console()

def webhook():
    clear_console()
    webhookdatadc = Write.Input(f"discord$ ", Colors.blue_to_purple, interval=0.025)
    import requests
    requests.post(webhookdatadc, json={'content': "Hello"})
    clear_console()

aaas = '''
ping / p - Pings A Internet Protocol / Website Address/n
prompt / pr - Changes window title/n
testweb / tw - Test's your discord webhook or any other webhook using post request
'''
def help():
    clear_console()
    print(Colorate.Horizontal(Colors.yellow_to_red, f"{aaas}"))
    time.sleep(60)
    clear_console()

def main():
    print(Colorate.Horizontal(Colors.blue_to_purple, f"{banner_header_1}", 1))
    time.sleep(0.5)

    while True:
        usrData = Write.Input(f"{os.getlogin()}$ ", Colors.blue_to_purple, interval=0.025)

        if usrData == 'ping' or usrData == 'p':
            ping_command()
        elif usrData == 'prompt' or usrData == 'pr':
            prompt_command()
        elif usrData == 'testweb' or usrData == 'tw':
            webhook()
        elif usrData == 'help' or usrData == 'h':
            help()
        elif usrData == 'exit':  
            print("Exiting the program...")
            break
        else:
            print("Unknown command! Please try again.")
            time.sleep(1)
            clear_console()

if __name__ == "__main__":
    main()
