# Credits to NeuralNine's video for helping me out here ( https://www.youtube.com/watch?v=iJ01q-sRJAw&t )
import log
import main
import string
import time


def check():
    log.general("This is the password strength checker.")

    log.question("Please enter your password:")
    password = input("")

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    characters = [upper_case, lower_case, special, digits]

    length = len(password)

    score = 0

    with open("common.txt", "r") as f:
        common = f.read().splitlines()

    if password in common:
        log.error("Password found in top 10 000 most common passwords, change immediately. Score: 0 / 7")
        exit()

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 16:
        score += 1
    if length > 20:
        score += 1

    log.general(f"Password length is {str(length)}, added {str(score)} points to your total.")

    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1
    log.general(f"Password has {str(sum(characters))} different types of characters, added {str(sum(characters) - 1)} points to your total.")

    if score < 4:
        log.error(f"Password is weak, password change recommended. Score: {str(score)} / 7")
    elif score <= 5:
        log.general(f"Password is okay, 2 factor authentication recommended and possible password change recommended. Score: {str(score)} / 7")
    elif score >= 6:
        log.result(f"Password is good, 2 factor authentication recommended. Score: {str(score)} / 7")

    log.question("Press 'C' to check another password, press 'M' to open the menu or press any other key to exit:")
    next_action = input("").lower()

    if next_action == "c":
        log.result("Chose check another password.")
        time.sleep(1)
        main.clear()
        check()
    elif next_action == "m":
        log.result("Chose open the menu.")
        time.sleep(1)
        main.clear()
        main.menu()
    else:
        log.general("Thank you for using this program!")
        time.sleep(1)
