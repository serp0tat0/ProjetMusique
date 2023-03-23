import tkinter as tk
from main import login, ILOVEPLAYLISTREADING,SartTesting

window = tk.Tk()
window.title("Hello Python")
window.geometry
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()
window.mainloop()
