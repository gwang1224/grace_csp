import random

num_guesses = 0
user_guess = 0

number = random.randint(1,100)

print(f"I'm thinking of a number between 1 and 100.")

def guess():
    guess = int(input("Guess a number: "))
    return guess

def search(number, guess):
    if guess < number:
        print("Your guess was too low :(")
    elif guess > number:
        print("Your guess was too high")

while user_guess != number:
    user_guess = guess()
    num_guesses += 1
    print(f"You guessed {user_guess}.")
    search(number, user_guess)

print(f"You guessed the number in {num_guesses} guesses!")


###########################################################################

# import random

# num_guesses = 0
# user_guess = 0
# upper_bound = 100
# lower_bound = 0

# number = random.randint(1,100)
# print(number)

# print(f"I'm thinking of a number between 1 and 100.")

# def guess():
#     guess = int(input("Guess a number: "))
#     return guess

# def search(number, guess):
#     global lower_bound, upper_bound
#     if guess < number:
#         print("Your guess was too low")
#         lower_bound = guess
#     elif guess > number:
#         print("Your guess was too high")
#         upper_bound = guess
#     return lower_bound, upper_bound

# while user_guess != number:
#     user_guess = guess()
#     num_guesses += 1
#     print(f"You guessed {user_guess}.")
#     lower_bound, upper_bound = search(number, user_guess)
#     print(f"Guess a number between {lower_bound} and {upper_bound}.")

# print(f"You guessed the number in {num_guesses} guesses!")