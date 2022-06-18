a = int(input("Enter the length of first side : "))
b = int(input("Enter the length of second side : "))
c = int(input("Enter the length of third side : "))

s = (a+b+c)/2
import math
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)