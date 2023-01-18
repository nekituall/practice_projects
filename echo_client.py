
#Клиентская сторона
from tkinter import *
from tkinter import ttk
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

def send():
    sock.send(entry.get().encode())
    data = sock.recv(1024).decode()
    label3["text"] = data

def finish():
    win.destroy()
    sock.send("sock_close".encode())
    sock.close()

win = Tk()
win.title("Echo client")
win.geometry("300x250")

label1 = ttk.Label(text="Enter your text here:  ")
label1.grid(column=0, row=0, pady=5, padx=4)

entry = ttk.Entry()
entry.grid(column=1, row=0, pady=5)

but1 = ttk.Button(text="Click to get echo!", command=send, width=20)
but1.grid(column=0, columnspan=2, row=1, pady=5)

label2 = ttk.Label(text="Get your echo here:  ")
label2.grid(column=0, row=2, pady=5, padx=4)

label3 = ttk.Label()
label3.grid(column=1, row=2, pady=5)


win.protocol("WM_DELETE_WINDOW", finish)
win.mainloop()



