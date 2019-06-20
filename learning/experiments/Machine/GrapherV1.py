import matplotlib.pyplot as plt
from scipy.interpolate import spline, UnivariateSpline
import numpy as np

'''
This source-code will not be manipulated further, but will instead be used as a reference for future programs
incorporating similar aspects. The functionality of the UnvariateSpline is interesting as it replaced spline,
furthermor it could assimilate values above 245.

The limit of 245 for spline is strange. Perhaps there is a max amount of x values it may treat, whereas the
UnvariateSpline is indifferent towards values beteen 246 and 1336; larger values that 1336 have not been investigated. 
'''

def main():
    dataFile = input("Plase input the name of the data-file: ")
    with open(dataFile, "r") as file:
        data = file.read()
    data = data.split("\n")
    x = [row.split(" ")[0] for row in data[:1336]]
    y = [row.split(" ")[1] for row in data[:1336]]
    x = np.array(x)
    x = x.astype(np.float)
    y = np.array(y)
    y = y.astype(np.float)

    x2 = np.linspace(x.min(), x.max(), 4000)
    y2 = spline(x,y,x2, 3)

    print(y2)
    with open("random.txt", "w") as file:
        a = 0
        x3 = x2.tolist()
        y3 = y2.tolist()
        for each in x3:
            file.write(str(each) + " " + str(y3[a]) + "\n")
            a +=1

    sp1 = UnivariateSpline(x,y) # Seemingly, this function is similar to spline, however functions better with larger values.
                                # It was discovered that spline does not like x-values going beyond 245; the source of the problem is being searched for.
                                # UnvariateSpline(x,y) is offering better functionality. Resultantly, the other programs incorporating spline will be converte to UnvariateSpline instead
    xs = np.linspace(x.min(), x.max(), 5000) # This incorporates the normal x.min x.max etc. 
    j1 = plt.figure()
    j = j1.add_subplot(111) # The add_subplot is necessary in order to permit define the figure for the subsequent .plot (matplot does not like it otherwise)
                            # Also the 111 merely refers to the dimensions of the figure, which is not important, simply aesthetic
    j.plot(xs, sp1(xs), "g", lw=3) # What is the purpose of the sp1(xs), why are parenthesis involved. Is sp1 not a variable? After further study, it became apparent that sp1 was a function, into which
                            # values could be parsed, note its definition. 
                            # What is the function of the 'g'. The source files of .plot must be scrutinized. 

    k1 = plt.figure()
    k = k1.add_subplot(111)
    k.plot(x,y)

if __name__=="__main__":
    main()
