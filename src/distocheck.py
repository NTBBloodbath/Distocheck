# -*- coding: utf-8 -*-
#
# NTB Bloodbath | Distocheck - Discord Token Checker
# ==================================================
# Distocheck is distributed under the MIT License.

import os
import time
import requests
from src.lib.colors import colors

uri = "https://discord.com/api/v7/users/@me"
logger_time = time.localtime()

def checker(token: str, extra_info: bool = False):
    req = requests.get(uri, headers = {
        "Authorization": token
    })

    data = req.json()
    if "id" not in data:
        print(
            f"\n[{colors.bold}{colors.fg.red}{logger_time.tm_year}-{logger_time.tm_mon}-{logger_time.tm_mday} / {logger_time.tm_hour}:{logger_time.tm_min}:{logger_time.tm_sec}{colors.reset}]",
            f"| [{colors.bold}{colors.fg.red}INVALID{colors.reset}]: {token}\n",
            end=""
        )
    else:
        if extra_info:
            print(
                f"\n[{colors.bold}{colors.fg.green}{logger_time.tm_year}-{logger_time.tm_mon}-{logger_time.tm_mday} / {logger_time.tm_hour}:{logger_time.tm_min}:{logger_time.tm_sec}{colors.reset}]",
                f"| [{colors.bold}{colors.fg.green}VALID{colors.reset}]: {token}\n                                  {data['username']}#{data['discriminator']} ({colors.disable}{data['id']}{colors.reset}) | {data['email'] if data['email'] is not None else 'No email'}\n",
                end=""
            )
        else:
            print(
                f"\n[{colors.bold}{colors.fg.green}{logger_time.tm_year}-{logger_time.tm_mon}-{logger_time.tm_mday} / {logger_time.tm_hour}:{logger_time.tm_min}:{logger_time.tm_sec}{colors.reset}]",
                f"| [{colors.bold}{colors.fg.green}VALID{colors.reset}]: {token}\n                                  {data['username']}#{data['discriminator']} ({colors.disable}{data['id']}{colors.reset})\n",
                end=""
            )
    time.sleep(1)

print("Enter checker type (one / list)")
print(f"{colors.disable}Note: If you don't know how to use it, put help.{colors.reset}")
print(">> ", end="")

ch_type = input()
while ch_type != "exit":
    if ch_type == "help":
        print(f"\n{colors.bold}Q: What is Distocheck for?{colors.reset}\nA: Distocheck is a port of RubyTokenChecker and is used to check Discord tokens.")
        print(f"\n{colors.bold}Q: So what can I do with this?{colors.reset}\nA: You can verify user/bot tokens and get information about the accounts.")
        print(f"\n{colors.bold}Q: How is Distocheck used?{colors.reset}\nA: When launching the Distocheck executable a prompt will open\n   and it'll ask you for the type of checker you want to use")
        print("   then you must enter what is requested according to\n   the case (token or file) and Distocheck will begin to verify the tokens!")
        print("\n>> ", end="")
        ch_type = input()
    elif ch_type == "one":
        print("\nEnter token")
        print(f"{colors.disable}Note: If you want to check a bot's token, you must add")
        print(f"      Bot before the token like this: Bot <token>{colors.reset}")
        print(">> ", end="")
        tk = input()

        print("\nDo you want to display extra information about the account? [Y/N]")
        print(">> ", end="")

        extra = input().lower()
        if extra == "y":
            checker(tk, True)
        elif extra == "n":
            checker(tk, False)
        break
    elif ch_type == "list":
        print("\nEnter tokenlist path")
        print(f"{colors.disable}Note: The path can be relative or absolute.{colors.reset}")
        print(">> ", end="")

        tks_path = input()
        if os.path.isfile(tks_path):
            tks_file = open(tks_path, 'r').readlines()

            print("\nDo you want to display extra information about the account? [Y/N]")
            print(">> ", end="")

            extra = input().lower()
            for token in tks_file:
                if extra == "y":
                    checker(token.strip(), True)
                elif extra == "n":
                    checker(token.strip(), False)
        else:
            print(
                f"\n[{colors.bold}{colors.fg.red}{logger_time.tm_year}-{logger_time.tm_mon}-{logger_time.tm_mday} / {logger_time.tm_hour}:{logger_time.tm_min}:{logger_time.tm_sec}{colors.reset}]",
                f"[{colors.bold}{colors.fg.red}ERROR{colors.reset}]: The file you have specified doesn't exists.\n",
                end=""
            )
        break
    else:
        print(
            f"\n[{colors.bold}{colors.fg.red}{logger_time.tm_year}-{logger_time.tm_mon}-{logger_time.tm_mday} / {logger_time.tm_hour}:{logger_time.tm_min}:{logger_time.tm_sec}{colors.reset}]",
            f"| [{colors.bold}{colors.fg.red}ERROR{colors.reset}]: {colors.bold}Unknown option{colors.reset} {ch_type}. Closing ...\n",
            end=""
        )
        break
else:
    print(
        f"\n[{colors.bold}{colors.fg.red}{logger_time.tm_year}-{logger_time.tm_mon}-{logger_time.tm_mday} / {logger_time.tm_hour}:{logger_time.tm_min}:{logger_time.tm_sec}{colors.reset}]",
        f"| [{colors.bold}{colors.fg.red}EXIT{colors.reset}]: Closing ...\n",
        end=""
    )
