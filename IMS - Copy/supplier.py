from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Supplier Data")
        self.root.geometry("1175x650+320+115")
        self.root.config(bg="#EEE8EC")
        self.root.focus_force()
        self.root.resizable(False,False)

        # ===================== Variables===================
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()

        txt_search=Entry(self.root,textvariable=self.var_searchtext,font=("times new roman",15),bg="light yellow",bd=0.5,relief="solid")
        txt_search.place(x=780,y=45,width=250)

        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15),cursor="hand2",bg="#4caf50",fg="white",bd=1,relief="solid").place(x=1040,y=45,width=118,height=26)
        lbl_sup_invoice=Label(self.root,text="Invoice No",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=680,y=45)
        
        # ============= title ==============
        title=Label(self.root,text="Supplier Details",font=("times new roman",15),bg="light blue",fg="black",bd=2,relief="ridg").place(x=50,y=5,width=1100)

        # ============= content =============
        # ============== row1 ===============
        lbl_sup_invoice=Label(self.root,text="Invoice No.",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=50,y=45)
        lbl_sup_name=Label(self.root,text="Supplier Name",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=50,y=85)
        lbl_sup_contact=Label(self.root,text="Contact",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=50,y=125)
        lbl_sup_desc=Label(self.root,text="Description",font=("times new roman",15),bg="#eee8ec",fg="black").place(x=50,y=165)

        txt_sup_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=185,y=45)
        txt_sup_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=185,y=85)
       

        txt_sup_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid").place(x=185,y=125)
        self.txt_sup_desc=Text(self.root,font=("times new roman",15),bg="light yellow",fg="black",bd=1,relief="solid")
        self.txt_sup_desc.place(x=185,y=165,height=100,width=450)

        btn_save=Button(self.root,text="Save",command=self.add,font=("times new roman",15),cursor="hand2",bg="#0F8FF1",fg="white",bd=1,relief="solid").place(x=200,y=400,width=85,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("times new roman",15),cursor="hand2",bg="#4caf50",fg="white",bd=1,relief="solid").place(x=300,y=400,width=85,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("times new roman",15),cursor="hand2",bg="red",fg="white",bd=1,relief="solid").place(x=400,y=400,width=85,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15),cursor="hand2",bg="grey",fg="white",bd=1,relief="solid").place(x=500,y=400,width=85,height=28)

        # ================== supplier details frame ====================
        sup_frame=Frame(self.root,bd=3,relief="ridge")
        sup_frame.place(x=680,y=80,height=500,width=480)

        scrolly=Scrollbar(sup_frame,orient="vertical")
        scrollx=Scrollbar(sup_frame,orient="horizontal")

        self.SupTable=ttk.Treeview(sup_frame,columns=("Invoice_No","Name","Contact","Desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side="bottom",fill=X)
        scrolly.pack(side="right",fill=Y)
        scrollx.config(command=self.SupTable.xview)
        scrolly.config(command=self.SupTable.yview)

        self.SupTable.heading("Invoice_No",text="Invoice No")
        self.SupTable.heading("Name",text="Name")
        self.SupTable.heading("Contact",text="Contact")
        self.SupTable.heading("Desc",text="Description")
        
        self.SupTable['show']='headings'

        self.SupTable.column("Invoice_No",width=50)
        self.SupTable.column("Name",width=100)
        self.SupTable.column("Contact",width=100)
        self.SupTable.column("Desc",width=100)
        self.SupTable.pack(fill=BOTH,expand=1)
        self.SupTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()

# ======================================= functions (save,update,delete,clear) ===========================================
    
    def add(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice number must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice_No=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This invoice number is already assigned, try different one.",parent=self.root)
                else:
                    cur.execute("Insert into supplier (Invoice_No,Name,Contact,Desc) values(?,?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_sup_desc.get('1.0',END)
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Supplier added successfully",parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def show(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.SupTable.delete(*self.SupTable.get_children())
            for row in rows:
                self.SupTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
      
    
    def get_data(self,ev):
        f=self.SupTable.focus()
        content=(self.SupTable.item(f))
        row=content['values']
        # print(row)
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_sup_desc.delete('1.0',END),
        self.txt_sup_desc.insert(END,row[3])
    
    def update(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice number is required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice_No=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice number",parent=self.root)
                else:
                    cur.execute("update supplier set Name=?,Contact=?,Desc=? where Invoice_No=?",(
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_sup_desc.get('1.0',END),
                                        self.var_sup_invoice.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Supplier updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def delete(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice number is required",parent=self.root)
            else:
                cur.execute("Select * from supplier where Invoice_No=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice number",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where Invoice_No=?",(self.var_sup_invoice.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","Supplier removed successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_sup_desc.delete('1.0',END),
        self.var_searchtext.set(" "),
        self.show()
        
    def search(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_searchtext.get()=="":
                messagebox.showerror("Error","Invoice Number is required!!",parent=self.root)
            else:
                cur.execute("select * from supplier where Invoice_No=?",(self.var_searchtext.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupTable.delete(*self.SupTable.get_children())
                    self.SupTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
        

if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()