from random import sample

#Write your symbol and number
upper="ZXCVBNMLKJHGFDSAQWERTYUIOP"
lower=upper.lower()
number="0123456789"
symbol="!@#$%^&*()/"

#All sybol addition
all = upper+lower+symbol+number

#Password length
length = int(input("How long you want to generated your password?: "))
password="".join(sample(all,length))
print("Generated password: " + password)

