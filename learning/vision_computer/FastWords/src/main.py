from Fast import FastWords
import time
from ButtonInterrupt import ButtonInterrupt

def main():
    FW = FastWords(no_dims=True)
    BI = ButtonInterrupt()

    while True:
        if BI.switch.bool:
            print("Starting bot")
        if not BI.switch.bool:
            print("Restarted")
            BI.switch.bool = True
        word = ""
        for i in range(25):
            word_ = FW.read_screen()
            if word_ > word:
                word = word_
            print(word)
        
        if not BI.switch.bool:
            continue

        for k in word:
            FW.find_letter(k, BI)
            if not BI.switch.bool:
                break
            
if __name__ == "__main__":
    main()