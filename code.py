import random 

number= random.randint(1,9)
chances = 0


while chances<5:
    guess = int(input("enter your guess"))
    if guess == number:
        print("congratulations")
        break
    elif guess<number:
        print("your guess was too low")
    else: 
        print("your guess was too high")
    chances +=1

