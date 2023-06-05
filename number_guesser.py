import random

top_of_range = input("Please type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("\nPlease type a number larger than '0' next time.\n")
        quit()

else:
    print("\nPlease type a number next time.\n")
    quit()


random_num = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("\nMake a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("\nPlease type a number next time.\n")
        continue

    if user_guess == random_num:
        print("\nYou guessed the correct number!")
        break

    elif user_guess > random_num:
        print("\nYou were above the number.")

    else:
        print("\nYou were below the number.")

print("\nYou guessed the correct number in", guesses, "guesses.")