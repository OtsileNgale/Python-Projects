import time
import calendar
import tkinter as tk
from tkinter import *
from tkinter import ttk

#method to print current date and time
d2 = time.asctime(time.localtime(time.time()))
print("Current date and time: ", d2)

#choose date
year = int(input("enter year:"))
month = int(input("Enter month as a number:"))

#method to print calendar
c1 = calendar.month(year, month)
print(c1)

#GUI code
top = tk.Tk()

label = tk.Label(
    text = year
    
    )
label.pack()



top.mainloop()