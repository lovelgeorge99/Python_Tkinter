from tkinter import Tk,StringVar,ttk
from tkinter import *

root=Tk()


#======================Functions=============

def exit():
    root.destroy()

def reset():
    operator=""
    distance.set(operator) 
    value0.set(operator)
    answer.set(operator)

def convert():
    if value0.get()=='Meter':
        convert1=float(distance.get())/100
        answer.set(convert1)
    elif value0.get()=='Millimeter':
        convert1=float(distance.get())*10
        answer.set(convert1)
    elif value0.get()=='Kilometer':
        convert1=float(distance.get())/1000
        answer.set(convert1)
    elif value0.get()=='Inch':
        convert1=float(distance.get())*0.394
        answer.set(convert1)
    elif value0.get()=='Feet':
        convert1=float(distance.get())*0.0328
        answer.set(convert1)   



#=====================================

root.geometry("800x300+400+200")
root.configure(background="black")
root.title("Distance Converter")

distance=StringVar()
value0=StringVar()
answer=StringVar()


frame1=Frame(root,width=600,height=100,bg="black")
frame1.pack(side=TOP)
heading=Label(frame1,text="Distance Converter",font=('arial',40,'italic'),fg="yellow",bg="black")
heading.grid(row=0,column=0)

frame2=Frame(root,width=300,height=300,bg="black")
frame2.pack()



lbl1=Label(frame2,text="Enter The Distance in cm:",font=('arial',20,'bold'),fg="red",bg="black")
lbl1.grid(row=0,column=0)


entrytxt=Entry(frame2,font=('arial',15,'bold'),textvariable=distance,bg="white",bd=5,insertwidth=5)
entrytxt.grid(row=0,column=1)


lbl2=Label(frame2,text="Convert Into :",font=('arial',20,'bold'),fg="red",bg="black")
lbl2.grid(row=1,column=0)



box=ttk.Combobox(frame2,textvariable=value0,state='readonly',font=('arial',15,'bold'),width=15)
box['values']=(' ','Millimeter','Inch','Feet','Meter','Kilometer')
box.current(0)
box.grid(row=1,column=1)

lbl3=Label(frame2,text=" Answer = ",font=('arial',20,'bold'),fg="red",bg="black")
lbl3.grid(row=2,column=0)


Answertxt=Entry(frame2,font=('arial',15,'bold'),textvariable=answer,bg="white",bd=5,insertwidth=5)
Answertxt.grid(row=2,column=1)


#=============================================Buttons=======================================================
btnConvert=Button(frame2,text="Convert",font=('arial',10,'bold'),width=8,pady=5,command=convert)
btnConvert.grid(row=3,column=0)

btnReset=Button(frame2,text="Reset",font=('arial',10,'bold'),width=8,pady=5,command=reset)
btnReset.grid(row=3,column=1)

btnExit=Button(frame2,text="Exit",font=('arial',10,'bold'),width=8,command=exit)
btnExit.grid(row=3,column=2)


root.mainloop()
