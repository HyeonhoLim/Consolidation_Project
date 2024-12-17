# “Tuple Out” Dice Game 🎲
---

# Getting Started
The Tuple out Dice game is a fun, turn-based dice game for two players. Your goal is to score 50 points before your opponent while avoiding the "tuple out" penalty. Follow these steps to set up and play the game.

# Type the following command to start the game:
**python main_game.py**

# Turn Order
- The game alternates turns between Player 1 and Player 2.
Each player rolls three dice on their turn.

---

# Dice Rolls
- The game automatically rolls three dice for the active player and displays the results.

---

# Making Decisions
- Fixed Dice:
If two dice are the same, they become "fixed" and cannot be rerolled.

- Rerolling:
The player can reroll any non-fixed dice as many times as they want.

- However, rerolling comes with the risk of "tupling out" (rolling three identical dice), which scores 0 points for the turn.
User Input:
After each reroll, the game asks:
Would you like to reroll? (yes or no)

- Type yes to reroll or no to stop.
If you type anything other than yes or no, the game will prompt you again to enter a valid answer.

---

# Ending a Turn
- Stop Rerolling:
If a player chooses to stop rerolling, their score is calculated as the total of the three dice.

- Tuple Out:
If a player tuples out (all three dice have the same value), they score 0 points for the turn.

---

# Winning the Game
- The game ends when a player scores 50 or more points.
The player with the highest score wins.