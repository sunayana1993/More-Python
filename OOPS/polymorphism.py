class Dog:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name+" WOOF!"

class Cat:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name +" Meow!"

niko=Dog("niko")
kiky=Cat("kiko")

print(niko.speak())
print(kiky.speak())

#for pet in [niko,kiky]:
 #   print(pet)
 #   print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(kiky)