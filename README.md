# 15-112-Final-Project-Candy-Crush
For the final project, I am going to do a game called Candy Crush—a popular match-three game. In this game, player is given a board with grids. Inside the grids are candies with different colors. The player can switch a candy’s position with the candy next to it (left, right, above, below). If three or more candies in a line have the same color after the switch, the candies which are in one line and have same color will be removed. Then the candies above the removed candies will replace the candies. The blank grids on the top of the board will be filled by new candies. If less than three candies with same color are in a line after the switch, the candies will switch back to the original position and the play can do the next move. 

For this project, I will use pygame and numpy libraries. I might also use other libraries. 

Features: The board for this game will have 8*8, 64 grids. There will be six colors of candies—orange, yellow, blue, green, red, purple. In this game, the player will earn some points for each successful switch. The player will get 100 points for each 3-candies match, 120 points for 4-candies match, 150 points for 5-candies match. The play will be given 2 minutes to play the game.  

User Interface: Player will first see a button saying “begin”. After clicking on the button, the player can see a board. Besides the board, there will be three boxes showing time left, current point and the point get from the last move. When the time is up, the player will see their score and a line telling him or her game is over. 

By November 25th,the game can be played although some details still need to be worked on. It means that the candies can be moved and removed and new candies can appear at this time. 

On December 6th, the user interface will be implemented. Three boxes showing time and score will be added. The interface before and after game will be added.
