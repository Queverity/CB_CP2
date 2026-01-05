# CB 1st Classes

class Cars:
    def _init_(self,brand,model,maxspeed,color):
        self.brand = brand
        self.model = model
        self.maxspeed = maxspeed
        self.color = color

tesla = Cars("Tesla","3","100 MP/H)","White")
for i in tesla:
    print(i)
