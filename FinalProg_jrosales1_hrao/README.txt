Final Project Proposal: Sudoku
Team: Humza and Jangael


What is the final project? 
This Final Project runs a game of Sudoku where a user would fill in all empty squares within a randomly generated puzzle grid with the numbers 1-9. The objective of the game is to make sure that the user solves the entire puzzle without repeating any numbers within each row, column, and squares. 


What’s in this project?
* Sudoku.py: This sudoku file is the main file that holds all the classes and functions of the Sudoku game, including the backend and the GUI. 
* Sudoku class:
   * Initializes empty grid
   * Make Grid function:
      * Creates the sudoku puzzle using the empty grid by checking if a number has been used in the row, column, or square before putting it.
      * Returns puzzle
   * Check Grid:
      * Check every space in the puzzle is complete
      * Returns true or false
   * Remove Numbers:
      * Uses “n” parameter to indicate how many numbers are to be removed
      * Before the puzzle is displayed on the graphics window, a copy of the complete puzzle is made before taking out random numbers from it. The amount of numbers (“n”) taken out depends on the difficulty level chosen by the user.
      * Returns incomplete puzzle
   * Check Answer Function:
      * Uses list of buttons from the graphics window as parameter
      * For each button (aka space) on the graphics sudoku puzzle in the window, the number from each button is stored into a 2D list (similar to the list of the initialized puzzle). Then it compares each index of the list to the complete puzzle list (answer key). If the number matches, the button on the window turns green, and vice versa.
      * Returns true or false whether the whole puzzle is correct.
   * Print Grid:
      * Uses parameter for puzzle list
      * Prints grid in IDLE shell using the puzzle list (used for testing)


* Main Function:
   * Title Screen Function:
      * Displays the main menu of the sudoku game using graphics.py
      * Main menu consists of start, quit, instructions, and difficulty buttons.
      * Each difficulty has a different number associated with it, which is returned at the end of the function. That number is used to indicate the amount of numbers to be taken out of the puzzle for the Remove Numbers function.
   * Game function:
      * Uses window, window width/height, and difficulty number parameters
      * Calls the Make Level function
      * Plots 9x9 grid of buttons with borders on the window using the puzzle returned by the Make Level function
      * Plots a row of buttons from 1 - 9 used for the input
      * Plots check the puzzle button.
      * Background music starts
      * While the game is running, each click is checked to see if it clicked a button on the puzzle or one of the input buttons.
         * If an input button is clicked, then the button highlights yellow, sound is played, and the number on the button is stored. If an empty space on the puzzle is clicked afterwards, the number is put on the space
         * If a puzzle button is clicked, it highlights yellow and sound is played
      * When the check button is clicked, the check answer function is called and the result is displayed with corresponding audio.
      * Try again and quit buttons are plotted. IF try again is clicked, then newGame = True is returned
   * * graphics.py: This Graphics library implements the frontend computer graphics for the GUI of the game. 
* audioplayer.py: This audio player library provides a basic audio player without external modules that allows the Sudoku file to play sound. 
* Button.py: This button class file incorporates the functionality and design of a button function once it’s called in the main Sudoku pain. Some aspects of code come from Zelle. 
   * Initial variables:
      * w, h, x, y, the drawing of the rectangle function, label function of the button, and status of button when activated and activated
   * Label Function: 
      * Sets the label style of the button
      * Rectangle Function:
         * Sets the rectangle style of the button
* Clicked Function: 
   * Tests if user’s click within a button and activates or deactivates the button
   * Get’s x and y points of user’s click
* Undraw Function: 
      * Undraws both label and rectangle aspect of button when called
* Activate/Deactivate Function: 
      * Changes active status to either activate or deactivate
      * Changes label color if needed
* getStatus Function: 
      * Returns the button status
What kinds of testing have you done?
* Used the print grid function in the sudoku class to check if the backtracking algorithm for the puzzle generation worked correctly.
* Random generation of puzzle grid every time the game is called, having a random generated key every time 
* Used trial and error to find the correct coordinates for the buttons on the graphical window.
* Tested if audio played at appropriate times when a button is clicked.
* Tested the flow of the main menu (start -> instruction -> difficulty)
* Tested if the number from the input buttons worked to put the numbers on the empty puzzle spaces. Also tested to make sure that the pre-filled numbers on the grid couldn’t be changed by the input list.
* What improvements do we need for the future?
* Implement a “back” function, so the user can be able to return to the previous slide/menu when clicking through buttons before the game begins/
* Add visual for the instructions for the users
   * We planned to add a .gif demonstration of the game, but it became one of our hardest challenges during the project, we had to cut it short. 
* Display the instructions graphics during the game, when the function is called through a button, it won’t undraw the grid or lose the data stored when the user is filling in the grid.
* User shouldn’t be penalized entirely for getting one square wrong; give the user the option to continue filling the grid if they got it wrong the previous time. 
* Add a timer for the user to keep track of how fast they can solve the puzzle


Links
Backtracking help and Backend for the game:
* https://python.plainenglish.io/solve-a-sudoku-puzzle-using-backtracking-in-python-8e9eb58e57e6
* https://www.101computing.net/sudoku-generator-algorithm/


Audio files for the game:
* Instrumental Sound of Game: https://www.youtube.com/watch?v=xmBfruermmo (C418 - Mall)
* Boo Track: https://www.youtube.com/watch?v=y1U6g-kJ5og
* Yay Track: https://www.youtube.com/watch?v=attUrDwfdr8
* Button Click: https://www.youtube.com/watch?v=h8y0JMVwdmM


Potential Future, implementing a .gif for gameplay demonstration in instructions:
* https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/
* https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
* https://www.soydemac.com/en/extrae-fotogramas-de-gifs-animados-en-vista-previa/