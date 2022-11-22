# We let the computer guess a random number that we chose
# The guess persists until it picks the right number for us

import random

def machine_guess(x):
    low = 1
    high = x
    result = ''
    while result != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        result = input(f'Is {guess} too low(L), too high(H) or correct(C)').lower()
        if result == 'l':
            guess = low + 1
        elif result == 'h':
            guess = high - 1
    print(f"Congratulations!, our machine guessed {guess} correctly")
machine_guess(10)