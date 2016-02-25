__author__ = 'AD'
'''
    Cultural Evolution Simulation

    Team members:   Alla Muench / Andreas Daul / Holger Muth-Hellebrandt

    Course:         Introduction into Python - WS 2016

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  Presets for values, variables and environmental rules that can be fine-tuned by the user
'''


# ========================================
# Amount of Agents per Generation
numberAgents = 9

# Percentages of our main recipe classes
facMeat =  3
facFish =  3
facVeggi = 3


# ====================================================
# Maximum size of social groups/ groups of 'friends'
maxSocSize = 5


# =================================================================================================
# Thresholds for what is considered a long/medium/short recipe ingredient list/ preparation time

timeDic = {"short":"0:25","medium":"1:00"}  # more than 1:00 implicates long
recDic = {"short":5,"medium":10}            # more than 10 elements implicates a long list