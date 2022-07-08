#COM110, Final Project, Sudoku; Sudoku Class | Due: Dec 20
#Authors: Humza Rao (hrao@conncoll.edu) and Jangael Rosales (jrosales1@conncoll.edu)
#This file runs the Sudoku game

#libraries used for the game
from graphics import * #using graphics library to have GUI
from audioplayer import * #audio file player made by Professor Lee

from Button import * #using button class to incorporate functionality of button
from random import* #using random library to randomnize puzzzles

# Color Code table: https://wiki.tcl-lang.org/page/Colors+with+Names
# Audio files come from Youtube

class Sudoku:

    def __init__(self): #creates the sudoku grid with 9 rows and 9 columns
        self.puzzle = []
        for x in range(9):
            self.puzzle.append([])
            for y in range(9):
                self.puzzle[x].append(0)
        

    def printGrid(self, puzzle): #prints the grid
        for i in range(len(puzzle)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            
            for j in range(len(puzzle[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(puzzle[i][j])
                else:
                    print(str(puzzle[i][j]) + " ", end="")

    def checkGrid(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.puzzle[row][col]==0:
                  return False

        #We have a complete grid!  
        return True

    def makeGrid(self): #creates the grid and seperates the grid by squares, rows, and columns
    # Source: https://www.101computing.net/sudoku-generator-algorithm/
    ## The source helped us identifying squares within the puzzle
    
        numberList=[1,2,3,4,5,6,7,8,9]
        for i in range(81): #creates 81 squares for 9x9 grid
            row=i//9 #creates 9 rows
            col=i%9 #creates 9 columns
            if self.puzzle[row][col]==0:
                shuffle(numberList)      
                for value in numberList:
                    #Check that this value has not already be used on this row
                    if not(value in self.puzzle[row]):
                        #Check that this value has not already be used on this column
                        if not value in (self.puzzle[0][col],self.puzzle[1][col],self.puzzle[2][col],self.puzzle[3][col],self.puzzle[4][col],self.puzzle[5][col],self.puzzle[6][col],self.puzzle[7][col],self.puzzle[8][col]):
                            #Identify which of the 9 squares we are working on
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[self.puzzle[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[self.puzzle[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[self.puzzle[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[self.puzzle[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[self.puzzle[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[self.puzzle[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[self.puzzle[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[self.puzzle[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[self.puzzle[i][6:9] for i in range(6,9)]
                            #Check that this value has not already be used on this 3x3 square
                            if not value in (square[0] + square[1] + square[2]):
                                self.puzzle[row][col]=value

                                #check grid
                                if self.checkGrid():
                                    return self.puzzle                                    
                                else:
                                    if self.makeGrid():
                                        return self.puzzle
                                    

                break
        self.puzzle[row][col]=0

    def removeNums(self, n):
        #Make copy of puzzle
        incPuzzle = []
        for x in range(9):
            incPuzzle.append([])
            for y in range(9):
                incPuzzle[x].append(0)
        for i in range(81):
            row=i//9
            col=i%9
            incPuzzle[row][col] = self.puzzle[row][col]

        #remove numbers
        for i in range(n):
            while True:
                row = randint(0,8)
                col = randint(0,8)
                if incPuzzle[row][col] == 0:
                    #redo
                    pass
                else:
                    incPuzzle[row][col] = 0
                    break

        return incPuzzle

    def checkAnswer(self, buttons):
        correct = True
        for i in range(0,81):
            row=i//9
            col=i%9
            if buttons[row][col].getLabel() == ' ':
                num = 0
            else:
                num = int(buttons[row][col].getLabel())

            #checks if user input is same as corresponding space of answer key
            if buttons[row][col].getStatus() == True:
                if num == self.puzzle[row][col]:
                    buttons[row][col].buttonColor('lightgreen')
                else:
                    buttons[row][col].buttonColor('lightcoral')
                    correct = False

        #return true or false whether puzzle is correct
        return correct
    
def titlescreen(): #opening title screen for the game
    WIN_WIDTH = 550
    WIN_HEIGHT = 700
    win = GraphWin("Sudoku", WIN_WIDTH, WIN_HEIGHT)
    win.setBackground("dark olive green") #sets the background color

    Rectborder = Rectangle(Point(50,50), Point(500,650)) 
    Rectborder.setFill('white smoke')
    Rectborder.setWidth(6)
    Rectborder.draw(win)

    Title = Text(Point(275, 350), "S U D O K U")
    Title.setFace("times roman")
    Title.setSize(36)
    Title.setStyle("bold italic")
    Title.draw(win)

    start = Button(win, Point(275, 400), 130, 40, 'START') 
    start.buttonColor('lime green')
    start.buttonOutline('black')
    start.buttonWidth(2)
    start.labelSize(15)

    quitBtn = Button(win, Point(445, 80), 90, 40, 'QUIT') 
    quitBtn.buttonColor('white')
    quitBtn.buttonOutline('black')
    quitBtn.buttonWidth(2)
    quitBtn.labelSize(15)

    #click checking
    pt = win.getMouse()
    menu = True
    while menu:
        #if start is clicked
        if start.clicked(pt):
            startSound('buttonClick.wav', asyncPlay=True, loop=False) #calls buttonClick audio file 
            #undraw everything
            start.undraw()

            Instborder = Rectangle(Point(70,250), Point(480,450))
            Instborder.setFill('white')
            Instborder.setWidth(2)
            Instborder.draw(win)
    
            Instrtit = Text(Point(275, 230), "I N S T R U C T I O N S")
            Instrtit.setFace("times roman")
            Instrtit.setSize(20)
            Instrtit.setStyle("bold italic")
            Instrtit.draw(win)

            Instrdes = Text(Point(275, 350), "In order to solve a Sudoku puzzle, you need to fill in the spaces\nwith the numbers 1-9 without repeating any numbers\nwithin each row, column, and squares.\nTo play the game, you need to click on the row that has all\n1-9 below the grid and make your guess on which numbers are \nmissing by picking your number and filling it into the grid. ")
            Instrdes.setFace("times roman")
            Instrdes.setSize(14)
            Instrdes.setStyle("bold italic")
            Instrdes.draw(win)

            #asks user to continue clicking to get to the game
            readyBtn = Button(win, Point(275, 500), 150, 40, 'READY TO PLAY?') 
            readyBtn.buttonColor('white')
            readyBtn.buttonOutline('black')
            readyBtn.buttonWidth(2)
            readyBtn.labelSize(15)
            
            menu = False
   
    inst = True
    while inst:
        if readyBtn.clicked(pt):
            startSound('buttonClick.wav', asyncPlay=True, loop=False) #calls buttonClick audio file 
            #undraws the instruction objects
            Instborder.undraw()
            Instrtit.undraw()
            Instrdes.undraw()
            readyBtn.undraw()
            
            #draw difficulty buttons
            easyBtn = Button(win, Point(275, 400), 130, 40, 'EASY')
            easyBtn.buttonColor('lime green')
            easyBtn.buttonOutline('black')
            easyBtn.buttonWidth(2)
            easyBtn.labelSize(15)

            medBtn = Button(win, Point(275, 450), 130, 40, 'MEDIUM')
            medBtn.buttonColor('light goldenrod')
            medBtn.buttonOutline('black')
            medBtn.buttonWidth(2)
            medBtn.labelSize(15)

            hardBtn = Button(win, Point(275, 500), 130, 40, 'HARD')
            hardBtn.buttonColor('firebrick')
            hardBtn.buttonOutline('black')
            hardBtn.buttonWidth(2)
            hardBtn.labelSize(15)
            
            pt = win.getMouse()
            while True:
                if easyBtn.clicked(pt):
                    startSound('buttonClick.wav', asyncPlay=True, loop=False) #calls buttonClick audio file 
                    n = 35
                    break
                elif medBtn.clicked(pt):
                    startSound('buttonClick.wav', asyncPlay=True, loop=False) #calls buttonClick audio file 
                    n = 45
                    break
                elif hardBtn.clicked(pt):
                    startSound('buttonClick.wav', asyncPlay=True, loop=False) #calls buttonClick audio file 
                    n = 55
                    break

                pt = win.getMouse()
            break
                

        #if quit button is clicked
        if quitBtn.clicked(pt):
            break

        pt = win.getMouse()    

    win.close()

    return n
        
def makeLevel(n): 
    #generate incomplete puzzle

    sudoku = Sudoku()
    #delete key
    key = sudoku.makeGrid()
    
    #easy:30
    #medium:45
    #hard:60        
    puzzle = sudoku.removeNums(n)

    return sudoku, puzzle
    
def game(win, WIN_WIDTH, WIN_HEIGHT, difficulty):
    #class call
    s, puzzle = makeLevel(difficulty)
    
    #game
    x = 75
    y = 50
    btnList = []
    for row in range(len(puzzle)):
        #append sublist to list
        btnList.append([])
        for col in range(len(puzzle[0])):
            #make blank squares have active status
            if puzzle[row][col] == 0:
                active = True
                label = ' '
            #make filled squares have not active status
            else:
                active = False
                label = str(puzzle[row][col])

            #draw space with button class
            space = Button(win, Point(x,y), 50, 50, label)
            space.buttonColor('white')
            space.buttonOutline('black')
            space.labelSize(25)

            #actually deactivate or activate buttons
            if active == False:
                space.deactivate()
                space.labelStyle('bold')
                active = True
            elif active == True:
                space.activate()
                #space.labelColor('orange')

            #append space button to sublist                
            btnList[row].append(space)
            #if on last column
            if col == 8:
                #reset x value button
                x = 75
            else:
                #otherwise increase x value for button
                x+=50
        y+=50

    #draw input buttons
    x = 75
    inputList = []
    for i in range(1,10):
        inputBtn = Button(win, Point(x, 550), 50, 50, str(i))
        inputBtn.buttonColor('white')
        inputBtn.buttonOutline('black')
        inputBtn.labelSize(25)
        inputList.append(inputBtn)
        x+=50

    #draw check button
    checkButton = Button(win, Point(WIN_WIDTH/2, 650), 100, 50, 'Check')

    #BORDERS for each square within grid
    lineList = []
    #columns
    for col in range(50,501,150):
        for x in range(col-1,col+2):
            line = Line(Point(x,475), Point(x,50-25))
            line.draw(win)
            lineList.append(line)
    #rows
    for row in range(25,476,150):
        for y in range(row-1,row+2):
            line = Line(Point(50,y), Point(500,y))
            line.draw(win)
            lineList.append(line)

    #SUDOKU GAME
    #tracks user click
    running = True
    num = 0
    pt = win.getMouse()
    
    #place holder button
    btn = Button(win, Point(300, 300), 0, 0, '')
    
    while running:
        while not checkButton.clicked(pt):
            #tracks input list
            for button in inputList:
                if button.clicked(pt):
                    startSound('buttonClick.wav', asyncPlay=True, loop=False) #calls buttonClick audio file 
                    btn = button
                    button.buttonColor('yellow')
                    num = button.getLabel()

            #tracks puzzle list
            for row in btnList:
                for button in row:
                    if button.clicked(pt):
                        startSound('buttonClick.wav', asyncPlay=True, loop=False) #calls buttonClick audio file 
                        btn = button
                        
                        #highlight
                        button.buttonColor('yellow')
                        
                        #if no input is selected
                        if num != 0:
                            #if button is active (aka if button doesn't already have a number)
                            if button.getStatus() == True:
                                button.setLabel(num)
                                num = 0
                        
            pt = win.getMouse()
            btn.buttonColor('white')
        
        running = False

    #stop instrumental audio for the game
    stopSound()

    #undraw input buttons and check button and borders
    checkButton.undraw()
    for button in inputList:
        button.undraw()
    for line in lineList:
        line.undraw()
    
    #sets up rectangle box behind "result"
    Resborder = Rectangle(Point(WIN_WIDTH/2 - 110, 500), Point(WIN_WIDTH/2 + 110, 540)) 
    Resborder.setFill('white smoke')
    Resborder.setWidth(2)
    
    #Check answer and display result
    correct = s.checkAnswer(btnList)
    if correct: #if user solves the sudoku puzzle successfully
        startSound('KidsCheering_WON.wav', asyncPlay=True, loop=False) #Kids Cheering audio plays if won; Source: https://www.youtube.com/watch?v=_Z3ra0CxCE0
        result = Text(Point(WIN_WIDTH/2, 520),'GOOD JOB!')
        result.setFill('green')
    else: #if user doesn't solve the sudoku puzzle successfully
        startSound('CROWDBOO_LOSE.wav', asyncPlay=True, loop=False) #Crowd Boos audio plays if lost; Source: https://www.youtube.com/watch?v=y1U6g-kJ5og
        result = Text(Point(WIN_WIDTH/2, 520),'WRONG')
        result.setFill('red')

    Resborder.draw(win)
    result.setStyle('bold')
    result.setSize(36)
    result.draw(win)
    
    #try again / quit buttons
    tryAgain = Button(win, Point(WIN_WIDTH/4, 570), 100, 50, 'Try Again?')
    quitButton = Button(win, Point(3*WIN_WIDTH/4, 570), 100, 50, 'Quit')

    pt = win.getMouse()
    #running = True
    while True:
        if tryAgain.clicked(pt):
            stopSound() #stops instrumental sound
            startSound('buttonClick.wav', asyncPlay=True, loop=False) #calls buttonClick audio file 
            #undraw everything
            tryAgain.undraw()
            quitButton.undraw()
            result.undraw()
            Resborder.undraw()
            for row in btnList:
                for button in row:
                    button.undraw()    
            newGame = True
            break
        elif quitButton.clicked(pt):
            newGame = False
            stopSound() #stops instrumental sound
            break
        pt = win.getMouse()
            
    return newGame

def main(): 
    difficulty = titlescreen()
    
    #game window
    WIN_WIDTH = 550
    WIN_HEIGHT = 700
    win = GraphWin("Sudoku", WIN_WIDTH, WIN_HEIGHT)
    win.setBackground("dark olive green") #sets the background color
    
    newGame = True
    while newGame:
        startSound('introMusic_C418.wav', asyncPlay=True, loop=True) #restarts sound
        newGame = game(win, WIN_WIDTH, WIN_HEIGHT, difficulty)

    win.close()
    
main()
