import random
print("what is my magic number (1 to 100) ?")
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber:
    yourguess = int(input("Enter your guess: "))
    if yourguess < mynumber:
        print("Your guess is too low")
    elif yourguess > mynumber:
        print("Your guess is too high")
    ntries += 1

if yourguess == mynumber:
    print("You guessed it!")
else:
    print("You failed to guess the number is ", mynumber)
