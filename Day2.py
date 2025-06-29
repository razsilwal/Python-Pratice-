# name = "   -----My ---- Sister's name is Sujata 1 2 3 ____ "

# new_name = name.strip(" -123_")
# print(new_name)

# # new_name = My ---- Sister's name is Sujata
# new_name_final = new_name.replace(" ---- ", " ")
# print(new_name_final)

name1 = "--- My name ___ is Ram 123 karki --"
new_name = name1.strip("- ").replace("___ ", "").replace("123 ","")
print(new_name)
