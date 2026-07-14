score = int(input("Enter your score: "))
score_1 = int(input("Enter your score: "))
score_2 = int(input("Enter your score: "))
math_score = (score + score_1 + score_2) / 3
print("Your average score is:", "%.2f" % math_score)
if math_score > 95:
    print("congratulations!")
