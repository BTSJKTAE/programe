temp = int(input("What is the tempreature outside?: "))
if temp >= 0 and temp <= 30:
    print("The temprature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("The temprature is bad today!")
    print("Stay inside")