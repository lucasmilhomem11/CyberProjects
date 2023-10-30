#created by Lucas Milhomem as a fun time to learn.
#Date: 10/25/2023

import requests, hashlib, maskpass

def main():
    print("""
      _      __    __                     __             __           __
    | | /| / /__ / /______  __ _  ___   / /____    ____/ /  ___ ____/ /_____ ____  ___  __ __
    | |/ |/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \  / __/ _ \/ -_) __/  '_/ -_) __/ / _ \/ // /
    |__/|__/\__/_/\__/\___/_/_/_/\__/  \__/\___/  \__/_//_/\__/\__/_/\_\\__/_/ (_) .__/\_, /
                                                                                /_/   /___/
    """)

    print("\nThis little project will check if your password has ever been breached!\n")

    num_passwords = get_integer_input("How many passwords would you like to check? ")

    for i in range(1, num_passwords + 1):
        password = password = maskpass.askpass(prompt=f"Password {i}/{num_passwords} - Please enter your password, it will be masked and nobody will see (or type 'done' to exit):\n", mask="*")

        if password.lower() == 'done':
            break  # Exit the loop if 'done' is entered

        check_password(password) # Check the safety of the entered password


def get_integer_input(prompt):
    while True:
        try:  # Get an integer input from the user
            user_input = int(input(prompt))
            return user_input  # If input is a valid integer, return it
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_password(password):      # Hash the password and check it against known data breaches
    password_enc = hashlib.sha1(password.encode()).hexdigest().upper()
    first5_hash = password_enc[:5]
    five_to_end_hash = password_enc[5:]
    url = F"https://api.pwnedpasswords.com/range/{first5_hash}"

    api_call = requests.get(url=url)

    line_divider = api_call.text.splitlines()
    safe_password = True

    for _ in line_divider:
        line = _.split(":")
        requested_list = []
        requested_list.append(line)

        for hex, count in requested_list:
            if hex in five_to_end_hash:
                print(F"\nThis password is not safe and it has appeared in {count} data breaches\n")
                safe_password = False

    if safe_password:
        print("""\nYour password seems to be safe, and it has not been found in any password leak.
    Keep rotating your passwords and always be careful\n""")


if __name__ == "__main__":
    main()

