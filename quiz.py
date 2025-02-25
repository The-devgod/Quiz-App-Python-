import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time

#LOGIN PAGE
def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Quiz App Login')
    login.geometry("720x440")
    login.configure(bg="#121212")

    user_name = StringVar()
    password = StringVar()

    login_canvas = Canvas(login, width=720, height=540, bg="#121212", highlightthickness=0)
    login_canvas.pack()

    login_frame = Frame(login_canvas, bg="#1E1E1E", bd=2, relief="solid")
    login_frame.place(relwidth=0.4, relheight=0.7, relx=0.3, rely=0.15)

    heading = Label(login_frame, text="Login", fg="#FFFFFF", bg="#1E1E1E", font=('Poppins', 16, 'bold'))
    heading.place(relx=0.1, rely=0.05)

    subheading = Label(login_frame, text="Welcome back, login to your account", fg="#B0B0B0", bg="#1E1E1E", font=("Poppins", 10))
    subheading.place(relx=0.1, rely=0.12)

    # USERNAME
    ulabel = Label(login_frame, text="Username", fg='#FFFFFF', bg='#1E1E1E', font=('Poppins', 10))
    ulabel.place(relx=0.1, rely=0.3)
    uname = Entry(login_frame, bg='#2A2A2A', fg='#FFFFFF', textvariable=user_name, font=('Poppins', 10), bd=0)
    uname.place(relx=0.1, rely=0.35, relwidth=0.8, height=30)
    uname.configure(highlightbackground="#555555", highlightthickness=1)
    uname.config(relief="flat")

    # PASSWORD
    plabel = Label(login_frame, text="Password", fg='#FFFFFF', bg='#1E1E1E', font=('Poppins', 10))
    plabel.place(relx=0.1, rely=0.5)
    pas = Entry(login_frame, bg='#2A2A2A', fg='#FFFFFF', textvariable=password, show="*", font=('Poppins', 10), bd=0)
    pas.place(relx=0.1, rely=0.55, relwidth=0.8, height=30)
    pas.configure(highlightbackground="#555555", highlightthickness=1)
    pas.config(relief="flat")

    def check():
        for a, b, c in logdata:
            if b == uname.get() and c == pas.get():
                print(logdata)
                menu(a)
                break
        else:
            error = Label(login_frame, text="Invalid Username or Password!", fg='red', bg='#1E1E1E', font=('Poppins', 10))
            error.place(relx=0.1, rely=0.72)

    # LOGIN BUTTON
    log = Button(login_frame, text='Login', command=check, fg="white", bg="#008CBA", font=('Poppins', 10, 'bold'), bd=0)
    log.place(relx=0.1, rely=0.8, relwidth=0.8, height=35)
    log.config(borderwidth=0, highlightthickness=0)  # Removing default button border
    log.configure(relief="flat", highlightbackground="#555555")

    login.mainloop()


#SIGNUP/REGISTER PAGE
def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Quiz App')
    sup.configure(bg="#1E1E1E")

    fname = StringVar()
    uname = StringVar()
    passW = StringVar()

    sup_canvas = Canvas(sup, width=720, height=540, bg="#1E1E1E", highlightthickness=0)
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="#2A2A2A", bd=2, relief="solid")
    sup_frame.place(relwidth=0.4, relheight=0.7, relx=0.3, rely=0.15)

    heading = Label(sup_frame, text="Create Account", fg="white", bg="#2A2A2A", font=("Helvetica", 18, "bold"))
    heading.place(relx=0.1, rely=0.05)

    subheading = Label(sup_frame, text="Join Quiz App and test your knowledge!", fg="#AAAAAA", bg="#2A2A2A", font=("Helvetica", 10))
    subheading.place(relx=0.1, rely=0.12)

    # Full Name
    flabel = Label(sup_frame, text="Full Name", fg='white', bg='#2A2A2A', font=("Helvetica", 10))
    flabel.place(relx=0.1, rely=0.25)
    fname_entry = Entry(sup_frame, bg='#3A3A3A', fg='white', textvariable=fname, font=("Helvetica", 10), bd=0)
    fname_entry.place(relx=0.1, rely=0.3, relwidth=0.8, height=30)
    fname_entry.config(highlightbackground="#555555", highlightthickness=1, relief=FLAT)

    # Username
    ulabel = Label(sup_frame, text="Username", fg='white', bg='#2A2A2A', font=("Helvetica", 10))
    ulabel.place(relx=0.1, rely=0.4)
    user_entry = Entry(sup_frame, bg='#3A3A3A', fg='white', textvariable=uname, font=("Helvetica", 10), bd=0)
    user_entry.place(relx=0.1, rely=0.45, relwidth=0.8, height=30)
    user_entry.config(highlightbackground="#555555", highlightthickness=1, relief=FLAT)

    # Password
    plabel = Label(sup_frame, text="Password", fg='white', bg='#2A2A2A', font=("Helvetica", 10))
    plabel.place(relx=0.1, rely=0.55)
    pas_entry = Entry(sup_frame, bg='#3A3A3A', fg='white', textvariable=passW, font=("Helvetica", 10), show="*", bd=0)
    pas_entry.place(relx=0.1, rely=0.6, relwidth=0.8, height=30)
    pas_entry.config(highlightbackground="#555555", highlightthickness=1, relief=FLAT)

    def addUserToDataBase():
        fullname = fname.get()
        username = uname.get()
        password = passW.get()
        
        if not fullname or not username or not password:
            error = Label(text="Please fill in all fields", fg='red', bg='#2A2A2A', font=("Helvetica", 9, "bold"))
            error.place(relx=0.37, rely=0.7)
        else:
            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text, PASSWORD text)')
            create.execute("INSERT INTO userSignUp VALUES (?, ?, ?)", (fullname, username, password))
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z = create.fetchall()
            conn.close()
            loginPage(z)

    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z = create.fetchall()
        loginPage(z)

    # Signup Button
    sp = Button(sup_frame, text='Sign Up', command=addUserToDataBase, bg="#007BFF", fg="white", font=("Helvetica", 10, "bold"), bd=0, relief=FLAT)
    sp.place(relx=0.1, rely=0.8, relwidth=0.8, height=35)

    # Already have an account?
    log = Button(sup_frame, text='Already have an account? Log in', command=gotoLogin, bg="#2A2A2A", fg="#007BFF", font=("Helvetica", 9, "bold"), bd=0, relief=FLAT)
    log.place(relx=0.1, rely=0.9, relwidth=0.8, height=25)

    sup.mainloop()


