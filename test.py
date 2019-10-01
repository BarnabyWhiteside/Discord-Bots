import random
Table = ['Odd','Under 7', '7', 'Over7', 'Even'
        '2', '3', '4', '5', '6', '8', '9', '10', '11', '12']

Dice1 = random.randint(1,6)
Dice2 = random.randint(1,6)
Total = Dice1 + Dice2

if Total == 3 or Total == 5 or Total == 7 or Total == 9 or Total == 11:
    Outcome = 'Odd'
else:
    Outcome = 'Even'

print (Outcome)
"The monster stands before you, ready to attack\nYour health is "
