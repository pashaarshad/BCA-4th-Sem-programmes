import cmath

a = int(input("Enter the Number : "))
b = int(input("Enter the Number : "))
c = int(input("Enter the Number : "))

d = (b**2)-(4*a*c)

r1 = (-b+cmath.sqrt(d)/(2*a))
r2 = (-b-cmath.sqrt(d)/(2*a))

print("The Root 1 is {0} and Root2 is {1}".format(r1,r2))
