while True:
    try:
        myInt=int(input("Enter a number!!: "))
    except:
        print("Please enter a number")
        continue
    else:
        print("Thank You")
        break
    finally:
        print("Finally is called")