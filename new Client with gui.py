import socket
import time
from threading import Thread
import tkinter as Chat
window = Chat.Tk()
window.geometry("700x350")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
Clients = Chat.Button(text="Clients", bg="blue", fg="yellow", width=15, height=3)
Clients.place(x=0, y=0)
send = Chat.Button(text="Send Message", bg="blue", fg="yellow", width=15, height=3)
send.place(x=0, y=58)
recive = Chat.Button(text="Recive Message", bg="blue", fg="yellow", width=15, height=3)
recive.place(x=0, y=116)
notification = Chat.Button(text="Notifications", bg="blue", fg="yellow", width=15, height=3)
notification.place(x=0,y=174)
help = Chat.Button(text="Help", bg="blue", fg="yellow", width=15, height=3)
help.place(x=0,y=232)
leave = Chat.Button(text="Exit", bg="blue", fg="yellow", width=15, height=3)
leave.place(x=0,y=290)

window.mainloop()
