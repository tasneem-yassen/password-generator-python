import secrets #Use secrets for cryptographic randomness
import argparse


def password_generator(length,lowercase,uppercase,special_chars): 
    counter = 0 
    digits = "0123456789"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?"
    password = ""
    pool = digits 
    if uppercase :
        pool += upper_letters 
    if lowercase : 
        pool += lower_letters
    if special_chars : 
        pool += special_characters
    while counter < length: 
        password += secrets.choice(pool)
        counter+=1 
    print("your password:",password)
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--length",type=int,required=True)
    parser.add_argument("--lowercase_letters",action="store_true")
    parser.add_argument("--uppercase_letters",action="store_true")
    parser.add_argument("--special_characters",action="store_true")
    args = parser.parse_args()
    pass_length = args.length 
    include_lowcase = args.lowercase_letters
    include_uppercase = args.uppercase_letters 
    include_special_characters = args.special_characters 
    if pass_length <=0 : 
        print("Length must be positive")
    else : 
        password_generator(pass_length,include_lowcase,include_uppercase,include_special_characters)