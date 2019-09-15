from math import factorial

####### FUNCTION TO USE #######
def probability(result, origin, **condition):
    if type(origin) is dict: origin = decompose(origin)[0]
    if type(result) is dict: result, calc = decompose(result, origin)
    else: calc = []
    if calc == []: calc = calculation(result, origin)
    
    prob = 1
    for p in calc: prob *= p
    if 'ordered' not in condition or not condition['ordered']: prob *= variations(result)
    if 'negated' in condition and condition['negated']: prob = 1-prob
        
    return prob
###############################

##### USED BY PROBABILITY #####
def decompose(items, origin=None):
    listing = []
    for item in items.keys():
        if items[item] == 0: return probabilityOfNone(items, origin)
        for e in range(items[item]):
            listing.append(item)
            
    return listing, []

def variations(result):
    distinct = []
    amounts = []
    repeated = 1
    for e in result:
        if e not in distinct: distinct.append(e)
    for e in distinct: amounts.append(len([x for x in result if x == e]))
    for i in range(len(amounts)): amounts[i] = factorial(amounts[i])
    for e in amounts: repeated *= e
    
    return factorial(len(result))/repeated

def probabilityOfNone(items, origin):
    nullItems = []
    itemsToGet = []
    for item in items.keys():
        if items[item] == 0:
            nullItems.append(item)
        else:
            for e in range(items[item]):
                itemsToGet.append(item)
                
    calc = calculation(itemsToGet, origin, nullItems)
    
    for e in nullItems: items.pop(e)
    return decompose(items)[0], calc

def calculation(itemsToGet, origin, nullItems=[]):
    calc = []
    for e in itemsToGet:
        if e in origin:
            calc.append(len([x for x in origin if x == e])/len(origin))
            origin.remove(e)
        elif e == 'other':
            if len(origin) == 0: return [0]
            calc.append(len([x for x in origin if x not in itemsToGet and x not in nullItems])/len(origin))
            for x in origin:
                if x not in itemsToGet and x not in nullItems:
                    origin.remove(x)
                    break
        else: return [0]
            
    return calc