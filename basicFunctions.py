from groupParams import checkParams
from math import sqrt

def givePositions(items):
    Fi = 0
    for item in sorted(items.keys()):
        Fi += items[item]
        items[item] = Fi
    return items, Fi

def getPosition(items, Fi):
    preItem = None
    for item in sorted(items.keys()):
        if preItem != None: return (item + preItem) / 2
        if items[item] > Fi: return item
        elif items[item] == Fi: preItem = item


def median(*items):
    items = checkParams(items, 'single')
    
    items = items.copy()
    items, Fi = givePositions(items)
    return getPosition(items, Fi/2)


def quartile(Q, *items):
    items = checkParams(items, 'single')
    
    items = items.copy()
    items, Fi = givePositions(items)
    return getPosition(items, Q*Fi/4)
        
        
def percentile(P, *items):
    items = checkParams(items, 'single')
    
    items = items.copy()
    items, Fi = givePositions(items)
    return getPosition(items, P*Fi/100)
        
        
def average(*items):
    items = checkParams(items, 'single')
    
    X = 0
    count = 0
    for item in items.keys():
        X += item * items[item]
        count += items[item]
    return X / count


def variance(*items):
    items = checkParams(items, 'single')
    
    count = 0
    count2 = 0
    for item in items.keys():
        count += item**2 * items[item]
        count2 += items[item]
    return count / count2 - average(items)**2


def varianceB(*items):
    items = checkParams(items, 'single')
    
    count = 0
    count2 = 0
    mean = average(items)
    for item in items.keys():
        count += ((item - mean)**2)*items[item]
        count2 += items[item]
    return count / count2