# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
from tkinter import *
import tkinter.messagebox
from random import choice, shuffle, sample, randint
import string


# Generate a password
def gen_password():
    password = ''
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    symbols = ['!', '§', '$', '%', '%', '&', '/', '(', ')', '=']
    numbers = [str(i) for i in range(0, 10)]
    for _ in range(4):
        password_upper = sample(letters_upper, randint(2, 5))
        password_lower = sample(letters_lower, randint(2, 5))
        password_number = sample(numbers, randint(2, 5))
        password_symbols = sample(symbols, randint(3, 8))
        password = password_upper + password_lower + password_number + password_symbols
    password = list(password)
    shuffle(password)
    password = ''.join(password)
    passentry.delete(0, END)
    passentry.insert(0, password)
    # return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Add an Entry
def add_entry():
    global websiteentry, userentry, passentry
    website = websiteentry.get()
    user = userentry.get()
    password = passentry.get()
    # print(website, user, password)
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        tkinter.messagebox.showwarning('Error', 'All fields must be filled!')
    else:
        write_file(website, user, password)
        delete_entries()


# Write to file
def write_file(website, user, password):
    with open(file='pw.txt', mode='a') as pwfile:
        pwfile.write(f'{website} | {user} | {password} \n')
        tkinter.messagebox.showinfo('Success!', 'Entry added!')


def delete_entries():
    websiteentry.delete(0, END)
    passentry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


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

lwebsite = Label(text='Website: ', bg='white', anchor='center', highlightbackground='white')
lwebsite.grid(column=0, row=2, sticky='w')
websiteentry = Entry(width=35)
websiteentry.focus()
websiteentry.grid(column=1, row=2, columnspan=2, sticky='w')

# Username Stuff

lusername = Label(text='Email/Username: ', bg='white', anchor='center')
lusername.grid(column=0, row=3, sticky='w')
userentry = Entry(width=35, bd=0)
userentry.grid(column=1, row=3, columnspan=2, sticky='w')
userentry.insert(0, 'bla@mail.com')

# Password Stuff

lpass = Label(text='Password: ', bg='white', anchor='center')
lpass.grid(column=0, row=4, sticky='w')
passentry = Entry(width=21, highlightthickness=0)
passentry.grid(column=1, row=4, columnspan=1, sticky='w')
passbutton = Button(text='Generate Password', width=10, background='white', command=gen_password)
passbutton.grid(column=2, row=4, sticky='w')

addbutton = Button(text='Add', anchor='center', width=36, command=add_entry)
addbutton.grid(column=1, row=5, columnspan=2)

window.mainloop()
