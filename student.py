# used for gui

from tkinter import*   
from tkinter import ttk
from tkinter import font
from wsgiref.validate import validator
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student attendence")


        #variables

        self.var_Class=StringVar()
        self.var_Name=StringVar()
        self.var_roll=StringVar()
        self.var_sec=StringVar()
        self.var_opt=StringVar()
        self.var_Year=StringVar()
        self.var_Teacher_Name=StringVar()
        self.var_DOB=StringVar()
        self.var_contact=StringVar()
        self.var_gender=StringVar()
        

        # # first image
        # img=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\s8.jpg")
        # img=img.resize((1530,250),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=1530,height=250)

        #    bg image
       
        img3=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\bg.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img =Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="Student Details",font=("Algerian",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # main_frame=Frame(bg_img,bd=2)
        # main_frame.place(x=0,y=0,width=1500,height=650)

        #left label frame

        Left_frame=LabelFrame(bd=2,relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"))
        Left_frame.place(x=50,y=70,width=660,height=700)

        img9=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\gradient_img.jpg")
        img9=img9.resize((650,700),Image.ANTIALIAS)
        # antialas is used for compressing images
        self.photoimg9=ImageTk.PhotoImage(img9)

        g_img =Label(Left_frame,image=self.photoimg9)
        g_img.place(x=4,y=0,width=650,height=700)


        img4=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\s9.jpg")
        img4=img4.resize((650,200),Image.ANTIALIAS)
        # antialas is used for compressing images
        self.photoimg4=ImageTk.PhotoImage(img4)

        s9_img =Label(Left_frame,image=self.photoimg4)
        s9_img.place(x=5,y=0,width=650,height=200)

# Current course
        current_course=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",16,"bold"))
        current_course.place(x=5,y=210,width=650,height=170)
# class
        Class_label=Label(current_course,text="Class",font=("times new roman",12,"italic"),bg="white")
        Class_label.grid(row=0,column=0,padx=10)


        Class_combo=ttk.Combobox(current_course,textvariable=self.var_Class,font=("times new roman",12,"italic"),width=20,state="read only")
        Class_combo['values']=("select Class",1,2,3,4,5,6,7,8,9,10,11,12)
        Class_combo.current(0)
        

        Class_combo.grid(row=0,column=1,padx=6,pady=10,sticky=W)

# section
        sec_label=Label(current_course,text="Section",font=("times new roman",12,"italic"),bg="white")
        sec_label.grid(row=0,column=2,padx=10,sticky=W)


        sec_combo=ttk.Combobox(current_course,textvariable=self.var_sec,font=("times new roman",12,"italic"),width=20,state="read only")
        sec_combo['values']=("select Section","A","B","C","D","PCM","PCB","Commerce")
        sec_combo.current(0)
        

        sec_combo.grid(row=0,column=3,padx=6,pady=10,sticky=W)

#optional
        opt_label=Label(current_course,text="optional subject",font=("times new roman",12,"italic"),bg="white")
        opt_label.grid(row=1,column=0,padx=10)


        opt_combo=ttk.Combobox(current_course,textvariable=self.var_opt,font=("times new roman",12,"italic"),width=20,state="read only")
        opt_combo['values']=("select optional_subject","Hindi","Marathi","Sanskrit","computer science","physical Education","Business studies")
        opt_combo.current(0)
        

        opt_combo.grid(row=1,column=1,padx=6,pady=10,sticky=W)

# academic year
        
        Year_label=Label(current_course,text="Annual Year",font=("times new roman",12,"italic"),bg="white")
        Year_label.grid(row=1,column=2,padx=10)


        Year_combo=ttk.Combobox(current_course,textvariable=self.var_Year,font=("times new roman",12,"italic"),width=20,state="read only")
        Year_combo['values']=("Annual Year","2021-2022","2022-2023","2023-2024")
        Year_combo.current(0)
        

        Year_combo.grid(row=1,column=3,padx=6,pady=10,sticky=W)

 #Name
        Teacher_Name_label=Label(current_course,text="Teacher Name",font=("times new roman",12,"italic"),bg="white")
        Teacher_Name_label.grid(row=2,column=0,padx=10,sticky=W)

        Name_combo=ttk.Entry(current_course,textvariable=self.var_Teacher_Name,font=("times new roman",12,"italic"),width=20)
        Name_combo.grid(row=2,column=1,padx=6,pady=10,sticky=W)



# Class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",16,"bold"))
        class_student_frame.place(x=5,y=390,width=650,height=280)


#roll number
        roll_label=Label(class_student_frame,text="Roll Number",font=("times new roman",12,"italic"),bg="white")
        roll_label.grid(row=0,column=0,padx=10,sticky=W)

        roll_combo=ttk.Entry(class_student_frame,textvariable=self.var_roll,font=("times new roman",12,"italic"),width=20)
        roll_combo.grid(row=0,column=1,padx=6,pady=10,sticky=W)

#Name
        Name_label=Label(class_student_frame,text="Name",font=("times new roman",12,"italic"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,sticky=W)

        Name_combo=ttk.Entry(class_student_frame,textvariable=self.var_Name,font=("times new roman",12,"italic"),width=20)
        Name_combo.grid(row=1,column=1,padx=6,pady=10,sticky=W)

#DOB
        DOB_label=Label(class_student_frame,text="Date of Birth",font=("times new roman",12,"italic"),bg="white")
        DOB_label.grid(row=1,column=2,padx=10,sticky=W)

        DOB_combo=ttk.Entry(class_student_frame,textvariable=self.var_DOB,font=("times new roman",12,"italic"),width=20,state="datetime-local")
        DOB_combo.grid(row=1,column=3,padx=6,pady=10,sticky=W)

#contact-details
        contact_label=Label(class_student_frame,text="Phone number",font=("times new roman",12,"italic"),bg="white")
        contact_label.grid(row=2,column=0,padx=10,sticky=W)

        DOB_combo=ttk.Entry(class_student_frame,textvariable=self.var_contact,font=("times new roman",12,"italic"),width=20,state="datetime-local")
        DOB_combo.grid(row=2,column=1,padx=6,pady=10,sticky=W)


 #gender
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"italic"),bg="white")
        gender_label.grid(row=2,column=2,padx=10,sticky=W)



        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"italic"),width=20,state="type")
        gender_combo['values']=("select","Male","Female","Other")
        gender_combo.current(0)
        
        gender_combo.grid(row=2,column=3,padx=6,pady=10,sticky=W)


