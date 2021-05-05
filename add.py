from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def songadd():

    title = songInfo1.get()
    artist = songInfo2.get()
    album = songInfo3.get()
    genre = songInfo4.get()
    rlsyr = songInfo5.get()
    
    try:  
        cur.execute('insert ignore into artist(artist_name) values(%s)',(artist))
        cur.execute("select id from artist where artist_name = '"+artist+"';")
        artist_id = cur.fetchone()[0]
        cur.execute('insert ignore into album(album_name, artist_id) values(%s,%s)',(album, artist_id))
        cur.execute("select id from album where album_name = '"+album+"';")
        album_id = cur.fetchone()[0]
        cur.execute('insert ignore into genre(genre_name) values(%s)',(genre))
        cur.execute("select id from genre where genre_name = '"+genre+"';")
        genre_id = cur.fetchone()[0]
        cur.execute('insert ignore into track(title, album_id, genre_id, artist_id, rlsyr) values(%s,%s,%s,%s,%s)',(title, album_id, genre_id, artist_id, rlsyr))
        con.commit()
        messagebox.showinfo('Success',"Song Added Successfully")
    except:
        messagebox.showinfo("Error","Can't Add Song Into Database")

    root.destroy()

def addsong():

    global img,songInfo1,songInfo2,songInfo3,songInfo4,songInfo5,Canvas1,con,cur,root

    root = Toplevel()
    root.title("Add Music Record")
    root.minsize(width=400,height=400)
    root.geometry("800x600")

    mypass = "password_here"
    mydatabase="database_name_here"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    background_image = Image.open("add.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth*0.25)
    newImageSizeHeight = int(imageSizeHeight*0.25)
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(300,340,image = img)
    Canvas1.config(bg="white", width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)
     
    headingFrame1 = Frame(root,bg="#2f2e2e",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Song Record",font='Helvetica 14 bold', bg= "#d7a26c", fg='black', )
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="#d7a26c")
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 =Label(labelFrame, text="Title:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb1.place(relx=0.05,rely=0.16, relheight=0.08,)

    songInfo1 = Entry(labelFrame)
    songInfo1.place(relx=0.3,rely=0.16, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame,text="Artist:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb2.place(relx=0.05,rely=0.32, relheight=0.08)

    songInfo2 = Entry(labelFrame)
    songInfo2.place(relx=0.3,rely=0.32, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame,text="Album:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb3.place(relx=0.05,rely=0.48, relheight=0.08)

    songInfo3 = Entry(labelFrame)
    songInfo3.place(relx=0.3,rely=0.48, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="Genre:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb4.place(relx=0.05,rely=0.64, relheight=0.08)

    songInfo4 = Entry(labelFrame)
    songInfo4.place(relx=0.3,rely=0.64, relwidth=0.62, relheight=0.08)

    lb5 = Label(labelFrame,text="Release Year:", font='Helvetica 13 bold',bg="#d7a26c", fg='black')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)

    songInfo5 = Entry(labelFrame)
    songInfo5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root,text="Submit",font='Helvetica 12 bold',bg='#d7a26c', fg='black',command=songadd)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",font='Helvetica 12 bold',bg='#d7a26c', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
