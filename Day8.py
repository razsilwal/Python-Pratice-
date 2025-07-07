# try catch 


# while True:
#     try:
#         x= int(input("Enter a number: "))
#     except ValueError:
#         pass
#     else:
#         break
# print(f"The entered number is {x}")


# Division By Zero Error
# Task -> write a Program that takes a number that divide number 10

# while True:
#     try:
#         num1 = int(input("Enter a number: "))
#         # if num1>0 or num1 <0:
#         result = 10/num1
#         # else:
#         #     print("cannot divide by zero")

#     except ValueError as e:
#         print(e)
#     else:
#         print(f"Result = {result}")
#         break


# try:
#     num = int(input("Enter a number: "))

# except ValueError as e:
#     print(e)

# def main():
#     x = get_int()
#     print(f"Number =  {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("Enter a number: "))
#         except ValueError as e:
#             print(e)
#         else:
#             return x # it will return value so it will break through loop 
            
# main()

'''
# Write a program takes three numbers as input 
sum, product and (num1+num2)/num3 of all three number 
 '''


# def main():
#     try:
#         num1 = int(input("Enter a first number: "))
#         num2 = int(input("Enter a second number"))
#         num3 = int(input("Enter a third number: "))
#     except ValueError:
#         pass
#     else:
#         print("Sum: ", sum_all(a,b,c))

# def sum_all(a,b,c):
#     return a + b + c



while True:
    try:
        num1 = int(input("Enter a first number: "))
        num2 = int(input("Enter a second number"))
        num3 = int(input("Enter a third number: "))

        operation = (num1 + num2) / num3
    except ValueError:
        pass

    except ZeroDivisionError:
        pass

    else:
        sum = num1 + num2 + num3
        product = num1 * num2 * num3
        print(f"Sum = {sum}")
        print(f"Product = {product}" )
        print(f"Operation = {operation}")
        break


# def main(num1,num2,num3):
#     print(f"The sum is: {num1 + num2 + num3}")
#     print(f"The product is: {num1 * num2 * num3}")
#     try:
#         print(f"The operation (num1 + num2)/num3 is {(num1 + num2)/num3}")
#     except ZeroDivisionError:
#         print(f"num3 = {num3} thus Division Invalid!!")
    
# def cal():
#     while True:
#         try:
#             num1 = int(input("Enter first number: "))
#             num2 = int(input("Enter second number: "))
#             num3 = int(input("Enter third number: "))
#         except ValueError:
#             print("Please enter an integer!!")
#         else:
#             return main(num1,num2,num3)
# cal()