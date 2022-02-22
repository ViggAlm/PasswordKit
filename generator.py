import log
import main
import random
import time

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*()-_=+{[}]|\;:',?/"


def gen():
    log.general("This is the password generator.")

    log.question("Please enter the length of your password(s):")
    password_length = int(input(""))
    log.question("Please enter the amount of passwords you wish to generate:")
    password_amount = int(input(""))

    for n in range(0, password_amount):
        password = ""
        password_num = n + 1
        for n in range(0, password_length):
            current_char = random.choice(chars)
            password += current_char
        log.result(f"Password {password_num} : {password}")

    log.question(f"Press 'G' to generate more passwords, press 'M' to open the menu or press any other key to exit:")
    next_action = input("").lower()

    if next_action == "g":
        log.result("Chose generate more passwords.")
        time.sleep(1)
        main.clear()
        gen()
    elif next_action == "m":
        log.result("Chose open the menu.")
        time.sleep(1)
        main.clear()
        main.menu()
    else:
        log.general("Thank you for using this program!")
        time.sleep(1)
