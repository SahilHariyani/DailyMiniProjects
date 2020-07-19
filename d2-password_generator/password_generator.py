from random import *


def message():
    print("Welcome to your random password generator!")
    num =int(input("Please select the length of your password (greater than 5): "))
    print(passGen(num))

def randomSet(set):
    passwordSet = {
    0:"ABCDEFGHIJKLMNOPQRTUVWXYZ",
    1:"ABCDEFGHIJKLMNOPQRTUVWXYZ".lower(),
    2:"!@#$%^&*()",
    3:"0123456789"}
    return passwordSet.get(set,"gg")

def passGen(num):
    new_password=""
    if (num)<6:
        print("Please enter atleast 6.")
    else:
      for i in range(1,num+1):
          new_password += choice(randomSet(randint(0,3)));
    pass_word=list(new_password)
    shuff=shuffle(pass_word)
    new_pass="".join(pass_word)
    return new_pass
message()