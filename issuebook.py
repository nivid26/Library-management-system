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

allbid=[]

def issue():
    global issuebtn,labelframe,lb1,inf1,inf2,quitbin,root,Canvas1,status

    bid=inf1.get()
    issueto=inf2.get()

    issuebtn.destroy()
    labelframe.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractbid="select bid from "+booktable
    try:
        cur.execute(extractbid)
        con.commit()
        for i in cur:
            allbid.append(i[0])

        if bid in allbid:
            checkavail="select status from "+booktable+" where bid='"+bid+"'"
            cur.execute(checkavail)
            con.commit()
            for i in cur:
                check=i[0]
            if check=='available':
                status=True
            else:
                status=False


        else:
            messagebox.showinfo("Error","BOOK ID NOT PRESENT")


    except:
        messagebox.showinfo("ERROR","CANNOT FETCH BOOK IDs")


    issuesql="insert into "+issuetable+" values('"+bid+"','"+issueto+"')"
    updatestatus="update "+booktable+" set status ='issued' where bid ='"+bid+"'"
    #try:
    if status == True:
        cur.execute(issuesql)
        con.commit()
        cur.execute(updatestatus)
        con.commit()
        messagebox.showinfo('SUCCESS','BOOK ISSUED SUCCESSFULLY')
        root.destroy()
    else:
        allbid.clear()
        messagebox.showinfo('MESSAGE','BOOK ALREADY ISSUED')
        return

    #except:
        #messagebox.showinfo('SEARCH ERROR',"THE VALUE ENTERES IS WRONG, TRY AGAIN")
        #root.destroy()



    print(bid)
    print(issueto)
    allbid.clear()




def issueBook():
    global issuebtn, labelframe, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelframe = Frame(root, bg='black')
    labelframe.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelframe, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelframe)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name
    lb2 = Label(labelframe, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelframe)

    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issuebtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=issue)
    issuebtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()