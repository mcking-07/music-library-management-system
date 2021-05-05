from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "password_here"
mydatabase="database_name_here"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def deletesong():

    title = songInfo1.get()
    
    try:
        cur.execute("delete from track, album, artist using track join album join artist on track.artist_id=artist.id and track.album_id=album.id where track.title = '"+title+"';")
        con.commit()
        messagebox.showinfo('Success',"Song Record Deleted Successfully")
    except:
        messagebox.showinfo("Please Check Song Title")

    songInfo1.delete(0, END)
    root.destroy()

def delete():

    global img,songInfo1,songInfo2,songInfo3,songInfo4,songInfo5,Canvas1,con,cur,root

    root = Toplevel()
    root.title("Delete Music Recordd")
    root.minsize(width=400,height=400)
    root.geometry("800x600")

    background_image = Image.open("delete.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth*0.8)
    newImageSizeHeight = int(imageSizeHeight*0.8)
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300,340,image = img)
    Canvas1.config(bg="black", width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#dfdee2",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Song Record",font='Helvetica 14 bold', bg="#010103", fg='white',)
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg="#010103")
    labelFrame.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.2)

    lb2 = Label(labelFrame,text="Song Title:", font='Helvetica 11 bold', bg="#000000", fg='white')
    lb2.place(relx=0.05,rely=0.5)

    songInfo1 = Entry(labelFrame)
    songInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root,text="Submit",font='Helvetica 11 bold',bg="#010103", fg='white',command=deletesong)
    SubmitBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",font='Helvetica 11 bold',bg="#010103", fg='white', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)

    root.mainloop()
