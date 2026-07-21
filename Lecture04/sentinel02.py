keep_going = 'Y'
while keep_going == 'Y':
    rows = int(input("Enter the number of rows: "))
    column = int(input("Enter the number of columns: "))
    for i in range(rows):
        for j in range(column):
            print("*", end="")
        print()
    keep_going = input("Do you want to create another rectangle? (Y/N): ").upper()
