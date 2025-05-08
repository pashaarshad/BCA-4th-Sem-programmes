file = open("arshadpa.txt","w")
f_w = file.write("HI i am Arshad")
file.close()
file = open("arshadpa.txt","r")
file_output = file.read()

print(file_output)
file.close()
