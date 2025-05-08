def menu():
    print("Menu")
    print("1.append")
    print("2.Remove")
    print("3.Reverse")
    print("4.Exit")

def main():
    d = {}

    while True:
        menu()
        c = int(input("Enter the Choice"))

        if c == 1:
            append_item(d)
        elif c == 2:
            remove_item(d)
        elif c == 3:
            reverse_item(d)
        else:
            print("Exit")
            break

def append_item(d):
    key = input("Enter the key name : ")
    val = input("Enter the valuse : ")
    d[key] = val
    print(f"The Dict is [{key}:{val}]")

def remove_item(d):
     key = input("Enter the key name for remove ")
     if key in d:
         del d[key]
         print(f"The key is Remove {key}")
     else:
         print("NO FOund")
def reverse_item(d):
    print("The Reverse Dicr is :")
    r_val = {v:k for k,v in d.items()}
    print(r_val)

if __name__ == "__main__" : main()
        
