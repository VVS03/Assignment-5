n= int(input("no of words:"))
input_list = []

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
# input_string = input("Enter the string you want to check for : ")

# def count_word_of_string(str):
    
#     word_count = dict()
    
#     words = str.split()

#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     return word_count

# print(count_word_of_string(input_string))