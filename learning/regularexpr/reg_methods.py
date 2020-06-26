import re


# An assertion: an assertion is defined as the following: '(?= . . .)' where ?= and the parenthesis are used.
# Assertions give up the match, and only return match or no match! it is almost binary boolean in nature. 
# So what is inside the (?= ...) will not be highlighted, i.e. matched. 
# Assertion: asserting presence of pattern

# POSITIVE: the assertion IS present
# 'Look-BEHIND' assertion: is using `<=` instead of `=` in the assertion, i.e. (?<= ...)
# The look-behind assertion refers to identifying an assertion (which does not highlight, instead just matched boolean wise, binary
# if it is there or not) BEFORE an expression. 
# Behind: (?<=  ), is preceeding our pattern.

# 'Look-AHEAD' is with `?=` (I guess searching for something behind...?)
# Ahead: this succeeds our pattern of interest

# Example:

t1 = '1: Hello there 2: World here'
re.search(r'(?<=\d:\W)([a-zA-Z\W]+)')
# will highlight the text after '1: '
# Several things is occurring:
# 1) Look-behind: (?<=\d:\W) which is saying that our pattern comes after a single digit ('\d'), a colon(':') and a whitespace ('\W')
# 2) our pattern inside the (...) which doesnt have the assertion parameter '?=' indicates that we are searching for:
# 2a) a-z any character a-z lowercase
# 2b) or A-Z any character A-Z uppercase
# 2c) or \W any non-character (e.g. whitespace) character
# 2d) grouped together, making them all or between each other with the hard brackets '[...]'
# 3e) '+' single or more of the stuff inside the brackets!

# NEGATIVE: the assertion is NOT persent
# negative look-behind: '(?<!  ...)' so instead of an '=' sign we get a '!' sign. 
# negative look-ahead: '(?! ...)'






