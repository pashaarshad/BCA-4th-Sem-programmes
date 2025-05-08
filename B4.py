def menu():
    print("Menu")
    print("1.Append")
    print("2.Remove")
    print("3.Reveres")
    print("4.Exit")

def main():
    list = []
    while True:
        menu()
        c = int(input("Enter the Choice"))

        if c == 1 :
             val = input("Enter the Append val")
             list.append(val)
             print(f"The List is {list}")
        elif c == 2:
            val = input("Enter the Removing Val")
            if val in list:
                list.remove(val)
                print(f"Now the list is {list}")
            else:
                print("Not Found")
        elif c == 3:
            print("Revised of List ")
            list.reverse()
            print(f"The List is {list}")
        else:
            print("Exit")
            break


main()
    
