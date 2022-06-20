input_string = input("Enter the string you want to check for : ")

def count_word_of_string(str):
    
    word_count = dict()
    
    words = str.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

print(count_word_of_string(input_string))
