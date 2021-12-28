import random
import smtplib

email = smtplib.SMTP("smtp.gmail.com",587)
email.starttls()

email.login("ajaysanjayingle7@gmail.com","ajay@123")

otp= random.randint(1000,9999)
otp = str(otp)

email.sendmail("ajaysanjayingle7@gmail.com","ajaysanjayingle7@gmail.com",otp)

print("OTP sent successfully")
email.quit()