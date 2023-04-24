import tkinter as tk
from main import login, ILOVEPLAYLISTREADING,SartTesting

from tkinter import ttk
login()
"""
FOR SOME REASON ALSO GONNA PUT BUTTON SIZES HERE MAN THIS IS UGLY ASL
"""
BWidth1 = 50
BHeight1 = 15
BWidth2 = 50
BHeight2 = 31
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
def switch():
    if button1["state"] == "normal":
        button1["state"] = "disabled"

def THE_CREACHURE():
    print("yeah")
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
button1 = tk.Button(root,
    text="Button-1",
    height= BHeight1,
    width= BWidth1,
    command = ILOVEPLAYLISTREADING)

button1.place(x=128, y=50)

button2 = tk.Button(root,
    text="Button-2",
    height=BHeight1,
    width=BWidth1,
    command=THE_CREACHURE)
button2.place(x=128, y=300)

button3 = tk.Button(root,
    text="Button-3",
    height=BHeight2,
    width=BWidth2,
    command=THE_CREACHURE)
button3.place(x=512, y=50)

#Create a Label
label = tk.Label(root, text="QM",).pack()


#similar artists section







root.mainloop()