from tkinter import*
from PIL import ImageTk,Image
from employee import employeeClass
from supplier import supplierClass
from component import categoryClass
from sales import salesClass
from products import productClass

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Inventory Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="#EEE8EC")

        # =====title=====
        # self.icon_title=PhotoImage(file="")
        title=Label(self.root,text="BridgeThings IoT",font=("times new roman",20,"bold"),bg="white",fg="#111",anchor="w",padx=80).place(x=0,y=5,relwidth=1,height=40)

        # ==== logout button ====
        btn_logout=Button(self.root,text="Logout",font=("Times new roman",18),fg="black",cursor="hand2").place(x=1350,y=10,height=30,width=150)

        # =====clock=====
        self.clock_label=Label(self.root,text="Welcome to BridgeThings Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",12),bg="#f8f9fa",fg="#111").place(x=0,y=50,relwidth=1,height=20)

        # ======left menu======
        LeftMenu=Frame(self.root,bd=2,relief="ridge",bg="white")
        LeftMenu.place(x=0,y=85,width=300,height=680)

        self.Menulogo=Image.open("images/menulogo.png")
        self.Menulogo=self.Menulogo.resize((300,250),Image.ANTIALIAS)
        self.Menulogo=ImageTk.PhotoImage(self.Menulogo)

        lbl_menulogo=Label(LeftMenu,image=self.Menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        label_Menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#109675").pack(side="top",fill=X)
        btn_employees=Button(LeftMenu,text="Employee",font=("times new roman",20,"bold"),bg="white",cursor="hand2",bd=1,relief="solid",command=self.employee).pack(side="top",fill=X,pady=10)
        btn_components=Button(LeftMenu,text="Components",command=self.category,font=("times new roman",20,"bold"),bg="white",cursor="hand2",bd=1,relief="solid").pack(side="top",fill=X,pady=10)
        btn_suppliers=Button(LeftMenu,text="Suppliers",command=self.supplier,font=("times new roman",20,"bold"),bg="white",cursor="hand2",bd=1,relief="solid").pack(side="top",fill=X,pady=10)
        btn_products=Button(LeftMenu,text="Products",command=self.products,font=("times new roman",20,"bold"),bg="white",cursor="hand2",bd=1,relief="solid").pack(side="top",fill=X,pady=10)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,font=("times new roman",20,"bold"),bg="white",cursor="hand2",bd=1,relief="solid").pack(side="top",fill=X,pady=10)
        
        # =======Content=======
        self.lbl_employee=Label(self.root,text="Total Employees\n[ 0 ]",bg="Grey",fg="white",font=("calibri",20,"bold"),bd=5,relief="ridge")
        self.lbl_employee.place(x=350,y=120,height=150,width=300)
        
        self.lbl_products=Label(self.root,text="Total Products\n[ 0 ]",bg="Grey",fg="white",font=("calibri",20,"bold"),bd=5,relief="ridge")
        self.lbl_products.place(x=750,y=360,height=150,width=300)
        
        self.lbl_suppliers=Label(self.root,text="Total Suppliers\n[ 0 ]",bg="Grey",fg="white",font=("calibri",20,"bold"),bd=5,relief="ridge")
        self.lbl_suppliers.place(x=350,y=360,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bg="Grey",fg="white",font=("calibri",20,"bold"),bd=5,relief="ridge")
        self.lbl_sales.place(x=750,y=120,height=150,width=300)

        self.lbl_stock=Label(self.root,text="Total Components\n[ 0 ]",bg="Grey",fg="white",font=("calibri",20,"bold"),bd=5,relief="ridge")
        self.lbl_stock.place(x=1150,y=120,height=150,width=300)


# =========================================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        
    def products(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
        
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()


