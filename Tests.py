__author__ = 'AD'
'''
    Cultural Evolution Simulation

    Team members:   Alla Muench / Andreas Daul / Holger Muth-Hellebrandt

    Course:         Introduction into Python - WS 2016

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  Collection of methods for quick testing purposes
'''



import Agent
import Recipe as REx
import Generation




def CntTest(agentArr):
    mCnt = 0
    fCnt = 0
    vCnt = 0
    for x in agentArr:
        if x.getPref() == "meat":
            mCnt += 1
        elif x.getPref() == "fish":
            fCnt += 1
        else:
            vCnt += 1

        print str(x.retIDA())+ " " + x.getPref()
        RecTest(x)

    print
    print "mCnt: " + str(mCnt)
    print "fCnt: " + str(fCnt)
    print "vCnt: " + str(vCnt)

def RecTest(agent):

    print agent.retRec().ingredients

def RetAllGenAgents(agentsArray):
    mCnt = 0
    fCnt = 0
    vCnt = 0
    for x in agentsArray:
        if x.getPref() == "meat":
            mCnt += 1
        elif x.getPref() == "fish":
            fCnt += 1
        else:
            vCnt += 1

        print str(x.retIDA())+ " " + x.getPref()
        RecTest(x)

    print
    print "mCnt: " + str(mCnt)
    print "fCnt: " + str(fCnt)
    print "vCnt: " + str(vCnt)

def RetAllAgents():
    mCnt = 0
    fCnt = 0
    vCnt = 0
    print Generation.agentsOverAllDict.__len__()
    for alst in Generation.agentsOverAllDict:
        for x in Generation.agentsOverAllDict[alst]:
            if x.getPref() == "meat":
                mCnt += 1
            elif x.getPref() == "fish":
                fCnt += 1
            else:
                vCnt += 1

            print str(x.retIDA())+ " " + x.getPref()
            #RecTest(x)
    print
    print "mCnt: " + str(mCnt)
    print "fCnt: " + str(fCnt)
    print "vCnt: " + str(vCnt)

def RetRecipies(start,end):

    for recipe in REx.recipes[start:end]:
        print
        print("Category: " + recipe.category.split("\\")[-1])
        print("Title: " + recipe.title)
        print("PrepTime: " + recipe.prep_time)
        print("Ingreds: ")
        print(recipe.ingredients)
        print("Ing Size: " + str(recipe.ing_size))
        print("Score: " + str(recipe.score))

   # print("All ingreds: ")
   # print(REx.retAllIngreds())

def RetAllRec():

    for recipe in REx.recipes:
        print
        print("Category: " + recipe.category.split("\\")[-1])
        print("Title: " + recipe.title)
        print("PrepTime: " + recipe.prep_time)
        print("Ingreds: ")
        print(recipe.ingredients)
        print("Ing Size: " + str(recipe.ing_size))
        print("Score: " + str(recipe.score))

def RetDciFromArray(array):
    dict = {}
    for x in array:
        rname = x.retRec().title

        x.retRec().counter += 1
        dict1 = {rname:x.retRec().counter}
        dict.update(dict1)

    for x in dict:
        print x + " - " + str(dict[x])

def RetGenRecArr(index):

    for rec in Generation.ArraysOverGenerations[index]:
        print
        print (rec.title)
        print ("Score: " + str(rec.score))

def RetWinGenRecArr(index):

    print Generation.WinningArrsOverGenerations.__len__()
    print Generation.WinningArrsOverGenerations[index].__len__()

    for rec in Generation.WinningArrsOverGenerations[index]:
        print "Score {:4}   -  Cat.: {:>5}  -   Title: {}".format(rec.score,rec.category,rec.title)

def RetSGArrs(index):
    """

    :return: All Agents in their 'social environment' for the indexed generation plus the score of their recipe
    """
    counter = 0
    for SGarr in Generation.SocialGroups[index]:
        print
        print "new Group: Size: " + str(SGarr.__len__() )
        for agnt in SGarr:
                print "Agent {:3}  |  RecScore: {:3}  |  RecCateg: {:6}  |  #Ingreds: {:3}".format(agnt.retIDA(),
                                   agnt.retRec().score,agnt.retRec().category, agnt.retRec().ing_size)
                counter += 1


    print ("----------")
    print ("Sum of Agents: " + str(counter))
