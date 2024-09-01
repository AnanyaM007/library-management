from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # variables
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()
        
        # Set the title
        lbltitle = Label(self.root, text="Library Management System", bg="#003366", fg="white", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        # Main frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="#f2f2f2")
        frame.place(x=0, y=130, width=1530, height=400)

        # Data frame Left
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="#f2f2f2", fg="#003366", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        # Member Type
        lblMember = Label(DataFrameLeft, bg="#f2f2f2", text="Member Type", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.member_var, width=27, state="readonly")
        comMember["value"] = ("Admin Staff", "Lecturer", "Student")
        comMember.current(0)
        comMember.grid(row=0, column=1)

       # PRN No
        lblPRN_NO = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PRN No:", padx=2, pady=6, bg="#f2f2f2")
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.prn_var)
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO.grid(row=1, column=1)

        # ID No
        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID No:", padx=2, pady=4, bg="#f2f2f2")
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.id_var)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle.grid(row=2, column=1)

        # First Name
        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="First Name", padx=2, pady=6, bg="#f2f2f2")
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.firstname_var)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName.grid(row=3, column=1)

        # Last Name
        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Last Name", padx=2, pady=6, bg="#f2f2f2")
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.lastname_var)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName.grid(row=4, column=1)

        # Address 1
        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 1", padx=2, pady=6, bg="#f2f2f2")
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.address1_var)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1.grid(row=5, column=1)

        # Address 2
        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 2", padx=2, pady=6, bg="#f2f2f2")
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.address2_var)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2.grid(row=6, column=1)

        # Post Code
        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code", padx=2, pady=6, bg="#f2f2f2")
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.postcode_var)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode.grid(row=7, column=1)

        # Mobile
        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile", padx=2, pady=6, bg="#f2f2f2")
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.mobile_var)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile.grid(row=8, column=1)

        # Book ID
        lblBookId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book ID:", padx=2, pady=6, bg="#f2f2f2")
        txtBookId = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.bookid_var)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId.grid(row=0, column=3)

        # Book Title
        lblBookTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title:", padx=2, pady=6, bg="#f2f2f2")
        txtBookTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.booktitle_var)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle.grid(row=1, column=3)

        # Author Name
        lblAuthor = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Author Name:", padx=2, pady=6, bg="#f2f2f2")
        txtAuthor = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.author_var)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor.grid(row=2, column=3)

        # Date Borrowed
        lblDateBorrowed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=6, bg="#f2f2f2")
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.dateborrowed_var)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed.grid(row=3, column=3)

        # Date Due
        lblDateDue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=6, bg="#f2f2f2")
        txtDateDue = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.datedue_var)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue.grid(row=4, column=3)

        # Days on Book
        lblDaysOnBook = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days On Book:", padx=2, pady=6, bg="#f2f2f2")
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.daysonbook_var)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook.grid(row=5, column=3)

        # Late Return Fine
        lblLateReturnFine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=6, bg="#f2f2f2")
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.lateratefine_var)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine.grid(row=6, column=3)

        # Date Over Due
        lblDateOverdue = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over Due:", padx=2, pady=6, bg="#f2f2f2")
        txtDateOverdue = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.dateoverdue_var)
        lblDateOverdue.grid(row=7, column=2, sticky=W)
        txtDateOverdue.grid(row=7, column=3)

        # Actual Price
        lblActualPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Actual Price:", padx=2, pady=6, bg="#f2f2f2")
        txtActualPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.finalprice_var)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice.grid(row=8, column=3)

        # Data frame Right
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="#f2f2f2", fg="#003366", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)
        
        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2, sticky="ns")
        
        listBooks = [
            'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Great Gatsby', 
            'Moby Dick', 'War and Peace', 'Hamlet', 'The Catcher in the Rye', 
            'The Hobbit', 'Crime and Punishment'
        ]

        def SelectBooks(event=""):
            value = str(ListBox.get(ListBox.curselection()))
            x = value
            
            if x == "To Kill a Mockingbird":
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Historical Novel")
                self.author_var.set("Harper Lee")
                
            elif x == "1984":
                self.bookid_var.set("BKID1984")
                self.booktitle_var.set("Dystopian Fiction")
                self.author_var.set("George Orwell")
                
            elif x == "Pride and Prejudice":
                self.bookid_var.set("BKID8743")
                self.booktitle_var.set("Romantic Novel")
                self.author_var.set("Jane Austen")
                
            elif x == "The Great Gatsby":
                self.bookid_var.set("BKID2314")
                self.booktitle_var.set("Tragedy")
                self.author_var.set("F. Scott Fitzgerald")
                
            elif x == "Moby Dick":
                self.bookid_var.set("BKID6874")
                self.booktitle_var.set("Adventure Fiction")
                self.author_var.set("Herman Melville")
                
            elif x == "War and Peace":
                self.bookid_var.set("BKID6743")
                self.booktitle_var.set("Historical Novel")
                self.author_var.set("Leo Tolstoy")
                
            elif x == "Hamlet":
                self.bookid_var.set("BKID4321")
                self.booktitle_var.set("Tragedy")
                self.author_var.set("William Shakespeare")
                
            elif x == "The Catcher in the Rye":
                self.bookid_var.set("BKID4598")
                self.booktitle_var.set("Realistic Fiction")
                self.author_var.set("J.D. Salinger")
                
            elif x == "The Hobbit":
                self.bookid_var.set("BKID9874")
                self.booktitle_var.set("Fantasy")
                self.author_var.set("J.R.R. Tolkien")
                
            elif x == "Crime and Punishment":
                self.bookid_var.set("BKID5637")
                self.booktitle_var.set("Psychological Fiction")
                self.author_var.set("Fyodor Dostoevsky")
            
            # Set common fields
            d1 = datetime.datetime.today().strftime('%Y-%m-%d')
            d3 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime('%Y-%m-%d')
            self.dateborrowed_var.set(d1)
            self.datedue_var.set(d3)
            self.daysonbook_var.set(15)
            self.lateratefine_var.set("Rs. 50")
            self.dateoverdue_var.set("NO")
            self.finalprice_var.set("Rs. 700")

        
        ListBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        ListBox.bind("<<ListboxSelect>>",SelectBooks)
        ListBox.grid(row=0, column=0, padx=4)
        
        # Create a Scrollbar and attach it to the ListBox
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        ListBox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=ListBox.yview)
        
        for item in listBooks:
            ListBox.insert(END, item)

        # Button Frame
        btnframe = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="#f2f2f2")
        btnframe.place(x=0, y=530, width=1530, height=60)

        # Buttons
        btnAddData=Button(btnframe, command=self.add_data, text="Add Data", font=("arial", 12, "bold"), width=23, bg="#006699", fg="white")
        btnAddData.grid(row=0, column=0)
        
        btnShowData = Button(btnframe, command=self.showData, text="Show Data", font=("arial", 12, "bold"), width=23, bg="#006699", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdateData = Button(btnframe, command=self.update, text="Update", font=("arial", 12, "bold"), width=23, bg="#006699", fg="white")
        btnUpdateData.grid(row=0, column=2)

        btnDeleteData = Button(btnframe, command=self.delete, text="Delete", font=("arial", 12, "bold"), width=23, bg="#006699", fg="white")
        btnDeleteData.grid(row=0, column=3)

        btnResetData = Button(btnframe, command=self.reset, text="Reset", font=("arial", 12, "bold"), width=23, bg="#006699", fg="white")
        btnResetData.grid(row=0, column=4)

        btnExit = Button(btnframe, command=self.iExit, text="Exit", font=("arial", 12, "bold"), width=23, bg="#006699", fg="white")
        btnExit.grid(row=0, column=5)

        # Information Frame
        frameDetails = Frame(self.root, bd=12, relief=RIDGE, bg="#f2f2f2")
        frameDetails.place(x=0, y=590, width=1530, height=210)
        
        Table_frame = Frame(frameDetails, bd=6, relief=RIDGE, bg="#f2f2f2")
        Table_frame.place(x=0, y=2, width=1460, height=190)
        
        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        
        self.library_table = ttk.Treeview(Table_frame, column=("membertype", "prnno", "title", "firstname", "lastname", "address1", "address2", "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)
        
        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)
        
        self.fetch_data()
        self.library_table.bind("<<ButtonRelease-1>>",self.get_cursor)
        
    def add_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        cur = con.cursor()
        cur.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()
        ))
        
        con.commit()
        self.fetch_data()
        con.close()
        
        messagebox.showinfo("Success", "Member has been inserted successfully")
    
    def update(self):
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        cur = con.cursor()
        cur.execute("update library set member_type=%s, prn_no=%s, id_no=%s, firstname=%s, lastname=%s, address1=%s, address2=%s, postcode=%s, mobile=%s, book_id=%s, book_title=%s, author=%s, date_borrowed=%s, date_due=%s, days_on_book=%s, late_return_fine=%s, date_overdue=%s, final_price=%s where prn_no=%s",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get()
        ))
        
        con.commit()
        self.fetch_data()
        self.reset()
        con.close()
        
        messagebox.showinfo("Success", "Member has been updated successfully")        
            
    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
        cur = con.cursor()
        cur.execute("select * from library")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert("", END, values=row)
            con.commit()
        con.close()    

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]
        
        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.lateratefine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])
        
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t" + self.member_var.get() + "\n")    
        self.txtBox.insert(END,"PRN No.\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No.\t\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address 1\t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address 2\t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Postcode\t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No.\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author\t\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END,"Date Borrowed\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"Date Due\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Days on Book\t\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"Late Rate Fine\t\t" + self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END,"Date Overdue\t\t" + self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"Final Price\t\t" + self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.lateratefine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")    
        self.txtBox.delete("1.0",END)
        
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Confirm if you want to exit")
        if iExit > 0:
            self.root.destroy()
        else:
            return  
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="123456", database="library_management")
            cur = con.cursor()
            query="delete from library where prn_no=%s"
            value=(self.prn_var.get(),)
            cur.execute(query,value)
            
            con.commit()
            self.fetch_data()
            self.reset()
            con.close()
            
            messagebox.showinfo("Success", "Member has been deleted successfully")          
        
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
