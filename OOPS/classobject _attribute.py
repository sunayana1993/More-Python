class Animal():

    #class object attribute
    species="mammal"

    def __init__(self,breed,type):
        #breed, type are user defined attribute
        self.breed=breed
        self.type=type

    def printAnimal(self):
        print(self.breed)
        print(self.type)

Animal1=Animal(breed="Lab",type="Dog")
Animal1.printAnimal()
print(Animal1.species)


