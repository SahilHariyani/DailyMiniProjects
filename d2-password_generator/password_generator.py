from random import *

# To demonstrate the importance of password complexity, 
# let's start with a pincode password such as "123456789". In this case, the character set (0123456789) consists of 10 characters. For a 9 digit password using this character set, there are 10^9 possible password combinations. Therefore, it will take (1.7*10^-6 * 10^9) seconds / 2, or 14.17 minutes, to break this password on average. On a supercomputer or botnet, we divide this by 100000, so it would take 0.0085 seconds to break a password.


#If you include symbols, then depending on the symbols used, 
# there are about 80 characters in the set. 
# To break a password such as "%ZBGbv]8", it would take (1.7*10^-6 * 80^8) seconds / 2, or 45.2 years. On a supercomputer or botnet, this will take 4 hours.

# So, even if you use a very secure set of characters, your password should be at least 10 characters long. To break a 10 character password that uses letters, numbers, and symbols, such as "%ZBGbv]8g?", it would take (1.7*10^-6 * 80^10) seconds / 2 or 289217 years. This would take about 3 years on a supercomputer or botnet.
# The moral of the story is that passwords should be at least 10 characters long and include a mix of numbers, lowercase letters, uppercase letters and symbols.


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