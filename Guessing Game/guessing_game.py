import random

def guessing_game():
    """
    A guessing game that challenges the user to guess a random number.
    The user receives feedback on whether their guess is too high or too low.
    """
    print("=" * 50)
    print("     Welcome to the Guessing Game!")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    # Game loop
    while not guessed:
        try:
            # Get user input
            user_guess = input("Enter your guess (1-100): ")
            
            # Validate input
            guess = int(user_guess)
            
            # Check if guess is within valid range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue
            
            attempts += 1
            
            # Compare guess with secret number
            if guess < secret_number:
                print(f"❌ Too low! Try a higher number.\n")
            elif guess > secret_number:
                print(f"❌ Too high! Try a lower number.\n")
            else:
                guessed = True
                print(f"\n🎉 Congratulations! You guessed it right!")
                print(f"🎯 The number was: {secret_number}")
                print(f"📊 You took {attempts} attempt(s) to win!")
                print("=" * 50)
        
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid number.\n")
            continue

def main():
    """Main function to run the game"""
    play_again = True
    
    while play_again:
        guessing_game()
        
        # Ask if user wants to play again
        while True:
            response = input("\nDo you want to play again? (yes/no): ").lower().strip()
            if response in ['yes', 'y']:
                print("\n" + "=" * 50 + "\n")
                break
            elif response in ['no', 'n']:
                play_again = False
                print("\nThanks for playing! Goodbye! 👋\n")
                break
            else:
                print("Please enter 'yes' or 'no'.\n")

if __name__ == "__main__":
    main()
