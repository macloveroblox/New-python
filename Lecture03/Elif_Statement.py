num_employees = int(input("Enter the number of employees: "))
if num_employees < 50:
    print("You have a small company.")
elif num_employees < 250:
    print("You have a medium-sized company.")
else:
    print("You have a large company.")