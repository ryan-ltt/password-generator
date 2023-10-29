from tkinter import *
import tkinter as tk
import random
import string
import pyperclip
length = 0
window = tk.Tk()
window.title('Password Generator')
window.geometry('350x250')
textfield = Text(window, height = 1, width = 50)
def copy():
    pyperclip.copy(l.cget("text"))
def generate_pw():
    length = (textfield.get('1.0', 'end-1c'))  
    if length == '':
        length = 0
        l.config(text = "Please input a password length.")
    else:
        length = int(length)
    start = 0
    end = 0
    total = 0
    choices = []
    for i in listvar:
        total+= i.get()
    if total - 8 >= 0:
        choices.append(1)
        total-=8
    if total - 4 >= 0:
        choices.append(2)
        total-=4
    if total - 2 >= 0:
        choices.append(3)
        total -=2
    if total - 1 >= 0:
        choices.append(4)
        total -=1
    pw = ""
    for i in range(length):
        choice = random.SystemRandom().choice(choices)
        match(choice):
            case 1:
                pw = pw + generate_upper()
            case 2:
                pw = pw + generate_lower()
            case 3:
                pw = pw + generate_numbers()
            case 4:
                pw = pw + generate_symbols()           
    l.config(text = pw)
        
def generate_upper():
    return (random.SystemRandom().choice(string.ascii_uppercase))
def generate_lower():
    return (random.SystemRandom().choice(string.ascii_lowercase))
def generate_numbers():
    return (random.SystemRandom().choice(string.digits))
def generate_symbols():
    return (random.SystemRandom().choice(string.punctuation))

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
listvar = [var1, var2, var3, var4]


l = tk.Label(window, bg='white', width=200, text='')
enter_pw = tk.Label(window, bg = "white", width = 200, text = "Enter password length")

button = Button(window, text = "Generate", command = lambda:generate_pw())
clipboard_button = Button(window, text = "Copy to clipboard", command = lambda:copy())
enter_pw.pack()
textfield.pack()
button.pack()

c1 = tk.Checkbutton(window, text='Include Uppercase',variable=var1, onvalue = 8, offvalue = 0)
c1.pack()
c2 = tk.Checkbutton(window, text='Include Lowercase',variable=var2, onvalue = 4, offvalue = 0)
c2.pack()
c3 = tk.Checkbutton(window, text = "Include numbers" , variable = var3, onvalue = 2, offvalue = 0)
c3.pack()
c4 = tk.Checkbutton(window, text = "Include symbols" , variable = var4, onvalue = 1, offvalue = 0)
c4.pack()

l.pack()
clipboard_button.pack()
window.mainloop()