#radio button
        
        self.var_radio1=StringVar()

        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=4,column=0)

       
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radiobtn2.grid(row=4,column=2)
#buttons frame
        # btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        # btn_frame.place(x=0,y=200,width=715,height=35)
#save

        save_photo_btn=Button(class_student_frame,text="Save",command=self.add_data,bg="light pink",width=8,font=("times new roman",14,"bold "),fg="black")
        save_photo_btn.grid(row=5,column=0)

#reset

        reset_photo_btn=Button(class_student_frame,text="Reset",command=self.reset_data,bg="light pink",width=8,font=("times new roman",14,"bold "),fg="black")
        reset_photo_btn.grid(row=5,column=1)

#update

        update_photo_btn=Button(class_student_frame,text="Update",command=self.Update_data,bg="light pink",width=8,font=("times new roman",14,"bold "),fg="black")
        update_photo_btn.grid(row=5,column=2)

#delete

        delete_photo_btn=Button(class_student_frame,text="Delete",command=self.delete_data,bg="light pink",width=8,font=("times new roman",14,"bold "),fg="black")
        delete_photo_btn.grid(row=5,column=3)


#photo sample

        photo_sample_btn=Button(class_student_frame,text="Take photo",bg="light pink",width=10,font=("times new roman",14,"bold "),fg="black")
        photo_sample_btn.grid(row=8,column=0)

#update photo

        update_photo_btn=Button(class_student_frame,text="Update photo",bg="light pink",width=10,font=("times new roman",14,"bold "),fg="black")
        update_photo_btn.grid(row=8,column=2)





        










 #right label frame

        Right_frame=LabelFrame(bd=2,bg="white",relief=RIDGE,font=("times new roman",16,"bold"))
        Right_frame.place(x=820,y=70,width=660,height=700)

        img10=Image.open(r"C:\Users\ASUS\OneDrive\Desktop\attendance\ui_images\gradient_img.jpg")
        img10=img10.resize((650,700),Image.ANTIALIAS)
        # antialas is used for compressing images
        self.photoimg10=ImageTk.PhotoImage(img10)

        g_img =Label(Right_frame,image=self.photoimg10)
        g_img.place(x=4,y=0,width=650,height=700)


  # search system /////////////////////////////////////////

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",16,"bold"))
        Search_frame.place(x=5,y=15,width=650,height=150)


        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",16,"italic"),bg="white")
        Search_label.grid(row=0,column=0,padx=10,sticky=W)

        
        
        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"italic"),width=20,state="type")
        Search_combo['values']=("select","Roll Number","Phone number")
        Search_combo.current(0)
        
        Search_combo.grid(row=0,column=1,padx=6,pady=10,sticky=W)


        Search_entry=ttk.Entry(Search_frame,font=("times new roman",12,"italic"),width=20,state="datetime-local")
        Search_entry.grid(row=0,column=2,padx=6,pady=10,sticky=W)

