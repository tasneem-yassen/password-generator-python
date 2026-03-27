import secrets #Use secrets for cryptographic randomness
import argparse


def password_generator(length,lowcase): 
    counter = 0 
    digits = "0123456789"
    digits_letters = "0123456789abcdefghijklmnopqrstuvwxyz"
    password = ""
    while counter < length: 
        if lowcase : 
            password += secrets.choice(digits_letters)
        else:
            password += secrets.choice(digits)
        counter+=1 
    print("your password:",password)
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--length",type=int,required=True)
    parser.add_argument("--lowercase_letters",action="store_true")
    args = parser.parse_args()
    pass_length = args.length 
    include_lowcase = args.lowercase_letters
    if pass_length <=0 : 
        print("Length must be positive")
    else : 
        password_generator(pass_length,include_lowcase)