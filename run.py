from tkinter import *
from random import *


def submit():
    global r
    global win2
    t = int(ent.get())
    win2.destroy()
    m = "YOU WIN" if (r == t) else "YOU LOSE"+"\nRight Number is {0}".format(r)
    win2 = Tk()
    win2.title("RESULTS")
    l = Label(win2, text=m)
    l.config(bg="peach puff", fg="black", font=50, height=25, width=50)
    l.pack(expand=YES, fill=BOTH)
    b = Button(win2, text="Ok", command=win2.destroy)
    b.config(height=2, width=10, bg='light grey', fg='dark red', font=('times', 15, 'bold'), bd=3, relief=GROOVE)
    b.pack(side=RIGHT)
    win2.mainloop()


def easy():
    global r
    global ent, win2
    r = randint(1, 5)
    win2 = Tk()
    win2.title("EASY MODE")
    l = Label(win2, text="Enter a number in range 1 to 5 (In Grey Box)")
    l.config(height=3, width=35, bg='light sea green', fg='yellow', font=('times', 20, 'italic'), bd=5, relief=SUNKEN)
    l.pack(expand=YES, fill=BOTH)
    ent = Entry(win2)
    ent.insert(0, "")
    ent.config(bg="light grey", fg="black", bd=10, relief=FLAT)
    ent.pack(expand=YES, fill=BOTH)
    b = Button(win2, text="SUBMIT", command=submit)
    b.config(height=2, width=35, bd=4, relief=SOLID, bg='misty rose', fg='black', font=10)
    b.pack(expand=YES, fill=BOTH)
    q = Button(win2, text="QUIT", command=win2.destroy)
    q.config(height=2, width=10, bg='light grey', fg='dark red', font=('times', 15, 'bold'), bd=3, relief=GROOVE)
    q.pack(side=RIGHT)
    win2.mainloop()


def medium():
    global r
    global ent, win2
    r = randint(1, 10)
    win2 = Tk()
    win2.title("MEDIUM MODE")
    l = Label(win2, text="Enter a number in range 1 to 10 (In Grey Box)")
    l.config(height=3, width=35, bg='light sea green', fg='yellow', font=('times', 20, 'italic'), bd=5, relief=SUNKEN)
    l.pack(expand=YES, fill=BOTH)
    ent = Entry(win2)
    ent.insert(0, "")
    ent.config(bg="light grey", fg="black", bd=10, relief=FLAT)
    ent.pack(expand=YES, fill=BOTH)
    b = Button(win2, text="SUBMIT", command=submit)
    b.config(height=2, width=35, bd=4, relief=SOLID, bg='misty rose', fg='black', font=10)
    b.pack(expand=YES, fill=BOTH)
    q = Button(win2, text="QUIT", command=win2.destroy)
    q.config(height=2, width=10, bg='light grey', fg='dark red', font=('times', 15, 'bold'), bd=3, relief=GROOVE)
    q.pack(side=RIGHT)
    win2.mainloop()


def hard():
    global r
    global ent, win2
    r = randint(1, 20)
    win2 = Tk()
    win2.title("HARD MODE")
    l = Label(win2, text="Enter a number in range 1 to 20 (In Grey Box)")
    l.config(height=3, width=35, bg='light sea green', fg='yellow', font=('times', 20, 'italic'), bd=5, relief=SUNKEN)
    l.pack(expand=YES, fill=BOTH)
    ent = Entry(win2)
    ent.insert(0, "")
    ent.config(bg="light grey", fg="black", bd=10, relief=FLAT)
    ent.pack(expand=YES, fill=BOTH)
    b = Button(win2, text="SUBMIT", command=submit)
    b.config(height=2, width=35, bd=4, relief=SOLID, bg='misty rose', fg='black', font=10)
    b.pack(expand=YES, fill=BOTH)
    q = Button(win2, text="QUIT", command=win2.destroy)
    q.config(height=2, width=10, bg='light grey', fg='dark red', font=('times', 15, 'bold'), bd=3, relief=GROOVE)
    q.pack(side=RIGHT)
    win2.mainloop()


win = Tk()
win.title("Mini Game")
l = Label(win, text="GUESS THE NUMBER")
l.config(height=3, width=35, bg='light sea green', fg='yellow', font=('times', 20, 'italic'), bd=5, relief=SUNKEN)
l.pack(expand=YES, fill=BOTH)
b1 = Button(win, text="Easy", command=easy)
b1.config(height=2, width=35, bd=4, relief=SOLID, bg='misty rose', fg='black', font=10)
b1.pack(expand=YES, fill=BOTH)
b2 = Button(win, text="Medium", command=medium)
b2.config(height=2, width=35, bd=4, relief=SOLID, bg='misty rose', fg='black', font=10)
b2.pack(expand=YES, fill=BOTH)
b3 = Button(win, text="Hard", command=hard)
b3.config(height=2, width=35, bd=4, relief=SOLID, bg='misty rose', fg='black', font=10)
b3.pack(expand=YES, fill=BOTH)
q = Button(win, text="QUIT", command=win.destroy)
q.config(height=2, width=10, bg='light grey', fg='dark red', font=('times', 15, 'bold'), bd=3, relief=GROOVE)
q.pack(side=RIGHT)
win.mainloop()
