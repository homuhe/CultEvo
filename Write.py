import time


# write general data about this generation to a file

class WriteGen(object):
    """
    Writing a textual class representation of this Generation to a file
    """

    def __init__(self,genPath,countGenUp,agentArr,SGArrs,winGenRecArr,WinningArrsOverGenerations,agentsOverAllDict,agentsOverGenerations):

        f = open(genPath+"Gen_and_SocGrps_{:03}.txt".format(countGenUp),'w')
        f.write("\n")
        f.write("Cultural Evolution Simulation:\n")
        f.write("==============================\n")
        f.write("\n")
        f.write("Author: AAH\n")
        f.write("Date  : {}\n".format(time.strftime("%Y-%m-%d at ") + time.strftime("[%H:%M:%S]")))
        f.write("\n")
        f.write("\n")
        f.write("Generation Overview\n")
        f.write("===================\n")
        f.write("\n")
        f.write("\n")
        f.write("Number of Agents       : {:03}\n".format(agentArr.__len__()))
        f.write("Number of Social Groups: {:03}\n".format(SGArrs.__len__()))
        f.write("Number of Meat eaters  : {:03}\n".format(1))
        f.write("Number of Fish eaters  : {:03}\n".format(1))
        f.write("Number of Vegetarians  : {:03}\n".format(1))
        f.write("\n")
        f.write("\n")
        f.write("Social Groups:\n")
        f.write("--------------\n")
        for sg in SGArrs:
            f.write("SG Number: {:02}\n".format(SGArrs.index(sg)))
            for agnt in sg:
                f.write("   Agent         : {:03}\n".format(agnt.getIDA()))
            f.write("   Winning recipe: {}\n".format(winGenRecArr[SGArrs.index(sg)].title))
            f.write("\n")

        f.write("Sum of all agents so far            : {}\n".format(agentsOverGenerations.__len__()))
        f.write("size of agentsOverAllDict           : {}\n".format(agentsOverAllDict.__len__()))
        f.write("and in the current generation:\n")
        for agnt in agentsOverAllDict[countGenUp]:
            f.write("   Agent {}\n".format(agnt.getIDA()))
        f.write("size of WinningArrsOverGenerations  : {}\n".format(WinningArrsOverGenerations.__len__()))
        f.write("All recipes contained: \n")
        for reclst in WinningArrsOverGenerations:
            f.write("------   ------   ------\n")
            for rec in WinningArrsOverGenerations[reclst]:
                f.write("   RecName: {}\n".format(rec.title))
        f.close()



class WriteAgent(object):
    """
    Writing a textual class representation of this Agent to a file
    """

    def __init__(self,genPath,agnt):
        f = open(genPath+"Agent_{:03}.txt".format(agnt.getIDA()),'w')
        f.write("\n")
        f.write("Cultural Evolution Simulation:\n")
        f.write("==============================\n")
        f.write("\n")
        f.write("Author: AAH\n")
        f.write("Date  : {}\n".format(time.strftime("%Y-%m-%d at ") + time.strftime("[%H:%M:%S]")))
        f.write("\n")
        f.write("\n")
        f.write("Agent Overview\n")
        f.write("==============\n")
        f.write("\n")
        f.write("ID         : {:>6}\n".format(agnt.getIDA()))
        f.write("Preference:: {:>6}\n".format(agnt.preference))
        f.write("\n")
        f.write("Recipe     : {}\n".format(agnt.getRec().title))
        f.close()



