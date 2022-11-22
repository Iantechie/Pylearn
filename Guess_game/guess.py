import random

# We guess a random number chosen by the computer
#Note: You can guess once or several times until you guess the right number.
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a random number between 1 and {x} :"))
        if guess < random_number:
            print('Guess too low. Try again')
        elif guess > random_number:
            print('Guess too high. Try again')
    print(f'Congratulations! You have guessed the random number {random_number} correctly')
guess(5)


