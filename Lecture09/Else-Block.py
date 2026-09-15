try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("cannot divide by zero!")
else:
    print(f"The resule is {result}")
print("End of program")