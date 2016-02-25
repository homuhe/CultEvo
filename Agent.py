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


import Recipe as REx


random.seed()

global idA
idA = 0

class Agent(object):

    inPref = []
    timePref = "none"

    preferences = ["meat","fish","veggi"]

    recipies = []

    ancestors = []

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

        # ReviseMe : giving back only the 1st one at the moment
        return self.recipies[0]



    def __init__(self, pref,parent):

        # start with empty list of recipies for each Agent
        del self.recipies[:]


        if ( isinstance(parent,Agent)):
            # Adding the parent element of each Agent of a Generation different than
            # the first Generation to this Agents ancestry
            # ReviseMe: actually using two agents as 'parents', right now we have a very modern single parent society

            self.parent = parent
            self.ancestors.append(self.parent.idA)




        # check if Agent has a valid preference
        if (isinstance(pref,str) and any(pref in x for x in self.preferences) ):
            self.preference = pref

            self.setIDA()

            # ToDo: differentiation between Agents in the 1st Gen and the following ones, just use #ofAgents as threshold
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
        # question arises: when are two recipes equal = ReviseMe
        if type(self)==type(other):
            if (self.retIDA() == other.retIDA()):
                return True
            else:
                return False
        else:
            return "Agent.__eq__() : Wrong type! Need 'Agent' type to compare."


    def getPref(self):
        return self.preference

    def mutate(self):
        
        recipe = self.thelist
        actions = ["none", "add", "delete", "substitute"]
        random_number = random.randrange(len(actions))
    
        action = actions[random_number]
    
        if action == "none":
            pass
        elif action == "delete":
            x = random.randrange(recipe.ing_size)
            recipe.ingredients.pop(x)
        elif action == "add":
            x = random.randrange(len(all_ingredients))
            recipe.ingredients.append(all_ingredients[x])
        else:
            x = random.randrange(recipe.ing_size)
            recipe.ingredients.pop(x)
            y = random.randrange(len(all_ingredients))
            recipe.ingredients.append(all_ingredients[y])
    
        #return recipe.ingredients
    
    
    def judgeMyRec(self,agentOb):

        # ReviseMe: Balancing of the points assigned to the individual Recipe score
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


