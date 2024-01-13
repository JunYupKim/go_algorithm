import random
class RandomizedSet(object):

    def __init__(self):
        self.object = list()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if object == []:
            object.insert(val)
            return True 
        for number in self.object:
            if number == val: 
                return False 
        self.object.insert(0,val)
        return True 

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        for number in self.object:
            if number == val: 
                self.object.remove(val)
                return True
        return False 

    def getRandom(self):
        """
        :rtype: int
        """
        return self.object[random.randint(0,len(self.object)-1)] 
     

    
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()