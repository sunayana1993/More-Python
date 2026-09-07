def ask():
    while True:
        try:
            x=int(input("Enter an integer"))
            print(x*x)
            break

        except TypeError:
            print("Error ocurred!Please try again!")

        except ValueError:
            print("error occured in value")
ask()