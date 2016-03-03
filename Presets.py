from Tkinter import *
from tkMessageBox import askokcancel

# ===============================
# Amount of Generations

#generations = 15

# ========================================
# Amount of Agents per Generation
#numberAgents = 60

# Percentages of our main recipe classes
#facMeat =  20
#facFish =  20
#facVeggi = 20


# ====================================================
# Maximum size of social groups/ groups of 'friends'
# ReviewMe: should be size (n) due to use of range, but is actually (n-1)
# if maxSocSize is greater than the initial amount of agents we get social
# groups of size two and one exclusively;
# maxSocSize must not be smaller than 3!
maxSocSize = 3


# =================================================================================================
# Thresholds for what is considered a long/medium/short recipe ingredient list/ preparation time

timeDic = {"short":"0:25","medium":"1:00"}  # more than 1:00 implicates long
recDic = {"short":5,"medium":10}            # more than 10 elements implicates a long list


# ==============================================================
# How often should we repeat the individual CultEvo simulation

#numberOfSimulationRuns = 3

# ===============
# Toggle mutation

#do_mutate = True 


parameter = []

class StartWindow(Frame):                          
    def __init__(self, parent=None):           
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='START Simulation', command=self.start)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)

    def start(self):
        answer = askokcancel('', "Values set and ready to run?")
        if answer: Frame.quit(self)

fields = "Number of Generations:", "Number of Agents:","Number of Simulations:",\
		 "Meat Agents %:", "Fish Agents %:", "Veggi Agents %:",\
		 "Mutate:"
defaults = 15, 60, 3,\
		   20, 20, 20,\
		   "True"

def run(input):
    global parameter
    parameter = [x.get() for x in input]
    generations     = int(parameter[0])
    numberAgents    = int(parameter[1])
    numberOfSimulationRuns = int(parameter[2])
    facMeat         = int(parameter[3])
    facFish         = int(parameter[4])
    facVeggi        = int(parameter[5])
    do_mutate       = bool(parameter[6])
    print(parameter)

def makeform(root, fields):
    form = Frame(root)                              
    left = Frame(form)
    right = Frame(form)
    form.pack(fill=X) 
    left.pack(side=LEFT, padx = 5, pady = 5)
    right.pack(side=RIGHT, expand=YES, fill=X)

    variables = []
    default = 0
    for field in fields:
        lab = Label(left, text=field)
        ent = Entry(right)
        lab.pack(side=TOP, anchor=E)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        
        var.set(defaults[default])
        variables.append(var)

        default += 1
    return variables


root = Tk()
root.title("CultEvo 0.5")
root.geometry("500x300")

vars = makeform(root, fields)
Button(root, text='Update Values', command=(lambda v=vars: run(v))).pack(side=LEFT)

StartWindow(root).pack(side=RIGHT)
root.bind('<Return>', (lambda event, v=vars: run(v)))   
root.mainloop()

if len(parameter) != 0:
    generations     = int(parameter[0])
    numberAgents    = int(parameter[1])
    numberOfSimulationRuns = int(parameter[2])
    facMeat         = int(parameter[3])
    facFish         = int(parameter[4])
    facVeggi        = int(parameter[5])
    do_mutate       = bool(parameter[6])
else:
    print("CultEvo is closed.")
    sys.exit()


