from colorama import Fore

prefix = "[" + Fore.YELLOW + "PasswordKit" + Fore.WHITE + "]"


def result(text):
    print(Fore.WHITE + f"{prefix}" + Fore.GREEN + f"{text}")


def error(text):
    print(Fore.WHITE + f"{prefix}" + Fore.RED + f"{text}")


def general(text):
    print(Fore.WHITE + f"{prefix}{text}")


def question(text):
    print(Fore.WHITE + f"{prefix}" + Fore.CYAN + f"{text}")
