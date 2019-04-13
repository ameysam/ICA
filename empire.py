class Empire:
    def __init__(self, imperialist):
        self.imperialist = imperialist
        self.colonies = []
        self.cost = self.calculateCost()
    
    def calculateCost(self):
        return self.imperialist.getCost() + sum([colony.getCost() for colony in self.colonies])

    def replaceColony(self, index, colony):
        self.colonies[index] = colony
        self.calculateCost()

    def replaceImperialist(self, colony):
        self.imperialist = colony
        self.calculateCost()

    def deleteColony(self, index):
        del self.colonies[index]
        self.calculateCost()

    def getCost(self):
        return self.cost

    def addColony(self, ctr, index=0):
        if index == 0:
            self.colonies.insert(len(self.colonies), ctr)
        else:
            self.colonies.insert(index, ctr)
        self.calculateCost()

    def getNumberOfColonies(self):
        return len(self.colonies)

    def getColony(self, index):
        return self.colonies[index]

    def getImperialist(self):
        return self.imperialist

