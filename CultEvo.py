
"""
    Cultural Evolution Simulation

    Team members:   Alla Muench / Andreas Daul / Holger Muth-Hellebrandt

    Course:         Introduction into Python - WS 2016

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  Main Module to run in order to start simulation
"""

import random

import Tests as Test
import Generation

random.seed()


import Presets as P




# Variable determining how many generations we want to allow
generations = P.generations



agentGen = Generation.Generation(P.numberAgents,generations)
agentArray = agentGen.getAgentArr()

#Test.CntTest(agentArray)

# when one generation is done, increase generation counter
#print Generation.agentsOverGenerations.__len__()
#print Generation.agentsOverAllDict.__len__()
#for agnLst in range(Generation.agentsOverAllDict.__len__()) :
#    print ( " ---   ---   --- ")
#    for x in Generation.agentsOverAllDict[agnLst]:
#        print"IDA: {:3}  Name: {:>50}   Parents: {}".format(x.retIDA(),x.retRec().title,x.ancestors)
#    print "Winning Recipe: {:35}".format(Generation.RecListOverGenerations[agnLst])



#Test.RetRecipies(0,5)
#Test.RetAllRec()
#Test.RetGenRecArr(0)
#Test.RetWinGenRecArr(0)

#for gen in range(Generation.SocialGroups.__len__()):
#    print "Generation: " + str(gen)
print()
Test.RetSGArrs(0)

#print Generation.WinningArrsOverGenerations.__len__()
#Test.RetWinGenRecArr(0)

#Test.RetAllGenAgents(agentArray)
#Test.RetAllAgents()

