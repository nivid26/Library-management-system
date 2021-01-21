from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from addbook import *
from deletebook import *
from viewbook import *
from issuebook import *
from returnboook import *
from help import *

mypass= "root"
mydatabase="db"
con=pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur=con.cursor()

root=Tk()
root.title("Library")
root.resizable(0,0)
root.geometry("500x500+300+50")

background_image=Image.open("123.png")

img=ImageTk.PhotoImage(background_image)
Canvas1=Canvas(root)
Canvas1.create_image(250,250,image=img)

Canvas1.pack(expand=True,fill=BOTH)
headingframe1= Frame(root,bg="grey",bd=1)
headingframe1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headinglabel=Label(headingframe1,text="Welcome to Books\n Management System", bg='black',fg='white', font=('Courieer',15))
headinglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

btn1=Button(root,text="Add Book\n Details",bg='silver',fg='black',font=('Times new roma',10,"bold"),relief=RAISED,borderwidth=8,command=addBook)
btn1.place(relx=0.15,rely=0.4,relwidth=0.2,relheight=0.2)
btn1.tk_focusFollowsMouse()

btn2=Button(root,text="Delete Book",fg='black',bg="silver",font=('Times new roma',10,"bold"),relief=RAISED,borderwidth=8,command=delete)
btn2.place(relx=0.38,rely=0.4,relwidth=0.2,relheight=0.2)

btn3=Button(root,text="View Book\n List",fg='black',bg='silver',font=('Times new roma',10,"bold"),relief=RAISED,borderwidth=8,command=view)
btn3.place(relx=0.61,rely=0.4,relwidth=0.2,relheight=0.2)

btn4=Button(root,text="Issue Book\nto Student",bg="silver",fg='black',font=('Times new roma',10,"bold"),relief=RAISED,borderwidth=8,command=issueBook)
btn4.place(relx=0.28,rely=0.63,relwidth=0.2,relheight=0.2)

btn5=Button(root,text="Return Book",fg='black',bg='silver',font=('Times new roma',10,"bold"),relief=RAISED,borderwidth=8,command=returnBook)
btn5.place(relx=0.51,rely=0.63,relwidth=0.2,relheight=0.2)

#btn6=Button(root,text="Help",fg='black',bg='silver',font=('Times new roma',10,"bold"),relief=RAISED,borderwidth=8,command=helpp)
#btn6.place(relx=0.61,rely=0.63,relwidth=0.2,relheight=0.2)


root.mainloop()