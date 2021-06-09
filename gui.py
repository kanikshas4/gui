from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector
from tkinter import ttk

class ConnectorDB:
    


    
    def __init__(self,root):

        
        self.root = root
        
       
        self.root.title("mydatabase")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width=False,height=False)
        MainFrame=Frame(self.root, bd=10, width= 770, height=700, relief=RIDGE, bg='RED')
        MainFrame.grid()


        def searchdetails():
            mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="apple123",database="mydb")
            print(mydb)
            mycursor = mydb.cursor()
            mycursor.execute("select * from mypython_table")
            result = mycursor.fetchall()

            if len(result) !=0:
                self.python_records.delete(*self.python_records.get_children())
                for row in result:
                    self.python_records.insert('',END,values=row)
            


        def search():
            mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="apple123",database="mydb")
            print(mydb)
            mycursor = mydb.cursor()
            mycursor.execute("select * from mypython_table where year_of_experience= '%s'" %year_of_experience.get())
            result= mycursor.fetchall()
            if len(result) !=0:
                self.python_records.delete(*self.python_records.get_children())
                for row in result:
                    self.python_records.insert('',END,values=row)

        def cloud():
            mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="apple123",database="mydb")
            print(mydb)
            mycursor = mydb.cursor()
            mycursor.execute("select * from mycloud_table")
            result = mycursor.fetchall()

            if len(result) !=0:
                self.python_records.delete(*self.python_records.get_children())
                for row in result:
                    self.python_records.insert('',END,values=row)

        def game():
            mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="apple123",database="mydb")
            print(mydb)
            mycursor = mydb.cursor()
            mycursor.execute("select * from mygame_table")
            result = mycursor.fetchall()

            if len(result) !=0:
                self.python_records.delete(*self.python_records.get_children())
                for row in result:
                    self.python_records.insert('',END,values=row)

        def data():
            mydb = mysql.connector.connect(host="127.0.0.1",user="root",passwd="apple123",database="mydb")
            print(mydb)
            mycursor = mydb.cursor()
            mycursor.execute("select * from mydata_table")
            result = mycursor.fetchall()

            if len(result) !=0:
                self.python_records.delete(*self.python_records.get_children())
                for row in result:
                    self.python_records.insert('',END,values=row)

            

            
            

            

            
        company = StringVar()
        year_of_experience = StringVar()
        description = StringVar()
        skills = StringVar()


        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame=Frame(TopFrame3, bd=5, width= 770, height=400, padx=2, bg='red', relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 =Frame(LeftFrame, bd=5, width= 600, height=180, padx=2,pady=4, relief=RIDGE)
        LeftFrame1.pack(side=TOP,padx=0,pady=0)

        RightFrame1=Frame(TopFrame3, bd=5, width= 100, height=400, padx=2, bg='red', relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a =Frame(RightFrame1, bd=5, width= 90, height=300, padx=2,pady=2, relief=RIDGE)
        RightFrame1a.pack(side=TOP)
#======================================================================================================
        self.lbltitle=Label(TitleFrame, font=('arial',40,'bold'),text="My Database", bd=7)
        self.lbltitle.grid(row=0,column=0, padx=132)

        self.lblyears_of_experience=Label(LeftFrame1, font=('arial',12,'bold'),text="years of experience",bd=7)
        self.lblyears_of_experience.grid(row=0,column=0,sticky=W, padx=5)
        self.entyears_of_experience=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5, width=44, justify='left',textvariable=year_of_experience)
        self.entyears_of_experience.grid(row=0,column=1,sticky=W, padx=5)
        #========================
        scroll_y = Scrollbar(LeftFrame,orient=VERTICAL)

        self.python_records=ttk.Treeview(LeftFrame,height=12,columns=("company","year_of_experience","description","skills"),yscrollcommand=scroll_y.set)

        scroll_y.pack(side = RIGHT , fill=Y)

        self.python_records.heading("company", text="company")
        self.python_records.heading("year_of_experience", text="year_of_experience")
        self.python_records.heading("description", text="description")
        self.python_records.heading("skills", text="skills")

        self.python_records['show']='headings'

        self.python_records.column("company", width=70)
        self.python_records.column("year_of_experience", width=70)
        self.python_records.column("description", width=70)
        self.python_records.column("skills", width=70)

        self.python_records.pack(fill=BOTH, expand=1)

        
        
        




        
#============================================================================================================
        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold') ,text=" python developer ",bd=4, pady=1, padx=24,width=8, height=2,command=searchdetails).grid(row=0,column=0,padx=1)
        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold') ,text="cloud computing",bd=4, pady=1, padx=24,width=8, height=2,command=cloud).grid(row=1,column=0,padx=1)
        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold') ,text="game devloper",bd=4, pady=1, padx=24,width=8, height=2,command=game).grid(row=2,column=0,padx=1)
        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold') ,text="data scientist",bd=4, pady=1, padx=24,width=8, height=2,command=data).grid(row=3,column=0,padx=1)

        self.btnSearch=Button(RightFrame1a,font=('arial',16,'bold') ,text="search",bd=4, pady=1, padx=24,width=8, height=2,command=search).grid(row=4,column=0,padx=1)
        
     












        

        
                         
        
if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
    
        


