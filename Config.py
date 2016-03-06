"""
    Cultural Evolution Simulation

    Team members:   Alla Muench / Andreas Daul / Holger Muth-Hellebrandt

    Course:         Introduction into Python - WS 2016

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  Config module holding all lists, dictionaries and in general variables
                    that are shared by different modules

"""


# <editor-fold desc=" Shared lists and dictionaries over modules ">

idA = 0

# All Agents ever created, one consecutive list
agentsOverGenerations = []

# same as above just as a dictionary
# {int_index : [Agent List for the Generation specified by int_index]}
agentsOverAllDict = {}

# a dictionary holding all the recipies for each Generation in an array
# RecListOverGenerations{"int_Index : Recipe"}
RecListOverGenerations = {}

# all the winning recipes in a dictionary
WinningArrsOverGenerations = {}

# The name says it all, Dictionary holding the social groups for each Generation
SocialGroups = {}

# </editor-fold>

def Config_Reset():
    global SocialGroups
    SocialGroups = {}
    global WinningArrsOverGenerations
    WinningArrsOverGenerations = {}
    global RecListOverGenerations
    RecListOverGenerations = {}
    global agentsOverAllDict
    agentsOverAllDict = {}
    global agentsOverGenerations
    agentsOverGenerations = []
    global idA
    idA = 0