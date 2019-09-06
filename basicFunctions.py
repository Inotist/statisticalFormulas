from math import sqrt

def groupItems(*stack):
    if type(stack[0]) is list or type(stack[0]) is tuple:
        items = sorted([item for item in stack[0]])
    else: items = sorted([item for item in stack])
    dic = {}
    for item in range(len(items)):
        if item is 0: dic[items[item]] = 1
        elif items[item] == items[item-1]: dic[items[item]] += 1
        else: dic[items[item]] = 1
        
    return dic


def median(*items):
    items = checkParams(items)
    
    items = items.copy()
    Fi = 0
    for item in items.keys():
        Fi += items[item]
        items[item] = Fi
        
    Fi /= 2
    preItem = None
    for item in items.keys():
        if preItem != None: return (item + preItem) / 2
        if items[item] > Fi: return item
        elif items[item] == Fi: preItem = item


def quartile(Q, *items):
    items = checkParams(items)
    
    items = items.copy()
    Fi = 0
    for item in items.keys():
        Fi += items[item]
        items[item] = Fi
        
    Fi *= Q/4
    preItem = None
    for item in items.keys():
        if preItem != None: return (item + preItem) / 2
        if items[item] > Fi: return item
        elif items[item] == Fi: preItem = item
        
        
def percentile(P, *items):
    items = checkParams(items)
    
    items = items.copy()
    Fi = 0
    for item in items.keys():
        Fi += items[item]
        items[item] = Fi
        
    Fi *= P/100
    preItem = None
    for item in items.keys():
        if preItem != None: return (item + preItem) / 2
        if items[item] > Fi: return item
        elif items[item] == Fi: preItem = item
        
        
def average(*items):
    items = checkParams(items)
    
    X = 0
    count = 0
    for item in items.keys():
        X += item * items[item]
        count += items[item]
    return X / count


def variance(*items):
    items = checkParams(items)
    
    count = 0
    count2 = 0
    for item in items.keys():
        count += item**2 * items[item]
        count2 += items[item]
    return count / count2 - average(items)**2


def varianceB(*items):
    items = checkParams(items)
    
    count = 0
    count2 = 0
    mean = average(items)
    for item in items.keys():
        count += ((item - mean)**2)*items[item]
        count2 += items[item]
    return count / count2


def checkParams(stack):
    if len(stack) > 1: stack = groupItems(stack)
    elif type(stack[0]) is list or type(stack[0]) is tuple: stack = groupItems(stack[0])
    else: stack = stack[0]
    return stack