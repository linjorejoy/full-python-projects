import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)
#tkinter._test()

mw = tkinter.Tk()

mw.title("Hello World")
mw.geometry('640x480')
mw.mainloop()