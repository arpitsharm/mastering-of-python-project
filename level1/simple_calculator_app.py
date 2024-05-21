while True:
    print("1 Addition")
    print("2 Substraction")
    print("3 Multiplcation")
    print("4 Division")
    print("5 Exit")

    choice = int(input("Enter choice(1/2/3/4): "))

    if choice != 1 or choice != 2 or choice != 3 or choice != 4 or choice != 5:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == 1:
            print(num1 + num2)
        elif choice == 2:
            print(num1 - num2)
        elif choice == 3:
            print(num1 * num2)
        elif choice == 4:
            print(num1 / num2)
            

    else:
        print("Please Select Correct Choice")