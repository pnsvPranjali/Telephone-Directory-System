from tkinter import *
import tkinter.messagebox
import pymysql as p
class Module:
	aen=None
	e11=None
	e22=None
	aep=None
	aeph=None
	aeci=None
	aead=None
	ne=None
	pe=None
	ee=None
	w=None
	w2=None
	de1=de2=None
	

	
	def register(self):
	
		con=p.connect("localhost","root","","db")
		cur=con.cursor()
		a=self.ne.get()
		b=self.pe.get()
		q="insert into login values('%s','%s')"
		cur.execute(q %(a,b))
		con.commit()
		con.close()

		self.ne.delete(0,'end')
		self.pe.delete(0,'end')
		self.ee.delete(0,'end')
		tkinter.messagebox.showinfo("Success","You are registered successfully !!")	


	def login(self):
		
		def verify():
			self.w2=Tk()
			self.w2.geometry('600x400')
			self.w2.title('Login')	
			h1=Label(self.w2,text="WELCOME !!",font="Times 14 bold")
			h1.grid(row=0,column=3)
			Label(self.w2,text="     ").grid(row=1,column=2)
			Label(self.w2,text=" ").grid(row=2,column=1)
			but=Button(self.w2,text="  ADD_Record  ",bg="green",fg="white",font='Times 10 bold ',cursor='plus',command=self.add_record)
			but.grid(row=3,column=1)
			but1=Button(self.w2,text="  DELETE_Record  ",bg="orange",fg="white",font='Times 10 bold ',cursor='plus',command=self.del_record)
			but1.grid(row=3,column=5)
			Label(self.w2,text="     ").grid(row=4,column=1)
			Label(self.w2,text="     ").grid(row=5,column=2)
			Label(self.w2,text="     ").grid(row=4,column=2)
			but2=Button(self.w2,text="  UPDATE_Record  ",bg="magenta",fg="white",font='Times 10 bold ',cursor='plus',command=self.update_record)
			but2.grid(row=6,column=3)
			Label(self.w2,text=" ").grid(row=7,column=1)
			Label(self.w2,text="     ").grid(row=8,column=2)
			but3=Button(self.w2,text="  SEARCH_Record  ",bg="purple",fg="white",font='Times 10 bold ',cursor='plus',command=self.search)
			but3.grid(row=9,column=1)
			but4=Button(self.w2,text="  DISPLAY_Record  ",bg="navy",fg="white",font='Times 10 bold ',cursor='plus',command=self.display)
			but4.grid(row=9,column=5)
			Label(self.w2,text="     ").grid(row=10,column=2)
			but5=Button(self.w2,text="   EXIT   ",bg="gray",fg="white",font='Times 10  ',cursor='plus',command=self.quit)
			but5.grid(row=12,column=3)
			self.w2.mainloop()

		c=0
		if self.e1.get() == '' or self.e2.get() == '':
			c=-1
		else:

			con=p.connect("localhost","root","","db")
			cur=con.cursor()
			q="select * from login where name='%s'"
			cur.execute(q%(self.e1.get()))
			self.data=cur.fetchone()
			if self.data : 
				l=list(self.data)
			
				if l[1] != self.e2.get():
					c=-1
				else :
					tkinter.messagebox.showinfo("LOGIN", "Login Successfull")
					self.e1.delete(0, 'end')
					self.e2.delete(0, 'end')
					verify()
			else:
				c=-1

		if c==-1:
			tkinter.messagebox.showerror("Error","Oops!! Invalid User ID or Password !!")		
			self.e1.delete(0,'end')
			self.e2.delete(0,'end')
	
	def quit(self):
		self.w2.destroy()			


	def signin(self):
		self.w.withdraw()
		self.w1=Tk()
		self.w1.geometry('600x400')
		self.w1.title('SignIn')
	
		h=Label(self.w1,text="NEW USER ? REGISTER NOW !! ",font="Times 14 bold")
		h.grid(row=0,column=2)
		n=Label(self.w1,text="Name ",font="Times 12",padx=10,pady=10).grid(row=2,column=0)
		p=Label(self.w1,text="Password ",font="Times 12",padx=10,pady=10).grid(row=4,column=0)
		e=Label(self.w1,text="EmailID ",font="Times 12",padx=10,pady=10).grid(row=6,column=0)
		self.ne=Entry(self.w1)
		self.ne.grid(row=2,column=1)
		self.pe=Entry(self.w1,show='*')
		self.pe.grid(row=4,column=1)
		self.ee=Entry(self.w1)
		self.ee.grid(row=6,column=1)
		bb1=Button(self.w1,text="SIGNIN",bg="blue",fg="white",font='Times 10 ',cursor='plus', command=self.register)
		bb1.grid(row=7,column=2)
		
		bb2=Button(self.w1,text="BACK",cursor='plus',command=self.backk)
		bb2.grid(row=8,column=3)

		self.w1.mainloop()
		
	def backk(self):
		self.w.update()	
		self.w.deiconify()
		self.w1.destroy()

	def exitt(self):
		self.a.destroy()

	def insert_re(self):
		na=(self.aen.get())
		pa=(self.aep.get())
		phno=int(self.aeph.get())
		acit=(self.aeci.get())
		addr=(self.aead.get())
	
		con=p.connect("localhost","root","","db")
		cur=con.cursor()
		q="insert into record values('%s','%s',%d,'%s','%s')"
		cur.execute(q %(na,pa,phno,acit,addr))
		con.commit()
		con.close()

		tkinter.messagebox.showinfo("Success","Record is Added Successfully !!")		
		self.aen.delete(0,'end')
		self.aep.delete(0,'end')
		self.aeph.delete(0,'end')
		self.aeci.delete(0,'end')
		self.aead.delete(0,'end')

	def add_record(self):
		self.w2.withdraw()
		self.a=Tk()
		self.a.geometry('600x400')
		self.a.title('SignIn')
	
		ah=Label(self.a,text="ADD RECORD !! ",font="Times 14 bold")
		ah.grid(row=0,column=2)
		an=Label(self.a,text="Name ",font="Times 12",padx=10,pady=10)
		an.grid(row=2,column=0)
		ap=Label(self.a,text="Password ",font="Times 12",padx=10,pady=10)
		ap.grid(row=4,column=0)
		aph=Label(self.a,text="Phone No. ",font="Times 12",padx=10,pady=10)
		aph.grid(row=6,column=0)
		ac=Label(self.a,text="City ",font="Times 12",padx=10,pady=10)
		ac.grid(row=8,column=0)
		aad=Label(self.a,text="Address ",font="Times 12",padx=10,pady=10)
		aad.grid(row=10,column=0)

		self.aen=Entry(self.a)
		self.aen.grid(row=2,column=1)
		self.aep=Entry(self.a,show='*')
		self.aep.grid(row=4,column=1)
		self.aeph=Entry(self.a)
		self.aeph.grid(row=6,column=1)
		self.aeci=Entry(self.a)
		self.aeci.grid(row=8,column=1)
		self.aead=Entry(self.a)
		self.aead.grid(row=10,column=1)
		ab1=Button(self.a,text="Add Record",bg="blue",fg="white",font='Times 10 ',cursor='plus', command=self.insert_re)
		ab1.grid(row=11,column=2)
		ab2=Button(self.a,text="EXIT",cursor='plus',command=self.exitt)
		ab2.grid(row=13,column=2)
		ab3=Button(self.a,text="BACK",cursor='plus',command=self.back)
		ab3.grid(row=15,column=2)

		self.a.mainloop()	

	def back(self):
		self.w2.update()	
		self.w2.deiconify()
		self.a.destroy()


	def del_record(self):
		self.w2.withdraw()
		self.a=Tk()
		self.a.geometry('600x400')
		self.a.title('Delete Record')
	
		d1=Label(self.a,text="REMOVE RECORD !! ",font="Times 14 bold")
		d1.grid(row=0,column=1)
		d2=Label(self.a,text="Enter the details of the record: ",font="Times 14",padx=10,pady=10)
		d2.grid(row=2,column=0)
		d3=Label(self.a,text="Name ",font="Times 12")
		d3.grid(row=4,column=0)
		d4=Label(self.a,text="Password ",font="Times 12")
		d4.grid(row=6,column=0)
		self.de1=Entry(self.a)
		self.de1.grid(row=4,column=1)
		self.de2=Entry(self.a,show='*')
		self.de2.grid(row=6,column=1)
		db1=Button(self.a,text="Delete",cursor='plus',bg="blue",fg="white",font='Times 10',command=self.process_del)
		db1.grid(row=8,column=1)
		db2=Button(self.a,text="BACK",cursor='plus',command=self.back)
		db2.grid(row=10,column=1)

		self.a.mainloop()	

	def process_del(self):
		dt=self.de1.get()
		du=self.de2.get()
		c=0
		if dt=="" or du=="":
			c=-1
		else:

			con=p.connect("localhost","root","","db")
			cur=con.cursor()
			q="select * from record where name='%s'"
			cur.execute(q%(self.de1.get()))
			self.data=cur.fetchall()
			if self.data : 
				l=list(self.data)
			
				for i in l:
					if du in i:
						q1="delete from record where name='%s' and pass='%s' "
						cur.execute(q1 %(self.de1.get(),self.de2.get()))
						con.commit()
						con.close()
						tkinter.messagebox.showinfo("Success","Record is Deleted Successfully !!")		
						self.de1.delete(0,'end')
						self.de2.delete(0,'end')
						break

					
				else :
					c=-1
					
			else:
				c=-1

		if c==-1:
			tkinter.messagebox.showerror("Error", "Record not Found!!")
			self.de1.delete(0, 'end')
			self.de2.delete(0, 'end')
	

		

		
		
	def update_record(self):
		
		self.w2.withdraw()
		self.a=Tk()
		self.a.geometry('600x400')
		self.a.title('Update Record')
	
		
	
		d1=Label(self.a,text="Update RECORD !! ",font="Times 14 bold")
		d1.grid(row=0,column=1)
		d2=Label(self.a,text="Choose from the list : ",font="Times 14",padx=10,pady=10)
		d2.grid(row=2,column=0)
		
		self.vb=IntVar()

		Label(self.a,text=" Name").grid(row=4,column=0)
		rb1=Radiobutton(self.a,variable=self.vb,value=1,command=self.processRadiobutton1)
		
		Label(self.a,text="  Password").grid(row=6,column=0)
		rb2=Radiobutton(self.a,variable=self.vb,value=2,command=self.processRadiobutton2)

		Label(self.a,text='     Phone-Number').grid(row=8,column=0)
		rb3=Radiobutton(self.a,variable=self.vb,value=3,command=self.processRadiobutton3)

		Label(self.a,text='City').grid(row=10,column=0)
		rb4=Radiobutton(self.a,variable=self.vb,value=4,command=self.processRadiobutton4)

		Label(self.a,text='  Address').grid(row=12,column=0)
		rb5=Radiobutton(self.a,variable=self.vb,value=5,command=self.processRadiobutton5)
		
		rb1.grid(row=4,column=1)
		rb2.grid(row=6,column=1)
		rb3.grid(row=8,column=1)
		rb4.grid(row=10,column=1)
		rb5.grid(row=12,column=1)

		l1=Label(self.a,text='Enter the existing value : ',padx=10,pady=10)
		l1.grid(row=14,column=0)
			
		self.E1=Entry(self.a)
		self.E1.grid(row=14,column=1)

		l2=Label(self.a,text='Enter the updated value : ',padx=10,pady=10)
		l2.grid(row=16,column=0)
			
		self.E2=Entry(self.a)
		self.E2.grid(row=16,column=1)

		B=Button(self.a,text="Submit",cursor='plus',bg="blue",fg="white",font='Times 10',command=self.submit_db)
		B.grid(row=18,column=1)
		B2=Button(self.a,text="BACK",cursor='plus',bg="gray",font='Times 10',command=self.back)
		B2.grid(row=20,column=0)

		B1=Button(self.a,text="EXIT",cursor='plus',bg="gray",font='Times 10',command=self.exitt)
		B1.grid(row=20,column=3)

		self.a.mainloop()
			

	def processRadiobutton1(self):

		self.vb=1

	def processRadiobutton2(self):

		self.vb=2

	def processRadiobutton3(self):

		self.vb=3

	def processRadiobutton4(self):

		self.vb=4

	def processRadiobutton5(self):

		self.vb=5


	def submit_db(self):
		con=p.connect("localhost","root","","db")
		cur=con.cursor()
		
		if self.vb==1:
			print(self.E1.get())
			q="update record set name='%s' where name='%s'"
			cur.execute(q %(self.E2.get(),self.E1.get()))
		elif self.vb==2:
			q="update record set pass='%s' where pass='%s'"
			cur.execute(q %(self.E2.get(),self.E1.get()))

		elif self.vb.get()==3:
			q="update record set phno=%d where phno=%d"
			cur.execute(q %(self.E2.get(),self.E1.get()))

		elif self.vb.get()==4:
			q="update record set city='%s' where city='%s'"
			cur.execute(q %(self.E2.get(),self.E1.get()))

		else:
			q="update record set addr='%s' where addr='%s'"
			cur.execute(q %(self.E2.get(),self.E1.get()))

		
		con.commit()
		con.close()
		tkinter.messagebox.showinfo("Success","Record is Updated Successfully !!")		
		self.E1.delete(0,'end')
		self.E2.delete(0,'end')


	

	def search(self):
		self.w2.withdraw()
		self.a=Tk()
		self.a.geometry('600x400')
		self.a.title('Search Record')
	
		d1=Label(self.a,text="SEARCH RECORD !! ",font="Times 14 bold")
		d1.grid(row=0,column=1)
		d2=Label(self.a,text="Enter the details of the record: ",font="Times 14",padx=10,pady=10)
		d2.grid(row=2,column=0)
		d3=Label(self.a,text="Name ",font="Times 12")
		d3.grid(row=4,column=0)
		d4=Label(self.a,text="Password ",font="Times 12")
		d4.grid(row=6,column=0)
		self.e11=Entry(self.a)
		self.e11.grid(row=4,column=1)
		self.e22=Entry(self.a,show='*')
		self.e22.grid(row=6,column=1)
		db1=Button(self.a,text="Search",cursor='plus',bg="blue",fg="white",font='Times 10',command=self.db_search)
		db1.grid(row=8,column=1)
		db2=Button(self.a,text="BACK",cursor='plus',command=self.back)
		db2.grid(row=10,column=1)

		self.a.mainloop()	

	
	def db_search(self):
		S1=(self.e11.get())
		S2=(self.e22.get())

		print("{},{}".format(S1, S2))
		c=0
		if S1 == '' or S2 == '':		#if the user tries to execute empty entry
			tkinter.messagebox.showerror("Error","Enter Valid Data !!")		
		else:

			con=p.connect("localhost","root","","db")
			cur=con.cursor()
			q="select * from record where name='%s'"
			cur.execute(q%(S1))
			self.Data=cur.fetchall()
			print(self.Data)

			if self.Data : 					#checks if name entered by user exist in database 
		 		l=list(self.Data)
			
		 		for i in l:
		 			if S2 in i:
		 				c=0
		 				tkinter.messagebox.showinfo("Congo", "Record Found !!")	
		 				break						
		 		else :
		 			c=-1
		 			self.e11.delete(0, 'end')
		 			self.e22.delete(0, 'end')
			else:							
		 		c=-1

		if c==-1:
		 	tkinter.messagebox.showerror("Error","Sorry !! Record not Found !!")		
		 	self.e11.delete(0,'end')
		 	self.e22.delete(0,'end')

			

	def display(self):
		
		self.w2.withdraw()   
		self.a=Tk()
		self.a.geometry('600x400')
		self.a.title('Display Record')
	
		d1=Label(self.a,text="DISPLAY RECORD !! ",font="Times 14 bold")
		d1.grid(row=0,column=2)
		d2=Label(self.a,text="NAME ",font="Times 12",padx=10,pady=10)
		d2.grid(row=2,column=0)
		d3=Label(self.a,text="Ph.NO. ",font="Times 12")
		d3.grid(row=2,column=2)
		d4=Label(self.a,text="CITY ",font="Times 12")
		d4.grid(row=2,column=4)
		d4=Label(self.a,text="ADDRESS ",font="Times 12")
		d4.grid(row=2,column=6)
		
		con=p.connect("localhost","root","","db")
		cur=con.cursor()
		q="select name,phno,city,addr from record"
		cur.execute(q)
		self.data=cur.fetchall()	
		
		
		r=4
		for i in self.data:
			r+=1
			for j in range(len(i)):
				ll=Label(self.a,text=i[j]).grid(row=r,column=2*j)

		
		Label(self.a,text="  ",padx=10,pady=10).grid(row=18,column=2)
		
		db2=Button(self.a,text="BACK",bg='gray',cursor='plus',command=self.back)
		db2.grid(row=20,column=2)

		self.a.mainloop()	

	

	def __init__(self):

		self.p1=None
		
		self.w=Tk()
		self.w.geometry('800x400')
		self.data=tuple()
		self.w.title("Welcome")
		self.frame1=Frame(self.w)
		self.frame1.pack()
		self.frame2=Frame(self.w)
		self.frame2.pack()
		self.password=StringVar()
		
		l=Label(self.frame1,text="WELCOME !! TO TELEPHONE DIRECTORY SYSTEM ",font="Helvetica 16 bold")
		
		l1=Label(self.frame1,text="Name",font="Times 14 bold",padx=10,pady=10)
		l2=Label(self.frame1,text="Password",font="Times 14 bold",padx=10,pady=10)
		photo=PhotoImage(file='index.gif')
		label=Label(self.frame1,image=photo)
		label.grid(row=0,column=0)

		self.e1=Entry(self.frame1)

		self.e2=Entry(self.frame1,textvariable=self.password,show='*')
	
		b1=Button(self.frame2,text="LOGIN",bg="blue",fg="white",font='Times 10 bold',cursor='plus', command=self.login)
		nu=Label(self.frame2,text="    New User?",fg="blue",font='Times 12 bold')
		b2=Button(self.frame2,text="SIGN IN",bg="blue",fg="white",font='Times 10 bold',cursor='plus', command=self.signin)
		
		l.grid(row=0,column=1)
		l1.grid(row=2,column=0)
		l2.grid(row=3,column=0)
		self.e1.grid(row=2,column=1)
		self.e2.grid(row=3,column=1)
		nu.grid(row=6,column=2)
		b1.grid(row=6,column=1)
		b2.grid(row=6,column=3)
		self.w.mainloop()
Module()