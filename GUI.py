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
ID=tk.StringVar()

"""
PUTTING THE BUTTONS HERE BECUSE BIG COPE I CANT PUT THEM AFTER
"""
button1= 0
button2= 0
button3= 0

def callback(url):
    webbrowser.open_new_tab(url)

def switch():
    if button1.winfo_exists() == 1:
        button1.place_forget()
    elif button1.winfo_exists() == 0:
        button1.place
    button2.place_forget()
    button3.place_forget()
    e1.place(x=E1posX, y= E1posY)
    L1.place(x=E1posX, y = E1posY-20)
    B1.place(x=E1posX, y=E1posY+20)
    GB.pack(anchor= "w",side = "bottom")
    link.pack()

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
    text="ReadPlaylist",
    height= BHeight1,
    width= BWidth1,
    command = switch,
    cursor="hand2")

button1.place(x=128, y=50)

button2 = tk.Button(root,
    text="Button-2",
    height=BHeight1,
    width=BWidth1,
    command=THE_CREACHURE,
    cursor="hand2")
button2.place(x=128, y=300)
def testing():
    playlist_id = ID.get()
    ID.set("")
    print(ID)
    ILOVEPLAYLISTREADING()
button3 = tk.Button(root,
    text="Button-3",
    height=BHeight2,
    width=BWidth2,
    command=THE_CREACHURE,
    cursor="hand2")
button3.place(x=512, y=50)

#text box somewhere around here
e1 = tk.Entry(root, textvariable=ID, width=30)
L1 = tk.Label(root, text="insert playlist id")
B1 = tk.Button(root, text="Got it!", command=testing)
link = tk.Label(root, text="How can I find my playlist id?", font=("Helveticabold", 15), fg= "blue", cursor="hand2")
link.bind("<Button-1>", lambda e:
callback("https://clients.caster.fm/knowledgebase/110/How-to-find-Spotify-playlist-ID.html#:~:text=To%20find%20the%20Spotify%20playlist,Link%22%20under%20the%20Share%20menu.&text=The%20playlist%20id%20is%20the,after%20playlist%2F%20as%20marked%20above."))
#Create a Label
GB = tk.Button(root, text="Go back!", command= switch)
label = tk.Label(root, text="QM",).pack()


#similar artists section


root.mainloop()