for attempt in range(3):# run a for loop 3 times

    try:
        number = int(input("Enter an integer: "))
        print(number)
        break# if it is success, do not go repeat

    except ValueError:
        print("Invalid input")# not valid

else:
    print("You failed 3 times")
    # if else, to ask true or false
    # for else, to ask that prosess is completed or not