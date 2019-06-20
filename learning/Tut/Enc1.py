import sys

def main():
    print('1aRa1 /n Simple Encryption Program')
    toEnc = input(">")
    lengthEnc = len(toEnc)  
    encText = ""
    while lengthEnc >= 0:
        encText = encText + toEnc[lengthEnc]
        lengthEnc -= 1
    print (encText)

if __name__ == "__main__":
    main()
print()
