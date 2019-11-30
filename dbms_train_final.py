from tkinter import * # importing the tkinter
import pymysql        # importing pymysql
import plotly.graph_objects as go    # importing plotly
from array import *         # importing array
import time                   # importing time
class train:                  # creating train class
    def __init__(self,root):
        self.frame1=Frame(root,width=3000,height=3000)          # creating the frame
        self.frame1.propagate(0)
        self.frame1.pack()
        self.T1 = Text(self.frame1, width=1000, height=1000)
        self.image1=PhotoImage(file="E:\mohan\Train\\train1.png")
        self.T1.image_create(END,image=self.image1)
        self.T1.pack()
        self.T2=Text(width=500,height=2,font=('edwardian script itc',40,'bold'),fg='black',bg='#706a5b')
        self.T2.insert(END,'                                            Welcome To  \n                                  Railway Tourism Corporation')
        self.T2.place(x=0,y=0)
        self.b1=Button(self.frame1,text="continue",bg='black',fg='white',width=15,height=2,command=self.first_page)                 # calling  first_page
        self.b1.place(x=1050,y=650)
        self.exit1=Button(self.frame1,text="EXIT",bg="black",fg='white',width=15,height=2,command=exit)
        self.exit1.place(x=50,y=650)
    def first_page(self):
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=1000)
        self.frame1.pack()
        self.T3=Text(self.frame1,width=1000,height=1000)
        self.image2=PhotoImage(file="E:\mohan\\train\\second1.png")
        self.T3.image_create(END,image=self.image2)
        self.T3.pack()
        self.T4=Text(self.frame1,width=100,height=1,bg='white',fg='black',font=('viner hand itc',30,'bold'))
        self.T4.insert(END,'    Select         What    You   Are ?')
        self.T4.place(x=0,y=0)
        self.b2=Button(self.frame1,width=13,height=1,text='Admine......',fg='black',bg='#b8b8b8' ,font=('algerian',20,'bold'),command=self.admin)
        self.b2.place(x=400,y=610)
        self.b3 = Button(self.frame1, width=13, height=1, text='passenger.....', fg='black', bg='#b8b8b8',
                         font=('algerian', 20, 'bold'),command=self.passenger)
        self.b3.place(x=400, y=460)
        self.b4 = Button(self.frame1, width=10, height=1, text='<< Exit', fg='white', bg='black',
                         font=('algerian', 10, 'bold'),command='exit')
        self.b4.place(x=50, y=660)
    def passenger(self):
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#d2b65d')
        self.frame1.pack()
        self.frame1.propagate(0)
        lb=Label(self.frame1,text='Sir if you are old user please login ==>>',bg='#d2b65d',fg='black',font=('French Script MT',40,'bold')).place(x=30,y=30)
        self.b=Button(self.frame1,text='LOGIN',fg='white',bg='black',font=('Arial black',15,'bold'),command=self.pass_login).place(x=800,y=30)
        lb1=Label(self.frame1,text='Sir if you are new user please sign in ==>>',bg='#d2b65d',fg='black',font=('French Script MT',40,'bold')).place(x=30,y=300)
        self.b1 = Button(self.frame1, text='SIGN IN', fg='white', bg='black', font=('Arial black', 15, 'bold'),command=self.pass_sign_in).place(x=800, y=300)
        self.back = Button(self.frame1, width=10, height=1, bg='black', fg='white', text='<< back',font=('arial black', 10, 'bold'), command=self.first_page).place(x=50, y=650)

    def pass_login(self):
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#b5ab00')
        self.frame1.propagate(0)
        self.frame1.pack()
        lb=Label(self.frame1,text='Please Enter the below details  to login ::',bg='#b5ab00',fg='black',font=('arial black',40,'bold')).place(x=30,y=30)
        lb1=Label(self.frame1,text='Enter the your ID -->',bg='#b5ab00',fg='black',font=('arial black',30,'bold')).place(x=40,y=150)
        self.e1=Entry(self.frame1,fg='black',bg='white',font=('french script mt',15,'bold'))
        self.e1.place(x=600,y=163)
        lb2=Label(self.frame1,text='Enter the your password -->',bg='#b5ab00',fg='black',font=('arial black',30)).place(x=40,y=300)
        lb3=Label(self.frame1,text='please press enter ___',fg='black',bg='#b5ab00',font=('blackadder itc',30,'bold')).place(x=100,y=400)
        self.b=Button(self.frame1,width=20,height=1,text='forgot password__?',fg='white',bg='#b5ab00',font=('bauhaus 93',10,'bold'),command=self.pass_forgot).place(x=700,y=350)
        self.back=Button(self.frame1,width=10,height=1,bg='black',fg='white',text='<< back',font=('arial black',10,'bold'),command=self.passenger).place(x=50,y=650)
        self.e2=Entry(self.frame1, fg='black', bg='white', font=('french script mt', 15, 'bold'))
        self.e2.place(x=700, y=313)
        self.e2.bind('<Return>', self.pass_login2)
    def pass_login2(self,event):
        pass_id =int(self.e1.get())
        pass_password=int(self.e2.get())
        connect = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = connect.cursor()
        str = "select * from passenger where pass_id & pass_pass='%d'&'%d'"
        args = (pass_id, pass_password)
        cursor.execute(str % args)
        row = cursor.fetchone()
        if row is not None:
            self.pass_action(pass_id)
        else:
            Label(text='Admin ID and admin Password is not matching,\n if you want you can retry -->>',bg='#b5ab00',font=('algerian',17,'bold')).place(x=100,y=500)
            self.b7 = Button(self.frame1, width=8, text='Retry', font=('algerian', 14, 'bold'), bg='black',fg='white', command=self.pass_login)
            self.b7.place(x=800, y=500)
    def pass_sign_in(self):
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=2000,bg='#b5ab00')
        self.frame1.propagate(0)
        self.frame1.pack()
        lb=Label(self.frame1,text='Enter the below details to get the account ------',bg='#b5ab00',font=('monotype corsival',30,'bold')).place(x=30,y=30)
        lb1=Label(self.frame1,text='Enter the ID you like -->',font=('calibri',20,'bold'),bg='#b5ab00',fg='black').place(x=30,y=100)
        lb2 = Label(self.frame1, text='Enter your Name -->', font=('calibri', 20, 'bold'), bg='#b5ab00',fg='black').place(x=30, y=150)
        lb3 = Label(self.frame1, text='Enter your phone number -->', font=('calibri', 20, 'bold'), bg='#b5ab00',fg='black').place(x=30, y=200)
        lb4 = Label(self.frame1, text='Enter your email-->', font=('calibri', 20, 'bold'), bg='#b5ab00',fg='black').place(x=30, y=250)
        lb5 = Label(self.frame1, text='Enter your user name -->', font=('calibri', 20, 'bold'), bg='#b5ab00',fg='black').place(x=30, y=300)
        lb6 = Label(self.frame1, text='Enter your account password -->', font=('calibri', 20, 'bold'), bg='#b5ab00',fg='black').place(x=30, y=350)
        lb6 = Label(self.frame1, text='Enter your location -->', font=('calibri', 20, 'bold'), bg='#b5ab00',fg='black').place(x=30, y=400)
        self.e1=Entry(self.frame1,width=40,font=('calibri',11))
        self.e1.place(x=550,y=110)
        self.e2 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e2.place(x=550, y=160)
        self.e3 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e3.place(x=550, y=210)
        self.e4 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e4.place(x=550, y=260)
        self.e5 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e5.place(x=550, y=310)
        self.e6 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e6.place(x=550, y=360)
        lbe=Label(self.frame1,text='please press enter __',fg='black',bg='#b5ab00',font=('blackadder itc',20,'bold')).place(x=300,y=450)
        self.back = Button(self.frame1, width=10, height=1, bg='black', fg='white', text='<< back',font=('arial black', 10, 'bold'), command=self.passenger).place(x=50, y=650)
        self.e7 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e7.place(x=550, y=410)
        self.e7.bind('<Return>',self.pass_insert)
    def pass_insert(self,event):
        e1=int(self.e1.get())
        e2=self.e2.get()
        e3=self.e3.get()
        e4=self.e4.get()
        e5=self.e5.get()
        e6=self.e6.get()
        e7=self.e7.get()
        connect = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = connect.cursor()
        str = "insert into passenger(pass_id,pass_name,pass_mob,pass_email,pass_uname,pass_pass,pass_adds) values('%d','%s','%s','%s','%s','%s','%s')"
        args = (e1,e2,e3,e4,e5,e6,e7)
        cursor.execute(str % args)
        connect.commit()
        cursor.close()
        connect.close()
        lb=Label(self.frame1,text='Thankyou for creating the account',font=('arial black',10,'bold'),bg='#b5ab00',fg='black',height=1).place(x=200,y=700)
        self.b=Button(self.frame1,width=10,height=1,text='LOGIN',font=('arial black',10,'bold'),bg='#b5ab00',fg='black',command=self.pass_login).place(x=600,y=700)

    def pass_forgot(self):
       self.frame1.destroy()                                                                                                                                                     
       self.frame1=Frame(root,width=3000,height=3000,bg='#b5ab00')                                                                                                               
       self.frame1.propagate(0)                                                                                                                                                 
       self.frame1.pack()                                                                                                                                                       
       lb=Label(self.frame1,text='Enter the bellow details to login In::',bg='#b5ab00',fg='black',font=('arial black',40,'bold')).place(x=30,y=30)
       lb1=Label(self.frame1,text='Enter the your ID -->',bg='#b5ab00',fg='black',font=('arial black',30,'bold')).place(x=40,y=150)                                             
       self.e1=Entry(self.frame1,fg='black',bg='white',font=('french script mt',15,'bold'))                                                                                     
       self.e1.place(x=600,y=163)                                                                                                                                               
       lb2=Label(self.frame1,text='Enter the your mobil number-->',bg='#b5ab00',fg='black',font=('arial black',30)).place(x=40,y=300)
       lb3=Label(self.frame1,text='please press enter ___',fg='black',bg='#b5ab00',font=('blackadder itc',30,'bold')).place(x=100,y=400)
       self.back=Button(self.frame1,width=10,height=1,bg='black',fg='white',text='<< back',font=('arial black',10,'bold'),command=self.passenger).place(x=50,y=650)             
       self.e2=Entry(self.frame1, fg='black', bg='white', font=('french script mt', 15, 'bold'))                                                                                
       self.e2.place(x=750, y=313)
       self.e2.bind('<Return>', self.pass_forgot1)
    def pass_forgot1(self,event):
         pass_id =int(self.e1.get())
         pass_mob=int(self.e2.get())
         connect = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')                                                             
         cursor = connect.cursor()                                                                                                                                        
         str = "select * from passenger where pass_id & pass_mob='%d'&'%d'"
         args = (pass_id, pass_mob)
         cursor.execute(str % args)                                                                                                                                       
         row = cursor.fetchone()                                                                                                                                          
         if row is not None:
             self.pass_action(pass_id)
         else:                                                                                                                                                            
             Label(text='passenger ID and passenger email is not matching,\n if you want you can retry -->>',bg='#b5ab00',font=('algerian',17,'bold')).place(x=100,y=500)
             self.b7 = Button(self.frame1, width=8, text='Retry', font=('algerian', 14, 'bold'), bg='black',fg='white', command=self.pass_forgot)
             self.b7.place(x=800, y=500)
    def pass_action(self,p_id):
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#b5ab00')
        self.frame1.propagate(0)
        self.frame1.pack()
        self.pa_id=p_id
        Label(text='wellcome you sir, choose what sevices you want ',font=('algeria',30,'bold'),bg='#b5ab00',fg='black').place(x=50,y=10)
        Label(text='1 -> Get Train detail \n\n2 -> Train Booking \n\n 3 -> Get the Ticket \n\n   4 -> Booking status\n\n       5 -> Delete the Booking\n\n             6 -> Delete the Account',font=('Segoe UI Semibold',20,'bold'),
              bg='#b5ab00',fg='black').place(x=300,y=100)
        Label(text='Enter your choose',font=('Segoe UI Semibold',20,'bold'),bg='#b5ab00',fg='black').place(x=300,y=600)
        Label(text='please press enter ___',bg='#b5ab00',fg='black',font=('Segoe UI Semibold',15,'bold'),width=30).place(x=300,y=650)
        self.b=Button(text='<<--Back',font=('Segoe UI Semibold',10,'bold'),bg='black',fg='white',command=self.pass_login).place(x=100,y=700)
        self.entry1=Entry(self.frame1,width=10,font=('Segoe UI Semibold',10,'bold'))
        self.entry1.place(x=600,y=600)
        self.entry1.bind('<Return>',self.service)
    def service(self,event):
        choise=int(self.entry1.get())
        pas_id=self.pa_id
        if choise==1:
            self.train_detail()
        elif choise==2:
            self.booking(pas_id)
        elif choise==3:
            self.ticket(pas_id)
        elif choise==4:
            self.booking_status(pas_id)
        elif choise==5:
            self.delete_book(pas_id)
        elif choise==6:
            self.delete_pass(pas_id)
        else:
            Label(text='In put is Wronge',font=('Segoe UI Semibold',10,'bold'),bg='#b5ab00',fg='red').place(x=600,y=600)
            self.b1=Button(text='Rentry',font=('Segoe UI Semibold',10,'bold'),bg='black',fg='white',command=self.pass_action).place(x=700,y=700)
    def train_detail(self):
        conn=pymysql.connect(host='localhost',user='root',
                             password='7338272260ksv',database='world')
        cursor=conn.cursor()
        cursor.execute("select * from train")
        res=cursor.fetchall()
        res1=[]
        for row in res:
             res1.append(row)
        fig=go.Figure(data=[go.Table(
                            header=dict(values=[['Train_id','Train_name','Train_type','source','dep_time','destination','rea_time','Amount'],
                                                res1[0],res1[1],res1[2],res1[3],res1[4],res1[5],res1[6],res1[7],res1[8],res1[9],res1[10],res1[11],res1[12],res1[13],res1[14]]))])
        print(fig.show())
        cursor.close()
        conn.close()
    def booking(self,pas1_id):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        self.cus_id=pas1_id
        Label(text='wellcome To booking site', font=('Matura MT Script Capitals', 40, 'bold'), bg='#ccb800',
              width=30).place(x=20, y=20)
        Label(text='Enter the Train ID -->', font=('monotype Corsiva', 25, 'bold'), width=20, bg='#ccb800').place(x=100,
                                                                                                                  y=200)
        Label(text='Enter the class -->', font=('Monotype Corsiva', 25, 'bold'), bg='#ccb800', width=20).place(x=100,y=300)
        Label(text='----> Class Type\n\n     1-> sleeping class\n\n2->First class\n\n3->second class',font=('arial',20,'bold'),bg='#ccb800',fg='blue').place(x=900,y=305)
        self.entry1 = Entry(self.frame1, width=20, font=('Segoe UI Semibold', 20, 'bold'))
        self.entry1.place(x=500, y=203)
        Label(text='please press enter __',font=('arial',15,'bold'),fg='black',bg='#ccb800').place(x=300,y=400)
        self.b=Button(self.frame1,text='<--back',font=('arial',10,'bold'),bg='black',fg='white',command=self.pass_action_back)
        self.b.place(x=200,y=500)
        self.entry2=Entry(self.frame1,width=20,font=('seqoe ui semibold',20,'bold'))
        self.entry2.place(x=500,y=303)
        self.entry2.bind('<Return>',self.seat)
    def pass_action_back(self):
        self.pass_action(self.cus_id)
    def seat(self,event):
        t_id=int(self.entry1.get())
        class_no=int(self.entry2.get())
        cus1_id=self.cus_id
        if class_no==1:
            class_name='sleeping'
        elif class_no==2:
            class_name='first'
        elif class_no==3:
            class_name='second'
        self.seat1(t_id,class_name,cus1_id)
    def seat1(self,t_id,class_name,cus1_id):
        self.frame1.destroy()
        self.f = Frame(root, width=3000, height=3000,bg='#ccb800')
        self.f.propagate(0)
        self.f.pack()
        self.t_id=t_id
        self.class_name=class_name
        self.cust_id=cus1_id
        self.tr_id=t_id
        self.cl_na=class_name
        self.cu_id=cus1_id
        arr = array('i', [])
        conn = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = conn.cursor()
        str="select seat_no from booking where train_id='%d' and coach_id='%s'"
        args=(t_id,class_name)
        cursor.execute(str%args)
        rows = cursor.fetchall()
        ''' color red for resurved and color green for not resurved'''
        for row in rows:
            for i in row:
                arr.append(i)
        self.red=Button(self.f,width=5,height=2,bg='red').place(x=1000,y=300)
        self.green = Button(self.f, width=5, height=2, bg='green').place(x=1000, y=500)
        self.exit3=Button(self.f,width=10,font=('arial',10,'bold'),bg='black',fg='white',height=2,text='Exit',command=exit)
        self.exit3.place(x=1050,y=650)
        Label(text='---> Reserved seats',font=('arial',20,'bold'),bg='#ccb800',fg='black').place(x=1050,y=300)
        Label(text='---> Not Reserved seat', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=1050, y=500)
        self.b1=Button(self.f,width=10,height=5,text='1',command=self.payment1)
        self.b1.place(x=50,y=50)
        if int(self.b1['text']) in arr:
            self.b1['bg'] = 'red'
        else:
            self.b1['bg'] = 'green'
        self.b2 = Button(self.f, width=10, height=5, text='2',command=self.payment2)
        self.b2.place(x=200, y=50)
        if int(self.b2['text']) in arr:
            self.b2['bg'] = 'red'
        else:
            self.b2['bg'] = 'green'
        self.b3 = Button(self.f, width=10, height=5, text='3',command=self.payment3)
        self.b3.place(x=350, y=50)
        if int(self.b3['text']) in arr:
            self.b3['bg'] = 'red'
        else:
            self.b3['bg'] = 'green'
        self.b4 = Button(self.f, width=10, height=5, text='4',command=self.payment4)
        self.b4.place(x=500, y=50)
        if int(self.b4['text']) in arr:
            self.b4['bg'] = 'red'
        else:
            self.b4['bg'] = 'green'
        self.b5 = Button(self.f, width=10, height=5, text='5',command=self.payment5)
        self.b5.place(x=650, y=50)
        if int(self.b5['text']) in arr:
            self.b5['bg'] = 'red'
        else:
            self.b5['bg'] = 'green'
        self.b6 = Button(self.f, width=10, height=5, text='6',command=self.payment6)
        self.b6.place(x=50, y=200)
        if int(self.b6['text']) in arr:
            self.b6['bg'] = 'red'
        else:
            self.b6['bg'] = 'green'
        self.b7 = Button(self.f, width=10, height=5, text='7',command=self.payment7)
        self.b7.place(x=200, y=200)
        if int(self.b7['text']) in arr:
            self.b7['bg'] = 'red'
        else:
            self.b7['bg'] = 'green'
        self.b8 = Button(self.f, width=10, height=5, text='8',command=self.payment8)
        self.b8.place(x=350, y=200)
        if int(self.b8['text']) in arr:
            self.b8['bg'] = 'red'
        else:
            self.b8['bg'] = 'green'
        self.b9 = Button(self.f, width=10, height=5, text='9',command=self.payment9)
        self.b9.place(x=500, y=200)
        if int(self.b9['text']) in arr:
            self.b9['bg'] = 'red'
        else:
            self.b9['bg'] = 'green'
        self.b10 = Button(self.f, width=10, height=5, text='10',command=self.payment10)
        self.b10.place(x=650, y=200)
        if int(self.b10['text']) in arr:
            self.b10['bg'] = 'red'
        else:
            self.b10['bg'] = 'green'
        self.b11 = Button(self.f, width=10, height=5, text='11',command=self.payment11)
        self.b11.place(x=50, y=350)
        if int(self.b11['text']) in arr:
            self.b11['bg'] = 'red'
        else:
            self.b11['bg'] = 'green'
        self.b12 = Button(self.f, width=10, height=5, text='12',command=self.payment12)
        self.b12.place(x=200, y=350)
        if int(self.b12['text']) in arr:
            self.b12['bg'] = 'red'
        else:
            self.b12['bg'] = 'green'
        self.b13 = Button(self.f, width=10, height=5, text='13',command=self.payment13)
        self.b13.place(x=350, y=350)
        if int(self.b13['text']) in arr:
            self.b13['bg'] = 'red'
        else:
            self.b13['bg'] = 'green'
        self.b14 = Button(self.f, width=10, height=5, text='14',command=self.payment14)
        self.b14.place(x=500, y=350)
        if int(self.b14['text']) in arr:
            self.b14['bg'] = 'red'
        else:
            self.b14['bg'] = 'green'
        self.b15 = Button(self.f, width=10, height=5, text='15',command=self.payment15)
        self.b15.place(x=650, y=350)
        if int(self.b15['text']) in arr:
            self.b15['bg'] = 'red'
        else:
            self.b15['bg'] = 'green'
        self.b16 = Button(self.f, width=10, height=5, text='16',command=self.payment16)
        self.b16.place(x=50, y=500)
        if int(self.b16['text']) in arr:
            self.b16['bg'] = 'red'
        else:
            self.b16['bg'] = 'green'
        self.b17 = Button(self.f, width=10, height=5, text='17',command=self.payment17)
        self.b17.place(x=200, y=500)
        if int(self.b17['text']) in arr:
            self.b17['bg'] = 'red'
        else:
            self.b17['bg'] = 'green'
        self.b18 = Button(self.f, width=10, height=5, text='18',command=self.payment18)
        self.b18.place(x=350, y=500)
        if int(self.b18['text']) in arr:
            self.b18['bg'] = 'red'
        else:
            self.b18['bg'] = 'green'
        self.b19 = Button(self.f, width=10, height=5, text='19',command=self.payment19)
        self.b19.place(x=500, y=500)
        if int(self.b19['text']) in arr:
            self.b19['bg'] = 'red'
        else:
            self.b19['bg'] = 'green'
        self.b20 = Button(self.f, width=10, height=5, text='20',command=self.payment20)
        self.b20.place(x=650, y=500)
        if int(self.b20['text']) in arr:
            self.b20['bg'] = 'red'
        else:
            self.b20['bg'] = 'green'
        self.b21 = Button(self.f, width=10, height=5, text='21',command=self.payment21)
        self.b21.place(x=50, y=650)
        if int(self.b21['text']) in arr:
            self.b21['bg'] = 'red'
        else:
            self.b21['bg'] = 'green'
        self.b22 = Button(self.f, width=10, height=5, text='22',command=self.payment22)
        self.b22.place(x=200, y=650)
        if int(self.b22['text']) in arr:
            self.b22['bg'] = 'red'
        else:
            self.b22['bg'] = 'green'
        self.b23 = Button(self.f, width=10, height=5, text='23',command=self.payment23)
        self.b23.place(x=350, y=650)
        if int(self.b23['text']) in arr:
            self.b23['bg'] = 'red'
        else:
            self.b23['bg'] = 'green'
        self.b24 = Button(self.f, width=10, height=5, text='24',command=self.payment24)
        self.b24.place(x=500, y=650)
        if int(self.b24['text']) in arr:
            self.b24['bg'] = 'red'
        else:
            self.b24['bg'] = 'green'
        self.b25 = Button(self.f, width=10, height=5, text='25',command=self.payment25)
        self.b25.place(x=650, y=650)
        if int(self.b25['text']) in arr:
            self.b25['bg'] = 'red'
        else:
            self.b25['bg'] = 'green'
        cursor.close()
        conn.close()
    def payment1(self):
        if self.b1['bg']=='red':
            self.f.destroy()
            self.frame1=Frame(root,width=3000,height=3000,bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ',font=('arial',40,'bold'),bg='#ccb800',fg='red').place(x=300,y=300)
            self.b=Button(self.frame1,text='retry',width=5,height=5,bg='blue',fg='black',font=('arial',10,'bold'),command=self.pass_login)
            self.b.place(x=500,y=600)
        elif self.b1['bg']=='green':
            seat_no=self.b1['text']
            r=self.t_id
            p=self.cust_id
            c_n=self.class_name
            conn=pymysql.connect(host='localhost',user='root',database='world',password='7338272260ksv')
            cursor=conn.cursor()
            str=("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args=(r)
            cursor.execute(str%args)
            res=cursor.fetchall()
            conn1=pymysql.connect(host='localhost',user='root',database='world',password='7338272260ksv')
            cursor1=conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1=cursor1.fetchone()
            res2=res1[0]+1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row=[]
            for i in res[0]:
                row.append(i)
            self.pay(res2,r,row[0],p,c_n,seat_no,h4,row[1],row[2],row[3])


    def payment2(self):
        if self.b2['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b2['bg']=='green':
            seat_no = self.b2['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment3(self):
        if self.b3['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b3['bg']=='green':
            seat_no = self.b3['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment4(self):
        if self.b4['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b4['bg']=='green':
            seat_no = self.b4['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment5(self):
        if self.b5['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b5['bg']=='green':
            seat_no = self.b5['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment6(self):
        if self.b6['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b6['bg']=='green':
            seat_no = self.b6['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment7(self):
        if self.b7['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b7['bg']=='green':
            seat_no = self.b7['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment8(self):
        if self.b8['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b8['bg']=='green':
            seat_no = self.b8['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment9(self):
        if self.b9['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b9['bg']=='green':
            seat_no = self.b9['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment10(self):
        if self.b10['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b10['bg']=='green':
            seat_no = self.b10['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment11(self):
        if self.b11['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b11['bg']=='green':
            seat_no = self.b11['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment12(self):
        if self.b12['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b12['bg']=='green':
            seat_no = self.b12['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment13(self):
        if self.b13['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b13['bg']=='green':
            seat_no = self.b13['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment14(self):
        if self.b14['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b14['bg']=='green':
            seat_no = self.b14['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment15(self):
        if self.b15['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b15['bg']=='green':
            seat_no = self.b15['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment16(self):
        if self.b16['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b16['bg']=='green':
            seat_no = self.b16['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment17(self):
        if self.b17['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b17['bg']=='green':
            seat_no = self.b17['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment18(self):
        if self.b18['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b18['bg']=='green':
            seat_no = self.b18['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment19(self):
        if self.b19['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b19['bg']=='green':
            seat_no = self.b19['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment20(self):
        if self.b20['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b20['bg']=='green':
            seat_no = self.b20['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment21(self):
        if self.b21['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b21['bg']=='green':
            seat_no = self.b21['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment22(self):
        if self.b22['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b22['bg']=='green':
            seat_no = self.b22['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment23(self):
        if self.b23['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b23['bg']=='green':
            seat_no = self.b23['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment24(self):
        if self.b24['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b24['bg']=='green':
            seat_no = self.b24['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def payment25(self):
        if self.b25['bg']=='red':
            self.f.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='This seat is already reserved ', font=('arial', 40, 'bold'), bg='#ccb800', fg='red').place(
                x=300, y=300)
            self.b = Button(self.frame1, text='retry', width=5, height=5, bg='blue', fg='black',
                            font=('arial', 10, 'bold'), command=self.pass_login)
            self.b.place(x=500, y=600)
        elif self.b25['bg']=='green':
            seat_no = self.b25['text']
            r = self.t_id
            p = self.cust_id
            c_n = self.class_name
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor = conn.cursor()
            str = ("select train_name,sour_adds,desc_adds,amount from train where train_id='%d'")
            args = (r)
            cursor.execute(str % args)
            res = cursor.fetchall()
            conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(book_id) from booking")
            res1 = cursor1.fetchone()
            res2 = res1[0] + 1
            epoch = time.time()
            t = time.localtime(epoch)
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            h1 = h * 100
            h2 = h1 + m
            h3 = h2 * 100
            h4 = h3 + s
            row = []
            for i in res[0]:
                row.append(i)
            self.pay(res2, r, row[0], p, c_n, seat_no, h4, row[1], row[2], row[3])

    def pay(self,b_id,t_id,t_n,p_id,c_id,seat_no,b_t,b_s,b_d,amo):
        self.b_id=b_id
        self.t_id=t_id
        self.t_n=t_n
        self.p_id=p_id
        self.c_id=c_id
        self.seat_no=seat_no
        self.b_t=b_t
        self.b_s=b_s
        self.b_d=b_d
        self.amo=amo
        self.f.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        Label(text='wellcome to payment site',font=('arial',50,'bold'),bg='#ccb800',fg='black').place(x=200,y=10)
        Label(text='your booking seat cost --- RS',font=('arial',30,'bold'),bg='#ccb800',fg='black').place(x=300,y=100)
        Label(text=amo,font=('arial',30,'bold'),bg='#ccb800',fg='black').place(x=850,y=100)
        Label(text='Pay the amount',font=('arial',20,'bold'),bg='#ccb800',fg='black').place(x=200,y=300)
        self.e=Entry(self.frame1,font=('arial',20,'bold'),bg='white',fg='red')
        self.e.place(x=600,y=300)
        Label(text='Enter the card number',font=('arial',20,'bold'),bg='#ccb800',fg='black').place(x=200,y=400)
        self.e1=Entry(self.frame1,font=('arial',20,'bold'),bg='white',fg='red')
        self.e1.place(x=600,y=400)
        Label(text='Enter the card cvv number',font=('arial',20,'bold'),bg='#ccb800',fg='black').place(x=200,y=500)
        Label(text='please press enter ____', font=('arial', 10, 'bold'), bg='#ccb800', fg='blue').place(x=300, y=550)
        self.e2=Entry(self.frame1,font=('arial',10,'bold'),bg='white',fg='red')
        self.e2.place(x=600,y=500)
        self.e2.bind('<Return>',self.pay_final)
    def pay_final(self,event):
        entry1=int(self.e.get())
        amount=self.amo
        if entry1==amount:
            Label(text='conform your payment',font=('arial',30,'bold'),bg='#ccb800',fg='black').place(x=100,y=650)
            self.b=Button(self.frame1,text='pay',bg='blue',fg='black',width=8,height=2,command=self.book)
            self.b.place(x=800,y=650)
        else:
            Label(text='Amount is not equal to above mentioned', font=('arial', 30, 'bold'), bg='#ccb800', fg='black').place(x=10, y=650)
            self.b=Button(self.frame1, text='retry', bg='blue', fg='black', width=8, height=2, command=self.pass_login)
            self.b.place(x=800, y=650)
    def book(self):
        book_id = int(self.b_id)
        train_id = int(self.t_id)
        train_name = str(self.t_n)
        pass_id = int(self.p_id)
        c_id = str(self.c_id)
        s_n = int(self.seat_no)
        b_t = int(self.b_t)
        b_s = str(self.b_s)
        b_d = str(self.b_d)

        self.book_id = int(self.b_id)
        self.train_id = int(self.t_id)
        self.train_name = str(self.t_n)
        self.pass_id = int(self.p_id)
        self.c_id = str(self.c_id)
        self.s_n = int(self.seat_no)
        self.b_t = int(self.b_t)
        self.b_s = str(self.b_s)
        self.b_d = str(self.b_d)
        amount=int(self.amo)
        conn2 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cursor2 = conn2.cursor()
        str1="insert into booking(book_id,train_id,train_name,pass_id,coach_id,seat_no,book_time,book_sour,book_desc) values('%d','%d','%s','%d','%s','%d','%d','%s','%s')"
        args1=(book_id,train_id,train_name,pass_id,c_id,s_n,b_t,b_s,b_d)
        cursor2.execute(str1%args1)
        conn2.commit()
        cursor2.close()
        conn2.close()
        conna = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cura = conna.cursor()
        str1 = "update seat_rem set rem_seat='%d' where train_id ='%d'and coach_id='%s'"
        args = (6, train_id, c_id)
        cura.execute(str1 % args)
        conna.commit()
        cura.close()
        conna.close()
        Label(text='------->', font=('arial', 10, 'bold'), bg='#ccb800', fg='green').place(x=900, y=650)
        self.b1 = Button(self.frame1, text='Book', bg='blue', fg='black', width=8, height=2, command=self.book1)
        self.b1.place(x=1000, y=650)

    def book1(self):
        conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cursor1 = conn1.cursor()
        cursor1.execute("select max(pay_id) from payment")
        resp1 = cursor1.fetchone()
        resp2 = resp1[0] + 1
        self.frame1.destroy()
        book_id = int(self.b_id)
        train_id = int(self.t_id)
        pass_id = int(self.p_id)
        amount = int(self.amo)
        epoch = time.time()
        t = time.localtime(epoch)
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        h1 = h * 100
        h2 = h1 + m
        h3 = h2 * 100
        h4 = h3 + s
        connect1=pymysql.connect(host='localhost',user='root',database='world',password='7338272260ksv')
        cursor1=connect1.cursor()
        strstr="insert into payment(pay_id,train_id,book_id,pass_id,pay_time,pay_amount) values('%d','%d','%d','%d','%d','%d')"
        argsargs=(resp2,train_id,book_id,pass_id,h4,amount)
        cursor1.execute(strstr%argsargs)
        connect1.commit()
        cursor1.close()
        connect1.close()
        self.lastbook()
    def lastbook(self):
        self.frame1=Frame(root,height=3000,width=3000,bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        self.back=self.pass_id
        connb = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        curb = connb.cursor()
        strb = "select rem_seat from seat_rem where train_id ='%d' and coach_id='%s'"
        argsb = (self.train_id,self.c_id)
        curb.execute(strb % argsb)
        res = curb.fetchone()
        connb.commit()
        curb.close()
        connb.close()
        row = []
        for i in res:
            row.append(i)
        Label(text='Thanks for Booking the seat',font=('Script MT Bold',40,'bold'),bg='#ccb800',fg='black').place(x=400,y=100)
        Label(text='Booking ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=200)
        Label(text=self.book_id, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=200)
        Label(text='Train ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=250)
        Label(text=self.train_id, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=250)
        Label(text='Train name -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=300)
        Label(text=self.train_name, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=300)
        Label(text='passenger ID-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=350)
        Label(text=self.pass_id, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=350)
        Label(text='class Type -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=400)
        Label(text=self.c_id, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=400)
        Label(text='seat number -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=450)
        Label(text=self.s_n, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=450)
        Label(text='source -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=500)
        Label(text=self.b_s, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=500)
        Label(text='Destination -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=550)
        Label(text=self.b_d, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=550)
        Label(text='Remaining seats are:: ', font=('arial', 20, 'bold'), bg='#ccb800', fg='blue').place(x=1000, y=300)
        Label(text=row[0], font=('arial', 20, 'bold'), bg='#ccb800', fg='white').place(x=1100, y=400)
        self.exit1 = Button(self.frame1, text="EXIT", bg="black", fg='white', width=15, height=5, command=exit)
        self.exit1.place(x=50, y=650)
        self.exit2 = Button(self.frame1, text="new Booking", bg="black", fg='white', width=15, height=5, command=self.book_book_back)
        self.exit2.place(x=500, y=650)
        self.exit3 = Button(self.frame1, text="services", bg="black", fg='white', width=15, height=5,
                            command=self.book_sevices_back)
        self.exit3.place(x=700, y=650)
    def book_sevices_back(self):
        self.pass_action(self.back)
    def book_book_back(self):
        self.booking(self.back)



    def ticket(self,pas_id):
        self.pas_id=pas_id
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        self.cus_id=pas_id
        Label(text='To Get the Ticket\n                                          Fill the Below Detail',font=('Castellar',30,'bold'),bg='#ccb800',fg='black').place(x=5,y=10)
        Label(text='Enter the Train Id -->',font=('arial',20,'bold'),bg='#ccb800',fg='black').place(x=200,y=200)
        Label(text='please press enter___',font=('arial',10,'bold'),bg='#ccb800',fg='black').place(x=250,y=230)
        self.b = Button(self.frame1, text='<--back', font=('arial', 10, 'bold'), bg='black', fg='white',
                        command=self.pass_action_back)
        self.b.place(x=200, y=500)
        self.e=Entry(self.frame1,font=('arial',10,'bold'),bg='white',fg='black')
        self.e.place(x=500,y=200)
        self.e.bind('<Return>',self.ticket1)

    def ticket1(self,event):
        t_id=int(self.e.get())
        conn1 = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cursor1 = conn1.cursor()
        cursor1.execute("select max(ticket_id) from ticket")
        resp1 = cursor1.fetchone()
        resp2 = resp1[0] + 1
        epoch = time.time()
        t = time.localtime(epoch)
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        h1 = h * 100
        h2 = h1 + m
        h3 = h2 * 100
        h4 = h3 + s
        self.pass1_id=self.pas_id
        conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cursor = conn.cursor()
        str = ("select train_name,sour_adds,desc_adds from train where train_id='%d'")
        args = (t_id)
        cursor.execute(str % args)
        res = cursor.fetchall()
        row = []
        for i in res[0]:
            row.append(i)
        conn3=pymysql.connect(host='localhost',user='root',database='world',password='7338272260ksv')
        cur3=conn3.cursor()
        str1="insert into ticket(ticket_id,train_id,train_name,pass_id,ticket_sour,ticket_desc) values ('%d','%d','%s','%d','%s','%s')"
        args1=(resp2,t_id,row[0],self.pas_id,row[1],row[2])
        cur3.execute(str1%args1)
        conn3.commit()
        Label(text=('Thanks for Getting the Ticket\n                                     Ticket Detail are given Bellow'),font=('arial',20,'bold'),bg='#ccb800',fg='black').place(x=200,y=300)
        Label(text='Ticket ID -->',font=('arial',20,'bold'),bg='#ccb800',fg='black').place(x=300,y=400)
        Label(text=resp2, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=400)
        Label(text='Train ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=450)
        Label(text=t_id, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=450)
        Label(text='Train name -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=500)
        Label(text=row[0], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=500)
        Label(text='passenger -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=550)
        Label(text=self.pas_id, font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=550)
        Label(text='source adds -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=600)
        Label(text=row[1], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=600)
        Label(text='Destination -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=650)
        Label(text=row[2], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=650)
        self.b=Button(self.frame1,text='Exit',bg='black',fg='white',width=5,height=2,command=exit)
        self.b.place(x=800,y=700)
        self.new = Button(self.frame1, text='new ticket', bg="black",font=('arial',10,'bold'), fg='white', width=15, height=5,
                            command=self.ticket_book_back)
        self.new.place(x=100, y=670)
        self.exit3 = Button(self.frame1, text="services", bg="black", fg='white', width=15, height=5,
                            command=self.ticket_sevices_back)
        self.exit3.place(x=500, y=650)

    def ticket_sevices_back(self):
        self.pass_action(self.pass1_id)
    def ticket_book_back(self):
        self.ticket(self.pass1_id)
    def booking_status(self,pass_id):
        self.pass_id=pass_id
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        self.cus_id=pass_id
        Label(text='If you want booking Detail\n                           Fill the bellow DEtail',font=('Castellar',30,'bold'),bg='#cbb800',fg='black').place(x=10,y=10)
        Label(text='Enter the Booking ID -->',font=('castellar',20,'bold'),bg='#ccb800',fg='black').place(x=100,y=200)
        Label(text='please press enter _____ ', font=('castellar', 10, 'bold'), bg='#ccb800', fg='black').place(x=130,y=250)
        self.b = Button(self.frame1, text='<--back', font=('arial', 10, 'bold'), bg='black', fg='white',
                        command=self.pass_action_back)
        self.b.place(x=200, y=500)
        self.e = Entry(self.frame1, font=('arial', 20, 'bold'), bg='white', fg='black')
        self.e.place(x=600, y=200)
        self.e.bind('<Return>',self.book_print)
    def book_print(self,event):
        book_id=int(self.e.get())
        conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cur = conn.cursor()
        str = "select book_id from booking where pass_id='%d'"
        args = (self.pass_id)
        cur.execute(str % args)
        res = cur.fetchall()
        arr = []
        for i in res:
            for j in i:
                arr.append(j)
        if book_id in arr:
            self.frame1.destroy()
            self.frame1=Frame(root,width=3000,height=3000,bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='your booking Details are shown Bellow',font=('Script MT Bold',40,'bold'),bg='#ccb800',fg='black').place(x=400,y=30)
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cur = conn.cursor()
            str = "select * from booking where book_id='%d'"
            args = (book_id)
            cur.execute(str%args)
            res1 = cur.fetchall()
            cur.close()
            conn.close()
            arr = []
            for i in res1[0]:
                arr.append(i)
            self.pass_id=arr[3]
            Label(text='Booking ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=200)
            Label(text=arr[0], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=200)
            Label(text='Train ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=250)
            Label(text=arr[1], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=250)
            Label(text='Train name -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=300)
            Label(text=arr[2], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=300)
            Label(text='passenger ID-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=350)
            Label(text=arr[3], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=350)
            Label(text='class Type -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=400)
            Label(text=arr[4], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=400)
            Label(text='seat number -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=450)
            Label(text=arr[5], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=450)
            Label(text='source -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=500)
            Label(text=arr[7], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=500)
            Label(text='Destination -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=550)
            Label(text=arr[8], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=550)
            self.exit1 = Button(self.frame1, text="EXIT", bg="black", fg='white', width=15, height=5, command=exit)
            self.exit1.place(x=50, y=650)
            self.exit3 = Button(self.frame1, text="services", bg="black", fg='white', width=15, height=5,
                                command=self.book_status_services_back)
            self.exit3.place(x=500, y=650)

        else:
            Label(text='you Does not Have athority to Get the Details of this Booking',font=('arial',30,'bold'),bg='#ccb800',fg='black').place(x=100,y=300)
            self.b=Button(text='<--back',width=10,height=5,bg='black',fg='white',command=self.book_status_back)
            self.b.place(x=300,y=500)
            self.b = Button(text='Exit', width=10, height=5, bg='black', fg='white', command=exit)
            self.b.place(x=700, y=500)

    def book_status_services_back(self):
        self.pass_action(self.pass_id)
    def book_status_back(self):
        self.booking_status(self.pass_id)
    def delete_book(self,p_id):
        self.cuss_id = p_id
        self.frame1.destroy()
        self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        Label(text='If you want Delete booking\n                           Fill the bellow DEtail',
              font=('Castellar', 30, 'bold'), bg='#cbb800', fg='black').place(x=10, y=10)
        Label(text='Enter the Booking ID -->', font=('castellar', 20, 'bold'), bg='#ccb800', fg='black').place(x=100,
                                                                                                               y=200)
        Label(text='please press enter _____ ', font=('castellar', 10, 'bold'), bg='#ccb800', fg='black').place(x=130,
                                                                                                                y=250)
        self.b = Button(self.frame1, text='<--back', font=('arial', 10, 'bold'), bg='black', fg='white',
                        command=self.pass_action_back)
        self.b.place(x=200, y=500)
        self.e = Entry(self.frame1, font=('arial', 20, 'bold'), bg='white', fg='black')
        self.e.place(x=600, y=200)
        self.e.bind('<Return>', self.delete_book1)
    def delete_book1(self,event):
        book_id = int(self.e.get())
        conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cur = conn.cursor()
        str = "select book_id from booking where pass_id='%d'"
        args = (self.pass_id)
        cur.execute(str % args)
        res = cur.fetchall()
        arr = []
        for i in res:
            for j in i:
                arr.append(j)
        if book_id in arr:
            self.frame1.destroy()
            self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
            self.frame1.propagate(0)
            self.frame1.pack()
            Label(text='The Deleted booking Details are as Below ::', font=('Script MT Bold', 40, 'bold'), bg='#ccb800',
                  fg='black').place(x=400, y=30)
            conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
            cur = conn.cursor()
            str = "select * from booking where book_id='%d'"
            args = (book_id)
            cur.execute(str % args)
            res1 = cur.fetchall()
            cur.close()
            conn.close()
            arr = []
            for i in res1[0]:
                arr.append(i)
            Label(text='Booking ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=200)
            Label(text=arr[0], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=200)
            Label(text='Train ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=250)
            Label(text=arr[1], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=250)
            Label(text='Train name -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=300)
            Label(text=arr[2], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=300)
            Label(text='passenger ID-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=350)
            Label(text=arr[3], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=350)
            Label(text='class Type -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=400)
            Label(text=arr[4], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=400)
            Label(text='seat number -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=450)
            Label(text=arr[5], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=450)
            Label(text='source -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=500)
            Label(text=arr[7], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=500)
            Label(text='Destination -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=550)
            Label(text=arr[8], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=600, y=550)
            self.exit1 = Button(self.frame1, text="EXIT", bg="black", fg='white', width=15, height=5, command=exit)
            self.exit1.place(x=50, y=650)
            self.exit2 = Button(self.frame1, text="new Booking", bg="black", fg='white', width=15, height=5,
                                command=self.pass_login)
            self.exit2.place(x=500, y=650)
            conna=pymysql.connect(host='localhost',user='root',database='world',password='7338272260ksv')
            cura=conna.cursor()
            stra="delete from booking where book_id='%d'"
            argsa=(book_id)
            cura.execute(stra%argsa)
            conna.commit()
        else:
            Label(text='you Does not Have athority to Delete this Booking', font=('arial', 30, 'bold'),
                  bg='#ccb800', fg='black').place(x=100, y=300)
            self.b = Button(text='<--back', width=10, height=5, bg='black', fg='white', command=self.pass_login)
            self.b.place(x=300, y=500)
            self.b = Button(text='Exit', width=10, height=5, bg='black', fg='white', command=exit)
            self.b.place(x=700, y=500)
    def delete_pass(self,pass_id):
        self.cuss_id=pass_id
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        Label(text='Conform your account Deletion bY pressing Button::',font=('Script MT Bold', 40, 'bold'),bg='#ccb800',fg='red').place(x=100,y=50)
        self.b=Button(self.frame1,text='Delete',width=10,height=2,bg='black',fg='white',command=self.delete_pass1)
        self.b.place(x=100,y=150)
        self.b1 = Button(self.frame1, text='<--back', font=('arial', 10, 'bold'), bg='black', fg='white',
                        command=self.pass_action_back)
        self.b1.place(x=200, y=500)
    def delete_pass1(self):
        conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cur = conn.cursor()
        str = "select * from passenger where pass_id='%d'"
        args = (self.pass_id)
        cur.execute(str % args)
        res = cur.fetchall()
        arr = []
        for i in res[0]:
            arr.append(i)
        Label(text='passenger ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=200)
        Label(text=arr[0], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=200)
        Label(text='passenger Name-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=250)
        Label(text=arr[1], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=250)
        Label(text='passenger mobile nO -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=300)
        Label(text=arr[2], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=300)
        Label(text='passenger email-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=350)
        Label(text=arr[3], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=350)
        Label(text='passenger user name -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=400)
        Label(text=arr[4], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=400)
        Label(text='passenger password -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=450)
        Label(text=arr[5], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=450)
        Label(text='passenger address-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=500)
        Label(text=arr[6], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=500)
        self.exit1 = Button(self.frame1, text="EXIT", bg="black", fg='white', width=15, height=5, command=exit)
        self.exit1.place(x=50, y=650)
        self.exit2 = Button(self.frame1, text="new Sing-in", bg="black", fg='white', width=15, height=5,
                            command=self.pass_sign_in)
        self.exit2.place(x=500, y=650)
        conna = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cura = conna.cursor()
        stra = "delete from passenger where pass_id='%d'"
        argsa = (self.pass_id)
        cura.execute(stra%argsa)
        conna.commit()

    def admin(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=3000, height=3000)
        self.frame1.pack()
        self.frame1.propagate(0)
        Label(
            text='                                                     Wellcome  you   ....... \n                     if you want any service ,pleace login below'
            , font=('viner hand itc', 30, 'bold'), fg='black').place(x=0, y=0)
        self.b5 = Button(self.frame1, width=8, height=1, bg='black', fg='white', text='login ==>>',
                         font=('algerian', 15, 'bold'), command=self.admin_login)
        self.b5.place(x=600, y=150)
        self.b = Button(self.frame1, width=14, text='<-- Back', command=self.first_page)
        self.b.place(x=100, y=500)

    def admin_login(self):
        l1 = Label(text='Enter your Admin ID =>', font=('algerian', 15, 'bold')).place(x=200, y=300)
        self.entry1 = Entry(self.frame1, width=50)
        self.entry1.place(x=600, y=300)
        l2 = Label(text="Enter the password =>", font=('algerian', 15, 'bold')).place(x=200, y=350)
        self.entry2 = Entry(self.frame1, width=50)
        self.entry2.place(x=600, y=350)
        self.entry2.bind('<Return>', self.admin_accpre)

    def admin_accpre(self, event):
        id = int(self.entry1.get())
        password = int(self.entry2.get())
        if id == 0 or password == 0:
            Label(text='Sorry the input is invalid   \n     if you want, you can retry',
                  font=('algerian', 15, 'bold')).place(x=100, y=500)
            self.b6 = Button(self.frame1, width=8, text='Retry', font=('algerian', 14, 'bold'), bg='black', fg='white',
                             command=self.admin)
            self.b6.place(x=500, y=500)
        else:
            connect = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
            cursor = connect.cursor()
            str = "select * from admin where admin_id & admin_password='%d'&'%d'"
            args = (id, password)
            cursor.execute(str % args)
            row = cursor.fetchone()
            if row == None:
                Label(text='Admin ID and admin Password is not matching,\n if you want you can retry -->>', bg='white',
                      font=('algerian', 17, 'bold')).place(x=100, y=500)
                self.b7 = Button(self.frame1, width=8, text='Retry', font=('algerian', 14, 'bold'), bg='black',
                                 fg='white',
                                 command=self.admin)
                self.b7.place(x=800, y=500)
            else:
                self.admin_choose()

    def admin_choose(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=3000, height=3000, bg='#b5ab00')
        self.frame1.pack()
        self.frame1.propagate(0)
        Label(text='Sir please select ,what service you want', bg='#b5ab00', fg='white',
              font=('magneto', 40, 'bold')).place(x=5, y=10)
        Label(text='service provided are -->', font=('blackadder itc', 35, 'bold'), bg='#b5ab00', fg='white').place(
            x=156,
            y=100)
        Label(
            text='  1 -> Insert the New Train\n\n\n2 -> Add a passenger\n\n\n3 -> passenger Detail\n\n\n  4 -> Delete the passenger',
            bg='#b5ab00', font=('bodole mt', 16, 'bold')).place(x=600, y=150)
        Label(text='Enter your choice ------>', bg='#b5ab00', font=('Bauhaus 93', 30, 'bold')).place(x=50, y=500)
        self.back = Button(self.frame1, width=10, height=1, bg='black', fg='white', text='<< back',
                           font=('arial black', 10, 'bold'), command=self.admin).place(x=50, y=650)
        self.entry2 = Entry(self.frame1, width=20, fg='black', bg='white', font=('arial', 20))
        self.entry2.place(x=500, y=500)
        self.entry2.bind('<Return>', self.admin_choose1)

    def admin_choose1(self, event):
        choise = int(self.entry2.get())
        if choise == 1:
            self.insert_train()
        elif choise == 2:
            self.insert_passenger()
        elif choise == 3:
            self.detail_passenger()
        elif choise == 4:
            self.delete_passenger()
        else:
            Label(text='Choise is invalid', font=('viner hand itc', 30, 'bold'), bg='#b5ab00').place(x=500, y=600)





    def insert_train(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=3000, height=2000, bg='#b5ab00')
        self.frame1.propagate(0)
        self.frame1.pack()
        lb = Label(self.frame1, text='To Insert New Train Fill the below Details  ------', bg='#b5ab00',
                   font=('monotype corsival', 30, 'bold')).place(x=30, y=30)
        lb1 = Label(self.frame1, text='Enter Train ID  -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=100)
        lb2 = Label(self.frame1, text='Enter Train Name -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=150)
        lb3 = Label(self.frame1, text='Enter Train Type-->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=200)
        lb4 = Label(self.frame1, text='Enter source address-->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=250)
        lb5 = Label(self.frame1, text='Enter Depercher time -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=300)
        lb6 = Label(self.frame1, text='Enter destination address -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=350)
        lb6 = Label(self.frame1, text='Enter Reaching time-->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=400)
        lb7 = Label(self.frame1, text='Enter Amount-->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=450)

        self.e1 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e1.place(x=550, y=110)
        self.e2 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e2.place(x=550, y=160)
        self.e3 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e3.place(x=550, y=210)
        self.e4 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e4.place(x=550, y=260)
        self.e5 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e5.place(x=550, y=310)
        self.e6 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e6.place(x=550, y=360)
        self.e7 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e7.place(x=550, y=410)

        lbe = Label(self.frame1, text='please press enter __', fg='black', bg='#b5ab00',
                    font=('blackadder itc', 20, 'bold')).place(x=300, y=450)
        self.back = Button(self.frame1, width=10, height=1, bg='black', fg='white', text='<< back',
                           font=('arial black', 10, 'bold'), command=self.admin_choose).place(x=50, y=650)
        self.e8 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e8.place(x=550, y=460)
        self.e8.bind('<Return>', self.train_insert)


    def train_insert(self, event):
        e1 = int(self.e1.get())
        e2 = str(self.e2.get())
        e3 = str(self.e3.get())
        e4 = str(self.e4.get())
        e5 = int(self.e5.get())
        e6 = str(self.e6.get())
        e7 = int(self.e7.get())
        e8 = int(self.e8.get())
        connect = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = connect.cursor()
        str1 = "insert into train(train_id,train_name,train_type,sour_adds,dep_time,desc_adds,rec_time,amount)values('%d','%s','%s','%s','%d','%s','%d','%d')"
        args1 = (e1, e2, e3, e4, e5, e6, e7,e8)
        cursor.execute(str1 % args1)
        connect.commit()
        cursor.close()
        connect.close()
        lb = Label(self.frame1, text='Thankyou for inserting New Train', font=('arial black', 10, 'bold'),
                   bg='#b5ab00', fg='black', height=1).place(x=200, y=700)
        self.b = Button(self.frame1, width=10, height=1, text='Exit', font=('arial black', 10, 'bold'), bg='#b5ab00',
                        fg='black', command=exit).place(x=600, y=700)
        self.b1 = Button(self.frame1, width=10, height=1, text=' new Service', font=('arial black', 10, 'bold'), bg='#b5ab00',
                        fg='black', command=self.admin_choose).place(x=900, y=700)

    def insert_passenger(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=3000, height=2000, bg='#b5ab00')
        self.frame1.propagate(0)
        self.frame1.pack()
        lb = Label(self.frame1, text='Enter the below details to get the account ------', bg='#b5ab00',
                   font=('monotype corsival', 30, 'bold')).place(x=30, y=30)
        lb1 = Label(self.frame1, text='Enter the ID you like -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=100)
        lb2 = Label(self.frame1, text='Enter your Name -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=150)
        lb3 = Label(self.frame1, text='Enter your phone number -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=200)
        lb4 = Label(self.frame1, text='Enter your email-->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=250)
        lb5 = Label(self.frame1, text='Enter your user name -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=300)
        lb6 = Label(self.frame1, text='Enter your account password -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=350)
        lb6 = Label(self.frame1, text='Enter your location -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=400)
        self.e1 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e1.place(x=550, y=110)
        self.e2 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e2.place(x=550, y=160)
        self.e3 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e3.place(x=550, y=210)
        self.e4 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e4.place(x=550, y=260)
        self.e5 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e5.place(x=550, y=310)
        self.e6 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e6.place(x=550, y=360)
        lbe = Label(self.frame1, text='please press enter __', fg='black', bg='#b5ab00',
                    font=('blackadder itc', 20, 'bold')).place(x=300, y=450)
        self.back = Button(self.frame1, width=10, height=1, bg='black', fg='white', text='<< back',
                           font=('arial black', 10, 'bold'), command=self.admin_choose).place(x=50, y=650)
        self.e7 = Entry(self.frame1, width=40, font=('calibri', 11))
        self.e7.place(x=550, y=410)
        self.e7.bind('<Return>', self.admin_pass_insert)

    def admin_pass_insert(self, event):
        e1 = int(self.e1.get())
        e2 = self.e2.get()
        e3 = self.e3.get()
        e4 = self.e4.get()
        e5 = self.e5.get()
        e6 = self.e6.get()
        e7 = self.e7.get()
        connect = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = connect.cursor()
        str = "insert into passenger(pass_id,pass_name,pass_mob,pass_email,pass_uname,pass_pass,pass_adds) values('%d','%s','%s','%s','%s','%s','%s')"
        args = (e1, e2, e3, e4, e5, e6, e7)
        cursor.execute(str % args)
        connect.commit()
        cursor.close()
        connect.close()
        lb = Label(self.frame1, text='Thankyou for creating the account', font=('arial black', 10, 'bold'),
                   bg='#b5ab00', fg='black', height=1).place(x=200, y=700)
        self.b = Button(self.frame1, width=10, height=1, text='Exit', font=('arial black', 10, 'bold'), bg='#b5ab00',
                        fg='black', command=exit).place(x=600, y=700)
        self.b1 = Button(self.frame1, width=10, height=1, text='New service', font=('arial black', 10, 'bold'), bg='#b5ab00',
                        fg='black', command=self.admin_choose).place(x=900, y=700)
    def detail_passenger(self):
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        Label(text='To get passenger Details insert the below details:',font=('blackadder itc', 30, 'bold'),bg='#ccb800',fg='black').place(x=100,y=50)
        Label(text='Enter the passenger ID --->',font=('arial',20,'bold'),bg='#ccb800',fg='black').place(x=200,y=200)
        Label(text='press Enter ___ ',font=('arial',10,'bold'),bg='#ccb800',fg='black').place(x=250,y=250)
        self.b=Button(self.frame1,width=10,height=1,text='back',bg='black',fg='white',command=self.admin_choose)
        self.b.place(x=100,y=800)
        self.back = Button(self.frame1, width=10, height=1, bg='black', fg='white', text='<< back',
                           font=('arial black', 10, 'bold'), command=self.admin_choose).place(x=50, y=650)
        self.entry2 = Entry(self.frame1, width=20, fg='black', bg='white', font=('arial', 20))
        self.entry2.place(x=650, y=200)
        self.entry2.bind('<Return>',self.detail_passenger1)
    def detail_passenger1(self,event):
        pass_id=int(self.entry2.get())
        self.frame1.destroy()
        self.frame1=Frame(root,width=3000,height=3000,bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        conn=pymysql.connect(host='localhost',user='root',database='world',password='7338272260ksv')
        cur=conn.cursor()
        str6 = "call passenger_('%d')"
        args6 = (pass_id)
        cur.execute(str6 % args6)
        res1=cur.fetchall()
        res=[]
        for i in res1[0]:
            res.append(i)
        Label( text='Detail of the passenger as below', bg='#b5ab00',
                   font=('monotype corsival', 30, 'bold')).place(x=30, y=30)
        Label( text='passenger ID  -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=100)
        Label( text='passenger Name -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=150)
        Label( text='passenger phone number -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=200)
        Label( text='passenger email-->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=250)
        Label( text='passenger user name -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=300)
        Label( text='passenger account password -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=350)
        Label(text='passenger location -->', font=('calibri', 20, 'bold'), bg='#b5ab00',
                    fg='black').place(x=30, y=400)
        Label( text=res[0], font=('calibri', 20, 'bold'), bg='#b5ab00',
              fg='black').place(x=400, y=100)
        Label( text=res[1], font=('calibri', 20, 'bold'), bg='#b5ab00',
              fg='black').place(x=400, y=150)
        Label( text=res[2], font=('calibri', 20, 'bold'), bg='#b5ab00',
              fg='black').place(x=400, y=200)
        Label( text=res[3], font=('calibri', 20, 'bold'), bg='#b5ab00',
              fg='black').place(x=400, y=250)
        Label( text=res[4], font=('calibri', 20, 'bold'), bg='#b5ab00',
              fg='black').place(x=400, y=300)
        Label( text=res[5], font=('calibri', 20, 'bold'), bg='#b5ab00',
              fg='black').place(x=400, y=350)
        Label( text=res[6], font=('calibri', 20, 'bold'), bg='#b5ab00',
              fg='black').place(x=400, y=400)
        self.b=Button(self.frame1,text='exit',width=10,height=1,font=('arial',10,'bold'),command=exit)
        self.b.place(x=400,y=600)
        self.b1 = Button(self.frame1, text='New sevices', width=10, height=1, font=('arial', 10, 'bold'), command=self.admin_choose)
        self.b1.place(x=600, y=600)

    def delete_passenger(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        Label(text='To Delete the  passenger  insert the below details:', font=('blackadder itc', 30, 'bold'),
              bg='#ccb800', fg='black').place(x=100, y=50)
        Label(text='Enter the passenger ID --->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=200,
                                                                                                              y=200)
        Label(text='press Enter ___ ', font=('arial', 10, 'bold'), bg='#ccb800', fg='black').place(x=250, y=250)
        self.back = Button(self.frame1, width=10, height=1, bg='black', fg='white', text='<< back',
                           font=('arial black', 10, 'bold'), command=self.admin_choose).place(x=50, y=650)
        self.entrya = Entry(self.frame1, width=20, fg='black', bg='white', font=('arial', 20))
        self.entrya.place(x=650, y=200)
        self.entrya.bind('<Return>', self.delete_passenger1)
    def delete_passenger1(self,event):
        self.pass_id=int(self.entrya.get())
        self.frame1.destroy()
        self.frame1 = Frame(root, width=3000, height=3000, bg='#ccb800')
        self.frame1.propagate(0)
        self.frame1.pack()
        Label(text='Conform Deletion bY pressing Button::', font=('Script MT Bold', 40, 'bold'),
              bg='#ccb800', fg='red').place(x=100, y=50)
        self.b = Button(self.frame1, text='Delete', width=10, height=2, bg='black', fg='white',
                        command=self.admin_delete_pass1)
        self.b.place(x=100,y=150)
        self.b1 = Button(self.frame1, text='<<back', width=10, height=2, bg='black', fg='white',
                        command=self.admin_choose)

        self.b1.place(x=100, y=400)

    def admin_delete_pass1(self):
        conn = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cur = conn.cursor()
        str = "select * from passenger where pass_id='%d'"
        args = (self.pass_id)
        cur.execute(str % args)
        res = cur.fetchall()
        arr = []
        for i in res[0]:
            arr.append(i)
        Label(text='passenger ID -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=200)
        Label(text=arr[0], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=200)
        Label(text='passenger Name-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=250)
        Label(text=arr[1], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=250)
        Label(text='passenger mobile nO -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=300)
        Label(text=arr[2], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=300)
        Label(text='passenger email-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=350)
        Label(text=arr[3], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=350)
        Label(text='passenger user name -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=400)
        Label(text=arr[4], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=400)
        Label(text='passenger password -->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=450)
        Label(text=arr[5], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=450)
        Label(text='passenger address-->', font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=300, y=500)
        Label(text=arr[6], font=('arial', 20, 'bold'), bg='#ccb800', fg='black').place(x=700, y=500)
        self.exit1 = Button(self.frame1, text="EXIT", bg="black", fg='white', width=15, height=5, command=exit)
        self.exit1.place(x=50, y=650)
        self.exit2 = Button(self.frame1, text="new sevices", bg="black", fg='white', width=15, height=5,
                            command=self.admin_choose)
        self.exit2.place(x=500, y=650)
        conna = pymysql.connect(host='localhost', user='root', database='world', password='7338272260ksv')
        cura = conna.cursor()
        stra = "delete from passenger where pass_id='%d'"
        argsa = (self.pass_id)
        cura.execute(stra % argsa)
        conna.commit()





def exit():
    quit()

root=Tk()
root.title('mohan')
d=train(root)
root.mainloop()
