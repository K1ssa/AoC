import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
argument = input("Wat is het IP adres wat je wil scannen: ")
print(Fore.YELLOW)
print("NMAP scan")
os.system("nmap -sV -A " + argument)
print(Fore.GREEN)
print("Nikto scan")
os.system("nikto -h " + argument)
