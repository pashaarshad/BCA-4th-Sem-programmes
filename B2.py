import re

ph = input("Enter the Phone number")
pattern ="\+[0-9]{10,10}"  #pattern ="\+\d\d\d\d\d\d\d\d\d\d\d\d"

output = re.search(pattern,ph)

if output:
    print("Valid phone number")
else:
    print("Not Valide")
