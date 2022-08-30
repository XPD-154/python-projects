from random import *
x = 0
choose = int(input("Choose upper limit: "))

random_number = randint(1, choose)
while x!=random_number:
    x = int(input(f"Guess a number between 1 and {choose}: "))
    if x > random_number:
        print('greater than number, try again')
    elif x < random_number:
        print('lesser than number, try again')

print('Got the answer')


