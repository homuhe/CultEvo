
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
import Presets as P
import exceptions
import statistics as stat


random.seed()






class CultEvo(object):

    numOfGenerations = 0

    def __init__(self):
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

        # for gen in range(Generation.SocialGroups.__len__()):
        #    print "Generation: " + str(gen)
        #    print()
        #    Test.RetSGArrsRec(gen)

        # print
        # print " =============================================== "
        # print " |                                             |"
        # print " | Recipes all similar after {:3} Generations!  |".format(agentGen.countGenUp)
        # print " |                                             |"
        # print " =============================================== "

        #print Generation.WinningArrsOverGenerations.__len__()
        #Test.RetWinGenRecArr(0)

        #Test.RetAllGenAgents(agentArray)
        #Test.RetAllAgents()

        self.numOfGenerations = agentGen.countGenUp





lstOfGenerationsNumbers = []

for x in range(P.numberOfSimulationRuns):
    runX = CultEvo();
    #runX
    lstOfGenerationsNumbers.append(runX.numOfGenerations)
    #print lstOfGenerationsNumbers.__len__()
    #print lstOfGenerationsNumbers

#for index,num in enumerate(lstOfGenerationsNumbers):
#    print"Simulation {:3} needed {:3} Generations for complete degradation! ".format(index+1,num)

print
print " ====================================================== "
print "||                                                    ||"
print "||   Statistical Properties of this simulation run    ||"
print "||                                                    ||"
print " ====================================================== "
print
print
print "Number of Agents                 : {:>5}".format(P.numberAgents)
print "Maximum size of social groups    : {:>5}".format(P.maxSocSize)
print "Maximum number of Generations    : {:>5}".format(P.generations)
print "Number of individual CultEvo runs: {:>5}".format(P.numberOfSimulationRuns)
print
print
print
print "Values:"
print "======="
print
print "Averages and measures of central location"
print "........................................."
print
print "mean        : {:>6.2f}".format(stat.mean(lstOfGenerationsNumbers))
print "median      : {:>6.2f}".format(stat.median(lstOfGenerationsNumbers))
print "mean_low    : {:>6.2f}".format(stat.median_low(lstOfGenerationsNumbers))
print "mean_high   : {:>6.2f}".format(stat.median_high(lstOfGenerationsNumbers))
print "mean_grouped: {:>6.2f}".format(stat.median_grouped(lstOfGenerationsNumbers))
try:
    print "mode        : {:>6.2f}".format(stat.mode(lstOfGenerationsNumbers) )
except exceptions.StatisticsError:
    print "mode        : two equal values found"
print
print
print
print "Measures of spread"
print ".................."
print
print "Population standard deviation of data: {0:>6.2f}".format(stat.pstdev(lstOfGenerationsNumbers))
print "Population variance of data          : {0:>6.2f}".format(stat.pvariance(lstOfGenerationsNumbers))
print "Sample standard deviation of data    : {0:>6.2f}".format(stat.stdev(lstOfGenerationsNumbers))
print "Sample variance of data              : {0:>6.2f}".format(stat.variance(lstOfGenerationsNumbers))




