number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3 :
    print("This number is bigger " + str(number1))

if number2 >= number1 and number2 >= number3 :
    print("This number is bigger " + str(number2))

if number3 >= number1 and number3 >= number2 :
    print("This number is bigger " + str(number3))

