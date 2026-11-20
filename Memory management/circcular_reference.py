import gc

class MyObject:
    def __init__(self,name):
        self.name=name
        print(f"An object {self.name} is created")

    def __del__(self):
        print(f"An object {self.name} is deleted")

obj1=MyObject("obj1")
obj2=MyObject("obj2")
obj1.ref=obj2
obj2.ref=obj1
gc.collect()