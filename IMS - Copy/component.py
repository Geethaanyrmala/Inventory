from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Components Info")
        self.root.geometry("1175x650+320+115")
        self.root.config(bg="#EEE8EC")
        self.root.focus_force()
        self.root.resizable(False,False)
        
        # ============variables==============
        self.var_cat_id=StringVar()
        self.var_Component_Name=StringVar()
        self.var_Component_Type=StringVar()
        self.var_Quantity=StringVar()
        self.var_location=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()
        
        
        # ============ title =================
        lbl_title=Label(self.root,text="Manage Components",font=("Times new roman",17),bg="light blue",fg="black",bd=2,relief="ridge").pack(side="top",fill=X,padx=10,pady=2)
        lbl_Component_id=Label(self.root,text="Component Id",font=("Times new roman",15),bg="#eee8ec").place(x=50,y=50)
        lbl_Component_Name=Label(self.root,text="Component Name",font=("Times new roman",15),bg="#eee8ec").place(x=50,y=95)
        lbl_Component_Type=Label(self.root,text="Component Type",font=("Times new roman",15),bg="#eee8ec").place(x=550,y=95)
        lbl_quantity=Label(self.root,text="Quantity",font=("Times new roman",15),bg="#eee8ec").place(x=50,y=140)
        lbl_location=Label(self.root,text="Location",font=("Times new roman",15),bg="#eee8ec").place(x=550,y=140)
        
        txt_id=Entry(self.root,textvariable=self.var_cat_id,font=("Times new roman",12),bg="light yellow",bd=0.5,relief="solid").place(x=200,y=52,height=25,width=300)
        txt_name=Entry(self.root,textvariable=self.var_Component_Name,font=("Times new roman",12),bg="light yellow",bd=0.5,relief="solid").place(x=200,y=97,height=25,width=300)
        txt_type=Entry(self.root,textvariable=self.var_Component_Type,font=("Times new roman",12),bg="light yellow",bd=0.5,relief="solid").place(x=700,y=97,height=25,width=300)
        txt_quantity=Entry(self.root,textvariable=self.var_Quantity,font=("Times new roman",12),bg="light yellow",bd=0.5,relief="solid").place(x=200,y=142,height=25,width=300)
        txt_location=Entry(self.root,textvariable=self.var_location,font=("Times new roman",12),bg="light yellow",bd=0.5,relief="solid").place(x=700,y=142,height=25,width=300)
        
        btn_add=Button(self.root,text="Add",command=self.add,font=("Times new roman",15),bg="#4caf50",fg="white",cursor="hand2",bd=0.5,relief="solid").place(x=100,y=200,width=200,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("Times new roman",15),bg="#0F8FF1",fg="white",cursor="hand2",bd=0.5,relief="solid").place(x=310,y=200,width=200,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Times new roman",15),bg="red",fg="white",cursor="hand2",bd=0.5,relief="solid").place(x=520,y=200,width=200,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("Times new roman",15),bg="grey",fg="white",cursor="hand2",bd=0.5,relief="solid").place(x=730,y=200,width=200,height=30)
        
        # ============= frame ============
        lbl_display=Label(self.root,text="Category Details: ",font=("Times new roman",15),bg="#eee8ec").place(x=50,y=250)
        
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="#EEE8EC",fg="black",font=("times new roman",12))
        SearchFrame.place(x=200,y=270,width=710,height=50)
        
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select one","Cat_Id","Component_Name","Component_Type","Quantity","Storage_Location"),state="readonly",justify="center",font=("times new roman",11))
        cmb_search.place(x=10,y=1,width=200)
        cmb_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtext,font=("times new roman",12),bg="light yellow",bd=0.5,relief="solid")
        txt_search.place(x=250,y=1,width=200)
        
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("times new roman",15),cursor="hand2",bg="#4caf50",fg="white",bd=1,relief="solid").place(x=500,y=1,width=200,height=23)
        
        cat_frame=Frame(self.root,bd=3,relief="ridge")
        cat_frame.place(x=190,y=330,width=750,height=300)

        scrolly=Scrollbar(cat_frame,orient="vertical")

        self.CatTable=ttk.Treeview(cat_frame,columns=("Cat_Id","Component_Name","Component_Type","Quantity","Storage_Location"),yscrollcommand=scrolly.set)
        scrolly.pack(side="right",fill=Y)
        scrolly.config(command=self.CatTable.yview)
        
        self.CatTable.heading("Cat_Id",text="Component Id")
        self.CatTable.heading("Component_Name",text="Component Name")
        self.CatTable.heading("Component_Type",text="Component Type")
        self.CatTable.heading("Quantity",text="Quantity")
        self.CatTable.heading("Storage_Location",text="Storage Location")
        
        
        self.CatTable['show']='headings'

        self.CatTable.column("Cat_Id",width=50)
        self.CatTable.column("Component_Name",width=100)
        self.CatTable.column("Component_Type",width=100)
        self.CatTable.column("Quantity",width=100)
        self.CatTable.column("Storage_Location",width=100)
        self.CatTable.pack(fill=BOTH,expand=1)
        self.CatTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()

# ======================================= functions (save,update,delete,clear) ===========================================
    
    def add(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Invoice number must be required",parent=self.root)
            else:
                cur.execute("Select * from category where Cat_Id=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This ID is already assigned, try a different one.",parent=self.root)
                else:
                    cur.execute("Insert into category (Cat_Id,Component_Name,Component_Type,Quantity,Storage_Location) values(?,?,?,?,?)",(
                                        self.var_cat_id.get(),
                                        self.var_Component_Name.get(),
                                        self.var_Component_Type.get(),
                                        self.var_Quantity.get(),
                                        self.var_location.get()
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Component added successfully",parent=self.root)
                    self.clear()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def show(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.CatTable.delete(*self.CatTable.get_children())
            for row in rows:
                self.CatTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
      
    
    def get_data(self,ev):
        f=self.CatTable.focus()
        content=(self.CatTable.item(f))
        row=content['values']
        # print(row)
        self.var_cat_id.set(row[0]),
        self.var_Component_Name.set(row[1]),
        self.var_Component_Type.set(row[2]),
        self.var_Quantity.set(row[3]),
        self.var_location.set(row[4])
    
    def update(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Category Id is required",parent=self.root)
            else:
                cur.execute("Select * from category where Cat_Id=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice number",parent=self.root)
                else:
                    cur.execute("update category set Component_Name=?,Component_Type=?,Quantity=?,Storage_Location=? where Cat_Id=?",(
                                        self.var_Component_Name.get(),
                                        self.var_Component_Type.get(),
                                        self.var_Quantity.get(),
                                        self.var_location.get(),
                                        self.var_cat_id.get(),
                    ))
                    conn.commit()
                    messagebox.showinfo("Success","Category updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
    
    def delete(self):
        conn=sqlite3.connect(database=r'ims.db')
        cur=conn.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Component ID is required",parent=self.root)
            else:
                cur.execute("Select * from category where Cat_Id=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where Cat_Id=?",(self.var_cat_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete","Component removed successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
    
    def clear(self):
        self.var_cat_id.set(""),
        self.var_Component_Name.set(""),
        self.var_Component_Type.set(""),
        self.var_Quantity.set(""),
        self.var_location.set(""),
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
                cur.execute("select * from category where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.CatTable.delete(*self.CatTable.get_children())
                    for row in rows:
                        self.CatTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root)
        
                    
        
if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()