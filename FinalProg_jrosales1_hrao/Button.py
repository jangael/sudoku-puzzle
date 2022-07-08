# button.py
 # partial code from Zelle chapter 10 (pp. 324)

from graphics import *

#define button class
class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        #initialize variables
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()

        self.xmin, self.xmax = x - w, x + w
        self.ymin, self.ymax = y - h, y + h       

        #draw button rectangle
        self.rect = Rectangle(Point(self.xmin, self.ymin),Point(self.xmax, self.ymax))
        self.rect.setFill('lightgrey')
        self.rect.draw(win)

        #draw label
        self.label = Text(center, label)
        self.label.draw(win)

        #status
        self.active = True

    #label functions
    def labelFont(self, font, size, style, color):
        "Sets the font of button label"
        self.label.setFace(font)
    def labelSize(self, size):
        "Sets the size of button label"
        self.label.setSize(size)
    def labelStyle(self, style):
        "Sets the style of button label"
        self.label.setStyle(style)
    def labelColor(self, color):
        "Sets the color of button label"
        self.label.setFill(color)
    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()
    def setLabel(self, string):
        "Changes the label string of this button."
        self.label.setText(string)


    #rectangle functions
    def buttonColor(self, color):
        "Sets the color of button"
        self.rect.setFill(color)
    def buttonOutline(self, color):
        "Sets the outline color of button"
        self.rect.setOutline(color)
    def buttonWidth(self, width):
        "Sets outline width of button"
        self.rect.setWidth(width)
        

    def clicked(self, p):
        "Returns true if button active and p is inside"

        #test if the point is within the rect area
        if self.xmin < p.getX() < self.xmax and self.ymin < p.getY() < self.ymax:
            return True
        else:
            return False
        
    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def activate(self):
        "Sets this button to 'active'."
        #change label color to black
        self.label.setFill('black')

        #chage active status to true
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."

        #change label color to darkgrey
        self.label.setFill('black')

        #change active status to false
        self.active = False

    def getStatus(self):
        "Returns the button status"
        return self.active
    
def main():
    
    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    ##testing Button constructor
    rollButton = Button(win, Point(5,4), 6, 1, "Roll Dice")
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")

    rollButton.buttonColor('black')
    rollButton.buttonOutline('red')
    rollButton.labelColor('red')

    ##testing activate method
    ##rollButton.activate()

    ##testing clicked() method
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        #when roll button is clicked
        if rollButton.clicked(pt):
            #activate the quit button
            quitButton.activate()
        pt = win.getMouse()
    
    #if quit button is clicked, then loop is broken
    #and we reach this line of code
    win.close()
    
if __name__ == "__main__":
    main()
