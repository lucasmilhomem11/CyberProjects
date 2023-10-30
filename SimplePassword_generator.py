#created by Lucas Milhome as a fun time to learn.
#Date: 9/28/2023

#Password generator
import string
import random
alphabet = list(string.ascii_letters)
nbr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbl = ['@', '#', '$', '!', '%', '&']
print("Welcome to the Password generator!")
letters = int(input("How many letters would you like in the passowrrd\n"))
symbols = int(input("How many symbols?\n"))
number = int(input("How many numbers?\n"))
password = []
for char in range(1,letters + 1):
    password .append( random.choice(alphabet))

for char in range(1,symbols + 1):
  password.append (random.choice(symbl))

for char in range(1,number + 1):
  password.append(random.choice(nbr))

random.shuffle(password)

password_string = ""
for char in password:
   password_string += char

print("\nHere is your new password: " + password_string)
