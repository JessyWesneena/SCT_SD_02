import random

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            return 50, 10
        elif choice == '2':
            return 100, 7
        elif choice == '3':
            return 200, 5
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


def play_game():
    max_range, max_attempts = choose_difficulty()
    secret_number = random.randint(1, max_range)

    print(f"\nI have selected a number between 1 and {max_range}.")
    print(f"You have {max_attempts} attempts to guess it.")

    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! 📉")
        elif guess > secret_number:
            print("Too high! 📈")
        else:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            return

        print(f"Remaining attempts: {max_attempts - attempts}")

    print(f"\n❌ Game Over! The correct number was {secret_number}.")


def main():
    print("🎮 Welcome to the Advanced Number Guessing Game!")

    while True:
        play_game()
        replay = input("\nDo you want to play again? (yes/no): ").lower()

        if replay != 'yes':
            print("Thank you for playing! 👋")
            break


if __name__ == "__main__":
    main()
