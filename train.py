from tkinter import*   
from tkinter import ttk
from tkinter import font
from wsgiref.validate import validator
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Training data")


        title_lbl=Label(self.root,text="Train Data",font=("Algerian",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"gradient_img.jpg")
        img_top=img_top.resize((1530,745),Image.ANTIALIAS)
        # antialas is used for compressing images
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        g_img =Label(self.root,image=self.photoimg_top)
        g_img.place(x=0,y=45,width=1530,height=745)

        #button
        b1=Button(self.root,text="TRAIN DATA",cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1.place(x=0,y=380,width=1530,height=60) 

        img_bottom=Image.open(r"gradient_img.jpg")
        img_bottom=img_top.resize((1530,745),Image.ANTIALIAS)
        # antialas is used for compressing images
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        g_img =Label(self.root,image=self.photoimg_top)
        g_img.place(x=0,y=440,width=1530,height=745)

      
    def train_classifier(self):
        data_dir=("data")
        path =[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale images
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image[1].split('.'[1])))


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)   

        #============train_classifier============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed") 





if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
