import tkinter as tk
from main import login, ILOVEPLAYLISTREADING,SartTesting

from tkinter import ttk

root = tk.Tk()
root.geometry("1024x576")
root.resizable(False,False)
root.title("Button Demo")
"""
PUTTING THE BUTTONS HERE BECUSE BIG COPE I CANT PUT THEM AFTER
"""
button1= 0
button2= 0
button3= 0
def THE_CREACHURE():
#uhhgghhhhhhhh yeah
    button1 = tk.DISABLED
    button2 = tk.DISABLED
    button3 = tk.DISABLED

exit_button = ttk.Button(
    root,
    text="Exit",
    command=lambda: root.quit()
)
# Create Buttons in the frame
button1 = tk.Button(root, text="Button-1", command=lambda: THE_CREACHURE)
button1.place(x=512, y=125)

button2 = tk.Button(root, text="Button-2")
button2.place(x=512, y=175)

button3 = tk.Button(root, text="Button-3")
button3.place(x=512, y=225)

#Create a Label
label = tk.Label(root, text="QM",).pack()


#similar artists section







root.mainloop()