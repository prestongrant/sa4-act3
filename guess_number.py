number = 10
print("I'm thinking of a number...")

while True:
    guess_input = input("What number is correct? (Enter 'q' to quit) ")

    if guess_input.lower() == 'q':
        print(f"The number is {number}.")
        break

    try:
        guess = int(guess_input)
    except ValueError:
        print("Wrong guess. Please try again or 'q' to quit.")
        continue

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry, your guess was too low.")
    else:
        print("Sorry, your guess was too high.")