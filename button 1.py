from tkinter import *
a1=Tk()
def c1():
    lc1= Label(text='why did you do that ', fg='blue',bg='white',font=25).pack()
def c2():
    tc2=a.get()
    lc2= Label(text = 'hello '+tc2 , fg='blue',bg='white',font=25).pack()
a= StringVar()
a1.title("hello")
a1.geometry("800x800+150+50")
l1= Label(text='what is your name ', fg='blue',bg='white',font=25).pack()
t1=Entry(textvariable = a).pack()  
b1= Button(text=' enter',fg='white' , command=c1,bg='red',font=25).pack()
b2= Button(text=' click this',command=c2, bg='black' ,fg='red',font=25).pack()
                           


a1.mainloop()
