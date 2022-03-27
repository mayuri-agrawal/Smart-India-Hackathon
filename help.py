from tkinter import*   
from tkinter import ttk
from tkinter import font
from wsgiref.validate import validator
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector
#import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Help Desk",font=("Algerian",35,"bold"),bg="light pink",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"gradient_img.jpg")
        img_top=img_top.resize((1530,745),Image.ANTIALIAS)
        # antialas is used for compressing images
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        g_img =Label(self.root,image=self.photoimg_top)
        g_img.place(x=0,y=45,width=1530,height=745)
        

        # class
        Class_label=Label(g_img,text="Email:dheer456jain@gmail.com",font=("times new roman",12,"italic"),bg="white")
        Class_label.grid(x=600,y=400)


if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()   