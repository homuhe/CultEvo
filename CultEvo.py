__author__ = 'AD'

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
generations = 8



agentGen = Generation.Generation(P.numberAgents,generations)
agentArray = agentGen.getAgentArr()

#Test.CntTest(agentArray)

# when one generation is done, increase generation counter

for x in Generation.agentsOverAllDict[1]:
    print x.retIDA()


#Test.RetRecipies(0,5)
#Test.RetAllRec()
#Test.RetGenRecArr(0)
#Test.RetWinGenRecArr(0)
#Test.RetSGArrs(0)

#print Generation.WinningArrsOverGenerations.__len__()
#Test.RetWinGenRecArr(0)

#Test.RetAllGenAgents(agentArray)
#Test.RetAllAgents()

