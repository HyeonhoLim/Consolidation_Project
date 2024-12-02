import random

def roll_dice():
    """
    Rolls three dice and returns their values as a list.
    """
    return [random.randint(1, 6) for _ in range(3)]

def check_tuple_out(dice):
    """
    Checks if all three dice have the same value.
    Returns True if tuple out, otherwise False.
    """
    return len(set(dice)) == 1

def calculate_score(dice):
    """
    Calculates the total score for the given dice.
    """
    return sum(dice)

def is_game_over(scores, target_score):
    """
    Checks if any player's score meets or exceeds the target score.
    """
    return any(score >= target_score for score in scores.values())

def fix_dice(dice):
    """
    Identifies which dice are 'fixed' (have the same value as another die).
    Returns a list of indices of fixed dice.
    """
    fixed_indices = []
    for i in range(len(dice)):
        if dice.count(dice[i]) > 1:
            fixed_indices.append(i)
    return fixed_indices