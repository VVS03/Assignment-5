
lower = int(input("Enter the Range : "))
upper = int(input("Enter the Range : "))
divisor = int(input("Enter The Number : "))

for n in range (lower,upper):
    if n%divisor == 0:
        print (n)
        continue


