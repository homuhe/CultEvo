__author__ = 'AD'


class Recipe(object):

    score = 0


    def __init__(self,taste,time,ingreds):
        self.taste = taste
        self.time = time
        self.ingreds = ingreds