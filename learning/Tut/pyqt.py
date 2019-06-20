import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv) # Important to have an app definition
'''
Worth noting that sys.argv permits passing arguments in the command-line (requires further research)
'''

window = QtGui.QWidget() #Qt's method always has a Q in front of them
window.setGeometry(50, 50, 500, 300)

'''here the first is (x, y (latter two from top left of the screen), 500 wide, 300 tall)
Furthermore, this setGeometry will tell how the application in itself will look like

Worth noting is also that there is a frame and there is a window to an application (or GUI based program), specifically
the window does not represent the frame containing the red "X" but borders with the frames inner borders.
'''


window.setWindowTitle("Tutorial")
window.show() # everything is created in the background, then this shows the app
