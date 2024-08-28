##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import os
import smtplib
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
def birth_day():
    now = dt.datetime.now()
    day = now.day
    month = now.month
    matches = []  # List to store all matching birthdays
    for index, row in data.iterrows():
        if row['month'] == month and row['day'] == day:
            name = row['name']
            email = row['email']
            matches.append((name, email))  # Append matching names and emails

    if matches:  # If there are any matches
        return True, matches
    else:
        return False, None
# Now handle all the matches
is_birthday, matches = birth_day()
if is_birthday:
    PLACEHOLDER = "[NAME]"
    for name, email in matches:
        random_file = random.choice(os.listdir("letter_templates"))
        with open(f"./letter_templates/{random_file}") as letter:
            personal_letter = letter.read()
            new_letter = personal_letter.replace(PLACEHOLDER, name)
            # Send the email
            my_email = "fabioerods@gmail.com"
            password = "lvryqfhzokoornku"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:Birthday wishes\n\n{new_letter}"
                )