# darts-game
Dart Counter:
A console-based dart scoring program for the classic 301 and 501 darts games. Supports multiple players and automatically tracks scores, handles invalid inputs, and announces the winner.
Try it out here: https://onlinegdb.com/ZdKhR0Rt_

Features:

Supports both 301 and 501 game modes
Supports 1 to 100 players
Tracks each player's score across multiple rounds
Validates all inputs (no invalid scores or out-of-range values accepted)
Detects when a player busts (goes below 0) and keeps their score the same
Announces the winner when a player reaches exactly 0 points

How to Run Locally:
Requirements:

Python 3.x installed on your machine

Steps:

Clone or download this repository
Open a terminal in the project folder
Run the following command:

python main.py

How to Use:

When prompted, type 301 or 501 to select the game mode
Enter the number of players (between 1 and 100)
Each round, every player enters the score of their 3 darts one by one

Each dart must be a number between 0 and 60


The program will subtract the total from the player's remaining points
If a player's score would go below 0, their points stay the same (bust)
The first player to reach exactly 0 points wins!
