from bs4 import BeautifulSoup as bs4
from urllib.request import urlopen, Request, urlretrieve
import os

url  = "https://www.google.se/search?hl=sv&site=imghp&tbm=isch&source=hp&q=hej"
html =  urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
soup = bs4(html, "html.parser")
# It took a while to figure this out;
# firstly, as soup accepts kwargs, or dicts, it implies that we can write
# previously undefined arguments, and then equate them to whatever
# and we will get a dict. This implies that img is given as tuple, and
# alt="Bildresultat för hej" is given as a dict. 
# secondly, we were forced to look at the info, that the 
# our own script instance of the webpage was, because, it was different
# from the html that was present in the firefox browser
# which had given much trouble. 

# Hence, we parsed in the img tag, with the attribute alt="Bildresultat för hej" as
# a specifier för the tags we were interested in. 

# We tried with css selectors before, however, these came from our browser instance
# and therefore differed from the css selectors that the scraper would have to use. 
imgs = soup.find_all("img", alt="Bildresultat för hej") 


# Now we were interested in the src attribute, and as this is an object
# of its own, we had to tame the beast. Later on, it became evident that 
# we had to write it in a dict fashion to get the attribute data. 

imgUrl = imgs[2]["src"]
print(imgUrl)
print(os.path.basename(imgUrl))
urlretrieve(imgUrl, filename=os.path.basename("C:\Users\Ali Rassolie\OneDrive\prwork\python\learnin\beautifulsoup"))
