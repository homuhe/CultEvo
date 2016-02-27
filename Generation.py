__author__ = 'AD'

import random
import sys

import Agent
import recipe_extractor as REx
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
    """
     Find winning recipies for a generation determined by 'counter'
    :param counter: The index determining the desired generation
    :return: List of all 'Recipies' that won in their respective social group
    """

    winLst = [REx.recipe("", "", "", [])]

    # social groups of the Generation determined by 'counter'
    scGrps = SocialGroups[counter]
    cnta = 0
    for agntGrp in scGrps:

        cntb = cnta + 1
        if agntGrp.__len__() > 1:
            for agnt in agntGrp:

                if winLst.__len__() < cntb:
                    winLst.append(agnt.retRec())
                else:
                    # if we have the same score we go for first come first serve
                    if winLst[cnta].score < agnt.retRec().score:
                        winLst[cnta] = agnt.retRec()
        elif isinstance(agntGrp[0],Agent.Agent):
            winLst.append(agntGrp[0].retRec())
        else:
            sys.exit("Generation.DetSGArrayWinners(): Could not determine winning recipies!")
        cnta += 1
    return winLst


class Generation(object):

    # ======================================
    #
    #    Infos regarding Lists and Dicts
    #
    # ======================================
    # All Agents ever created, one consecutive list
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

    # List holding the Recipies that got the highest score in each social
    # group and were passed on

    winGenRecArr = []


    # The name says it all, Dictionary holding the social groups for each Generation
    SocialGroups = {}
    SGArrs = []

    # ReviewMe: Number of modifications per Agents and recipe
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

            # ===================================
            #           MAIN 'IF' BRANCH
            # - Running through the Generations -
            # ===================================


            if self.countGenUp == 0:

                # ====================================
                #
                #           FIRST GENERATION
                # -            base case             -
                # ====================================


                # <editor-fold desc="1st Generation SetUp">

                # assigning the arrays only for the first Generation
                self.SGArrs = []
                SocialGroups[self.countGenUp] = self.SGArrs

                self.genRecArr = []
                RecListOverGenerations[self.countGenUp] = self.genRecArr

                self.winGenRecArr = []
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
                #print()
                #print "  --- --- --- "
                #print "Agents in Generation: {:3}".format(self.countGenUp)
                for pref in weightedPreferences:
                    self.agnt = Agent.Agent(pref, None)
                #    print "self.agnt idA = {:3} ||  Ancestors = {:3}".format(self.agnt.idA,self.agnt.ancestors)
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

                # ReviewMe: Interactions
                # <editor-fold desc="SocGroups and Interactions">

                self.gen1 = self.agentArr[:]

                while self.gen1.__len__() != 0:

                    # AmDone: we need a way to adjust our upper bound for the random sampling
                    # so that we dont want to sample 10 items when our array only consists of
                    # ,e.g., 9 or less elements

                    if self.gen1.__len__() >= self.maxSocSize:

                        try:
                            self.friendArr = random.sample(self.gen1, random.randrange(2, self.maxSocSize))

                            self.SGArrs.append(self.friendArr[:])

                            # popping the Agents out of the tmp collection so we dont draw them twice
                            for friendx in self.friendArr:
                                self.gen1.remove(friendx)

                            # right now we have set up a social environment

                            if self.friendArr.__len__() > 0:
                                for me in self.friendArr:
                                    # AmDone: remember that you belong to this social group
                                    me.setSocGrp(self.countGenUp,self.SGArrs.__len__())
                                    # dont judge your own recipe
                                    self.tmpArr = self.friendArr[:]
                                    self.tmpArr.remove(me)
                                    for friend in self.tmpArr:
                                        me.judgeMyRec(friend)

                            #else:
                            #    pass
                        except ValueError:
                            print ("Could not create social environment of large size!")


                    # only little amount of Agents left in the array
                    elif self.gen1.__len__() >= 2:

                        try:
                            self.friendArr = random.sample(self.gen1, 2)
                            self.SGArrs.append(self.friendArr[:])

                            for x in self.friendArr:
                                self.gen1.remove(x)
                            # right now, at this point, we should have set up a social environment

                            if self.friendArr.__len__() > 0:
                                for individual in self.friendArr:
                                    #AmDone: also soc group assignment
                                    individual.setSocGrp(self.countGenUp,self.SGArrs.__len__())
                                    # dont judge your own recipe
                                    self.tmpArr = self.friendArr[:]
                                    self.tmpArr.remove(individual)
                                    for friend in self.tmpArr:
                                        individual.judgeMyRec(friend)

                        except ValueError:
                            print ("Could not create social environment of small size!")


                    else:
                        # again, dont judge your own again, only keep track of lonely singles in the social statistics
                        # ReviewMe: Careful now: we pass on a single agent as a LIST with one entry: DO NOT MIX THAT UP!
                        self.SGArrs.append([self.gen1[0]])
                        self.gen1[0].setSocGrp(self.countGenUp,self.SGArrs.__len__())
                        self.gen1.pop()

                        # We have created the first generation now, instantiated Agents,
                        # given them recipies,
                        # and judged the recipies by the individual Agent and the peers
                        # in his randomly selected social group (ReviewMe: social group size as GUI element)
                        # ReviewMe: we could go for a copy by reference approach with the sgID as well instead
                        # saving a little bit of memory, but the code isnt optimised anyway, so just take a note


                # </editor-fold>
                ###
                # print self.winGenRecArr.__len__()
                self.winGenRecArr = DetSGArrayWinners(self.countGenUp)

                WinningArrsOverGenerations[self.countGenUp] = self.winGenRecArr
               # print self.winGenRecArr.__len__()

            elif self.countGenUp > 0:

                # ============================================
                #
                #           HIGHER ORDER GENERATIONS
                #  ToDo: individual higher Order Generations
                # ============================================


                # <editor-fold desc="Higher Order Generation SetUp">
                self.SGArrs = []
                SocialGroups[self.countGenUp] = self.SGArrs

                self.genRecArr = []
                RecListOverGenerations[self.countGenUp] = self.genRecArr

                self.winGenRecArr = []
                WinningArrsOverGenerations[self.countGenUp] = self.winGenRecArr

                self.agentArr = []
                agentsOverAllDict[self.countGenUp] = self.agentArr

                # populating the array with Agent instances as offsprings of our
                # predecessor generation
                #print()
                #print "  --- --- --- "
                #print "Agents in Generation: {:3}".format(self.countGenUp)
                for x in agentsOverAllDict[self.countGenUp-1]:
                    self.agnt = Agent.Agent(x.preference, x)
                    #print
                    #print "self.agnt idA = {:3} ||  x.idA = {:3}".format(self.agnt.idA,x.idA)
                    #print "Py ID self.agnt.ancestors: {:10}  || Py ID x.ancestors: {:10}".format(id(self.agnt.ancestors),id(x.ancestors))
                    #print "own ancestors: {:25}".format(self.agnt.ancestors)
                    #print "x's ancestors: {:25}".format(x.ancestors)
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

                # ToDo : Higher Order Generation interactions
                # ReviewMe : outsorce the whole code block, its getting harder and harder to read, even with folding
                # FixMe : assign the sgID !!!
                # <editor-fold desc="Higher Order Generation interactions">
                self.gen1 = self.agentArr[:]

                while self.gen1.__len__() != 0:

                    # AmDone: we need a way to adjust our upper bound for the random sampling
                    # so that we dont want to sample 10 items when our array only consists of
                    # ,e.g., 9 or less elements

                    if self.gen1.__len__() >= self.maxSocSize:

                        try:
                            self.friendArr = random.sample(self.gen1, random.randrange(2, self.maxSocSize))

                            self.SGArrs.append(self.friendArr[:])

                            # popping the Agents out of the tmp collection so we dont draw them twice
                            for friendx in self.friendArr:
                                self.gen1.remove(friendx)

                            # right now we have set up a social environment

                            if self.friendArr.__len__() > 0:
                                for me in self.friendArr:
                                    # AmDone: remember that you belong to this social group
                                    me.setSocGrp(self.countGenUp,self.SGArrs.__len__())
                                    # dont judge your own recipe
                                    self.tmpArr = self.friendArr[:]
                                    self.tmpArr.remove(me)
                                    for friend in self.tmpArr:
                                        me.judgeMyRec(friend)

                            #else:
                            #    pass
                        except ValueError:
                            print ("Could not create social environment of large size!")


                    # only little amount of Agents left in the array
                    elif self.gen1.__len__() >= 2:

                        try:
                            self.friendArr = random.sample(self.gen1, 2)
                            self.SGArrs.append(self.friendArr[:])

                            for x in self.friendArr:
                                self.gen1.remove(x)
                            # right now, at this point, we should have set up a social environment

                            if self.friendArr.__len__() > 0:
                                for individual in self.friendArr:
                                    #AmDone: also soc group assignment
                                    individual.setSocGrp(self.countGenUp,self.SGArrs.__len__())
                                    # dont judge your own recipe
                                    self.tmpArr = self.friendArr[:]
                                    self.tmpArr.remove(individual)
                                    for friend in self.tmpArr:
                                        individual.judgeMyRec(friend)

                        except ValueError:
                            print ("Could not create social environment of small size!")
                # </editor-fold>

                # print self.winGenRecArr.__len__()
                self.winGenRecArr = DetSGArrayWinners(self.countGenUp)

                WinningArrsOverGenerations[self.countGenUp] = self.winGenRecArr
               # print self.winGenRecArr.__len__()






            # AmDone: make sure this is working as it is supposed to!
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


