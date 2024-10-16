# Guess a number
import random
number = random.randint(1,10)
attempts = 3
count = 1
while count in range(attempts):
    guess = int(input("Guess a number between 1-10:"))
if guess > number:
   print("Too high")
elif guess < number:
    print("Too low")
else:
    print("Correct")
    count += 1


    
