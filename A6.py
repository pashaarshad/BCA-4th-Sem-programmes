arr = [4,8,2,9,1,5]
print(arr)
n = int(input("Enter the Number to Find"))

for i in range(len(arr)):
    if arr[i] == n:
        print(f"Fount at Index {i}")
        break
    else:
        print(f"Not found at Index {i}")
