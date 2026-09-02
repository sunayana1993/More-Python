class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        #abstract method in abstract class because method is not doing anything
        raise NotImplementedError("subclass must be implemented")

class Dog(Animal):
    def speak(self):
        return self.name+"Woof!"

class Cat(Animal):
    def speak(self):
        return self.name+"Meow!"

fido=Dog("Fido")
isis=Cat("isis")
print(fido.speak())
print(isis.speak())
