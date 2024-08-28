import smtplib
import datetime as dt
import random


# my_email = "fabioerods@gmail.com"
# password = "lvryqfhzokoornku"
#
# # Corrected SMTP server address
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="fabs7777@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of the email."
#     )

now = dt.datetime.now()
weekday =  now.weekday()
my_email = "fabioerods@gmail.com"
password = "lvryqfhzokoornku"

lines_list = open('quotes.txt').read().splitlines()
randon_num = random.randint(0, len(lines_list) + 1)
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="faboorod2@gmail.com",
            msg=f"Subject:Monday motivation \n\n{lines_list[randon_num]}"
        )
