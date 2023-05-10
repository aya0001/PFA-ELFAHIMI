from tkinter import Label, Button, Frame, RIDGE, Checkbutton, StringVar, IntVar, TOP, X, LabelFrame, W, Entry,HORIZONTAL,BOTTOM,VERTICAL,Y,RIGHT,BOTH,END,Toplevel
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow (for images)
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import io
from datetime import datetime, date




def main():
    from tkinter import Tk
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # background of login window
        image_path = r"C:\Users\PC\Desktop\projet_python\images\bg_login.jpg"
        image = Image.open(image_path)
        image = image.resize((1300, 800), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        

        frame = Frame(self.root, bg="black")
        frame.place(x=500, y=170, width=340, height=450)
        #login icon
        img1 = Image.open(r"C:\Users\PC\Desktop\projet_python\images\Loginicon.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=630, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=100, y=100)

        # label
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=155)
        # textbox (pour saisir username)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # label
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y=225)
        # textbox (pour saisir mot de passe)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*")
        self.txtpass.place(x=40, y=250, width=270)

        #============Icon Images================
        img2 = Image.open(r"C:\Users\PC\Desktop\projet_python\images\Loginicon.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=544, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\PC\Desktop\projet_python\images\lock-img.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=544, y=395, width=25, height=25)
        #button login
        loginbtn=Button(frame,text="Login", command=self.login,font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red" , activeforeground="red",activebackground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button 
        registerbtn=Button(frame,text="New User Register?",command=self.register_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black" , activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forget password button
        registerbtn=Button(frame,text="Forget Password?",command=self.forgot_password_window,font=("times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black" , activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)


    def register_window(self):
         self.new_window=Toplevel(self.root)
         self.app=Register(self.new_window)
        # test les champs de login 
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            messagebox.showinfo("Success","welcome")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="123456",database="biblio")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from admin where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                 open_main=messagebox.askyesno("YesNo","Access only admin")
                 if open_main>0:
                    # self.new_window=Toplevel(self.new_window)
                    # self.app=Book(self.new_window)
                    self.new_window=Toplevel(self.root)
                    self.app=Book(self.new_window)
                 else:
                     if not open_main:
                         return
            conn.commit()
            conn.close()



#===============================reset password=================================

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="123456",database="biblio")
            my_cursor=conn.cursor()
            qury=("select * from admin where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update admin set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()




#======================================================forgot password window=======================================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="123456",database="biblio")
            my_cursor=conn.cursor()
            query=("select * from admin where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please entre the valid user name")
            else:
                conn.close()
                self.root2=Toplevel(bg="white")
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"), fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)
                security_Q=Label(self.root2,text="Select Security Questions",font=("Times new roman",15,"bold"),bg="white", fg="black")
                security_Q.place(x=55,y=80)
                self.combo_security_Q=ttk.Combobox(self.root2,font=("Times new roman",15),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your pet Name","Your bestfriend Name")
                self.combo_security_Q.place(x=55,y=120,width=200)
                self.combo_security_Q.current(0)
                security_A=Label(self.root2,text="Security Answer",font=("Times new roman",15,"bold"),bg="white", fg="black")
                security_A.place(x=55,y=170)
                self.txt_security=ttk.Entry(self.root2,font=("Times new roman",15))
                self.txt_security.place(x=55,y=200,width=200)


                new_password=Label(self.root2,text="New Password",font=("Times new roman",15,"bold"),bg="white", fg="black")
                new_password.place(x=55,y=250)

                self.txt_newpass=ttk.Entry(self.root2,font=("Times new roman",15))
                self.txt_newpass.place(x=55,y=280,width=200)

                btn=Button(self.root2,text="Reset", command=self.reset_pass,font=("Times new roman",15,"bold"),bg="red", fg="white")
                btn.place(x=120,y=330)









#================================================================================================


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # background of login window
        image_path = r"C:\Users\PC\Desktop\projet_python\images\library.jpg"
        image = Image.open(image_path)
        image = image.resize((1290, 900), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)


        #left image
        image_path1 = r"C:\Users\PC\Desktop\projet_python\images\book_lib.jpg"
        image1 = Image.open(image_path1)
        image1 = image1.resize((470, 510), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(image1)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100)
        # main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=650,height=514)


        register_lbl=Label(frame,text="Register  Here",font=("Times new roman",30,"bold"),fg="orange",bg="white")
        register_lbl.place(x=200,y=20)


        # label et textbox (pour saisir les champs)
        #row 1
        fname=Label(frame,text="First Name",font=("Times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

       
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=200)

        l_name=Label(frame,text="Last Name",font=("Times new roman",15,"bold"),bg="white", fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Times new roman",15))
        self.txt_lname.place(x=370,y=130,width=200)

        #row 2

        contact=Label(frame,text="Contact No",font=("Times new roman",15,"bold"),bg="white", fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact ,font=("Times new roman",15))
        self.txt_contact.place(x=50,y=200,width=200)

        email=Label(frame,text="Email",font=("Times new roman",15,"bold"),bg="white", fg="black")
        email.place(x=365,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Times new roman",15))
        self.txt_email.place(x=370,y=200,width=200)

        #row 3

        security_Q=Label(frame,text="Select Security Questions",font=("Times new roman",15,"bold"),bg="white", fg="black")
        security_Q.place(x=50,y=245)


        # self.txt_security=ttk.Entry(frame,font=("Times new roman",15))
        # self.txt_security.place(x=370,y=270,width=200)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Times new roman",15),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your pet Name","Your bestfriend Name")
        self.combo_security_Q.place(x=50,y=280,width=200)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("Times new roman",15,"bold"),bg="white", fg="black")
        security_A.place(x=370,y=245)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("Times new roman",15))
        self.txt_security.place(x=370,y=280,width=200)

        #row 4

        pswd=Label(frame,text="Password",font=("Times new roman",15,"bold"),bg="white", fg="black")
        pswd.place(x=50,y=320)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Times new roman",15),show="*")
        self.txt_pswd.place(x=50,y=350,width=200)

        confirm_pswd=Label(frame,text="Confirm Password",font=("Times new roman",15,"bold"),bg="white", fg="black")
        confirm_pswd.place(x=370,y=320)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("Times new roman",15),show="*")
        self.txt_confirm_pswd.place(x=370,y=350,width=200)

        #check button
        self.var_check=IntVar()
        chekbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("Times new roman",10,"normal"),bg="white", fg="black",onvalue=1,offvalue=0)
        chekbtn.place(x=50,y=390)

        # buttons
        img=Image.open(r"C:\Users\PC\Desktop\projet_python\images\register-button.png")
        img=img.resize((165,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2", bg="white",activebackground="white")
        b1.place(x=10,y=440,width=300)

        img1=Image.open(r"C:\Users\PC\Desktop\projet_python\images\login-button.png")
        img1=img1.resize((180,58),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2", bg="white",activebackground="white")
        b1.place(x=330,y=430,width=300)
        

        #functions
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be the same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="123456",database="biblio")
            my_cursor=conn.cursor()
            query=("select * from admin where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into admin values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register successfully")
        
        

    def return_login(self):
        self.root.destroy()

#================================== CLASS BOOK ====================================================



class Book:
    def __init__(self,root):
        self.root=root
        self.root.title("Books Managment System")
        self.root.geometry("1600x900+0+0")
        self.root.configure(bg="white")

        #========================add button variables================
        self.var_Ref=StringVar()
        self.var_Title=StringVar()
        self.var_Author=StringVar()
        self.var_PubDate=StringVar()
        self.var_Lang=StringVar()
        self.var_Editor=StringVar()
        self.var_NbPages=StringVar()
        self.var_ISBN=StringVar()
        self.var_Image=StringVar()
        self.filename = None
        
        


        lbltitle=Label(self.root,text=" Books Managment System", bd=15,relief=RIDGE,bg='white',fg="red",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open(r"C:\Users\PC\Desktop\projet_python\images\book_png.png")
        img1=img1.resize((100,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0,bg="white")
        b1.place(x=20,y=15)

        #======================Main DataFrame====================================

        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20, bg="white")
        DataFrame.place(x=0,y=120,width=1280,height=300)

        #======================DataFrame Book====================================
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Book Information",fg="black",font=("arial",12,"bold"), bg="white")
        DataFrameLeft.place(x=0,y=5,width=800,height=250)



        #======================DataFrameRight Photo====================================
  
        self.DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Photo",fg="black",font=("arial",12,"bold"), bg="white")
        self.DataFrameRight.place(x=850,y=5,width=350,height=200)        
        #=====================ButtonFrame=================================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20, bg="white")
        ButtonFrame.place(x=0,y=425,width=1280,height=65)   

        #=====================Main Button=================================
            #Bouton Ajouter
        btnAddData=Button(ButtonFrame,command=self.AddBook,text="Add Book",font=("arial",12,"bold"),fg="white",bg="black",activebackground="white",width=10)
        btnAddData.grid(row=0,column=0)
        

            #Bouton Modifier

        btnUpdate=Button(ButtonFrame,command=self.update_book,text="Update Book",font=("arial",12,"bold"),fg="white",bg="black",activebackground="white",width=10)
        btnUpdate.grid(row=0,column=1,padx=2)

            #Bouton Supprimer
        
        btnDelete=Button(ButtonFrame,command=self.delete_book,text="Delete Book",font=("arial",12,"bold"),fg="white",bg="red",activebackground="white",width=10)
        btnDelete.grid(row=0,column=2,padx=2)

            #Bouton Reset

        btnReset=Button(ButtonFrame,command=self.reset,text="Reset",font=("arial",12,"bold"),fg="white",bg="black",activebackground="white",width=10)
        btnReset.grid(row=0,column=3,padx=2)

            #Bouton Exit

        btnExit=Button(ButtonFrame,command=self.Exit,text="Exit",font=("arial",12,"bold"),fg="white",bg="black",activebackground="white",width=10)
        btnExit.grid(row=0,column=4,padx=2)

            #======================Search By=============

        lblSearch=Label(ButtonFrame,font=("arial",16,"bold"),text="Search By",padx=2,fg="white",bg="red",width=10)     
        lblSearch.grid(row=0,column=5,sticky=W,padx=2)
        
        
        #variable
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",12,"bold"), state="readonly")
        search_combo["values"]=("Ref","Title","Author","Publication Date")
        search_combo.grid(row=0,column=6,padx=2)
        search_combo.current(0)
        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",12,"bold"))
        txtSearch.grid(row=0,column=7,padx=2)

        searchBtn=Button(ButtonFrame,command=self.search_data,text="Search",font=("arial",12,"bold"),fg="white",bg="black",activebackground="white",width=10)
        searchBtn.grid(row=0,column=8,padx=2)
            
        showAll=Button(ButtonFrame,command=self.fatch_data,text="Show All",font=("arial",12,"bold"),fg="white",bg="black",activebackground="white",width=10)
        showAll.grid(row=0,column=9)


        #=================label et textbox===========================

            #================Reference book===========================

        lblRefno=Label(DataFrameLeft,font=("arial",16,"normal"),text="Reference No",padx=15,fg="black",bg="white")
        lblRefno.grid(row=0,column=0,sticky=W,pady=8)

        txtRefno=Entry(DataFrameLeft,relief=RIDGE,width=16,font=("arial",12,"normal"),state="disabled",textvariable=self.var_Ref)
        txtRefno.grid(row=0,column=1,pady=8)



        lbltitle=Label(DataFrameLeft,font=("arial",16,"normal"),text="Book Title",padx=15,fg="black",bg="white")
        lbltitle.grid(row=1,column=0,sticky=W,pady=8)
        txtTitle=Entry(DataFrameLeft,relief=RIDGE,width=16,font=("arial",12,"normal"),bg="beige",textvariable=self.var_Title )
        txtTitle.grid(row=1,column=1,pady=8)


        lblAuthor=Label(DataFrameLeft,font=("arial",16,"normal"),text="Author Name",padx=15,fg="black",bg="white")
        lblAuthor.grid(row=2,column=0,sticky=W,pady=8)
        txtAuthor=Entry(DataFrameLeft,relief=RIDGE,width=16,font=("arial",12,"normal"),bg="beige" ,textvariable=self.var_Author)
        txtAuthor.grid(row=2,column=1,pady=8)


        lblPubDate=Label(DataFrameLeft,font=("arial",16,"normal"),text="Publication Date",padx=15,fg="black",bg="white")
        lblPubDate.grid(row=3,column=0,sticky=W,pady=8)
        txtPubDate=Entry(DataFrameLeft,relief=RIDGE,width=16,font=("arial",12,"normal"),bg="beige",textvariable=self.var_PubDate)
        txtPubDate.grid(row=3,column=1,pady=8,padx=20)

        
        lblLang=Label(DataFrameLeft,font=("arial",16,"normal"),text="Language",padx=20,fg="black",bg="white")
        lblLang.grid(row=0,column=2,sticky=W,pady=8)

        Lang_combo=ttk.Combobox(DataFrameLeft,width=14,font=("arial",12,"bold"), state="readonly",textvariable=self.var_Lang)
        Lang_combo["values"]=("Select","AR","FR","EN")
        Lang_combo.grid(row=0,column=5,padx=20,pady=8)
        Lang_combo.current(0)
       
        lblEditor=Label(DataFrameLeft,font=("arial",16,"normal"),text="Editor",padx=15,fg="black",bg="white")
        lblEditor.grid(row=1,column=2,sticky=W,pady=8)
        txtEditor=Entry(DataFrameLeft,relief=RIDGE,width=16,font=("arial",12,"normal"),bg="beige",textvariable=self.var_Editor)
        txtEditor.grid(row=1,column=5,pady=8,padx=20)
       
        lblNbPage=Label(DataFrameLeft,font=("arial",16,"normal"),text="Number of Pages",padx=15,fg="black",bg="white")
        lblNbPage.grid(row=2,column=2,sticky=W,pady=8)
        txtNbPage=Entry(DataFrameLeft,relief=RIDGE,width=16,font=("arial",12,"normal"),bg="beige",textvariable=self.var_NbPages)
        txtNbPage.grid(row=2,column=5,pady=8,padx=20)


        lblISBN=Label(DataFrameLeft,font=("arial",16,"normal"),text="ISBN",padx=15,fg="black",bg="white")
        lblISBN.grid(row=3,column=2,sticky=W,pady=8)
        txtISBN=Entry(DataFrameLeft,relief=RIDGE,width=16,font=("arial",12,"normal"),bg="beige",textvariable=self.var_ISBN)
        txtISBN.grid(row=3,column=5,pady=8,padx=20)

        #====================Button Upload Image===========================================

    
                                  
        #==========================Frame Details===========================================

        Framedetails=Frame(self.root,bd=15,relief=RIDGE,bg="white")
        Framedetails.place(x=0,y=490,width=1280,height=195)

        #========================Scrollbar================================================
        Table_frame=Frame(self.root,bd=15,relief=RIDGE,bg="white")
        Table_frame.place(x=15,y=505,width=1250,height=165)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        #===================================================================================================
        self.book_table=ttk.Treeview(Table_frame,columns=("Ref","Book Title","Author Name","Publication Date","Language","Editor","Nb Pages","ISBN"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.book_table.xview)
        scroll_y.config(command=self.book_table.yview)

        self.book_table["show"]="headings"
        self.book_table.heading("Ref",text="Ref")
        self.book_table.heading("Book Title",text="Book Title")
        self.book_table.heading("Author Name",text="Author Name")
        self.book_table.heading("Publication Date",text="Publication Date")
        self.book_table.heading("Language",text="Language")
        self.book_table.heading("Editor",text="Editor")
        self.book_table.heading("Nb Pages",text="Nb Pages")
        self.book_table.heading("ISBN",text="ISBN")
        
        self.book_table.pack(fill=BOTH,expand=1)

        self.book_table.column("Ref",width=100)
        self.book_table.column("Book Title",width=100)
        self.book_table.column("Author Name",width=100)
        self.book_table.column("Publication Date",width=100)
        self.book_table.column("Language",width=100)
        self.book_table.column("Editor",width=100)
        self.book_table.column("Nb Pages",width=100)
        self.book_table.column("ISBN",width=100)
        
        self.fatch_data()
        self.book_table.bind("<ButtonRelease-1>",self.get_cursor)

        #==========================FUNCTIONS=====================================
        
        btnUploadImg=Button(DataFrame,command=self.upload,text="Upload Image",font=("arial",12,"bold"),fg="white",bg="brown",activebackground="white",width=14)
        btnUploadImg.grid(row=4,column=5,sticky=W,padx=950,pady=220)
        self.label_img = ttk.Label(self.DataFrameRight)
        self.label_img.pack()
        
        
        
    def upload(self):
        f_types = [('PNG files', '*.png'), ('JPG files', '*.jpg')]
        self.filename = filedialog.askopenfilename(filetypes=f_types)

        if self.filename:
            img = Image.open(self.filename)
            img = img.resize((100, 150))
            self.img = ImageTk.PhotoImage(img)
            self.label_img.configure(image=self.img)
            
    
    def AddBook(self):
        if not self.filename:
            return
        with open(self.filename, 'rb') as f:
            image_binary = f.read()
        try:
            
            
            if self.var_Title.get()=="" or self.var_Author.get()=="" or self.var_PubDate.get()=="" or self.var_Lang.get()=="Select" or self.var_Editor.get()=="" or self.var_NbPages.get()=="" or self.var_ISBN.get()=="":
              messagebox.showerror("Error","All fields are Required")
            
            else:
               cnx = mysql.connector.connect(username='root', password='123456', host='localhost', database='biblio')
               cursor = cnx.cursor()
               add_image = ("INSERT INTO books VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (None,self.var_Title.get(),self.var_Author.get(),self.var_PubDate.get(),self.var_Lang.get(),self.var_Editor.get(),self.var_NbPages.get(),self.var_ISBN.get(), image_binary))
               cursor.execute(*add_image)
               cnx.commit()
               self.fatch_data()
               cursor.close()
               cnx.close()
               messagebox.showinfo("Success", "Book inserted in Database.")
               self.var_Title.set("")
               self.var_Author.set("")
               self.var_PubDate.set("")
               self.var_Lang.set("Select")
               self.var_Editor.set("")
               self.var_NbPages.set("")
               self.var_ISBN.set("")
               self.var_Ref.set("")
               self.filename = None
               self.label_img.configure(text="")
               
               
        except mysql.connector.Error as err:
           messagebox.showerror("Error", err.msg)

    def fatch_data(self):
          cnx = mysql.connector.connect(username='root', password='123456', host='localhost', database='biblio')
          cursor = cnx.cursor()
          cursor.execute("SELECT * FROM books")
          row=cursor.fetchall()
          if len(row)!=0:
             self.book_table.delete(*self.book_table.get_children())
             for i in row:
                self.book_table.insert("",END,values=i)
             cnx.commit()
          cnx.close()
     
    def get_cursor(self,evnt):
        cursor_row=self.book_table.focus()
        content=self.book_table.item(cursor_row)
        row=content["values"]
        
        self.var_Ref.set(row[0])
        self.var_Title.set(row[1])
        self.var_Author.set(row[2])
        self.var_PubDate.set(row[3])
        self.var_Lang.set(row[4])
        self.var_Editor.set(row[5])
        self.var_NbPages.set(row[6])
        self.var_ISBN.set(row[7])
        
 
        
        
    def update_book(self):
        if not self.filename:
            return
        with open(self.filename, 'rb') as f:
            image_binary = f.read()
        try:
            if self.var_Title.get() == "" or self.var_Author.get() == "" or self.var_PubDate.get() == "" or self.var_Lang.get() == "Select" or self.var_Editor.get() == "" or self.var_NbPages.get() == "" or self.var_ISBN.get() == "":
                messagebox.showerror("Error", "All fields are Required")
            else:
                cnx = mysql.connector.connect(username='root', password='123456', host='localhost', database='biblio')
                cursor = cnx.cursor()
                update_book_query = "UPDATE books SET Title = %s, Author = %s, Publication_date = %s, Lang = %s, Editor = %s, Nb_Pages = %s, ISBN = %s, Img_Book = %s WHERE Ref = %s"
                book_data = (self.var_Title.get(), self.var_Author.get(), self.var_PubDate.get(), self.var_Lang.get(), self.var_Editor.get(), self.var_NbPages.get(), self.var_ISBN.get(), image_binary,self.var_Ref.get())
                cursor.execute(update_book_query, book_data)
                cnx.commit()
                self.fatch_data()
                cursor.close()
                cnx.close()
                messagebox.showinfo("Success", "Book updated in Database.")
                self.var_Title.set("")
                self.var_Author.set("")
                self.var_PubDate.set("")
                self.var_Lang.set("Select")
                self.var_Editor.set("")
                self.var_NbPages.set("")
                self.var_ISBN.set("")
                self.var_Ref.set("")
                self.filename = None
                self.label_img.configure(text="")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", err.msg)

    def delete_book(self):
        cnx = mysql.connector.connect(username='root', password='123456', host='localhost', database='biblio')
        cursor = cnx.cursor()
        sql="DELETE FROM books where Ref=%s"
        val=(self.var_Ref.get(),)
        cursor.execute(sql,val)
        cnx.commit()
        self.fatch_data()
        cnx.close()
        messagebox.showinfo("Success", "Book Deleted From Database.")
        self.var_Title.set("")
        self.var_Author.set("")
        self.var_PubDate.set("")
        self.var_Lang.set("Select")
        self.var_Editor.set("")
        self.var_NbPages.set("")
        self.var_ISBN.set("")
        self.var_Ref.set("")
        self.filename = None
        self.label_img.configure(text="")
        
    def reset(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to reset the form?"):
            self.var_Title.set("")
            self.var_Author.set("")
            self.var_PubDate.set("")
            self.var_Lang.set("Select")
            self.var_Editor.set("")
            self.var_NbPages.set("")
            self.var_ISBN.set("")
            self.var_Ref.set("")
            self.filename = None
            self.label_img.configure(text="")
            self.searchTxt_var.set("")
    
    
    
    
    def search_data(self):
        cnx = mysql.connector.connect(username='root', password='123456', host='localhost', database='biblio')
        cursor = cnx.cursor()
        
        search_var = self.search_var.get()
        search_text = self.searchTxt_var.get()
        if search_var == "Publication Date":
            try:
                date_obj = datetime.strptime(search_text, '%Y-%m-%d').date()
                cursor.execute(f"SELECT * FROM books WHERE `Publication_Date` = %s", (date_obj,))
            except ValueError:
                messagebox.showerror("Error", "Invalid date format! Please use YYYY-MM-DD.")
                return
        else:
            cursor.execute(f"SELECT * FROM books WHERE `{search_var}` LIKE %s", (f"%{search_text}%",))
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.book_table.delete(*self.book_table.get_children())
            for i in rows:
                self.book_table.insert("", END, values=i)
            cnx.commit()
        else:
            messagebox.showinfo("No result", "No matching record found!")
            
        cnx.close()

    def Exit(self):
        MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?',icon = 'warning')
        if MsgBox == 'yes':
            self.root.destroy()
    
    
    


    





#=================================================================================================




if __name__ == "__main__":
    main()
    
    
    