#MENU PAGE
def menu(username):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Quiz App Menu')
    menu.geometry("720x440")
    menu.configure(bg="#E8EAF6")
    
    menu_canvas = Canvas(menu, width=720, height=440, bg="#E8EAF6", highlightthickness=0)
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas, bg="white", bd=2, relief="solid")
    menu_frame.place(relwidth=0.6, relheight=0.6, relx=0.2, rely=0.2)

    wel = Label(menu_frame, text='WELCOME TO QUIZ STATION', fg="#1E88E5", bg="white", font=('Poppins', 16, 'bold'))
    wel.place(relx=0.15, rely=0.05)
    
    username_text = 'Welcome, ' + username
    level34 = Label(menu_frame, text=username_text, bg="#1E88E5", font=("Poppins", 12, "bold"), fg="white")
    level34.place(relx=0.17, rely=0.15)
    
    level = Label(menu_frame, text='Select your Difficulty Level', bg="white", font=("Poppins", 12))
    level.place(relx=0.25, rely=0.3)
    
    var = IntVar()
    easyR = Radiobutton(menu_frame, text='Easy', bg="white", font=("Poppins", 10), value=1, variable=var)
    easyR.place(relx=0.25, rely=0.4)
    
    mediumR = Radiobutton(menu_frame, text='Medium', bg="white", font=("Poppins", 10), value=2, variable=var)
    mediumR.place(relx=0.25, rely=0.5)
    
    hardR = Radiobutton(menu_frame, text='Hard', bg="white", font=("Poppins", 10), value=3, variable=var)
    hardR.place(relx=0.25, rely=0.6)
    
    def navigate():

        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
            
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    
    letsgo = Button(menu_frame, text="Let's Go", bg="#1E88E5", fg="white", font=("Poppins", 10, "bold"), bd=0, command=navigate)
    letsgo.place(relx=0.15, rely=0.8, relwidth=0.7, height=35)
    menu.mainloop()

