from tkinter import *

def submit():
    label1 = Label(window,text = entry1.get())
    label1.grid(row=5, column=3)
    label2 = Label(window,text = entry2.get())
    label2.grid(row=6, column=3)
    
window = Tk() #To create a GUI window
window.title("Siva Balan")
window.geometry("600x600+0+0") #To fix the window size
label1 = Label(window,text = "Welcome to our world", foreground = "Red")
label1.grid(row=1, column=1)
label2 = Label(window,text = "First Name")
label2.grid(row=2, column=2)
entry1 = Entry(window,text = "")
entry1.grid(row=2, column=3)
label3 = Label(window,text = "Last Name")
label3.grid(row=3, column=2)
entry2 = Entry(window,text = "")
entry2.grid(row=3, column=3)
button1 = Button(window,text = "Submit",command = submit)
button1.grid(row=4,column=3)
