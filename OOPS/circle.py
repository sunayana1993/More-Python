class circle:
    #class object attribute
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius

    #METHOD
    def get_circumfrence(self):
        return self.radius*self.pi*2

my_circle=circle(30)
print(my_circle.pi)
print(my_circle.get_circumfrence())