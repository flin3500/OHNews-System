from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
import os

__user_service = UserService()

while True:
    os.system("clear")
    print(Fore.LIGHTBLUE_EX, "\n\t================")
    print(Fore.LIGHTBLUE_EX, "\n\tWelcome to OHNews v0.1")
    print(Fore.LIGHTBLUE_EX, "\n\t================")
    print(Fore.LIGHTGREEN_EX, "\n\t1. Log in")
    print(Fore.LIGHTGREEN_EX, "\n\t2. Exit")
    print(Style.RESET_ALL)
    opt = input("\n\tInput the number: ")

