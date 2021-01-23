import math
def calculateStats(numbers):
    computedStats={}
    if len(numbers) == 0:
        computedStats["avg"]=computedStats["max"]=computedStats["min"]=math.nan
    else:
        computedStats["avg"]=sum(numbers)/len(numbers)
        computedStats["max"]=max(numbers)
        computedStats["min"]=min(numbers)
    return computedStats

