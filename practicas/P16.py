my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# region Codigo del ejercicio
new_list = []
i = 0
while i < len(my_list):
    if my_list[i] in new_list:
        del my_list[i]
    else:
        new_list.append(my_list[i])
        i += 1

del i
del new_list
# endregion

print("La lista con elementos únicos:")
print(my_list)
