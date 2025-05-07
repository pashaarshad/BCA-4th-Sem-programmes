n = int(input("Enter the Number :"))
a,b=0,1
while b<n:
    a,b = b,a+b
print( "Yes" if b==n else "No")
