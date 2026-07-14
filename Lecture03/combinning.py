age = int(input("Please enter your age: "))
income = float(input("Please enter your income: "))

if age >= 18 and age <= 65 and income >30000:
    print("you are eligible for the loan.")
else:
    print("you are not eligible for the loan.")