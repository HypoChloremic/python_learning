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


exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}',exampleString)
names= re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

ageDict= {}

for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1










