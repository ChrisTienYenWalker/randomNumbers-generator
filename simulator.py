from random import *
count = 0
numbers = [1, 2, 3, 4, 5, 6]
pick = sample(numbers, 1)
print("your dice roll number is")
print(pick)
print("and your lucky numbers are")
while count < 6:
    print(randint(1, 100))
    count += 1







