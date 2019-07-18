class Calculator:
    def __init__(self, data):
        import math
        self.data = data
        self.length = len(data) #self.data
        self.__update_stats()
    
    def __update_stats(self):  
        self.mean = self.calc_mean()
        self.median = self.calc_median()
        self.variance = self.calc_var()
        self.standev = self.calc_std()
        
    def calc_mean(self):
        n = self.length
        total = sum(self.data)
        return total/n
    
    def calc_median(self):
        self.data.sort()
        n = int(self.length)
        # if the list of numbers has odd numbers
        median = self.data[round(n/2)]
        # if the list has an even number
        if n % 2 == 0:
            down = self.data[int(n/2-1)]
            up = self.data[int(n/2)]
            median = (up + down)/2
        return median
    
    def calc_var(self):
        # get the mean
        n = self.length
        mean = self.mean
        # substract each value from the mean and raise the value power of 2
        variance  = list(map(lambda x: (x-mean)**2/(n-1) ,self.data))
        var_sum = sum(variance)
        return var_sum
    
    def calc_std(self): 
        return self.variance**0.5
    
    def add_data(self, numbers):
        if type(numbers) == list:
            self.data.extend(numbers)
        else:
            self.data.append(numbers)
        self.__update_stats()
        return
    
    def remove_data(self, index):
        del self.data[index]
        self.__update_stats()
        return 
        





