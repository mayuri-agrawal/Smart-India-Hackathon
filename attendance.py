from tkinter import*   
from tkinter import ttk
from tkinter import font
from wsgiref.validate import validator
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 




class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student attendence")

 
        # img=Image.open(r"attendance\ui_images\s8.jpg")
        # img=img.resize((1530,250),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=1530,height=250)

        
       
        # img3=Image.open(r"ui_images\bg.jpg")
        # img3=img3.resize((1530,790),Image.ANTIALIAS)
        # self.photoimg3=ImageTk.PhotoImage(img3)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=1530,height=250)

#tittle------------------------
        title_lbl=Label(self.root,text="Attendance Management System",font=("Times New Roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

#main frame----------------------------

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=20,y=55,width=1480,height=600)

#left frame------------------------------
        Left_frame=LabelFrame(bd=2,relief=RIDGE,text="student attendance details",font=("times new roman",16,"bold"))
        Left_frame.place(x=10,y=55,width=730,height=600)

#image in left frame
        img4=Image.open(r"ui_images\train_data.png")
        img4=img4.resize((650,200),Image.ANTIALIAS)
        # antialas is used for compressing images
        self.photoimg4=ImageTk.PhotoImage(img4)

        g_img =Label(Left_frame,image=self.photoimg4)
        g_img.place(x=0,y=0,width=700,height=200)

#frame in left frame
        Left_frame_inside=Frame( Left_frame,bd=2,relief=RIDGE,bg="white")
        Left_frame_inside.place(x=0,y=210,width=730,height=350)

#Label and entry---------------------------------
#attendance id
        atten_label=Label(Left_frame_inside,text="AttendanceId:",font=("times new roman",15,"bold"),bg="white")
        atten_label.grid(row=0,column=0,padx=10,sticky=W)

        atten_combo=ttk.Entry(Left_frame_inside,font=("times new roman",12,"bold"),width=20)
        atten_combo.grid(row=0,column=1,padx=6,pady=10,sticky=W)
        
#Roll no
        roll_label=Label(Left_frame_inside,text="Roll_no:",font=("times new roman",15,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,sticky=W)

        roll_combo=ttk.Entry(Left_frame_inside,font=("times new roman",15,"bold"),width=20)
        roll_combo.grid(row=0,column=3,padx=6,pady=10,sticky=W)

#Name
        Name_label=Label(Left_frame_inside,text="Name:",font=("times new roman",15,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,sticky=W)

        Name_combo=ttk.Entry(Left_frame_inside,font=("times new roman",15,"bold"),width=20)
        Name_combo.grid(row=1,column=1,padx=6,pady=10,sticky=W)

#Department
        department_label=Label(Left_frame_inside,text="AttendanceId:",font=("times new roman",15,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Entry(Left_frame_inside,font=("times new roman",12,"bold"),width=20)
        dep_combo.grid(row=1,column=3,padx=6,pady=10,sticky=W)
#Time
        time_label=Label(Left_frame_inside,text="Time:",font=("times new roman",15,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,sticky=W)

        roll_combo=ttk.Entry(Left_frame_inside,font=("times new roman",12,"bold"),width=20)
        roll_combo.grid(row=2,column=1,padx=6,pady=10,sticky=W)

#Date
        date_label=Label(Left_frame_inside,text="Date:",font=("times new roman",15,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,sticky=W)

        date_combo=ttk.Entry(Left_frame_inside,font=("times new roman",12,"italic"),width=20)
        date_combo.grid(row=2,column=3,padx=6,pady=10,sticky=W)

#attendance status
        atten_status_label=Label(Left_frame_inside,text="Attendance Status:",font=("times new roman",15,"bold"),bg="white")
        atten_status_label.grid(row=3,column=0,padx=10,sticky=W)

        atten_status_combo=ttk.Combobox(Left_frame_inside,font=("times new roman",12,"bold"),width=20)
        atten_status_combo['values']=("select","Present","Absent")
        atten_status_combo.current(0)
        
        atten_status_combo.grid(row=3,column=1,padx=6,pady=10,sticky=W)

#buttons---------------------------------

        btn_frame=Frame(Left_frame_inside,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)
#import csv

        import_csv_btn=Button(btn_frame,text="Import csv",bg="light pink",width=16,font=("times new roman",14,"bold "),fg="black")
        import_csv_btn.grid(row=7,column=0)

#Export csv

        export_csv_btn=Button(btn_frame,text="Export csv",bg="light pink",width=16,font=("times new roman",14,"bold "),fg="black")
        export_csv_btn.grid(row=7,column=1)

#update

        update_photo_btn=Button(btn_frame,text="Update",bg="light pink",width=15,font=("times new roman",14,"bold "),fg="black")
        update_photo_btn.grid(row=7,column=2)

#Reset

        reset_photo_btn=Button(btn_frame,text="Reset",bg="light pink",width=15,font=("times new roman",14,"bold "),fg="black")
        reset_photo_btn.grid(row=7,column=3)



#right frame----------------------------
        
        Right_frame=LabelFrame(bd=2,relief=RIDGE,font=("times new roman",16,"bold"))
        Right_frame.place(x=820,y=55,width=660,height=600)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=715,height=550)
 
 #scroll bar table------------------------
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
       

if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()