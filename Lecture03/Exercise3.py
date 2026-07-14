hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the pay rate: "))

if hours <= 40:
    gross_pay = hours * pay_rate
else:
    gross_pay = (40 * pay_rate) + ((hours - 40) * pay_rate * 1.5)

print(f"The gross pay is: ${gross_pay:.2f}")