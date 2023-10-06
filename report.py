from tkinter import *
from tkinter import ttk
import tkinter  as tk 
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
import mysql.connector
from attendance import Attendance
import os


class report:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")
        self.root.wm_iconbitmap("faceicon.ico")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images\facialrecognition.png")
        img=img.resize((1366,130))
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"Images\bg.png")
        bg1=bg1.resize((1366,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Report Pannel",font=("verdana",30,"bold"),bg="white",fg="black")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        det_img_btn=Image.open(r"Images\istockphoto-1161644228-612x612.jpg")
        det_img_btn=det_img_btn.resize((180,180))
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        #button back
        tra_b1_1 = Button(bg_img,command=root.destroy,text="Back",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="black")
        tra_b1_1.place(x=1200,y=10,width=150,height=30)


        det_b1 = Button(bg_img,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=300,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.attendance,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        det_b1_1.place(x=300,y=380,width=180,height=45)

        # student button 2
        det_img_btn=Image.open(r"Images\std1.jpg")
        det_img_btn=det_img_btn.resize((180,180))
        self.det_img2=ImageTk.PhotoImage(det_img_btn)

        #button back
        tra_b2_2 = Button(bg_img,command=root.destroy,text="Back",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="black")
        tra_b2_2.place(x=1200,y=10,width=150,height=30)


        det_b2 = Button(bg_img,image=self.det_img2,cursor="hand2",)
        det_b2.place(x=600,y=200,width=180,height=180)

        det_b2_2 = Button(bg_img,command=self.student,text="Student",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        det_b2_2.place(x=600,y=380,width=180,height=45)

        # student button 3
        det_img_btn=Image.open(r"Images\authorization-manager-2306571-1948731.webp")
        det_img_btn=det_img_btn.resize((180,180))
        self.det_img3=ImageTk.PhotoImage(det_img_btn)

        #button back
        tra_b3_3 = Button(bg_img,command=root.destroy,text="Back",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="black")
        tra_b3_3.place(x=1200,y=10,width=150,height=30)


        det_b3 = Button(bg_img,image=self.det_img3,cursor="hand2",)
        det_b3.place(x=900,y=200,width=180,height=180)

        det_b3_3 = Button(bg_img,command=self.register,text="Registered",cursor="hand2",font=("tahoma",15,"bold"),bg="blue",fg="white")
        det_b3_3.place(x=900,y=380,width=180,height=45)

        # Detect Face  button 2

        # Attendance System  button 3

    def attendance(self):
        my_w = tk.Tk()
        my_w.geometry("500x250") 
        my_connect = mysql.connector.connect(
          host="localhost",
          user="root", 
          passwd="",
          database="face_recognition"
        )

        my_conn = my_connect.cursor()
        my_conn.execute("SELECT * FROM stdattendance limit 0,10")
        i=0 
        for student in my_conn: 
          for j in range(len(student)):
            e = Entry(my_w, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
          i=i+1
        my_w.mainloop()
        

    def student(self):
        my_w = tk.Tk()
        my_w.geometry("1000x250") 
        my_connect = mysql.connector.connect(
          host="localhost",
          user="root", 
          passwd="",
          database="face_recognition"
        )

        my_conn = my_connect.cursor()
        my_conn.execute("SELECT * FROM student limit 0,10")
        i=0 
        for student in my_conn: 
          for j in range(len(student)):
            e = Entry(my_w, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
          i=i+1
        my_w.mainloop()

    def register(self):
        my_w = tk.Tk()
        my_w.geometry("800x250") 
        my_connect = mysql.connector.connect(
          host="localhost",
          user="root", 
          passwd="",
          database="face_recognition"
        )

        my_conn = my_connect.cursor()
        my_conn.execute("SELECT * FROM register limit 0,10")
        i=0 
        for student in my_conn: 
          for j in range(len(student)):
            e = Entry(my_w, width=20, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
          i=i+1
        my_w.mainloop()

        # Help  Support  button 4
    def Face_Recognition_System(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=report(root)
    root.mainloop()