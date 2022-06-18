input_list = []
for i in range (0,11):
    input_integer = int(input("Enter Integer"))
    input_list.append(input_integer)
    
print(input_list)

#a
print("Positive Numbers")
for elem in input_list:
    if elem > 0:
        print (elem , end=", ")

#b
print("\nNegative Numbers")
for elem in input_list:
    if elem < 0:
        print (elem , end=", ")

#c
print("\nOdd Numbers")
for elem in input_list:
    if elem%2 != 0:
        print (elem , end=", ")

#d
print("\nEven Numbers")
for elem in input_list:
    if elem%2 == 0:
        print (elem , end=", ")

#e
temprory_list = []
for elem in input_list:
    count = 0
    if elem in temprory_list:
        continue
else:
    temprory_list.append(elem)
    for repeat_elem in input_list:
        if repeat_elem == elem :
            count += 1
    print (count)

