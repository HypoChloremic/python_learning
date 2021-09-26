import cv2
import mss
import pytesseract
import pyautogui
import re
import numpy as np
import time

from PIL import Image
from BoundBox import GUI


class FastWords:
    def __init__(self, no_dims=False):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Ali\AppData\Local\Tesseract-OCR\tesseract'

        self.SCT = mss.mss()
        if no_dims:
            gui = GUI()
            gui.mainloop()
            self.dimensions = {
                'left':     gui.bbox_r[0].get(),
                'top':      gui.bbox_r[1].get(),
                'width':    gui.bbox_r[2].get() - gui.bbox_r[0].get(),
                'height':   gui.bbox_r[3].get() - gui.bbox_r[1].get()
            }

            gui = GUI()
            gui.mainloop()
            self.dimensions_large = {
                'left':     gui.bbox_r[0].get(),
                'top':      gui.bbox_r[1].get(),
                'width':    gui.bbox_r[2].get() - gui.bbox_r[0].get(),
                'height':   gui.bbox_r[3].get() - gui.bbox_r[1].get()
            }

        else: 
            self.dimensions = {
                    'left': 787,
                    'top': 117,
                    'width': 1110,
                    'height': 195
                }
            
            self.dimensions_large = {
                    'left': 787,
                    'top': 117,
                    'width': 1110,
                    'height': 195
            }

        self.init_text_box(self.dimensions)

    def init_text_box(self, dims): 
        img = np.array(self.SCT.grab(dims))
        while True:
            cv2.imshow('', img)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

    def clean_text(self, tes_out:str) -> str:
        try: 
            res = re.search('[A-Z]+', tes_out).group()
        except AttributeError as e:
            res = ""
        print(tes_out)
        print(res)
        return res
    
    def convert_to_text(self, img): 
        txt = pytesseract.image_to_string(img)
        return self.clean_text(txt)

    def read_screen(self) -> str: 
        img = np.array(self.SCT.grab(self.dimensions))
        color = cv2.cvtColor(img, cv2.IMREAD_COLOR)
        return self.convert_to_text(color)

    def find_letter(self, letter, SwitchBool):
        '''Looks for letter
        
        Args:
            letter: letter to be looked for
            
        '''

        while SwitchBool.switch.bool:
            print('looking for letter')
            time.sleep(1)

        
            

if __name__ == '__main__':
    FW = FastWords(no_dims=True)
    print(FW.dimensions)