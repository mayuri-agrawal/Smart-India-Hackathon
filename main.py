# used for gui

from tkinter import*   
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance System")
# first image
        img=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\s8.jpg")
        img=img.resize((1530,250),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=250)
        
# # second image
#         img1=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\s7.jpg")
#         img1=img1.resize((500,230),Image.ANTIALIAS)
#         self.photoimg1=ImageTk.PhotoImage(img1)

#         f_lbl=Label(self.root,image=self.photoimg1)
#         f_lbl.place(x=500,y=0,width=500,height=230)
        
# #  third image
#         img2=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\s6.jpg")
#         img2=img2.resize((500,230),Image.ANTIALIAS)
#         self.photoimg2=ImageTk.PhotoImage(img2)

#         f_lbl=Label(self.root,image=self.photoimg2)
#         f_lbl.place(x=1000,y=0,width=500,height=230)
       
    #    bg image
       
        img3=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\bg.jpg")
        img3=img3.resize((1530,540),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img =Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=250,width=1530,height=540)

        title_lbl=Label(bg_img,text="Smart Attendance System",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

# student button
        img4=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\b1.png")
        img4=img4.resize((160,160),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=160,height=160)

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",16,"bold"),bg="grey",fg="white")
        b1.place(x=200,y=240,width=160,height=40)


#  detect face button
        img5=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\b1.png")
        img5=img5.resize((160,160),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=160,height=160)

        b2=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",16,"bold"),bg="grey",fg="white")
        b2.place(x=500,y=240,width=160,height=40)

# developer
        img6=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\b1.png")
        img6=img6.resize((160,160),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=800,y=100,width=160,height=160)

        b3=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",16,"bold"),bg="grey",fg="white")
        b3.place(x=800,y=240,width=160,height=40)

# Help desk
        img11=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\b1.png")
        img11=img11.resize((160,160),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        
        b8=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b8.place(x=1100,y=100,width=160,height=160)

        b8=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",16,"bold"),bg="grey",fg="white")
        b8.place(x=1100,y=240,width=160,height=40)


#  attendence
        img7=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\b1.png")
        img7=img7.resize((160,160),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=200,y=350,width=160,height=160)

        b4=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",16,"bold"),bg="grey",fg="white")
        b4.place(x=200,y=490,width=160,height=40)
        

        #  Training data
        img8=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\b1.png")
        img8=img8.resize((160,160),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=500,y=350,width=160,height=160)

        b5=Button(bg_img,text="Training Data",cursor="hand2",font=("times new roman",16,"bold"),bg="grey",fg="white")
        b5.place(x=500,y=490,width=160,height=40)
        


 #  photo
        img9=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\b1.png")
        img9=img9.resize((160,160),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=800,y=350,width=160,height=160)

        b6=Button(bg_img,text="Photo",cursor="hand2",font=("times new roman",16,"bold"),bg="grey",fg="white")
        b6.place(x=800,y=490,width=160,height=40)
        

# exit
        img10=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\b1.png")
        img10=img10.resize((160,160),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        
        b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b7.place(x=1100,y=350,width=160,height=160)

        b7=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",16,"bold"),bg="grey",fg="white")
        b7.place(x=1100,y=490,width=160,height=40)

#function button
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.new_window=Student(self.new_window)
        
                
         
        


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()