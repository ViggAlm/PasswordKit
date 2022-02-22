import checker
import generator
import log
import os
import time
from colorama import init


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    init()
    os.system("title PasswordKit")

    log.general("Welcome to the PasswordKit made by ViggAlm on github, where you can also find the discord server.#")
    log.general("This was  made as a fun side project, please report any issues by discord.")

    log.question("Press 'C' for the password strength checker or press 'G' for the password generator:")
    action = input("").lower()

    if action == "c":
        log.result("Chose password strength checker.")
        time.sleep(1)
        clear()
        checker.check()
    elif action == "g":
        log.result("Chose password generator.")
        time.sleep(1)
        clear()
        generator.gen()
    else:
        log.error("Invalid answer, please try again.")
        time.sleep(2)
        clear()
        menu()


if __name__ == "__main__":
    menu()
