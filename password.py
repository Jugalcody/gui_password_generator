#!/bin/python3
import tkinter as tk,os
root=tk.Tk()

#image label

  

try:
        n=f'{os.getcwd()}/life.png'
        bg=tk.PhotoImage(file=(r''+str(n)))
        frame =tk.Frame(root, width=600, height=400)  # creating frame
        frame.pack(expand=True,fill="both")
        frame.place(anchor='center', relx=0.5, rely=0.5)
        tk.Label(frame,image=bg).place(x=0,y=0)

              
except:
         frame=root
                
root.geometry("580x400-320+170")
h=tk.Label(root,text="Password Generator",bd=1,bg="yellow",font=("Helvatica",14))
h.place(relx=0.01,rely=0.01)
root.title("Password Generator")

name=tk.Label(frame,text="Name : ",bd=2,bg="yellow",font=("Helvatica",14))
name.place(relx=0.08,rely=0.4)

e=tk.Entry(root,width=30,font=("Helvatica",14,"bold"),bd=4)
e.place(relx=0.22,rely=0.395)
r=tk.Label(root,text="",bd=2,bg="yellow",font=("Helvatica",14))
r.place(relx=0.01,rely=0.7)

root.resizable(False,False)

  
n=f'{os.getcwd()}/im.png'
try:
         icon=tk.PhotoImage(file=(r''+str(n)))
         root.iconphoto(False,icon)
              
except:
         pass
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
b.place(relx=0.15,rely=0.49)

root.mainloop()

