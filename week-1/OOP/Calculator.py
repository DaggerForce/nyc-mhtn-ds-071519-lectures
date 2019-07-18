class Calculator:
    ### google assert function
    #create attributes to hold the list if numbers and the length of the list
    #update changes if needed
    def __init__(self, data):
 #       assert all(isinstance(x, (int, float))) for x in data), "give me numbers not letters man"
        import math
        self.data = data
        self.length = len(data) #self.data
        self.__update_stats()
    
    # updates our attributes if the user changes the data using "add_date" or "remove_data"
    def __update_stats(self):  
        self.mean = self.calc_mean()
        self.median = self.calc_median()
        self.variance = self.calc_var()
        self.standev = self.calc_std()

    # calculating the mean by    
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
        # saving the mean and length attributes on readble elements
        n = self.length
        mean = self.mean
        # substract each value from the mean and raise the value power of 2
        variance  = list(map(lambda x: (x-mean)**2/(n-1) ,self.data))
        var_sum = sum(variance)
        return var_sum
    
    #find standard deviation by using square root on the variance attribute
    def calc_std(self): 
        return self.variance**0.5
    
    #this method can add one or more numbers into our data
    def add_data(self, numbers):
        #if user tries to add more than one number
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
        





