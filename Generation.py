__author__ = 'AD'

import random
import sys

import Agent
import Recipe as REx
import Presets as P

global agentsOverGenerations
agentsOverGenerations = []
global RecListOverGenerations
RecListOverGenerations = {}
global agentsOverAllDict
agentsOverAllDict = {}
global WinningArrsOverGenerations
WinningArrsOverGenerations = {}
global SocialGroups
SocialGroups = {}


def DetSGArrayWinners(counter):
    # find winning recipies for a generation determined by 'counter'

    winLst = [REx.recipe("", "", "", [])]

    # social groups of the Generation determined by 'counter'
    scGrps = SocialGroups[counter]
    cnta = 0
    for agntGrp in scGrps:

        cntb = cnta + 1
        for agnt in agntGrp:

            if winLst.__len__() < cntb:
                winLst.append(agnt.retRec())
            else:
                # if we have the same score we go for first come first serve
                if winLst[cnta].score < agnt.retRec().score:
                    winLst[cnta] = agnt.retRec()
        cnta += 1
    return winLst


class Generation(object):

    # ======================================
    #
    #    Infos regarding Lists and Dicts
    #
    # ======================================
    # All Agents ever created
    agentsOverGenerations = []

    # same as above just as a dictionary
    # {int_index : [Agent List for the Generation specified by int_index]}
    agentsOverAllDict = {}

    # array with Agents of one Generation
    agentArr = []

    # a dictionary holding all the recipies for each Generation in an array
    # RecListOverGenerations{"int_Index : Recipe"}

    RecListOverGenerations = {}
    # the Array holding the recipies for an individual Generation
    genRecArr = []

    # Dict holding the Recipies that got the highest score in each social
    # group and were passed on



    winGenRecArr = []
    # The name says it all, Dictionary holding the social groups for each Generation
    SocialGroups = {}
    SGArrs = []

    # ReviseMe: Number of modifications per Agents and recipe
    # cntMod = 1

    def __init__(self, numberAgents, counterGen):
        #   ===================================
        #    Initialisation of the GENERATIONS
        #   ===================================

        self.counterGen = counterGen

        self.countGenUp = 0

        # maximum size of social group
        self.maxSocSize = P.maxSocSize



        while self.countGenUp < self.counterGen:

            # ===========================
            #       MAIN 'IF' BRANCH
            # ===========================

            if self.countGenUp > 0:

                # ================================
                #  ToDo: higher Order Generations
                # ================================

                # <editor-fold desc="GenSetUp">

                # assigning the arrays only for the first Generation
                SocialGroups[self.countGenUp] = self.SGArrs

                RecListOverGenerations[self.counterGen] = self.genRecArr

                WinningArrsOverGenerations[self.counterGen] = self.winGenRecArr

                self.agentArr = []
                agentsOverAllDict[self.countGenUp] = self.agentArr

                # populating the array with Agent instances as offsprings of our
                # predecessor generation

                for x in agentsOverAllDict[self.countGenUp-1]:
                    self.agnt = Agent.Agent(x.preference, x)
                    # You get to judge your own culinary oeuvre
                    self.agnt.judgeMyRec(self.agnt)
                    # after creating an agent we store his/her Recipe in genRecArr
                    self.genRecArr.append(self.agnt.retRec())
                    self.agentArr.append(self.agnt)
                    agentsOverGenerations.append(self.agnt)

                # if we want to let them interact we need to shuffle the array so that the instances are
                # randomly distributed
                random.shuffle(self.agentArr)
                # Tests.CntTest(agentsOverGenerations)
                # </editor-fold>

                # FixMe: take pass out and complete me
                #pass
            elif self.countGenUp == 0:

                # ============================================
                #
                #        FIRST GENERATION base case
                #
                #=============================================


                # <editor-fold desc="GenSetUp">

                # assigning the arrays only for the first Generation
                SocialGroups[self.countGenUp] = self.SGArrs

                RecListOverGenerations[self.countGenUp] = self.genRecArr

                WinningArrsOverGenerations[self.countGenUp] = self.winGenRecArr


                self.agentArr = []
                agentsOverAllDict[self.countGenUp] = self.agentArr

                # Setting up a weighted distribution of preferences so that we can determine what flavor might be
                # the predominant one; integers obviously need to add up to 100



                weightedPreferences = ["meat"] * P.facMeat + ["fish"] * P.facFish + ["veggi"] * P.facVeggi

                # Check if percentages add up to 100%
                if weightedPreferences.__len__() != numberAgents:
                    sys.exit(
                        "Generations.__init__(): Preference percentages don't add up too 100%, please check! \nProgram ends!")

                # populating the array with Agent instances

                for x in weightedPreferences:
                    self.agnt = Agent.Agent(x, None)
                    self.agnt.judgeMyRec(self.agnt)
                    # after creating an agent we store his/her Recipe in genRecArr
                    self.genRecArr.append(self.agnt.retRec())
                    self.agentArr.append(self.agnt)
                    agentsOverGenerations.append(self.agnt)

                # if we want to let them interact we need to shuffle the array so that the instances are
                # randomly distributed
                random.shuffle(self.agentArr)

                # Tests.CntTest(agentsOverGenerations)
                # </editor-fold>

                # ReviseMe: Interactions

                self.gen1 = self.agentArr[:]

                while self.gen1.__len__() != 0:

                    # AmDone: we need a way to adjust our upper bound for the random sampling
                    # so that we dont want to sample 10 items when our array only consists of
                    # ,e.g., 9 or less elements
                    # <editor-fold desc="SocArrs">
                    if self.gen1.__len__() >= self.maxSocSize:
                        # <editor-fold desc="RandomSocArr">
                        try:
                            self.friendArr = random.sample(self.gen1, random.randrange(2, self.maxSocSize))

                            self.SGArrs.append(self.friendArr[:])

                            # popping the Agents out of the tmp collection so we dont draw them twice
                            for friendx in self.friendArr:
                                self.gen1.remove(friendx)

                            # right now we have set up a social environment

                            if self.friendArr.__len__() > 1:
                                for me in self.friendArr:
                                    # dont judge your own recipe
                                    self.tmpArr = self.friendArr[:]
                                    self.tmpArr.remove(me)
                                    for friend in self.tmpArr:
                                        me.judgeMyRec(friend)

                            else:
                                pass
                        except ValueError:
                            print ("Could not create social environment of large size!")
                            # </editor-fold>

                    # only little amount of Agents left in the array
                    elif self.gen1.__len__() >= 2:

                        try:
                            self.friendArr = random.sample(self.gen1, 2)
                            self.SGArrs.append(self.friendArr[:])

                            for x in self.friendArr:
                                self.gen1.remove(x)
                            # right now we have set up a social environment

                            if self.friendArr.__len__() > 1:
                                for individual in self.friendArr:
                                    # dont judge your own recipe
                                    self.tmpArr = self.friendArr[:]
                                    self.tmpArr.remove(individual)
                                    for friend in self.tmpArr:
                                        individual.judgeMyRec(friend)

                        except ValueError:
                            print ("Could not create social environment of small size!")
                    # </editor-fold>

                    else:  # again, dont judge your own again

                        self.gen1.pop()

                        # We have created the first generation now, instantiated Agents,
                        # given them recipies,
                        # and judged the recipies by the individual Agent and the peers
                        # in his randomly selected social group (ReviseMe: social group size as GUI element)


                ###
               # print self.winGenRecArr.__len__()
                self.winGenRecArr = DetSGArrayWinners(self.countGenUp)

                WinningArrsOverGenerations[self.countGenUp] = self.winGenRecArr
               # print self.winGenRecArr.__len__()


            # ReviseMe: make sure this is working as it is supposed to!
            self.countGenUp += 1



    def getAgentArr(self):
        '''
        The Array containing the Agent instances that
        belong to the current Generation.
        :return: Array of all Agents of one Generation
        '''
        return self.agentArr

    def getAllAgents(self):
        '''
         An Array with ALL Agents ever instantiated up to the point of calling
         so that we can take a look at the individual agent instances and their
         Recipies after the simulation is done
        :return: Array with ALL Agents over all Generations
        '''
        return agentsOverGenerations
