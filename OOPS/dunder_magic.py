class Book:
    def __init__(self,pages,name,author):
        self.pages=pages
        self.name=name
        self.author=author

    def __str__(self):
        return f"{self.name} for {self.author}"

b=Book(200,"science","HC verma")
print(b) #gives you where b is lo