from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
mypass="root"
mydatabase="db"

con=pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur=con.cursor()

issuetable="books_issued"
booktable="books"

def deletebook():

    bid=bookinfo1.get()
    deletesql="delete from "+booktable+" where bid='"+bid+"'"
    deleteissue="delete from "+issuetable+" where bid='"+bid+"'"
    try:
        cur.execute(deletesql)
        con.commit()
        cur.execute(deleteissue)
        con.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo('Error',"Please check BOOK ID")
        print(bid)
        bookinfo1.delete(0,END)
    root.destroy()

def delete():
    global bookinfo1,bookinfo2,bookinfo3,bookinfo4,Canvas1,con,cur,booktable,root
    root=Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1=Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
    headingframe1=Frame(root,bg='#FFBB00',bd=5)
    headingframe1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headinglable1=Label(headingframe1,text="Delete Book",bg='black',fg='white',font=('Courier',15))
    headinglable1.place(relx=0,rely=0,relwidth=1,relheight=1)
    labelframe=Frame(root,bg='black')
    labelframe.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    lb2=Label(labelframe,text="Book ID: ",bg='black',fg='white')
    lb2.place(relx=0.05,rely=0.5)
    bookinfo1=Entry(labelframe)
    bookinfo1.place(relx=0.3,rely=0.5,relwidth=0.62)
    submitbtn=Button(root,text="SUBMIT",bg='#d1ccc0',fg='black',command=deletebook)
    submitbtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    quitbtn = Button(root, text="QUIT", bg='#f7f1e3', fg='black', command=root.destroy)
    quitbtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()

