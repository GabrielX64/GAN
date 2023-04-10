class Update:
    def __init__(self):
        self.__num = 0
    
    """def display(self):
        print(self.__num)"""
    
    @property #PROPIEDADES SET-GET-DELETE
    def num(self):
        print(f"Num: {self.__num}")
        return self.__num
    
    @num.setter #SET
    def num(self, value):
        print(f"{self.__num} ahora es {value}")
        self.__num = value

u = Update()