print("Welcome to the new game")
name = str(input("Register your name Here: "))
print(name)
import random
number1 = int(input("enter any number betwwen 0 to 8: "))
random_number = random.randint(0, 9)
print(random_number)
if number1>random_number:
    print("Congrats!!, Your number was gretest than computer you win")
elif number1==random_number:
    print("The game was tie")
else:
    print("You loss the pleasr try again later")
