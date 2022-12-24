import secrets
import string

if __name__ == "__main__":
    print("Random Passwords generate.")

def randPasswordsNumbers(arg1):
    alphabet = string.digits 
    password = passwordGenerate(arg1,alphabet)
    return password

def randPasswordLetters(arg1):
    alphabet = string.ascii_letters
    password = passwordGenerate(arg1,alphabet)
    return password

def randPasswordsMedium(arg1):
    alphabet = string.ascii_letters + string.digits
    password = passwordGenerate(arg1,alphabet)
    return password

def randPasswordsHard(arg1):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = passwordGenerate(arg1,alphabet)
    return password

def passwordGenerate(arg1,arg2):
    passwordGenerate = ''.join(secrets.choice(arg2) for i in range(arg1))
    return passwordGenerate