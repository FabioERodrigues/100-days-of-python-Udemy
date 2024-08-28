from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=300, height=50)
window.config(padx=20, pady=20)

label = Label(text="Miles")
label.grid(column=2, row=0)
#Entries



label2 = Label(text="is equal to")
label2.grid(column=0, row=1)



label4 = Label(text="Km")
label4.grid(column=2, row=1)

entry = Entry(width=7)
# Add some text to begin with
entry.insert(END, string=" ")
# Gets text in entry
print(entry.get())
entry.grid(column=1, row=0)



label3 = Label(text="0")
label3.grid(column=1, row=1)

def convert():
    miles = entry.get()
    mile_int = float(miles)
    km = mile_int *  1.609
    label3.config(text=f"{km}")

button = Button(text="calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
