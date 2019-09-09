from groupParams import checkParams
from basicFunctions import average, variance, varianceB
from math import sqrt

def covariance(*stack):
    items = checkParams(stack, 'plural')
    
    X = average(items['Xi'])
    Y = average(items['Yi'])
    
    return items['XiYiFi']/items['Fi'] - X*Y


def correlationCoefficient(*stack):
    items = checkParams(stack, 'plural')
    
    return covariance(items)/(sqrt(varianceB(items['Xi']))*sqrt(varianceB(items['Yi'])))


def regressionLine(value, *stack):
    items = checkParams(stack, 'plural')
    value = {k.lower(): v for k,v in value.items()}
    
    if 'x' in value:
        diff = covariance(items)/varianceB(items['Xi'])
        return diff*value['x']-diff*average(items['Xi'])+average(items['Yi'])
        
    if 'y' in value:
        diff = covariance(items)/varianceB(items['Yi'])
        return diff*value['y']-diff*average(items['Yi'])+average(items['Xi'])