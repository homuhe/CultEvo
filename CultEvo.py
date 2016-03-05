
"""
    Cultural Evolution Simulation

    Team members:   Alla Muench / Andreas Daul / Holger Muth-Hellebrandt

    Course:         Introduction into Python - WS 2016

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  Main Module to run in order to start simulation

"""

import random

import time
import Generation
import Presets as P
import os
import Analysis as stat


random.seed()





class CultEvo(object):

    numOfGenerations = 0

    def writeToFileSimulation(self):
        pass

    def __init__(self,ce_id):

        self.simulationsPath = os.path.dirname(os.path.realpath(__file__)) + "/Simulations/"
        if os.path.isdir(self.simulationsPath):
            pass
        else:
            os.makedirs(self.simulationsPath)

        # Collection of all CultEvo runs
        # something of the form : ..cwd..\Simulations_2016-03-04_[13_23_06]\
        self.simulationPath = self.simulationsPath + "/Sim_{}/".format(ce_id)
        if os.path.isdir(self.simulationPath):
            pass
        else:
            os.makedirs(self.simulationPath)

        # individual simulation run paths(holding all its generation folders):
        self.simRunPath = self.simulationPath + "SimRun_000/"

        if os.listdir(self.simulationPath).__len__() == 0:
            os.makedirs(self.simRunPath)

        else:
            # get the highest index of the already existing folders.
            # ReviewMe: in order to work YOU MUST NOT ALTER THE CONTENT OR NAMES OF THE
            #           FOLDER STRUCTURE MANUALLY IN ANY WAY !!!!!!...!!!!!!!!!!!!

            self.simRunPath = self.simulationPath + "SimRun_{:03}/".format(int(list(os.listdir(self.simulationPath).__reversed__())[0].split("_")[1])+1)
            os.makedirs(self.simRunPath)

        # for Generation folders check in Generation.py



        # Variable determining how many generations we want to allow
        generations = P.generations

        generationRun = Generation.Generation(P.numberAgents,generations,self.simRunPath)

        self.numOfGenerations = generationRun.countGenUp







lstOfGenerationsNumbers = []

# setting up an unique identifier for each simulation
ce_id = time.strftime("%Y-%m-%d_") + time.strftime("[%H_%M_%S]")

for x in range(P.numberOfSimulationRuns):

    global idA
    idA = 0
    runX = CultEvo(ce_id);


    lstOfGenerationsNumbers.append(runX.numOfGenerations)



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
except :
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




