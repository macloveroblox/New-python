print_colum = int(input("Enter colum :"))
for i in range(1, 101):
        print(f"{i:>3}", end=" ")
        if i % print_colum == 0:
            print()