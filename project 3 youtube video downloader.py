from pytube import YouTube

from tkinter import *

root = Tk()

root.geometry("300x400")
root.title("you tube video downloader")

def youtube():
    a = var.get()   #https://www.youtube.com/watch?v=jkBfGvb7NzM
    ytvideo = YouTube(a).streams.filter(progressive=True,file_extension="mp4").order_by('resolution').desc().first()
    ytvideo.download(r"F:\\")
    print("Entry box",a)
    

l1 = Label(root,text="You Tube video",fg="Red",font=("bold"))
l1.place(x=50,y=20)

var = StringVar()
e1 = Entry(root,textvariable=var,width=60)
e1.place(x=40,y=80)

b1 = Button(root,text="Download",command=youtube,bg="green",width=20,fg="white")
b1.place(x=80,y=120)





root.mainloop()



