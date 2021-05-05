from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from tkinter.ttk import *
from add import *
from delete import *
from view import *

mypass = "password_here"
mydatabase="database_name_here"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Music Library Management System")
root.minsize(width=400,height=400)
root.geometry("800x600")

background_image =Image.open("main.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*0.7)
newImageSizeHeight = int(imageSizeHeight*0.7)
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#dfdee2",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to\nMusic Library Management System", bg="black", fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Track",font='Helvetica 10 bold',bg='black', fg='white', command=addsong)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Delete Track",font='Helvetica 10 bold',bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="View Tracks",font='Helvetica 10 bold',bg='black', fg='white', command=view)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

root.mainloop()
