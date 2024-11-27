from tuple_out_functions import roll_dice, check_tuple_out, calculate_score, is_game_over

def get_yes_no_input(prompt):
    """
    Ensures the user provides a valid 'yes' or 'no' response.
    """
    while True:
        response = input(prompt).lower().strip()
        if response in ['yes', 'no']:
            return response
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def play_game():
    print("Welcome to the Tuple Out Dice Game!")
    player_scores = {}
    num_players = int(input("Enter the number of players: "))
    
    # Initialize player scores
    for i in range(1, num_players + 1):
        player_scores[f"Player {i}"] = 0

    target_score = 50  # Define the score required to win

    while not is_game_over(player_scores, target_score):
        for player in player_scores.keys():
            print(f"\n{player}'s turn:")
            dice = roll_dice()
            print(f"Initial roll: {dice}")
            
            if check_tuple_out(dice):
                print(f"{player} tupled out! No points this turn.")
                continue
            
            while True:
                re_roll = get_yes_no_input("Do you want to reroll any dice? (yes/no): ")
                if re_roll == "yes":
                    indices_to_reroll = input("Enter the positions (1, 2, or 3) of dice to reroll, separated by spaces: ").strip().split()
                    indices_to_reroll = [int(i) - 1 for i in indices_to_reroll if i.isdigit() and 1 <= int(i) <= 3]
                    
                    for i in indices_to_reroll:
                        dice[i] = roll_dice()[0]
                    
                    print(f"New roll: {dice}")
                    if check_tuple_out(dice):
                        print(f"{player} tupled out! No points this turn.")
                        break
                else:  # If the user says 'no', calculate score and end turn
                    turn_score = calculate_score(dice)
                    player_scores[player] += turn_score
                    print(f"{player} scored {turn_score} points this turn.")
                    print(f"Total score: {player_scores[player]}")
                    break

        # Check again if game is over after the round
        if is_game_over(player_scores, target_score):
            break

    # Determine the winner
    winner = max(player_scores, key=player_scores.get)
    print("\nGame over!")
    print("Final Scores:")
    for player, score in player_scores.items():
        print(f"{player}: {score}")
    print(f"Congratulations, {winner}! You won the game!")

if __name__ == "__main__":
    play_game()