def ask_for_int():
    while True:
        try:
           result= int(input(("Provide input number:")))
        except:
            print("Whoops! that is not a number")
            continue
        else:
            print("Yes!thank you")
            break
        finally:
            print("end of try xcept")
ask_for_int()