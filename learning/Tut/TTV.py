import sys
import urllib.request
import urllib.parse
import re

'''
Regular expressions:

Identifiers (looking for this or that):

\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
.  any character, except for a newline
\b the whitespace around words
\. a period

Modifiers (looking)

{1, 3} e.g. \d{1,3) we are looking for digits 1-3 in length
+ Match 1 or more, \d+ will match one or more of the digits
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ matching the beginning of a string
| Matching either or, \d{1,3} | \w{5-6} digit one to three in length or character 5-6 in length
[] range or "variance" e.g. [A-Z] looking for cap. A to Z, [1-5a-qA-Z] looking for 1 to 5 followed by a to q followed by anything with A to Z
{x} expecting 'x' amount

White Space Characters (characters you do not see):
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

DO NOT FORGET:

. + * ? [] $ ^() {} | \ if you want to use these, one must escape them

'''

def inter():
    url = "http://www.reuters.com/news/archive/worldNews?view=page"
    source = urllib.request.urlopen(url)
    sourceText = str(source.read())
    p = re.findall(r'<h2>(\S.*?)/a>', str(sourceText))
    P = re.findall(r'>(\S.*?)<', str(p))
    for eachP in P:
        eachP += ".\n"
        print (eachP)
        
def dom():
    url = "http://texttv.nu/101"
    source = urllib.request.urlopen(url)
    sourceText = str(source.read())
    paragraphs = re.findall(r'<span class="W">(\w.*?)\.', str(sourceText))
    for eachP in paragraphs:
        print(eachP)


def main():
    print("\nWelcome to the Text TV News Feed")
    print("International (1) or domestic (2):")
    x = int(input())
    
    if x == 1:
        inter()

        try:
            Q = str(input("Would you like to restart the program y/n: "))
            if Q == "y":
                main()
            else:
                exit()
        except:
            print("This is the exception: ")
            main()
        
    elif x == 2:
        dom()

        try:
            Q = str(input("Would you like to restart the program y/n: "))
            if Q == "y":
                main()
            else:
                exit()
        except:
            print("This is the exception: ")
            main()
        
    else:
        print("Error, the program will be restarted.")
        input("Press any button.")
        main()


if __name__ == "__main__":  
        main()
