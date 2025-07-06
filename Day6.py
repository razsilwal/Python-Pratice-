# looping or iterative statement

# for loop 
# fruits = ['Apple', 'Banana', 'kiwi', 'Orange', 'Mango' ]
# for fruit in fruits:
#     print(fruit)

# my_list = list(range(1, 11, 2))
# print(my_list)

# for i in range(1,21,2):
#     print(i, end=" ")

# my_dict = {
#     "1":"Apple",
#     "2":"Banana",
#     "3":"Mango"
# }
# for k in my_dict:
#     print(f"{k} : {my_dict[k]}")

# fruits = ['Apple', 'Banana', 'kiwi', 'Orange', 'Mango' ]
# count = 0
# for fruit in fruits:
#     count = count + 1
#     print(f"{count} : {fruit}")


# While Loop
# count = 0 
# while count<=5:
#     print("My name is Raz")
#     count += 1

# break keyword

# for i in range(1,10):
#     if i == 6:
#         break
#     print(i)

skipped = []
for i in range(1,10):
    if i in [6,7,8]:
        skipped.append(i)
        continue
    print("value: ",i, end=" ")

print("\nSkipped Value:",skipped)
    