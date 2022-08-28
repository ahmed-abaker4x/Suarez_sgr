from tkinter import*

app = Tk()
app.geometry('1010x550+200+40')
app.resizable(False,False)
app.config(background='white')
app.title('Ahmed [Database Controlle v1.1]')
app.iconbitmap('image/icon.ico')
title = Label(app, text='Database Controle v1.0 System', fg='white',bg='#19282F',font=(15))
title.pack(fill=X)
#=======sql comand=======

def show_db():
    import mysql.connector
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd ='root'
    )
    mycur = conn.cursor()
    mycur.execute('SHOW DATABASES')
    F= Frame(app, bg='whitesmoke',bd=2,relief=GROOVE)
    F.place(x=440,y=240,width=170,height=300)
    title2 = Label(F,text='Database Found',fg='black',bg='#5534A5',height=2)
    title2.pack(fill=X)
    for x in mycur:
       Label(F,text=x).pack()
#=====DB connect=======
def db_connect():
    import mysql.connector
    from tkinter import messagebox
    host = Enn1.get()
    user = Enn2.get()
    passwd = Enn3.get()
    try:
        conn = mysql.connector.connect(
            host = host,
            user = user,
            passwd = passwd
        )
        messagebox.showinfo('DB[System]', 'تم الاتصال بنجاح')
    except mysql.connector.Error as r:
        messagebox.showerror('Error',r)

#======Create DB=====
def db_create():
    import mysql.connector
    from tkinter import messagebox
    db = En1.get()
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root'
        )

        mycur = conn.cursor()
        mycur.execute('CREATE DATABASE {}'.format(db))
        messagebox.showinfo('DB[System','تم نشاء قاهدة البيانات جديدة ')
    except mysql.connector.Error as r:
        messagebox.showerror('Error',r)

# ======crear tabls=====
def col():

    global FF
    global Ent
    global Ent0
    global Ent1
    global Ent2
    global Ent3
    FF = Frame(app, bg='whitesmoke',bd=2,relief=GROOVE )
    FF.place(x=5,y=240,width=215,height=300)
    tiltle2 = Label(FF,text='Table_colums',fg='black',bg='#FF6363',height=2)
    tiltle2.pack(fill=X)

    lab = Label(FF,text='DB_name:',bg='green')
    lab.place(x=2,y=50)
    Ent = Entry(FF)
    Ent.place(x=80,y=50)

    lab0 = Label(FF,text='Table_name:',bg='red')
    lab0.place(x=2,y=80)
    Ent0 = Entry(FF)
    Ent0.place(x=80,y=80)

    lab1 = Label(FF, text='Col_name:', bg='blue')
    lab1.place(x=2, y=110)
    Ent1 = Entry(FF)
    Ent1.place(x=80, y=110)

    lab2 = Label(FF, text='Col_type:', bg='yellow')
    lab2.place(x=2, y=140)
    Ent2 = Entry(FF)
    Ent2.place(x=80, y=140)

    lab3 = Label(FF, text='Col_length:', bg='grey')
    lab3.place(x=2, y=170)
    Ent3 = Entry(FF)
    Ent3.place(x=80, y=170)

    B = Button(FF,text='Create Table and Column',cursor='hand2',fg='black',bg='#FFEBC1',bd=1,relief=SOLID,command=Create_Table)
    B.place(x=10,y=210,width=190,height=60)

def coll():
    global FFF
    global Ent
    global Ent0
    global Ent1
    global Ent2
    global Ent3

    FFF = Frame(app, bg='whitesmoke', bd=2, relief=GROOVE)
    FFF.place(x=222, y=240, width=215, height=300)
    tiltle2 = Label(FFF, text='New_column', fg='black', bg='#FF6363', height=2)
    tiltle2.pack(fill=X)

    lab = Label(FFF, text='DB_name:', bg='green')
    lab.place(x=2, y=50)
    Ent = Entry(FFF)
    Ent.place(x=80, y=50)

    lab0 = Label(FFF, text='Table_name:', bg='red')
    lab0.place(x=2, y=80)
    Ent0 = Entry(FFF)
    Ent0.place(x=80, y=80)

    lab1 = Label(FFF, text='Col_name:', bg='blue')
    lab1.place(x=2, y=110)
    Ent1 = Entry(FFF)
    Ent1.place(x=80, y=110)

    lab2 = Label(FFF, text='Col_type:', bg='yellow')
    lab2.place(x=2, y=140)
    Ent2 = Entry(FFF)
    Ent2.place(x=80, y=140)

    lab3 = Label(FFF, text='Col_length:', bg='grey')
    lab3.place(x=2, y=170)
    Ent3 = Entry(FFF)
    Ent3.place(x=80, y=170)

    B = Button(FFF, text='Add New Column', cursor='hand2', fg='black', bg='#FFEBC1', bd=1, relief=SOLID,command=Add_Cols)
    B.place(x=10, y=210, width=190, height=60)

