from random import *

choose = int(input("Choose upper limit: "))
lower = 1
upper = choose
feedback =''

while feedback != 'c':
    if lower != upper:
        guess = randint(lower, upper)
    else:
        guess = lower   #could also be upper because they are equal
    feedback = input(f"is the {guess} too high(H), too low(L) or correct(C)").lower()
    if feedback == 'h':
        upper = guess - 1
    elif feedback == 'l':
        lower = guess + 1

print(f'the computer got it right {guess}')


