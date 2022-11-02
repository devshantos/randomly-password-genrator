import random
upper="ZXCVBNMLKJHGFDSAQWERTYUIOP"
lower="zxcvbnmlkjhgfdsaqwertyuiop"
number="0123456789"
symbol="!@#$%^&*()"
all= upper+lower+symbol+number
length=16
password="".join(random.sample(all,length))
print("Take your password:" + password)