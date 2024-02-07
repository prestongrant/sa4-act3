number = 10
max_guesses = 3
print("I'm thinking of a number...")

guess_count = 0

while guess_count < max_guesses:
    guess_input = input("What number is correct? (Enter 'q' to quit) ")

    if guess_input.lower() == 'q':
        print(f"The number is {number}.")
        break

    try:
        guess = int(guess_input)
    except ValueError:
        print("Wrong guess. Please try again or 'q' to quit.")
        continue

    guess_count += 1

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry, your guess was too low>")
    else:
        print("Sorry, your guess was too high.")

if guess_count == max_guesses:
    print("Sorry, you ran out of guesses. The correct number is {number}.")