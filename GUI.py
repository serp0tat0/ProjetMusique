import tkinter as tk
from main import login, ILOVEPLAYLISTREADING,SartTesting
from passwords_ts import playlist_id

import webbrowser

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
E1posX = 128
E1posY = 50
ID = tk.StringVar()
AN = tk.StringVar()
#also putting the button positions here, don't feel like actually copying and pasting them
B1posX=128
B1posY=50
B2posX=128
B2posY=300
B3posX=512
B3posY=50

"""
PUTTING THE BUTTONS HERE BECUSE BIG COPE I CANT PUT THEM AFTER
"""
button1= 0
button2= 0
button3= 0

def callback(url):
    webbrowser.open_new_tab(url)

def defaultswitch(): #literally the default thing, gonna spawn things accordingly to avoid repetition
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    GB.pack(anchor="w", side="bottom")

def switch():
    defaultswitch()
    e1.place(x=E1posX, y=E1posY)
    L1.place(x=E1posX, y=E1posY-20)
    B1.place(x=E1posX, y=E1posY+20)
    link.pack()

def switch2(): #the switch for the second button, could also just do it in one function. might do that actually.
    defaultswitch()
    e2.place(x=E1posX, y=E1posY)
    B2.place(x=E1posX. y=E1posy)


#SPAGHETTICODE MOMENT, not gonna place the buttons in the code itself but in the goback function
def goback():
    button1.place(x=B1posX, y=B1posY)
    button2.place(x=B2posX, y=B2posY)
    button3.place(x=B3posX, y=B3posY)
    e1.place_forget()
    L1.place_forget()
    B1.place_forget()
    GB.pack_forget()
    link.pack_forget()
    exit_button.pack(anchor="e", side="bottom")


exit_button = ttk.Button(
    root,
    text="Exit",
    command=lambda: root.quit(),
    cursor="hand2"
)
# Create Buttons in the frame
button1 = tk.Button(root,
    text="ReadPlaylist",
    height= BHeight1,
    width= BWidth1,
    command = switch,
    cursor="hand2")


button2 = tk.Button(root,
    text="Button-2",
    height=BHeight1,
    width=BWidth1,
    command=switch2,
    cursor="hand2")
def PReadButton():



    print(ID.get())
    ILOVEPLAYLISTREADING(ID.get())

def SArtistsButton():
    print(AN.get())
    SartTesting(AN.get())
button3 = tk.Button(root,
    text="Button-3",
    height=BHeight2,
    width=BWidth2,
    cursor="hand2")

#text box somewhere around here

e1 = tk.Entry(root, textvariable=ID, width=30)
e2 = tk.Entry(root, textvariable=AN, width=30)
L1 = tk.Label(root, text="insert playlist id")
B1 = tk.Button(root, text="Got it!", command=PReadButton)
B2 = tk.Button(root,text="Got it!")

link = tk.Label(root, text="How can I find my playlist id?", font=("Helveticabold", 15), fg= "blue", cursor="hand2")
link.bind("<Button-1>", lambda e:
callback("https://clients.caster.fm/knowledgebase/110/How-to-find-Spotify-playlist-ID.html#:~:text=To%20find%20the%20Spotify%20playlist,Link%22%20under%20the%20Share%20menu.&text=The%20playlist%20id%20is%20the,after%20playlist%2F%20as%20marked%20above."))
#Create a Label
GB = tk.Button(root, text="Go back!", command=goback)
label = tk.Label(root, text="QM",).pack()
goback()

#similar artists section


root.mainloop()