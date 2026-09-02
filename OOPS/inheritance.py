class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOF!")

mydog=Dog()
print(mydog.eat())
print(mydog.who_am_i())

myanimal=Animal()
print(myanimal.eat())
print(myanimal.who_am_i())
