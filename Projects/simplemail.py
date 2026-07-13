#Email Automation
#OTP AUTHENTICATION
import random
import math
import smtplib#simple mail tranfer protocol library

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is your otp"
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("kavyasrikota989@gmail.com","wtxf ecwh gken qkqs")
user="kavyasrikota989@gmail.com"
email=input("enter the mail which you want to send otp")
s.sendmail(user,email,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("wrong otp")
