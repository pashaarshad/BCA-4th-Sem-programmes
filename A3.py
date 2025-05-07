n = int(input("Enter The Number : "))

if(n<0):
    print("Placese Enter the Possitive Number")
else:
    sum = 0
    while(n>0):
        sum +=n
        n -=1
    print(f"The Natural number is : {sum}")
