# Following will import tkinter.ttk module  
from tkinter.ttk import *
import tkinter as tk

# Following will import messagebox widget of tkinter module
import tkinter.messagebox

# Import for random number generator
import random


# Create Object tk
root = tk.Tk() 

# Initialize tkinter window with dimensions 500x500	
root.title('Login window')	 
root.geometry('500x500')
root.iconbitmap('./icons/login.ico')

# store email address and password
email_var = tk.StringVar()
password_var = tk.StringVar()


# The logic when 'Login' button is pressed
def Login():
  global btn
  email = email_var.get()
  password = password_var.get()
  
  # Check if the password and email are empty
  if (password == '') and (email == ''):
    tkinter.messagebox.showinfo("Missing inputs",  "Enter Email and Password")
  elif (password == '')and (email != ''):
    tkinter.messagebox.showinfo("Missing input",  "Enter Password")
  elif (email == '') and (password != ''):
    tkinter.messagebox.showinfo("Missing input",  "Enter Email")
  else:
    # if the password is wrong, change its position in the GUI
    if password != '12345':
      password_entry = tk.Entry(root, textvariable=password_var)
      password = password_var.get()
      btn.place(x = random.randrange(60, 400), y = random.randrange(45, 400))
    # if the password is correct, show the message and close the GUI
    else:
      tkinter.messagebox.showinfo("Hello",  "Correct Password")
      root.destroy()


# Create a Email Label and Email Entry and the place it should appear in the GUI
email_label = tk.Label(root, text="Email Address:")
email_label.grid(row = 0, column = 0, pady = 0, padx = 0)

email_entry = tk.Entry(root, textvariable=email_var)
email_entry.grid(row = 0, column = 1, pady = 0, padx = 0)


# Create a Password Label and Password Entry and the place it should appear in the GUI
password_label = tk.Label(root, text="Password:")
password_label.grid(row = 1, column = 0, pady = 0, padx = 0)

password_entry = tk.Entry(root, textvariable=password_var)
password_entry.grid(row = 1, column = 1, pady = 0, padx = 0)


# Create a Button and the place it should appear in the GUI
btn = Button(root, text = 'Login', command = Login)
btn.place(x = 60, y = 45)
  
root.mainloop()