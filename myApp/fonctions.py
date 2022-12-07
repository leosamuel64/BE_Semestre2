import secrets
import string
import hashlib


def randomPassword(pwd_length = 12):
# necessary imports


# define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

# fix password length

# generate a password string
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    return pwd

def hashMdp(mdp):
    mdp=hashlib.sha256(mdp.encode())
    mdpC= mdp.hexdigest()
    return mdpC


