from tkinter import *
base=Tk()
base.geometry('500x500')
base.title('Application Form ')
lab0 = Label(base, text="APPLICATION FORM",width=25,font=("bold", 20))  
lab0.place(x=90,y=53)
lab1=Label(base, text='First Name ',width=20,font=(10))
lab1.place(x=50,y=130)
entry1=Entry(base)
entry1.place(x=200,y=130)  
lab2=Label(base, text='Last Name ',width=20,font=(10))
lab2.place(x=500,y=130)
entry2=Entry(base)
entry2.place(x=650,y=130)
lab3 = Label(base, text="Gender",width=20,font=( 10))  
lab3.place(x=35,y=180) 
varbl=IntVar()
Radiobutton(base, text='Male', variable=varbl,padx=25, value=1).place(x=180,y=180)
Radiobutton(base, text='Female', variable=varbl,padx=25, value=2).place(x=280,y=180)

Button(base, text='Submit ', width=20, bg='blue', fg='white').place(x=230,y=230)
base.mainloop()