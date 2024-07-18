import sqlite3
def create_db():
    conn=sqlite3.connect(database=r'ims.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(Emp_Id INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Email text,Gender text,DOB text,Salary text,Contact text,DOJ text,Usertype text,Password text,Address text)")
    conn.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(Invoice_No INTEGER PRIMARY KEY UNIQUE,Name text,Contact text,Desc text)")
    conn.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS category(Cat_Id INTEGER PRIMARY KEY AUTOINCREMENT,Component_Name,Component_Type,Quantity,Storage_Location)")
    conn.commit()
    
create_db()
