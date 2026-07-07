weight = int(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2)
print("Your BMI is:", format(bmi, ".2f"))