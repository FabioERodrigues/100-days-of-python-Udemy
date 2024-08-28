from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_var.get()
    email = email_var.get()
    password = passw_var.get()

    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("password_man.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("password_man.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            #updating old data with new data
            with open("password_man.json", "w") as file:
                #saving new data
                json.dump(data, file, indent=4)
        finally:
            entry_web.delete(0, END)
            entry_password.delete(0, END)

def search():
    website = web_var.get()
    try:
        with open("password_man.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Password manager", message="No Data file found.")

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"Password for {website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=f"Password manager", message="No details for the website exists.")






# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

web_var=StringVar()
email_var=StringVar()
passw_var=StringVar()

#Label website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#Label Email/username
email_label = Label(text="Email/username:")
email_label.grid(column=0, row=2)

#Label Password
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

#Entry web
entry_web = Entry(width=35, textvariable = web_var)
entry_web.grid(column=1, row=1, columnspan=2)

entry_web.focus() #sets the cursor to this entry
#Entry email
entry_email = Entry(width=35, textvariable = email_var)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "faboorod2@gmail.com")
#Entry password
entry_password = Entry(width=35, textvariable = passw_var)
entry_password.grid(column=1, row=3)

#Button generate password

button_gen_pass = Button(width=13, text="Generate Password", command=generate_password)
button_gen_pass.grid(column=3, row=3)

#Button Add
button_Add = Button(text="Add", width=30, command=save)
button_Add.grid(column=1, row=4, columnspan=3)

# Button find
button_find = Button(width=13, text="Search", command=search)
button_find.grid(column=3, row=1, columnspan=2)

window.mainloop()