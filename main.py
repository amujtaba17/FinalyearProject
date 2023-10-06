
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from report import report
#=========================================



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face_Recogonition_System")
        self.root.wm_iconbitmap("faceicon.ico")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images\Ims3.jpg")
        img=img.resize((1600,600))
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1540,height=130)

        # backgorund image 
        bg1=Image.open(r"Images\depart.jpeg")
        bg1=bg1.resize((1920,1080))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=120,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Project ID: ",font=("Helvetica",30,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1600,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"Images\stuinfo.png")
        std_img_btn=std_img_btn.resize((180,180))
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        std_b1_1.place(x=250,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"Images\fdetector.jpg")
        det_img_btn=det_img_btn.resize((180,180))
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2")
        det_b1.place(x=480,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        det_b1_1.place(x=480,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"Images\attendance.png")
        att_img_btn=att_img_btn.resize((180,180))
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2")
        att_b1.place(x=710,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Check Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        att_b1_1.place(x=710,y=280,width=180,height=45)

         # Report  button 4
        hlp_img_btn=Image.open(r"Images\report.png")
        hlp_img_btn=hlp_img_btn.resize((180,180))
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.report,image=self.hlp_img1,cursor="hand2")
        hlp_b1.place(x=940,y=100,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.report,text="Reports",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        hlp_b1_1.place(x=940,y=280,width=180,height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"Images\trainm.jpg")
        tra_img_btn=tra_img_btn.resize((180,180))
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2")
        tra_b1.place(x=250,y=330,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Images",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        tra_b1_1.place(x=250,y=510,width=180,height=45)

        # Photo   button 6
        pho_img_btn=Image.open(r"Images\deep-face-recognition-02.WEBP")
        pho_img_btn=pho_img_btn.resize((180,180))
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2")
        pho_b1.place(x=480,y=330,width=180,height=180)

        pho_b1_1 = Button(bg_img,command=self.open_img,text=" View Samples Taken",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        pho_b1_1.place(x=480,y=510,width=180,height=45)

        # Developers   button 7
        dev_img_btn=Image.open(r"Images\devel.png")
        dev_img_btn=dev_img_btn.resize((180,180))
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2")
        dev_b1.place(x=710,y=330,width=180,height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        dev_b1_1.place(x=710,y=510,width=180,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"Images\exittt.png")
        exi_img_btn=exi_img_btn.resize((180,180))
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.iExit,image=self.exi_img1,cursor="hand2")
        exi_b1.place(x=940,y=330,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.iExit,text="Exit App",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        exi_b1_1.place(x=940,y=510,width=180,height=45)

# ==================Funtion for Open Images Folder ==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=report(self.new_window)

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure To Exit This Project",parent=self.root)
         if self.iExit>0:
             self.root.destroy()
         else:
                 return
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
