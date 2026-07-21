keep_going = 'y'
while keep_going == 'y':
    wholesale = float(input("Enter the wholesale cost: "))
    retail_price = wholesale * 2.5
    print(f"The retail price is: {retail_price:.2f}")
    keep_going = input("Do you want to calculate another retail price? (y/n): ")