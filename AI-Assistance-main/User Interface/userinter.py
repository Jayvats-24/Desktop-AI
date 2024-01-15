import tkinter as tk
from tkinter import *
from tkinter.ttk import Label


def create_rectangle_outline(parent, width, height, border_color="white", border_width=2):
    frame = tk.Frame(parent, width=width, height=height, borderwidth=border_width, relief="solid", background="#2C2C2C")
    return frame

root=tk.Tk()

root['background']='#2C2C2C'
root.geometry('1000x1000')
root.title("Memo AI")

# creating a rectangle box that will put the suggestion content
rectangle_frame = create_rectangle_outline(root, width=900, height=300)


lable1=Label(root,text="Welcome User, I am Memo",font=("Arial",25),foreground='white',background="#2C2C2C")
lable1.pack(padx=20,pady=40)

head=Label(rectangle_frame,text=" Suggestions ",foreground='white',font=("Arial",20),background='#2C2C2C')
head.pack(padx=8,pady=8)


eg1=Label(rectangle_frame,text=" '' 1. Google Search '' ",foreground='white',font=("Arial",10),background='#2C2C2C')
eg1.pack(padx=8,pady=8)


eg2=Label(rectangle_frame,text=" '' 2. Youtube Search '' ",foreground='white',font=("Arial",10),background='#2C2C2C')
eg2.pack(padx=8,pady=8)

eg3=Label(rectangle_frame,text=" '' 3. System Information '' ",foreground='white',font=("Arial",10),background='#2C2C2C')
eg3.pack(padx=8,pady=8)

eg4=Label(rectangle_frame,text=" '' 4. Location Fetch '' ",foreground='white',font=("Arial",10),background='#2C2C2C')
eg4.pack(padx=8,pady=8)

eg5=Label(rectangle_frame,text=" '' 5. Calling and message Capability '' ",font=("Arial",10),foreground='white',background='#2C2C2C')
eg5.pack(padx=8,pady=8)

rectangle_frame.pack(padx=10,pady=10)

label=Label(root,text=" I am Listening Whatever You Say.....",font=("Arial",20),foreground='white',background='#2C2C2C')
label.pack(padx=0,pady=50)

label=Label(root,text="For better Experience Keep in touch with Terminal window",font=("Arial",15),foreground='white',background='#2C2C2C')
label.pack(padx=0,pady=0)

root.mainloop()
