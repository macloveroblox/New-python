max = 5
total = 0.0
print('this program calculates the sum of')
print(max, 'numbers you will enter.')
for counter in range(max):
    number = int(input('enter a number: '))
    total = total + number
print('the total is', total)