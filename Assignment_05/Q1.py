#reverse a string
def reverse(s):
    str = ''
    for i in s:
        str=i+str
    return str    

string = input("enter the string:")
print(reverse(string))

