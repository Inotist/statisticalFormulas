from math import sqrt

class singleStatistic:
    def __init__(self, *stack):
        if len(stack) > 1: self.__values = self.__groupItems(stack)
        elif type(stack[0]) is list or type(stack[0]) is tuple: self.__values = self.__groupItems(stack[0])
        else: self.__values = stack[0]
        
        self.__median = None
        self.__quartile = {}
        self.__percentile = {}
        self.__average = None
        self.__variance = None
        self.__standardDeviation = None
        
    def __groupItems(self, stack):
        dic = {}
        for item in stack:
            if item not in dic: dic[item] = 1
            else: dic[item] += 1
        return dic


    def median(self):
        if self.__median is not None: return self.__median
        
        items = self.__values.copy()
        items, Fi = self.__givePositions(items)
        self.__median = self.__getPosition(items, Fi/2)
        return self.__median


    def quartile(self, Q):
        if Q in self.__quartile.keys(): return self.__quartile[Q]
        
        items = self.__values.copy()
        items, Fi = self.__givePositions(items)
        self.__quartile[Q] = self.__getPosition(items, Q*Fi/4)
        return self.__quartile[Q]
            
            
    def percentile(self, P):
        if P in self.__percentile.keys(): return self.__percentile[P]
        
        items = self.__values.copy()
        items, Fi = self.__givePositions(items)
        self.__percentile[P] = self.__getPosition(items, P*Fi/100)
        return self.__percentile[P]
    
    
    def __givePositions(self, items):
        Fi = 0
        for item in sorted(items.keys()):
            Fi += items[item]
            items[item] = Fi
        return items, Fi

    def __getPosition(self, items, Fi):
        preItem = None
        for item in sorted(items.keys()):
            if preItem != None: return (item + preItem) / 2
            if items[item] > Fi: return item
            elif items[item] == Fi: preItem = item
            
            
    def average(self):
        if self.__average is not None: return self.__average
        
        X = 0
        count = 0
        for value in self.__values.keys():
            X += value * self.__values[value]
            count += self.__values[value]
        self.__average = X / count
        return self.__average


    def variance(self):
        if self.__variance is not None: return self.__variance
        
        count = 0
        count2 = 0
        for value in self.__values.keys():
            count += value**2 * self.__values[value]
            count2 += self.__values[value]
        self.__variance = count / count2 - self.average()**2
        return self.__variance


    def varianceB(self):
        if self.__variance is not None: return self.__variance
        
        count = 0
        count2 = 0
        for value in self.__values.keys():
            count += ((value - self.average())**2)*self.__values[value]
            count2 += self.__values[value]
        self.__variance = count / count2
        return self.__variance
    
    def standardDeviation(self):
        if self.__standardDeviation is not None: return self.__standardDeviation
        
        self.__standardDeviation = sqrt(self.varianceB())
        return self.__standardDeviation