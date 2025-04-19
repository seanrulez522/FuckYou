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
        os
