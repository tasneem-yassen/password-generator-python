import secrets #Use secrets for cryptographic randomness
import argparse


def password_generator(length): 
    counter = 0 
    digits = "0123456789"
    password = ""
    while counter < length: 
        password += secrets.choice(digits)
        counter+=1 
    print("your password:",password)
if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument("--length",type=int,required=True)
    args = parser.parse_args()
    pass_length = args.length 
    password_generator(pass_length)