import requests as r

data = r.get("https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?transform=rdiff", params=None)
data = data.text

with open("new.txt", "w") as file:
    data = data.replace("],","\n").replace("[","")
    file.write(data)
