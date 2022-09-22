from cryptography.fernet import Fernet
from random import seed
from random import random
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
def password_gen():
    seed(1)
    print(random(),random(),random())
    seed(1)
    print(random(),random(),random())

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())    
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
def masterPW():
    mpw = input("What is your master password?: ")
    print(mpw)
    enterMpwAgain = input("Please re-enter your master password: ")
    if(enterMpwAgain == mpw):
        print("Access Granted")
    else:
        print("Invalid access.")

while True:
    masterPW()
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
    random = input("Would you want to generate a random password?: ")
    if(random == "yes"):
        password_gen()
    if(random == "no"):
        print("Exiting...")
        exit
    

