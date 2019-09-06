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
    if len(items) > 1: items = groupItems(items)
    elif type(items[0]) is list or type(items[0]) is tuple: items = groupItems(items[0])
    else: items = items[0]
    
    items = items.copy()
    Fi = 0
    for item in items.keys():
        Fi += items[item]
        items[item] = Fi
        
    Fi /= 2
    preItem = 0
    for item in items.keys():
        if preItem != 0: return (item + preItem) / 2
        if items[item] > Fi: return item
        elif items[item] == Fi: preItem = item


def quartile(Q, *items):
    if len(items) > 1: items = groupItems(items)
    elif type(items[0]) is list or type(items[0]) is tuple: items = groupItems(items[0])
    else: items = items[0]
    
    items = items.copy()
    Fi = 0
    for item in items.keys():
        Fi += items[item]
        items[item] = Fi
        
    Fi *= Q/4
    preItem = 0
    for item in items.keys():
        if preItem != 0: return (item + preItem) / 2
        if items[item] > Fi: return item
        elif items[item] == Fi: preItem = item
        
        
def percentile(P, *items):
    if len(items) > 1: items = groupItems(items)
    elif type(items[0]) is list or type(items[0]) is tuple: items = groupItems(items[0])
    else: items = items[0]
    
    items = items.copy()
    Fi = 0
    for item in items.keys():
        Fi += items[item]
        items[item] = Fi
        
    Fi *= P/100
    preItem = 0
    for item in items.keys():
        if preItem != 0: return (item + preItem) / 2
        if items[item] > Fi: return item
        elif items[item] == Fi: preItem = item
        
        
def average(*items):
    if len(items) > 1: items = groupItems(items)
    elif type(items[0]) is list or type(items[0]) is tuple: items = groupItems(items[0])
    else: items = items[0]
    
    X = 0
    count = 0
    for item in items.keys():
        X += item * items[item]
        count += items[item]
    return X / count


def variance(*items):
    if len(items) > 1: items = groupItems(items)
    elif type(items[0]) is list or type(items[0]) is tuple: items = groupItems(items[0])
    else: items = items[0]
    
    count = 0
    count2 = 0
    for item in items.keys():
        count += item**2 * items[item]
        count2 += items[item]
    return count / count2 - average(items)**2


def varianceB(*items):
    if len(items) > 1: items = groupItems(items)
    elif type(items[0]) is list or type(items[0]) is tuple: items = groupItems(items[0])
    else: items = items[0]
    
    count = 0
    count2 = 0
    mean = average(items)
    for item in items.keys():
        count += ((item - mean)**2)*items[item]
        count2 += items[item]
    return count / count2