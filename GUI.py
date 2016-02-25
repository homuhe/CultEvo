import Tkinter
from Tkinter import *
import time
import webbrowser
import tkMessageBox
	
def openLog():
    webbrowser.open('/home/alla/Dokumente/PythonCourse/TCourse/Project/log.txt')

def open4Window(previouswindow):
    previouswindow.destroy()

    def close_window():
        fourthWindow.destroy()
    
    fourthWindow = Tk()
    fourthWindow.title("Culinary Evolution Simulator")
    fourthWindow["padx"] = 20
    fourthWindow["pady"] = 20
    Label(fourthWindow, 
		 text="Now everyone is ready to offer the cooked dish to friends",
		 fg = "dark green",
		 font = "Times 18 bold").pack()
    Label(fourthWindow, 
		 text="See if they like the cooking!",
		 fg = "dark green",
		 font = "Times 18 bold").pack()
    Label(fourthWindow, 
		 text="The best recipes will be passed on to the next generation",
		 fg = "dark green",
		 font = "Times 16 bold").pack()

    logo5 = PhotoImage(file="/home/alla/Dokumente/PythonCourse/TCourse/Project/feuer.gif")
    w1 = Label(fourthWindow, image=logo5)
    w1.pack()

    b1 = Button(fourthWindow, text='Quit',command=close_window)
    b1.pack(side=RIGHT, padx=15, pady=10)
    b2 = Button(fourthWindow, text='Start next generation', command=lambda: openSecondWindow(fourthWindow))
    b2.pack(side=RIGHT, padx=5, pady=10)
    b3 = Button(fourthWindow, text='Show output',command=openLog)
    b3.pack(side=RIGHT, padx=5, pady=10)
   
    fourthWindow.mainloop()

   
def openThirdWindow(previouswindow):
    previouswindow.destroy()

    def close_window():
        thirdWindow.destroy()
    
    thirdWindow = Tk()
    thirdWindow.title("Culinary Evolution Simulator")
    thirdWindow["padx"] = 20
    thirdWindow["pady"] = 20
    Label(thirdWindow, 
		 text="Now everyone has a recipe to cook.",
		 fg = "dark green",
		 font = "Times 18 bold").pack()
    Label(thirdWindow, 
		 text="Some ingredients can be forgotten, added or substituted",
		 fg = "dark green",
		 font = "Times 16 bold").pack(padx=15)
    Label(thirdWindow, 
		 text="See what happens!",
		 fg = "dark green",
		 font = "Times 16 bold").pack()

    logo4 = PhotoImage(file="/home/alla/Dokumente/PythonCourse/TCourse/Project/Koechin.gif")
    w1 = Label(thirdWindow, image=logo4)
    w1.pack()
   
    b1 = Button(thirdWindow, text='Quit',command=close_window)
    b1.pack(side=RIGHT, padx=15, pady=10)
    b2 = Button(thirdWindow, text='Cook', command=lambda: open4Window(thirdWindow))
    b2.pack(side=RIGHT, padx=5, pady=10)
    b3 = Button(thirdWindow, text='Show output',command=openLog)
    b3.pack(side=RIGHT, padx=5, pady=10)
   
    thirdWindow.mainloop()

def openSecondWindow(previouswindow):
    previouswindow.destroy()

    def close_window():
        secondWindow.destroy()
        
    def saveCallback():
        try:
            facMeat = int(e1.get())
            facFish = int(e2.get())
            facVeggi = int(e3.get())
        except ValueError:
            tkMessageBox.showinfo("Warning", "Invalid input")
        with open("log.txt", 'w') as outfile:
            outfile.write(e1.get())
            outfile.write(e2.get())
            outfile.write(e3.get())
	
    secondWindow = Tk()
    secondWindow.title("Culinary Evolution Simulator")
    secondWindow["padx"] = 20
    secondWindow["pady"] = 20
    Label(secondWindow, 
		 text="Create your generations of eaters",
		 fg = "dark green",
		 font = "Times 18 bold").pack()
    Label(secondWindow, 
		 text="Decide how many meat-eaters, fish-eaters and vegetarians",
		 fg = "dark green",
		 font = "Times 16 bold").pack(padx=15)
    Label(secondWindow, 
		 text="are in the first generation!",
		 fg = "dark green",
		 font = "Times 16 bold").pack()
    f1 = Frame(secondWindow)
    l1 = Label(f1, width=15, font = "Times 12 bold",fg = "dark green",text='Meat eaters', anchor='w')
    e1 = Entry(f1)
    logo1 = PhotoImage(file="/home/alla/Dokumente/PythonCourse/TCourse/Project/meat.gif")
    w1 = Label(f1, image=logo1)
    f1.pack(side=TOP, fill=X, padx=45)
    l1.pack(side=LEFT)
    e1.pack(side=LEFT)
    w1.pack(side=LEFT,padx=25)
    f2 = Frame(secondWindow)
    l2 = Label(f2, width=15,font = "Times 12 bold",fg = "dark green",text='Fish eaters', anchor='w')
    e2 = Entry(f2)
    logo2 = PhotoImage(file="/home/alla/Dokumente/PythonCourse/TCourse/Project/fisch.gif")
    w2 = Label(f2, image=logo2)
    f2.pack(side=TOP, fill=X, padx=45)
    l2.pack(side=LEFT)
    e2.pack(side=LEFT)
    w2.pack(side=LEFT,padx=25)
    f3 = Frame(secondWindow)
    l3 = Label(f3, width=15,font = "Times 12 bold",fg = "dark green",text='Vegetarians', anchor='w')
    e3 = Entry(f3)
    logo3 = PhotoImage(file="/home/alla/Dokumente/PythonCourse/TCourse/Project/salad.gif")
    w3 = Label(f3,image=logo3)
    f3.pack(side=TOP, fill=X, padx=45)
    l3.pack(side=LEFT)
    e3.pack(side=LEFT)
    w3.pack(side=LEFT,padx=25)
    b1 = Button(secondWindow, text='Quit',command=close_window)
    b1.pack(side=RIGHT, padx=15, pady=10)
    b2 = Button(secondWindow, text='Next', command= lambda: openThirdWindow(secondWindow))
    b2.pack(side=RIGHT, padx=5, pady=10)
    b3 = Button(secondWindow, text='Show output',command=openLog)
    b3.pack(side=RIGHT, padx=5, pady=10)
    b4 = Button(secondWindow, text='Enter data',command=saveCallback)
    b4.pack(side=RIGHT, padx=5, pady=10)
     
    secondWindow.mainloop()
 


def openFirstWindow():
	
    top = Tkinter.Tk()
    top["padx"] = 30
    top["pady"] = 20
    top.title("Culinary Evolution Simulator")
    frame = Frame(top)
    frame.pack()

    bottomframe = Frame(top)
    bottomframe.pack( side = BOTTOM, pady=20 )

    Label(frame, 
		 text="Welcome to Culinary Evolution Simulator",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 20 bold italic").pack()
    Label(frame, 
		 text="Create your generations of eaters",
		 fg = "dark green",
		 font = "Times 18 bold").pack()

    Label(frame, 
		 text="Cook, eat and communicate!",
		 fg = "dark green",
		 font = "Times 18").pack()
    logo = PhotoImage(file="/home/alla/Dokumente/PythonCourse/TCourse/Project/caveman.gif")
    w1 = Label(frame, image=logo, pady=20).pack(side=BOTTOM)
    B = Tkinter.Button(bottomframe, text ="Start",font = "Times 18 bold",fg = "dark green",height=2, width=10,command= lambda: openSecondWindow(top))
    B.pack()
    top.mainloop()

openFirstWindow()
