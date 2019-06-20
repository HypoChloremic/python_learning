import sys
from PyQt4 import QtGui

'''
Object oriented programming is important for dynamic GUI programs
'''


class Window(QtGui.QMainWindow):
    def __init__ (self): # self is obligatory
        super(Window, self).__init__() #super tells what the parent object is...
        self.setGeometry(50, 50, 500, 300) # instead of writing Window.setblabla, we write self.blabla
        self.setWindowTitle("1aRa1")
        self.setWindowIcon(QtGui.QToon(''))
