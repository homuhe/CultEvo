__author__ = 'AD'
'''
    Cultural Evolution Simulation

    Team members:   Alla Muench / Andreas Daul / Holger Muth-Hellebrandt

    Course:         Introduction into Python - WS 2016

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  Module and Class to represent an individual Agents in our simulation
'''


import random
import sys
import itertools    # for permutations on our agent array
import Generation

import recipe_extractor as REx


random.seed()

global idA
idA = 0

class Agent(object):

    inPref = []
    timePref = "none"

    preferences = ["meat","fish","veggi"]

    recipies = []

    #ancestors = []

    def setIDA(self):
        """
        Function to assign each Agent instance a easy to read ID for quick testing purposes

        :return:
        """
        global idA
        self.idA = idA
        idA += 1

    def retIDA(self):
        """
        Read out the easy to read ID provided by Agent.setIDA()
        :return:
        """
        return self.idA

    def retRec(self):

        '''
        :return: The Recipies that this agent uses
        '''

        # ReviewMe : giving back only the 1st one at the moment
        return self.recipies[0]



    def __init__(self, pref,parent):

        # each Agent will eventually be assigned to a social group, we may want to know
        # to which one later on:
        self.sgID = None

        # start with empty list of recipies for each Agent, ReviewMe self.recipies = [] should be correct
        del self.recipies[:]

        # List of IDs of ancestor agents, in order (oldest at [0] - direct parent at [__len__()-1]),
        self.ancestors = []

        # <editor-fold desc="Ancestor-SetUp">
        if ( isinstance(parent,Agent)):
            # Adding the parent element of each Agent of a Generation different than
            # the first Generation to this Agents ancestry
            # ReviewMe: actually using two agents as 'parents', right now we have a very modern single parent society

            self.parent = parent

            if self.parent.ancestors.__len__() == 0 :
                self.ancestors.append(self.parent.idA)
            else:
                self.ancestors += self.parent.ancestors
                self.ancestors.append(self.parent.idA)

        # </editor-fold>


        # check if Agent has a valid preference
        if (isinstance(pref,str) and any(pref in x for x in self.preferences) ):
            self.preference = pref

            self.setIDA()

            # ReviewMe: differentiation between Agents in the 1st Gen and the following ones, just use number of Agents as threshold
            # an 'Original' Agent or not?
            if self.ancestors.__len__() > 0:

                # every agent should get the recipe assigned that was the winner in his parents social group
                # the parent ID is:     self.ancestors[self.ancestors.__len__()-1]] FixMe: ne ist der UR-Ahn, muss anders rum
                # the Agent instance for that ID can be found (in constant time) under:
                #                       Generation.agentsOverGenerations[self.ancestors[self.ancestors.__len__()-1]]

                index_gen = Generation.agentsOverGenerations[self.ancestors[self.ancestors.__len__()-1]].sgID[0]
                index_socLst = Generation.agentsOverGenerations[self.ancestors[self.ancestors.__len__()-1]].sgID[1]
                self.recipies.append(Generation.WinningArrsOverGenerations[index_gen][index_socLst])

            else:
                if self.preference == "meat":
                    self.thelist = REx.recipesMeat
                elif self.preference == "fish":
                    self.thelist = REx.recipesFish
                elif self.preference == "veggi":
                    self.thelist = REx.recipesVeggi

                # only use the main preference to randomly pick recipe
                self.recipies = random.sample(self.thelist,1)
                # determine what time is acceptable for this Agent
                self.timePref = self.recipies[0].prep_time

        else:
            print("Agent.__init__() - error: false parameters at instantiation")




    def __eq__(self,other):
        # test for equality according to our definition
        # question arises: when are two recipes equal = ReviewMe
        if type(self)==type(other):
            if (self.retIDA() == other.retIDA()):
                return True
            else:
                return False
        else:
            return "Agent.__eq__() : Wrong type! Need 'Agent' type to compare."


    def getPref(self):
        return self.preference


    def Mutate(self, recipe, run):
        # ToDo: Mutate() still unfinished
        #

        # method to simulate random changes in recipes: this is meant to consider
        # a bad memory in our individual Agents for example
        if not isinstance(recipe, REx.recipe):
            sys.exit("Agent.Mutate(): argument is not Recipe type! \nProgram ends!")

        # if <run> variable is 1 dont to anything, otherwise let random changes happen
        mutator = random.randrange(30)
        if mutator == 1:
            pass


    def judgeMyRec(self,agentOb):

        # ReviewMe: Balancing of the points assigned to the individual Recipe score
        # if each ingred gets one point we have a bias for recipies with many
        # ingreds (not necessarily a bad thing), but we have to adjust the time too
        # by using margins as discussed, e.g., fast - medium - long and respective points

            if not type(agentOb) is Agent:
                sys.exit("Agent.judgeMyRec() - object not of type Agent")
            else:
                if self.getPref() == agentOb.getPref(): self.retRec().score += 1
                if self.timePref == agentOb.retRec().prep_time: self.retRec().score += 1
                for i in agentOb.retRec().ingredients:
                    if i in  self.retRec().ingredients: self.retRec().score += 1
                # FixMe: Range for number of ingreds

    def setSocGrp(self,genCounter,sgID):
        """
        Sets the ID for this Agents Social Group
        :param genCounter: Generation in which this Agent occurred
        :param sgID: Social Group in which this Agent occurred
        :return: nothing
        """
        self.sgID = [genCounter,sgID]

    def getSocGrp(self):
        return "Gen-{:2} SG-{:2}".format(self.sgID[0],self.sgID[1])