# search button
        Search_btn=Button(Search_frame,text="Search",bg="light pink",width=10,font=("times new roman",14,"bold "),fg="black")
        Search_btn.grid(row=2,column=1,padx=4)



        Show_btn=Button(Search_frame,text="Show All",bg="light pink",width=10,font=("times new roman",14,"bold "),fg="black")
        Show_btn.grid(row=2,column=2,padx=4)


#table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=170,width=650,height=510)
 # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,column=("Name","Roll number","Class","Section","gender","Date of birth","contact","Teacher_Name","PhotoSampleStatus","Annual Year","Optional Subject"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll number",text="Roll number")
        self.student_table.heading("Class",text="Class")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("Date of birth",text="Date of birth")
        self.student_table.heading("contact",text="Phone number")
        self.student_table.heading("Teacher_Name",text="Teacher_Name")
        self.student_table.heading("PhotoSampleStatus",text="PhotoSampleStatus")
        self.student_table.heading("Annual Year",text="Annual Year")
        self.student_table.heading("Optional Subject",text="Optional Subject")

        self.student_table["show"]="headings"

        self.student_table.column("Name",width=100)
        self.student_table.column("Roll number",width=100)
        self.student_table.column("Class",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("Date of birth",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("Teacher_Name",width=100)
        self.student_table.column("PhotoSampleStatus",width=100)
        self.student_table.column("Annual Year",width=100)
        self.student_table.column("Optional Subject",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



 #function declaration
#     def add_data(self):  

    def add_data(self) :

            if self.var_Class.get()=="Select Class" or self.var_Name.get()=="" or self.var_roll.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=self.root)
            else:

                    try:


                            conn=mysql.connector.connect(host="localhost",username="root",password="Garvit@123",database="face_recognisation")
                            my_cursor=conn.cursor()
                            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                self.var_Name.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_Class.get(),
                                                                                                self.var_sec.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_DOB.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_Teacher_Name.get(),
                                                                                                self.var_radio1.get(),
                                                                                                self.var_Year.get(),
                                                                                                self.var_opt.get()
                                                                                                ))
                            conn.commit()
                            self.fetch_data()
                            conn.close()
                            messagebox.showinfo("success","student details has been stored",parent=self.root)
                    except Exception as es:
                            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


# fetch data
    def fetch_data(self):

                conn=mysql.connector.connect(host="localhost",username="root",password="Garvit@123",database="face_recognisation")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                data=my_cursor.fetchall()

                if len(data)!=0:
                   self.student_table.delete(*self.student_table.get_children())
                for i in data:
                        self.student_table.insert("",END,values=i)
                conn.commit()
                conn.close()

    def get_cursor(self,event=""):
                cursor_focus=self.student_table.focus()
                content=self.student_table.item(cursor_focus)
                data=content["values"]

                self.var_Name.set(data[0]),
                self.var_roll.set(data[1]),
                self.var_Class.set(data[3]),
                self.var_sec.set(data[4]),
                self.var_gender.set(data[5]),
                self.var_DOB.set(data[6]),
                self.var_contact.set(data[7]),
                self.var_Teacher_Name.set(data[8]),
                self.var_radio1.set(data[9]),
                self.var_Year.set(data[10]),
                self.var_opt.set(data[11]),
                
