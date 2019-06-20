import urllib.request
import urllib.error

# instance.read() returns the data retrieved from the site
# instance.info() returns the HTTP message from the server, includes cookie and server type
# instance.geturl() returns the requested url
# instance.getcode() returns the HTTP status code

# Retrieve Data from Google

def retriever():
    url = str("http://") + str(input("Enter the url: \n >"))
    website = urllib.request.urlopen(url)
    print (website.info())

def html():
    url = str("http://") + str(input("Enter the url: \n >"))
    website = urllib.request.urlopen(url)
    print(website.read())


def main():
    print("Data retriever service")
    x = int(input ("HTTP response (1) or the source (2)"))

    if x == 1:
        retriever()
    elif x == 2:
        html()
    else:
        print("Error, restart the program.")





if __name__ == "__main__":
    main()
