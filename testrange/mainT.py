__author__ = 'AD'

import recT, agentT, interactT, random, itertools

# ============================
# manual setup of a generation
#=============================

rec1 = recT.Recipe("fish","0:25",["i1","i3","i6"])
agent1 = agentT.Agent("A1",rec1)

rec2 = recT.Recipe("fish","0:55",["i2","i3","i8"])
agent2 = agentT.Agent("A2",rec2)

rec3 = recT.Recipe("meat","1:25",["i1","i5","i7"])
agent3 = agentT.Agent("A3",rec3)

rec4 = recT.Recipe("meat","0:35",["i1","i3","i7"])
agent4 = agentT.Agent("A4",rec4)

rec5 = recT.Recipe("veggi","0:15",["i1","i3","i4","i5","i8"])
agent5 = agentT.Agent("A5",rec5)

rec6 = recT.Recipe("veggi","0:05",["i2","i4","i6","i8"])
agent6 = agentT.Agent("A6",rec6)

rec7 = recT.Recipe("veggi","0:05",["i2","i3","i6","i8"])
agent7 = agentT.Agent("A7",rec7)

genX = [agent1,agent2,agent3,agent4,agent5,agent6,agent7]

# =================================

# number of friends per generation: random pick of 1 to 10
gen1 = genX[:]

while gen1.__len__()!=0:

    # ToDo: we need a way to adjust our upper bound for the random sampling
    # so that we dont want to sample 10 items when our array only consists of
    # ,e.g., 9 or less elements

    if gen1.__len__()>=10:
        #friendArr = random.sample(gen1,random.randrange(randIntLB,randIntUB))
        friendArr = random.sample(gen1,10)
        for x in friendArr:
            gen1.remove(x)
        # right now we have set up a social environment

        if friendArr.__len__()>1:
            for x in friendArr:
                # dont judge your own recipe
                tmpArr = friendArr
                tmpArr.remove(x)
                for y in tmpArr:
                    x.judgeMyRec(y)
        else:
            pass

    elif gen1.__len__()>=2:
        friendArr = random.sample(gen1,2)
        for x in friendArr:
            gen1.remove(x)
        # right now we have set up a social environment

        if friendArr.__len__()>1:
            for x in friendArr:
                # dont judge your own recipe
                tmpArr = friendArr
                tmpArr.remove(x)
                for y in tmpArr:
                    x.judgeMyRec(y)

    else: # again, dont judge your own....just yet

        gen1.pop()





print
print genX.__len__()
print
for x in genX:
    print
    x.toString()

#agent1.toString()

