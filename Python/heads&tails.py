import random

total_guesses = 0
correct_guesses = 0

while True:
    guess = input(
        "\nGuess the coin toss! Enter heads or tails (or type exit to quit): "
    ).lower()

    if guess == "exit":
        if total_guesses > 0:
            percentage = (correct_guesses / total_guesses) * 100
            print(f"\nYou were correct {percentage:.1f}% of the time.")
        else:
            print("\nYou didn't make any guesses.")

        print("\nThanks for playing!\n")
        break

    if guess not in ("heads", "tails"):
        print("\nPlease enter heads, tails, or exit.")
        continue

    total_guesses += 1

    toss = random.choice(("heads", "tails"))

    if toss == guess:
        correct_guesses += 1
        print("\nYou got it!")
    else:
        print("\nNope! The toss was", toss)
