# Othello in Python
## How to Play
Two players take turns placing their pieces on an 8x8 game board. At the start, 4 pieces are placed in the middle of the board like in the screenshot below.
![screenshot](screenshots/start game.png)
Current pieces on the board are filled in with the players' colors while empty spaces are grey. Each piece that is placed by a player must be placed horizontally, vertically, or diagonally from one of their existing pieces, and must have at least one
of their opponents pieces between them. The available spaces for the next move will be circled with the color of the player that will make the move.

When a piece has been placed, all the opponents pieces that were between the new piece and any of the player's existing pieces will flip to the
player's color.
INSERT MOVE 1 SCREENSHOT
This will conclude their turn. This will go back and forth. If one player has no more valid moves to make, they forfeit their
turn.
INSERT MID GAME SCREENSHOT
If no player has any valid moves, the game is over and thus, a winner will be crowned.
INSERT END GAME SCREENSHOT

## How to Run
Install Python and the Pygame library. Download all the files and run the main.py program in an IDE to begin the game.
