a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a>=b and a<=c:
    middle = a
elif b >= a and b<= c:
    middle = b
else:
    middle = c
print("The middle number is:",middle)