def Create_Table():
    import mysql.connector
    from tkinter import messagebox
    db = Ent.get()
    tb_name = Ent0.get()
    col_name = Ent1.get()
    col_type = Ent2.get()
    col_length = Ent3.get()

    try:
        conn = mysql.connector.connect(
            host= 'localhost',
            user = 'root',
            passwd = 'root',
            database = db
        )
        mycur = conn.cursor()
        mycur.execute('CREATE TABLE {} ({} {} ({}))'.format(tb_name,col_name,col_type,col_length))
        messagebox.showinfo('Db[System]','تم انشاء جدول بنجاح')
    except mysql.connector.Error as r:
        messagebox.showerror('Error',r)

def Add_Cols():
    import mysql.connector
    from tkinter import messagebox
    db = Ent.get()
    tb_name = Ent0.get()
    col_name = Ent1.get()
    col_type = Ent2.get()
    col_length = Ent3.get()

    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database=db
        )
        mycur = conn.cursor()
        mycur.execute('ALTER TABLE {} ({} {} ({}))'.format(tb_name, col_name, col_type, col_length))
        messagebox.showinfo('Db[System]', 'تم اضافة حقل جديدة الي جدول')
    except mysql.connector.Error as r:
        messagebox.showerror('Error', r)

#=====DROP DB=======
def Drop_bd():
    import mysql.connector
    from tkinter import messagebox
    db = En11.get()
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root'
        )
        mycur = conn.cursor()
        mycur.execute('DROP DATABASE {}'.format(db))
        messagebox.showinfo('DB[System', 'تم مسح قاعدة البيانات بنجاج....!! ')
    except mysql.connector.Error as r:
        messagebox.showerror('Error', r)


F1 =Frame(app,bg='whitesmoke',bd=2,relief=GROOVE)
F1.place(x=5 ,y=40 ,width=300,height=190)
title1 = Label(F1, text='Database Controle ', fg='white',bg='#5534A5',font=(15))
title1.pack(fill=X)
#=======Show DB=======
L =Label(F1, text='All DB')
L.place(x=10 ,y=50)
button1 = Button(F1,text='All DB',cursor='hand2',command=show_db)
button1.place(x= 100,y=47,width=125)
button2 =Button(F1, text='Hide', bg='#F4DFBA', cursor='hand2')
button2.place(x=230, y=47 ,width=60)
#=======DB Name ========
L1 = Label(F1,text='DB_NAME: ')
L1.place(x=10 ,y=80)
En1 = Entry(F1)
En1.place(x=100 ,y=80 )
b1 = Button(F1,text='Create ',bg='#F4DFBA',cursor='hand2',command=db_create)
b1.place(x=230,y=78,width=60)
#======DROP DB=========
L1 = Label(F1,text='DB_Drop: ')
L1.place(x=10 ,y=110)
En11 = Entry(F1)
En11.place(x=100 ,y=110 )
b1 = Button(F1,text='Drop DB ',bg='#F4DFBA',cursor='hand2',command= Drop_bd)
b1.place(x=230,y=110,width=60)
#====== Columun======
L3 = Label(F1,text='Add_Cols: ')
L3.place(x=10 ,y=140)
button = Button(F1,text='Add_columns:',cursor='hand2')
button.place(x= 100,y=137,width=125)
button2 =Button(F1, text='Hide', bg='#F4DFBA', cursor='hand2')
button2.place(x=230, y=137 ,width=60)
#======Frame two======
FF1 =Frame(app,bg='whitesmoke',bd=2,relief=GROOVE)
FF1.place(x=305 ,y=40 ,width=300,height=190)
title1 = Label(FF1, text='Database Connect ', fg='white',bg='#5534A5',font=(15))
title1.pack(fill=X)
#=========Server====
LL1 = Label(FF1,text='Server_Name: ')
LL1.place(x=10 ,y=50)
Enn1 = Entry(FF1)
Enn1.place(x=100 ,y=50 )
#======User_name=======
LL2 = Label(FF1,text='User_NAME: ')
LL2.place(x=10 ,y=80)
Enn2 = Entry(FF1)
Enn2.place(x=100 ,y=80 )
#====Passwd=====
LL3 = Label(FF1,text='Passwd: ')
LL3.place(x=10 ,y=110)
Enn3 = Entry(FF1)
Enn3.place(x=100 ,y=110)
#=====DB_conn=====
btn_conn = Button(FF1, text='Connect',relief=SOLID,fg='black',bg='#FFEBC1',cursor='hand2',command=db_connect)
btn_conn.place(x=227,y=49,width=65,height=80)
LL4 = Label(FF1,text='Test To Connecter the Server ',fg='blue')


LL4.place(x=10,y=165)
#========logo=======
Logo = PhotoImage(file='image/logo.png')
loglaple = Label(app,image=Logo)
loglaple.place(x=610,y=40,width=390,height=500,)




coll()
col()
#show_db()
app.mainloop()
