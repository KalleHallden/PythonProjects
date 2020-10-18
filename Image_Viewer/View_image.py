from tkinter import *
from PIL import Image,ImageTk
import os

root=Tk()
root.geometry('1000x1000')




def resize_image(root,copy1,label1):
    nh=700
    nw=900
    image=copy1.resize((nw,nh))
    photo=ImageTk.PhotoImage(image)
    
    label1.configure(image=photo)
    label1.image=photo


n=0

def next1():
    global n
    global items_list
    n=(n+1)%len(items_list)
    img=items_list[n]
    
    image=Image.open('./Screenshots/'+img)
    copy1=image.copy()
    photo=ImageTk.PhotoImage(image)
    
    label=Label(root,image=photo)
    label.bind('<configure>',resize_image(root,copy1,label1))
    label.pack()



def previous():
    global n
    global items_list
    n=(n-1)
    img=items_list[n]
    image=Image.open('./Screenshots/'+img)
    copy1=image.copy()
    photo=ImageTk.PhotoImage(image)
    
    label=Label(root,image=photo)
    label.bind('<configure>',resize_image(root,copy1,label1))
    label.pack()



items_list=os.listdir('Screenshots')

img1=items_list[n]

image=Image.open('./Screenshots/'+img1)
copy1=image.copy()
photo=ImageTk.PhotoImage(image)

label1=Label(root,image=photo)
label1.bind('<configure>',resize_image(root,copy1,label1))

label1.pack()

b1=Button(root,text=">>",width=5,height=10,command=next1)
b1.place(x=955,y=350)

b1=Button(root,text="<<",width=5,height=10,command=previous)
b1.place(x=0,y=350)


root.mainloop()

