import tkinter as tk

window = tk.Tk()
greeting = tk.Label(
    text = "Hello my world!",
    foreground = 'white',
    background = 'black',
    width = 10,
    height = 7
    )
greeting.pack()

button = tk.Button(
    text = "click",
    width = 5,
    height = 5,
    bg = "blue",
    fg = "yellow"
    )
button.pack()

entry = tk.Entry()
entry.pack()

name = entry.get()

window.mainloop()
