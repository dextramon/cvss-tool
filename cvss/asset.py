class Asset:
    def __init__(self, name, description=None):
        self._name = name 
        self._decription = description

    @property
    def name(self): 
        return self._name 

    @name.setter
    def name(self,value): 
        self._name = value


    @property
    def description(self): 
        if self._description == None: 
            return "No description available!"
        else: 
            return self._description

    
    @description.setter
    def description(self, value): 
        self._value = value 
