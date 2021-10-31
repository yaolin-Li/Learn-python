import random

answer = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")
print("Take a guess.")
num = int(input())
count = 1
while(num != answer):
    count += 1
    if num < answer:
        print("Your guess is too low.")
        print("Take a guess.")
    elif num > answer:
        print("Your guess is too high.")
        print("Take a guess.")
    num = int(input())
print("Good job! You guessed my number in "+str(count)+" guesses!")