# update function
    def Update_data(self):
            if self.var_Class.get()=="Select Class" or self.var_Name.get()=="" or self.var_roll.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                 try:
                      Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                      if Update>0:
                           conn=mysql.connector.connect(host="localhost",username="root",password="Garvit@123",database="face_recognisation")
                           my_cursor=conn.cursor()
                           my_cursor.execute("Update student set Name=%s,Roll number=%s,Class=%s,Section=%s,gender=%s,Date of birth=%s,contact=%s,Teacher_Name=%s,PhotoSampleStatus=%s,Annual Year=%s,Optional Subject=%s",(
                                                                                                          self.var_Name.get(),
                                                                                                          self.var_roll.get(),
                                                                                                          self.var_Class.get(),
                                                                                                          self.var_sec.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_DOB.get(),
                                                                                                          self.var_contact.get(),
                                                                                                          self.var_Teacher_Name.get(),
                                                                                                          self.var_radio1.get(),
                                                                                                          self.var_Year.get(),
                                                                                                          self.var_opt.get()
                                                                                                          
                                                                                                ))
                           
                      else:
                                if not Update:
                                        return 
                      messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                      conn.commit()
                      self.fetch_data()
                      conn.close()
                 except Exception as es:
                         messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


        #delete function
    def delete_data(self):
             if self.var_roll.get()=="":
                     messagebox.showerror("Error","Roll Number must be required",parent=self.root)
             else:
                     try:
                             delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student's data?",parent=self.root)
                             if delete>0:
                                     conn=mysql.connector.connect(host="localhost",username="root",password="Garvit@123",database="face_recognisation")
                                     my_cursor=conn.cursor()
                                     sql="delte from student where Roll Number=%s"
                                     val=(self.var_roll.get(),)
                                     my_cursor.execute(sql,val)
                             else:
                                     if not delete:
                                             return 
                             conn.commit()
                             self.fetch_data()
                             conn.close()
                             messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                     except Exception as es:
                         messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

 # reset function                        
    def reset_data(self):
            self.var_Name.set("Select Name")
            self.var_roll.set("")
            self.var_Class.set("Select Class")
            self.var_sec.set("Select Section")
            self.var_gender.set("Male")
            self.var_DOB.set("")
            self.var_contact.set("")
            self.var_Teacher_Name.set("")
            self.var_radio1.set("")
            self.var_Year.set("Annual Year")
            self.var_opt.set("Optional Subject")


            #=========Generate data set or Take photo Smaples==========
            def generate_data_set(self):
                    if self.var_Class.get()=="Select Class" or self.var_Name.get()=="" or self.var_roll.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                 try:
                      Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                      if Update>0:
                           conn=mysql.connector.connect(host="localhost",username="root",password="Garvit@123",database="face_recognisation")
                           my_cursor=conn.cursor()
                           my_cursor.execute("select * from student")
                           myresult=my_cursor.fetchall()
                           id=0
                           for x in myresult:
                                   id+=1
                           my_cursor.execute("Update student set Name=%s,Roll number=%s,Class=%s,Section=%s,gender=%s,Date of birth=%s,contact=%s,Teacher_Name=%s,PhotoSampleStatus=%s,Annual Year=%s,Optional Subject=%s",(
                                                                                                          self.var_Name.get(),
                                                                                                          self.var_roll.get(),
                                                                                                          self.var_Class.get(),
                                                                                                          self.var_sec.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_DOB.get(),
                                                                                                          self.var_contact.get(),
                                                                                                          self.var_Teacher_Name.get(),
                                                                                                          self.var_radio1.get(),
                                                                                                          self.var_Year.get(),
                                                                                                          self.var_opt.get()==id+1
                                                                                                          
                                                                                                        ))        


                           conn.commit()
                           self.fetch_data()
                           self.reset_data
                           conn.close()


                           #============= Load predifined data on face frontals from opencv===============

                           face_classifier =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                           def face_cropped(img):
                                   gray=cv2.cvtcolor(img, cv2.COLOR_BGR2GRAY)
                                   faces=face_classifier.detectMultiScale(gray,1.3,5)
                                   #sacling factor=1.3
                                   #Minimum Neighbour=5

                                   for(x,y,w,h) in faces:
                                           face_cropped=img[y:y+h,x:x+w]
                                           return face_cropped

                           cap=cv2.videoCapture(0)
                           img_id=0
                           while True:
                                   ret,frame=cap.read()
                                   if face_cropped(my_frame) is not None:
                                           img_id+=1
                                   face=cv2.resize(face_cropped(my_frame),(450,450))
                                   face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                   file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                   cv2.imWrite(file_name_path)
                                   cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                                   cv2.imshow("Crooped Face",face)

                                   if cv2.waitKey(1) ==13 or int(img_id)==100:
                                           break
                           cap.release()
                           cv2.destroyAllWindows()
                           messagebox.showinfo("Result","Generating data sets completed!!!")


                                         
                                   

                                






                        


                 


                          






 
 
if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()