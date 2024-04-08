import random


def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the rock-paper-scissors game.

    Arguments:
    user_choice (str): The user's choice ('rock', 'paper', or 'scissors').
    computer_choice (str): The computer's randomly generated choice.

    Returns:
    str: The result of the game ('User wins', 'Computer wins', or "It's a tie").
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "User wins!"
    else:
        return "Computer wins!"


def main():
    print("Welcome to Rock, Paper, Scissors!")

    # Ask if the user wants instructions
    while True:
        show_instructions = input("Would you like to see instructions? (yes/no): ").lower()
        if show_instructions == 'yes':
            print("Instructions:")
            print("- Type 'rock', 'paper', or 'scissors' to make your choice.")
            print("- Rock beats scissors, scissors beat paper, paper beats rock.")
            print("- Have fun!")
            break
        elif show_instructions == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Ask how many rounds
    while True:
        try:
            num_rounds_input = input("Enter the number of rounds you want to play: ")
            num_rounds = int(num_rounds_input)
            if num_rounds < 1:
                raise ValueError("Number of rounds must be 1 or more.")
            break
        except ValueError as e:
            print("\nInvalid input:", e)

    # Initialize scores
    user_score = 0
    computer_score = 0

    # Game loop
    for round_num in range(1, num_rounds + 1):
        print(f"\nRound {round_num}")

        # Get user's choice
        while True:
            user_choice = input("Choose 'rock', 'paper', or 'scissors' (or 'x' to quit): ").lower()

            # End the game loop if user types 'x'
            if user_choice == 'x':
                print("Game ended.")
                break

            if user_choice not in ['rock', 'paper', 'scissors']:
                print("\nInvalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            else:
                break

        if user_choice == 'x':
            break

        # Generate computer's choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chooses:", computer_choice)

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores based on the result
        if "User wins" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        # Display current score
        print(f"Score - User: {user_score}, Computer: {computer_score}")

    # Display final score at the end of the game
    print("\nGame over!")
    print(f"Final Score - User: {user_score}, Computer: {computer_score}")


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()