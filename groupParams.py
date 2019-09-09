def groupItems(*stack):
    if type(stack[0]) is list or type(stack[0]) is tuple: stack = stack[0]
    
    dic = {}
    for item in stack:
        if item not in dic: dic[item] = 1
        else: dic[item] += 1
        
    return dic


def groupPairs(*stack):
    if type(stack[0][0]) is list or type(stack[0][0]) is tuple: stack = stack[0]
    
    Xi = {}
    Yi = {}
    XiYiFi = 0
    Fi = 0
    for pair in range(len(stack)):
        x = stack[pair][0]
        y = stack[pair][1]
        if len(stack[0]) == 3: f = stack[pair][2]
        else: f = 1
            
        if x not in Xi.keys(): Xi[x] = f
        else: Xi[x] += f
            
        if y not in Yi.keys(): Yi[y] = f
        else: Yi[y] += f
            
        XiYiFi += x*y*f
        Fi += f
        
    return {'Xi': Xi, 'Yi': Yi, 'XiYiFi': XiYiFi, 'Fi': Fi}


def checkParams(stack, form='single'):
    if len(stack) > 1:
        if form == 'single': stack = groupItems(stack)
        elif form == 'plural': stack = groupPairs(stack)
    elif type(stack[0]) is list or type(stack[0]) is tuple:
        if form == 'single': stack = groupItems(stack[0])
        elif form == 'plural': stack = groupPairs(stack[0])
    else: stack = stack[0]
    return stack