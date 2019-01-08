import math

while True:

    user = input("This is a calculator what do you wanna do?: multiply, divide, add, subtract, percent, pi, eulier, squere? m/d/a/s/p/pi/e/sq ")

    if user == "p":
        print("You count ..% from a value")

    num1 = int(input("Give your first number "))
    num2 = int(input("Give your secound number "))

# def function

    def multiply(num1,num2):
        return num1*num2
    result = multiply(num1,num2)

    def divide(num1,num2):
        return num1/num2
    result1 = divide(num1,num2)

    def add(num1,num2):
        return num1+num2
    result2 = add(num1,num2)

    def subtract(num1,num2):
        return num1-num2
    result3 = subtract(num1,num2)

    def percent(num1,num2):
        return num1/100*num2
    result4 = percent(num1,num2)

#EULIER You only have to write your value in num1, in num2 it's whatever you want

    def eulier(num1):
        return math.sqrt(num1)
    result5 = eulier(num1)
#PI You only have to write your value in num1, in num2 it's whatever you want
    def pi(num1):
        return num1*3.14
    result6 = pi(num1)

# SQUERE You only have to write your value in num1, in num2 it's whatever you want
    def squere(num1):
        return (num1**2)
    result7 = squere(num1)

#Below are the command who giving a results

    if user == "m":
        print("Multiply result is:",result)
    elif user == "d":
        print("Divide result is:",result1)
    elif user == "a":
        print("Add result is:",result2)
    elif user == "s":
        print("Subtract result is:",result3)
    elif user == "p":
        print("Percent result is:",result4)
    elif user == "e":
        print("Eulier result is:",result5)
    elif user == "pi":
        print("PI result is: ",result6)
    elif user == "sq":
        print("Squere is:",result7)

