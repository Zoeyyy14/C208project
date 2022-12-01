import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name=None
listBox=None
textArea=None
labelChat=None
text_message=None

def connectToServer():
    global SERVER
    global name
    global sending_files
    cName=name.get()
    SERVER.send(cName.encode())

def openChatWindow():
    print("\n\t\t\t IP MESSENGER")
    window=Tk()
    window.title("Music Window")
    window.geometry("500x350")
    global name
    global listBox
    global textArea
    global labelChat
    global text_message
    global filePathLabel

    nameLabel=Label(window,text="Enter Your Name", font=("Calibri", 10))
    nameLabel.place(x=10, y=8)

    name=Entry(window, width=30, font=("Calibri", 10))
    name.place(x=120, y=8)
    name.focus()

    connectServer=Button(window, text="Connect to chat server", bd=1, font=("Calibri", 10), command=connectToServer)
    connectServer.place(x=350, y=6)
    seperator=ttk.Separator(window,orient="horizontal")
    seperator.place(x=0, y=35, relwidth=1, height=0.1)

    labelUsers=Label(window, text="Active Users", font=("Calibri, 10"))
    labelUsers.place(x=10, y=50)

    listBox=Listbox(window, height=5, width=67, activestyle="dotbox", font=("Calibri, 10"))
    listBox.place(x=10, y=70)

    scrollbar1=Scrollbar(listBox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command=listBox.yview)
    
    connectButton=Button(window, text="Connect", bd=3, font=("Calibri, 10"))
    connectButton.place(x=282, y=160)
    
    disconnectButton=Button(window, text="Disconnect", bd=3, font=("Calibri, 10"))
    disconnectButton.place(x=350, y=160)

    refresh=Button(window, text="Refresh", bd=3, font=("Calibri, 10"))
    refresh.place(x=435, y=160)

    labelChat=Label(window, text="Chat window", font=("Calibri, 10"))
    labelChat.place(x=10, y=180)
    textArea=Text(window, width=68, height=6, font=("Calibri, 10"))
    textArea.place(x=10, y=200)

    scrollbar2=Scrollbar(listBox)
    scrollbar2.place(relheight=1, relx=1)
    scrollbar2.config(command=listBox.yview)

    attach=Button(window, text="Attach and send", bd=3, font=("Calibri, 10"))
    attach.place(x=10, y=305)
    
    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    openChatWindow()

setup()
