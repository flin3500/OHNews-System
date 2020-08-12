from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
import os
import sys
import time

__user_service = UserService()
__news_service = NewsService()

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
        password = getpass("\n\tPassword: ")
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
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1. Review news")
                            print(Fore.LIGHTGREEN_EX, "\n\t2. Delete news")
                            print(Fore.LIGHTRED_EX, "\n\t3. Back to account")
                            print(Style.RESET_ALL)
                            opt = input("\n\tInput the number: ")
                            if opt == "1":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __news_service.search_unreview_count_page()
                                    result = __news_service.search_unreview_list(page)
                                    for index in range(len(result)):
                                        news = result[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s" % (index+1, news[1], news[2],news[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tprev. Prev page")
                                    print(Fore.LIGHTRED_EX, "\n\tnext. Next page")
                                    print(Fore.LIGHTRED_EX, "\n\tback. Back")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\tInput the number: ")
                                    if opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif opt == "back":
                                        break
                                    elif 1 <= int(opt) <= 5:
                                        __news_service.review_news()
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

