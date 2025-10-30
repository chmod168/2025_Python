class vehicle:
    def __init__(self, make,model,color,price):
        self.make=make
        self.model=model
        self.color=color
        self.price=price

    def setMake(self,make):
        self.make=make

    def getMake(self):
        return self.make
    
    def getDesc(self):
        return "차량=("+str(self.make)+","+str(self.model)+str(self.color)+","+str(self.price)+")"
    
    