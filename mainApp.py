import tkinter as tk
from tkinter import *
import subprocess

window = tk.Tk()
window.title("Password Saver")
window.geometry("500x500")
window.resizable(0,0)
window.configure(bg = "light blue")

app = StringVar()
email = StringVar()
passw = StringVar()

file = r"file.txt" #! ENTER .txt FILE DESTINATION HERE
f = open(file, 'a')

#? =============================================================

def GeneratePassword():
    X = password.get()
    f.write(X + "\n")
def GenerateApp():
    X = app.get()
    f.write("\n" + X + " : ")
def GenerateEmail():
    X = email.get()
    f.write(X + " : ")
    
def GenAll():
    GenerateApp()
    GenerateEmail()
    GeneratePassword()
    f.close()

def Close():
    window.destroy()
    subprocess.run(['notepad.exe', file])

#? =============================================================

label = Label(window, text = "Password Saver", font = ("Arial", 30), bg = "light blue")
label.pack()

label1 = Label(window, text = "App Name", font = ("Arial", 15), bg = "light blue")
label1.pack()

#?

password = Entry(window, textvariable = app, font = ("Arial", 15))
password.pack()

#?

label1 = Label(window, text = "Email", font = ("Arial", 15), bg = "light blue")
label1.pack()

password = Entry(window, textvariable = email, font = ("Arial", 15))
password.pack()

#?

label1 = Label(window, text = "Password", font = ("Arial", 15), bg = "light blue")
label1.pack()


password = Entry(window, textvariable = passw, font = ("Arial", 15))
password.pack()

#?

button = Button(window, text = "Generate", font = ("Arial", 15), command = GenAll)
button.pack()

button = Button(window, text = "Close", font = ("Arial", 15), command = Close)
button.pack()

#? =============================================================

window.mainloop()