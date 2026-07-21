score = int(input('Enter a test scrore: '))
while score < 0 or score > 100:
    print('Invalid score. Please enter a score between 0 and 100.')
    print('or greater than 100. ')
    score = int(input('Enter the correct score: '))
