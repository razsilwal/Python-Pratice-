# IF ELSE

# num = 9

# if num >0:
#     print("The number is positive ")

# else:
#     print("The number is negative ")


# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive")

# elif(num==0):
#     print("Number is nor negative nor postive")

# else:
#     print("The number is negative ")


# num = int(input("Enter a number to check odd or even: "))

# if (num%2==0):
#     print("Even")
# else:
#     print("odd")


# num1 = int(input("Enter a First number: "))
# num2 = int(input("Enter a Second number: "))
# num3 = int(input("Enter a Third number: "))

# if num1 > num2:
#     if num1 > num3:
#         print("Num1 is grater")
#     else:
#         print("num3 is greater")
# else:
#     if num2 > num3:
#         print("Num2 is greater")
#     else:
#         print("Num3 is greater")

# if num1 > num2 and num1 > num3:
#     print("Num1 is Greater")
# elif num2 > num1 and num2 > num3:
#     print("Num2 is Grater")
# else:
#     print("Num3 is greater")


num1 = int(input("Enter a first number: "))
num2 = int(input("Enter another number: ")) 

ch = int(input("1: Addition\n 2: Subtraction\n 3: Multiply\n Enter choice: "))

match ch:
    case 1:
        add = num1 +num2
        print(f"{num1} + {num2} = {add}")
    case 2:
        if num1 > num2:
            sub = num1 - num2
            print(f"{num1} - {num2} = {sub}")
        else:
            sub = num2 - num1
            print(f"{num2} - {num1} = {sub}")
    case 3:
        mul = num1 * num2
        print(f"{num1} * {num2} = {mul}")

    case _:
        print("Invalid Choice")