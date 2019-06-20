import sys
import urllib.request
import re

def main():
    print("DN Reader")
    url = input("Paste in the url for the desired article:\n")
    request = urllib.request.urlopen(url)
    source = str(request.read())
    pgraphs = re.findall(r'<p>(.*?)</p>', str(source))
    for eachp in pgraphs:
        x = eachp + "\n"
        print(x)
    input("Return to exit.")

if __name__== "__main__":
    main()
