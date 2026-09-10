def hello(name='Jose'):
    print("the hello() function has been executed")

    def greet():
        return "This is greet() function inside hello"

    def welcome():
        return "This is welcome inside hello"

    print(greet())
    print(welcome())
    print("This is the end of the hello function")

my_new_func=hello('Jose')
print(my_new_func)

def cool():
    def super_cool():
        return "I am very cool!"
    return super_cool
some_func=cool()
print(some_func)