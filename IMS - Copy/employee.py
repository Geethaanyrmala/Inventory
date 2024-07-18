from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Data")
        self.root.geometry("1175x650+320+115")
        self.root.config(bg="#EEE8EC")
        self.root.focus_force()
        self.root.resizable(False,False)

        # ===================== Variables===================
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()
        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_doj=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()

        # ============Search Bar=============
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="#EEE8EC",fg="black",font=("times new roman",15))
        SearchFrame.place(x=280,y=20,width=700,height=70)

        # ==============Options================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select one","Emp_Id","Email","Name"),state="readonly",justify="center",font=("times new roman",15))
        cmb_search.place(x=10,y=5,width=200)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtext,font=("times new roman",15),bg="light yellow",bd=0.5,relief="solid")
        txt_search.place(x=250,y=5)

        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",15),cursor="hand2",bg="#4caf50",fg="white",bd=1,relief="solid").place(x=500,y=4,width=150,height=28)

        # ============= title ==============
        title=Label(self.root,text="Employee Details",font=("times new roman",15),bg="light blue",fg="black").place(x=50,y=125,width=1075)

        # ============= content =============
        lbl_emp_id=Label(self.root,text="Employee ID",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=50,y=175)
        lbl_emp_gender=Label(self.root,text="Gender",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=450,y=175)
        lbl_emp_contact=Label(self.root,text="Contact No",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=800,y=175)

        txt_emp_id=Entry(self.root,textvariable=self.var_emp_id,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=175,y=175)
        txt_emp_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=175,y=255)
        txt_emp_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=175,y=335)

        lbl_emp_name=Label(self.root,text="Name",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=50,y=255)
        lbl_emp_dob=Label(self.root,text="D.O.B",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=450,y=255)
        lbl_emp_doj=Label(self.root,text="D.O.J",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=800,y=255)

        # txt_emp_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=525,y=175)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select one","Male","Female"),state="readonly",justify="center",font=("times new roman",12))
        cmb_gender.place(x=525,y=175,width=200)
        cmb_gender.current(0)
        txt_emp_dob=Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=525,y=255)
        txt_emp_salary=Entry(self.root,textvariable=self.var_salary,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=525,y=335)

        lbl_emp_email=Label(self.root,text="Email",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=50,y=335)
        lbl_emp_salary=Label(self.root,text="Salary",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=450,y=335)
        lbl_emp_utype=Label(self.root,text="User Type",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=800,y=335)
        lbl_emp_address=Label(self.root,text="Address",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=50,y=415)
        lbl_emp_password=Label(self.root,text="Password",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=650,y=415)

        txt_emp_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=905,y=175)
        txt_emp_doj=Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=905,y=255)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select one","Employee","Admin","Intern"),state="readonly",justify="center",font=("times new roman",12))
        cmb_utype.place(x=905,y=335,width=200)
        cmb_utype.current(0)
        self.txt_emp_address=Text(self.root,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid")
        self.txt_emp_address.place(x=175,y=415,height=80,width=450)
        txt_emp_password=Entry(self.root,textvariable=self.var_password,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=755,y=414)

        btn_save=Button(self.root,text="Save",command=self.add,font=("times new roman",15),cursor="hand2",bg="#0F8FF1",fg="white",bd=1,relief="solid").place(x=650,y=467,width=85,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",15),cursor="hand2",bg="#4caf50",fg="white",bd=1,relief="solid").place(x=750,y=467,width=85,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15),cursor="hand2",bg="red",fg="white",bd=1,relief="solid").place(x=850,y=467,width=85,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15),cursor="hand2",bg="grey",fg="white",bd=1,relief="solid").place(x=950,y=467,width=85,height=28)

        # ================== employee details frame ====================
        emp_frame=Frame(self.root,bd=3,relief="ridge")
        emp_frame.place(x=0,y=520,relwidth=1,height=100)

        scrolly=Scrollbar(emp_frame,orient="vertical")
        scrollx=Scrollbar(emp_frame,orient="horizontal")

        self.EmpTable=ttk.Treeview(emp_frame,columns=("Emp_Id","Name","Email","Gender","DOB","Salary","Contact","DOJ","Usertype","Password","Address"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side="bottom",fill=X)
        scrolly.pack(side="right",fill=Y)
        scrollx.config(command=self.EmpTable.xview)
        scrolly.config(command=self.EmpTable.yview)

        self.EmpTable.heading("Emp_Id",text="Emp ID")
        self.EmpTable.heading("Name",text="Name")
        self.EmpTable.heading("Email",text="Email")
        self.EmpTable.heading("Gender",text="Gender")
        self.EmpTable.heading("DOB",text="DOB")
        self.EmpTable.heading("Salary",text="Salary")
        self.EmpTable.heading("Contact",text="Contact")
        self.EmpTable.heading("DOJ",text="DOJ")
        self.EmpTable.heading("Usertype",text="User Type")
        self.EmpTable.heading("Password",text="Password")
        self.EmpTable.heading("Address",text="Address")
        
        self.EmpTable['show']='headings'

        self.EmpTable.column("Emp_Id",width=50)
        self.EmpTable.column("Name",width=100)
        self.EmpTable.column("Email",width=150)
        self.EmpTable.column("Gender",width=100)
        self.EmpTable.column("DOB",width=100)
        self.EmpTable.column("Salary",width=100)
        self.EmpTable.column("Contact",width=100)
        self.EmpTable.column("DOJ",width=100)
        self.EmpTable.column("Usertype",width=100)
        self.EmpTable.column("Password",width=100)
        self.EmpTable.column("Address",width=100)
        self.EmpTable.pack(fill=BOTH,expand=1)
        self.EmpTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()

# ======================================= functions (save,update,delete,clear) ===========================================
    
    def add(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Emp_Id=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This employee id is already assigned, try different one.",parent=self.root)
                else:
                    cur.execute("Insert into employee (Emp_Id,Name,Email,Gender,DOB,Salary,Contact,DOJ,Usertype,Password,Address) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_salary.get(),
                                        self.var_contact.get(),
                                        self.var_doj.get(),
                                        self.var_utype.get(),
                                        self.var_password.get(),
                                        self.txt_emp_address.get('1.0',END)
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Employee added successfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def show(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmpTable.delete(*self.EmpTable.get_children())
            for row in rows:
                self.EmpTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
      
    
    def get_data(self,ev):
        f=self.EmpTable.focus()
        content=(self.EmpTable.item(f))
        row=content['values']
        # print(row)
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_salary.set(row[5]), 
        self.var_contact.set(row[6]),
        self.var_doj.set(row[7]),
        self.var_utype.set(row[8]),
        self.var_password.set(row[9]),
        self.txt_emp_address.delete('1.0',END),
        self.txt_emp_address.insert(END,row[10])
    
    def update(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Emp_Id=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("update employee set Name=?,Email=?,Gender=?,DOB=?,Salary=?,Contact=?,DOJ=?,Usertype=?,Password=?,Address=? where Emp_Id=?",(
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_salary.get(),
                                        self.var_contact.get(),
                                        self.var_doj.get(),
                                        self.var_utype.get(),
                                        self.var_password.get(),
                                        self.txt_emp_address.get('1.0',END),
                                        self.var_emp_id.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Employee updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def delete(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where Emp_Id=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where Emp_Id=?",(self.var_emp_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","EMployee deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select One"),
        self.var_dob.set(""),
        self.var_salary.set(""), 
        self.var_contact.set(""),
        self.var_doj.set(""),
        self.var_utype.set("Select One"),
        self.var_password.set(""),
        self.txt_emp_address.delete('1.0',END),
        self.var_searchtext.set(" "),
        self.var_searchby.set("Select One") 
        self.show()
        
    def search(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_searchby.get()=="Select One":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search input is required!!",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmpTable.delete(*self.EmpTable.get_children())
                    for row in rows:
                        self.EmpTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
        

if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()