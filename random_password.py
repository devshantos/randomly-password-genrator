from random import sample

upper="ZXCVBNMLKJHGFDSAQWERTYUIOP"
lower=upper.lower()
number="0123456789"
symbol="!@#$%^&*()/"
all = upper+lower+symbol+number

length = 16

try:
    length = input("How long do you want your generated password to be?: ")
except Exception:
    print("Invalid answer! try again.")
    try:
        length = input("How long do you want your generated password to be?: ")
    except Exception:
        print("Invalid answer! Using 16 letter length.")

password="".join(sample(all,length))

print("Generated password: " + password)