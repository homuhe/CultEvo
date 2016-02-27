__author__ = 'AD'
import sys

class Agent(object):


    def __init__(self,name,rec):
        self.name = name
        self.taste = rec.taste
        self.time = rec.time
        self.rec = rec


    def judgeMyRec(self,agentOb):

        if not type(agentOb) is Agent:
            sys.exit("judgeMyRec - object not of type Agent")
        else:
            if self.taste == agentOb.taste: self.rec.score += 1
            if self.time == agentOb.time: self.rec.score += 1
            for i in agentOb.rec.ingreds:
                if i in  self.rec.ingreds: self.rec.score += 1

    def toString(self):
        print self.name
        print self.taste
        print self.time
        print self.rec.score