#!/bin/python3
import tkinter as tk
from PIL import *
root=tk.Tk()

#image label 
bg=tk.PhotoImage(file="life.png")
frame =tk.Frame(root, width=600, height=400)  # creating frame
frame.pack(expand=True,fill="both")
frame.place(anchor='center', relx=0.5, rely=0.5)
tk.Label(frame,image=bg).place(x=0,y=0)

root.geometry("580x400-320+170")
h=tk.Label(root,text="Password Generator",bd=1,bg="yellow",font=("Helvatica",14))
h.place(relx=0.01,rely=0.01)
root.title("Password Generator")

name=tk.Label(frame,text="Name : ",bd=2,bg="yellow",font=("Helvatica",14))
name.place(relx=0.08,rely=0.4)

e=tk.Entry(root,width=30)
e.place(relx=0.22,rely=0.4)
r=tk.Label(root,text="",bd=2,bg="yellow",font=("Arial",14))
r.place(relx=0.1,rely=0.7)

root.resizable(False,False)

icon=tk.PhotoImage(file="life.png")
root.iconphoto(False,icon)
def password():
        string=e.get()
        l=list(string)
        p=""
        for i in range(len(l)):
               o=int(ord(l[i]))
               if(o%2==0):
                     d=o//2
                     n=f"M{d}W2"
                     p=p+n
               elif(o%2!=0):
                      d=(o-1)//2
                      n=f"M{d}W2P1"
                      p=p+n  
        r.config(text=p)                  
       



b=tk.Button(root,text="Generate",cursor="hand2",bg="cyan",command=password,font=("Helvatica",14))
b.place(relx=0.65,rely=0.39)

root.mainloop()

