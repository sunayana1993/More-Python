def ask_for_it():
    try:
        result=int(input("Please provide a number"))

    except:
        print("Whoops! that is not a number")

    finally:
        print("End of try/except/finally")

ask_for_it()