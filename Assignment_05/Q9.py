n= int(input("no of words:"))
input_list = []
print(input_list)
for i in range (0,n):
    input_word = input("Enter word : ")
    input_list.append(input_word)

k= {}
for i in input_list:
        if i not in k:
            k[i]=1
        else :
            k[i]+=1
print ("no of occurance =",k)