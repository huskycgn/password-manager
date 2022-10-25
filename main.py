# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.config(padx=20, pady=20, background='white')
window.title('Password Manager')
logo_can = Canvas(window, background='white', width=200, height=200, highlightthickness=0)
# logo_can.grid(column=1, row=1, padx=20, pady=20)
logo_img = PhotoImage(file='logo.png')
logo_can.create_image(100, 100, anchor='center', image=logo_img)
# logo_can.create_image(100, 100, anchor='center', image=logo_img)

logo_can.grid(column=1, row=1)

# Website Data

lwebsite = Label(text='Website: ', bg='white', anchor='center')
lwebsite.grid(column=0, row=2, sticky='w')
websiteentry = Entry(width=35)
websiteentry.grid(column=1, row=2, columnspan=2, sticky='w')

# Username Stuff

lusername = Label(text='Email/Username: ', bg='white', anchor='center')
lusername.grid(column=0, row=3, sticky='w')
userentry = Entry(width=35)
userentry.grid(column=1, row=3, columnspan=2, sticky='w')

# Password Stuff

lpass = Label(text='Password: ', bg='white', anchor='center')
lpass.grid(column=0, row=4, sticky='w')
passentry = Entry(width=21)
passentry.grid(column=1, row=4, columnspan=1, sticky='w')
passbutton = Button(text='Generate Password', width=10, background='white')
passbutton.grid(column=2, row=4, sticky='w')

addbutton = Button(text='Add', anchor='center', width=36)
addbutton.grid(column=1, row=5, columnspan=2)

window.mainloop()