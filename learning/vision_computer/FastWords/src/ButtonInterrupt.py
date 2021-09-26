import tkinter as tk    
import time      
import threading

class SWITCH:
    def __init__(self):
        self.bool = True

    def on(self):      
        print('switch on')
        self.bool = True  
        
    def off(self):    
        print('switch off')
        self.bool = False
    
    def kill(self):    
        #self.root.destroy()    
        pass

class ButtonInterrupt(threading.Thread):
    '''ButtoInterrupts
    
    Info:
        Creates interrupt buttons to be used in a game

    Args:
        root:   tkinter root object.
    '''
    def __init__(self):

        super().__init__()
        self.start()
        # Important instanitation of the variable obj
        self.switch = SWITCH()
    
    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol('WM_DELETE_WINDOW', self.callback)


        # Create the buttons and run the mainloop
        self.create_buttons()
        self.root.mainloop() 

    def create_buttons(self):
        '''ButtonInterrupts
        Create buttons with tkinter
        
        Args:
            self
        
        '''
        self.onbutton = tk.Button(self.root, text = "Blink ON", command = self.switch.on)    
        self.offbutton =  tk.Button(self.root, text = "Blink OFF", command = self.switch.off)    
        self.killbutton = tk.Button(self.root, text = "EXIT", command = self.switch.kill)    
        self.onbutton.pack()    
        self.offbutton.pack()    
        self.killbutton.pack()        

if __name__ == "__main__":
    BI = ButtonInterrupt()
    print("parallel")