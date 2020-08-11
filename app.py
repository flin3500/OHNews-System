from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
import os
import sys
import time

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
    if opt == "1":
        username = input("\n\tUsername: ")
        password = input("\n\tPassword: ")
        result = __user_service.login(username, password)
        # successfully log in
        if result:
            # The user role
            role = __user_service.search_role(username)
            os.system("clear")
            while True:
                if role == "Editor":
                    pass
                elif role == "Admin":
                    print(Fore.LIGHTGREEN_EX, "\n\t1. Manage news")
                    print(Fore.LIGHTGREEN_EX, "\n\t2. Manage users")
                    print(Fore.LIGHTRED_EX, "\n\t3. Log out")
                    print(Fore.LIGHTRED_EX, "\n\t4. Exit system")
                    print(Style.RESET_ALL)
                    opt = input("\n\tInput the number: ")
                    if opt == "1":
                        pass
                    elif opt == "2":
                        pass
                    elif opt == "3":
                        break
                    elif opt == "4":
                        sys.exit(0)
        else:
            print("\n\tLogin failed (Wait 3s)")
            time.sleep(3)
    elif opt == "2":
        sys.exit(0)

