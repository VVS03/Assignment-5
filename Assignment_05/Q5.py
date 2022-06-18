n = int(input("Enter the number of rows : "))

asciichr = 65
for i in range (0,n):
    for j in range (0,i+1):
        char = chr(asciichr)
        print (char, end="")
        asciichr = asciichr +1
    print()