def easy():
    global e
    e = Tk()
    e.title('Quiz App - Easy Level')
    e.geometry("720x440")
    e.configure(bg="#F9F9F9")

    easy_canvas = Canvas(e, width=720, height=440, bg="black", highlightthickness=0)
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas, bg="white", bd=2, relief="solid")
    easy_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(15, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0

    easyQ = [
        [
            "What will be the output of the following Python code?\n"
            "l=[1, 0, 2, 0, 'hello', '', []]\n"
            "list(filter(bool, l))",
            "[1, 0, 2, ‘hello’, '', []]",
            "Error",
            "[1, 2, ‘hello’]",
            "[1, 0, 2, 0, ‘hello’, '', []]"
        ],
        [
            "What will be the output of the following Python expression if the value of x is 34?\nprint(“%f” % x)",
            "34.00",
            "34.000000",
            "34.0000",
            "34.00000000"
        ],
        [
            "What will be the value of X in the following Python expression?\nX = 2+9*((3*12)-8)/10",
            "30.8",
            "27.2",
            "28.4",
            "30.0"
        ],
        [
            "Which of these is not a core data type?",
            "Tuples",
            "Dictionary",
            "Lists",
            "Class"
        ],
        [
            "Which of the following represents the bitwise XOR operator?",
            "&",
            "!",
            "^",
            "|"
        ]
    ]
    
    answer = [
                "[1, 2, ‘hello’]",
                "34.000000", 
                "27.2", 
                "Class", 
                "^"
                ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])

    ques = Label(easy_frame, text=easyQ[x][0], font=("Poppins", 12), bg="gray", wraplength=500, justify="center")
    ques.place(relx=0.5, rely=0.15, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(easy_frame, text=easyQ[x][1], font=("Poppins", 10), value=easyQ[x][1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.35, anchor=CENTER)

    b = Radiobutton(easy_frame, text=easyQ[x][2], font=("Poppins", 10), value=easyQ[x][2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.45, anchor=CENTER)

    c = Radiobutton(easy_frame, text=easyQ[x][3], font=("Poppins", 10), value=easyQ[x][3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.55, anchor=CENTER) 

    d = Radiobutton(easy_frame, text=easyQ[x][4], font=("Poppins", 10), value=easyQ[x][4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.65, anchor=CENTER) 
    
    li.remove(x)

    timer = Label(easy_frame, text="15", font=("Poppins", 12, "bold"), fg="red", bg="white")
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)
    

    def display():
        global x  # Ensure x is accessible globally

        if len(li) == 1:
            e.destroy()
            showMark(score)

        if len(li) == 2:
            nextQuestion.configure(text='End', command=calc)

        if li:
            x = random.choice(li[1:])  # Fix: Pick from entire list instead of li[1:]
        
            ques.configure(text=easyQ[x][0])
            a.configure(text=easyQ[x][1], value=easyQ[x][1])
            b.configure(text=easyQ[x][2], value=easyQ[x][2])
            c.configure(text=easyQ[x][3], value=easyQ[x][3])
            d.configure(text=easyQ[x][4], value=easyQ[x][4])
        
            li.remove(x)
        
            y = countDown()
            if y == -1:
                display()

    def calc():
        global score
        if var.get() in answer:
            score += 1
        display()

    # Improved UI for buttons
    submit = Button(easy_frame, command=calc, text="Submit", fg="white", bg="#007BFF", font=("Poppins", 10, "bold"))
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)

    nextQuestion = Button(easy_frame, command=display, text="Next", fg="white", bg="#28A745", font=("Poppins", 10, "bold"))
    nextQuestion.place(relx=0.87, rely=0.82, anchor=CENTER)

    # Previous button (commented out in code)
    # pre = Button(easy_frame, command=display, text="Previous", fg="white", bg="#FFC107", font=("Poppins", 10, "bold"))
    # pre.place(relx=0.75, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()

    e.mainloop()

    
    
def medium():
    global m
    m = Tk()
    m.title('Quiz App - Medium Level')
    m.geometry("720x440")
    m.configure(bg="#F9F9F9")

    med_canvas = Canvas(m, width=720, height=440, bg="#F9F9F9", highlightthickness=0) 
    med_canvas.pack()

    med_frame = Frame(med_canvas, bg="white", bd=2, relief="solid")  # Dark gray background for contrast
    med_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(15, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0

    mediumQ = [
        [
            "Which of the following is not an exception handling keyword in Python?", 
            "accept", 
            "finally", 
            "except", 
            "try"
            ],
        [
            "Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?", 
            "3", 
            "5", 
            "25", 
            "1"
            ],
        [
            "Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?", 
            "Error", 
            "None", 
            "25", 
            "2"
            ],
        [
            "print(0xA + 0xB + 0xC):", 
            "0xA0xB0xC", 
            "Error", 
            "0x22", 
            "33"
            ],
        [
            "Which of the following is invalid?", 
            "_a = 1", 
            "__a = 1", 
            "__str__ = 1", 
            "none of the mentioned"
            ],
    ]
    answer = ["accept", 
              "1", 
              "25", 
              "33", 
              "none of the mentioned"
              ]

    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(med_frame, text=mediumQ[x][0], font=("Poppins", 12), bg="gray", wraplength=500, justify="center")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(med_frame, text=mediumQ[x][1], font=("Poppins", 10), value=mediumQ[x][1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.35, anchor=CENTER)

    b = Radiobutton(med_frame, text=mediumQ[x][2], font=("Poppins", 10), value=mediumQ[x][2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.45, anchor=CENTER)

    c = Radiobutton(med_frame, text=mediumQ[x][3], font=("Poppins", 10), value=mediumQ[x][3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.55, anchor=CENTER)

    d = Radiobutton(med_frame, text=mediumQ[x][4], font=("Poppins", 10), value=mediumQ[x][4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.65, anchor=CENTER)

    li.remove(x)

    timer = Label(med_frame, text="15", font=("Poppins", 12, "bold"), fg="red", bg="white")
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc, text="Submit", fg="white", bg="#007BFF", font=("Poppins", 10, "bold"))
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_frame,command=display, text="Next", fg="white", bg="#28A745", font=("Poppins", 10, "bold"))
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()


def difficult():
    global h
    h = Tk()
    h.title('Quiz App - Hard Level')
    h.geometry("720x440")
    h.configure(bg="#F9F9F9")

    hard_canvas = Canvas(h, width=720, height=440, bg="#F9F9F9", highlightthickness=0) 
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas, bg="white", bd=2, relief="solid")  # Dark gray background for contrast
    hard_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    def countDown():
        check = 0
        for k in range(15, 0, -1):
            if k == 1:
                check = -1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)

        timer.configure(text="Times up!", fg="red", font=("Poppins", 12, "bold"))
        if check == -1:
            return -1
        else:
            return 0

    global score
    score = 0

    hardQ = [
        ["All keywords in Python are in _________", "lower case", "UPPER CASE", "Capitalized", "None of the mentioned"],
        ["Which of the following cannot be a variable?", "__init__", "in", "it", "on"],
        ["Which of the following is a Python tuple?", "[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "{}"],
        ["What is returned by math.ceil(3.4)?", "3", "4", "4.0", "3.0"],
        ["What will be the output of print(math.factorial(4.5))?", "24", "120", "error", "24.0"]
    ]
    answer = ["None of the mentioned", "in", "(1, 2, 3)", "4", "error"]

    li = ['', 0, 1, 2, 3, 4]
    x = random.choice(li[1:])

    ques = Label(hard_frame, text=hardQ[x][0], font=("Poppins", 14, "bold"), bg="#FF6F61", fg="black", wraplength=600)
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    a = Radiobutton(hard_frame, text=hardQ[x][1], font=("Poppins", 10), value=hardQ[x][1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.35, anchor=CENTER)

    b = Radiobutton(hard_frame, text=hardQ[x][1], font=("Poppins", 10), value=hardQ[x][1], variable=var, bg="white")
    b.place(relx=0.5, rely=0.45, anchor=CENTER)

    c = Radiobutton(hard_frame, text=hardQ[x][1], font=("Poppins", 10), value=hardQ[x][1], variable=var, bg="white")
    c.place(relx=0.5, rely=0.55, anchor=CENTER)

    d = Radiobutton(hard_frame, text=hardQ[x][1], font=("Poppins", 10), value=hardQ[x][1], variable=var, bg="white")
    d.place(relx=0.5, rely=0.65, anchor=CENTER)

    li.remove(x)

    timer = Label(hard_frame, text="15", font=("Poppins", 12, "bold"), fg="red", bg="white")
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)

    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        #count=count+1
        if (var.get() in answer):
            score+=1
        display()
    
   # def lastPage():
    #    h.destroy()
     #   showMark()
    
    submit = Button(hard_frame,command=calc, text="Submit", fg="white", bg="#007BFF", font=("Poppins", 10, "bold"))
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_frame,command=display, text="Next", fg="white", bg="#28A745", font=("Poppins", 10, "bold"))
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    #pre=Button(hard_frame,command=display, text="Previous", fg="white", bg="black")
    #pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
   # end=Button(hard_frame,command=showMark(m), text="End", fg="white", bg="black")
    # end.place(relx=0.8, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    sh = Tk()
    sh.title('Your Marks')
    
    st = "Your score is "+str(mark)+"/5"
    mlabel = Label(sh,text=st,fg="black", bg="white")
    mlabel.pack()
    
    def callsignUpPage():
        sh.destroy()
        start()
    
    def myeasy():
        sh.destroy()
        easy()
    
    b24=Button(text="Re-attempt", command=myeasy, bg="black", fg="white")
    b24.pack()
    
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    import numpy as np

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = 'Marks Obtained','Total Marks'
    sizes = [int(mark),5-int(mark)]
    explode = (0.1,0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=0)
    

    canvas = FigureCanvasTkAgg(fig, master=sh)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    b23=Button(text="Sign Out",command=callsignUpPage,fg="white", bg="black")
    b23.pack()
    
    sh.mainloop()

def start():
    global root 
    root = Tk()
    root.title('Welcome To Quiz App')
    canvas = Canvas(root,width = 720,height = 440, bg = 'yellow')
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="output-onlinepngtools.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage,bg="red",fg="yellow") 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if __name__=='__main__':
    start()