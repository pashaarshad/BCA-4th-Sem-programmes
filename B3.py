import re

n = input("Enter Your Universuity Number : ")
pattern ="^U[0-9]{2}[C][T][0-9]{2}[S][0-9]{4}"

output = re.search(pattern,n)

if output:
    print("Vallid University number")
else:
    print("Not a Valid Number")
