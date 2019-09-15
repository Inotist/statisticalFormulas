from singleStatisticalObject import singleStatistic

class pluralStatistic:
    def __init__(self, *stack):
        if len(stack) > 1: stack = self.__groupItems(stack)
        elif type(stack[0]) is list or type(stack[0]) is tuple: stack = self.__groupItems(stack[0])
        else: stack = stack[0]
        
        self.__Xi = singleStatistic(stack['Xi'])
        self.__Yi = singleStatistic(stack['Yi'])
        self.__XiYiFi = stack['XiYiFi']
        self.__Fi = stack['Fi']
        self.__covariance = None
        self.__correlationCoefficient = None
        
    def Xi(self):
        return self.__Xi
    def Yi(self):
        return self.__Yi
        
    def __groupItems(self, stack):
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
    
    
    def covariance(self):
        if self.__covariance is not None: return self.__covariance
        
        self.__covariance = self.__XiYiFi/self.__Fi - self.__Xi.average()*self.__Yi.average()
        return self.__covariance


    def correlationCoefficient(self):
        if self.__correlationCoefficient is not None: return self.__correlationCoefficient
        
        self.__correlationCoefficient = self.covariance()/(self.__Xi.standardDeviation()*self.__Yi.standardDeviation())
        return self.__correlationCoefficient


    def regressionLine(self, **value):
        value = {k.lower(): v for k,v in value.items()}
        
        if 'x' in value:
            diff = self.covariance()/self.__Xi.varianceB()
            return diff*value['x']-diff*self.__Xi.average()+self.__Yi.average()
            
        if 'y' in value:
            diff = self.covariance()/self.__Yi.varianceB()
            return diff*value['y']-diff*self.__Yi.average()+self.__Xi.average()