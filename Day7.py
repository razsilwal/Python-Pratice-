'''
User Defined functions
'''

# write  a program that greets the user using functions


# def greet(hello):
#     print(f"Welcome {hello}")


# name = input("Enter a name: ")
# greet(name)


# def celsius_to_farenheite(celsius):
#     farenheite = (celsius * 9 / 5) + 32
#     return farenheite

# def main():
#     celsius = float(input("Enter Temperature in Celsius: "))
#     feren = celsius_to_farenheite(celsius)
#     print(f"Temprtature in farenheit = {feren:.2f} degree farenheit")
    
# main()


# Task 3: Write a program to find the maximum among 3 number 

# def max_three_num(num1, num2, num3):
#     if (num1 >= num2) and (num1 >= num3):
#         return num1
#     if (num2 >= num1) and (num2 >= num3):
#         return num2
#     if (num3 >= num2) and (num3 >= num1):
#         return num3

# def main():
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a second number: "))
#     num3 = int(input("Enter a third number: "))

#     greatest = max_three_num(num1, num2, num3)
#     print(f"The greatest number among {num1}, {num2} and {num3} is {greatest}")

# main()

# def min_three_no(num1, num2, num3):
#     return min(num1, num2, num3)


# def main():
#     num1, num2, num3 = input("Enter three number: ").split("\n")# -> 1 2 3 -> [1, 2, 3] -> num1 = 1, num2 = 2, num3 = 3
#     smallest = min_three_no(int(num1), int(num2), int(num3))
#     print(f"The smallest number among {num1}, {num2}, {num3} = {smallest}")
    
# main()


# def min_three_no(num1, num2, num3):
#     return min(num1, num2, num3)


# def main():
#     numbers = input("Enter three number: ").split(" ")# -> 1 2 3 -> [1, 2, 3] -> num1 = 1, num2 = 2, num3 = 3
#     smallest = min_three_no(int(numbers[0]), int(numbers[1]), int(numbers[2]))
#     print(f"The smallest number among {numbers[0]}, {numbers[1]}, {numbers[2]} = {smallest}")
    
# main()

'''
Task -4 Build a simple calculator that performs 
addition, subtraction, multiplication and Division
of 2 numbers according to the user input using the concept
of functional programming

'''
def add(num1, num2):
    sum = num1 + num2
    print(sum)

def sub(num1, num2):
    sub = num1 - num2
    print(sub)

def mul(num1, num2):
    pro =  num1 * num2
    print(pro)

def div(num1, num2):
    if num2!=0:
        divi = num1/num2
        print(divi)

    else:
        print("Cannot divide by zero")
    
def calculator():
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))
    print("Enter your choice")
    choice = input("1. + \t2. -\t3.*\t4./")
    
    if choice=="+"or choice=="1":
        add(num1, num2)
    
    elif choice=="-" or choice=="2":
        sub(num1, num2)
    
    elif choice=="*"or choice=="3":
        mul(num1, num2)
    
    elif choice=="/"or choice=="4":
        div(num1, num2)
    else:
        print("invalid input")

calculator()

# import time

# print("Hello", end=" ")
# time.sleep(3)
# print("World!!")