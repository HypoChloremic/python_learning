def function(a,b):
    mn = 5
    mx = 10
    b = 0

    if a < mn: 
      mn = a
      print(mn, mx, b, sep=" ")
    elif a > mx: 
      mx = a
      print(mn, mx, b, sep=" ")
    else:
     b += 1
     print(mn, mx, b, sep=" ")
    
#function(-2,7)

def l(x,y):
    if x > 2:
      if y > 4:
        print("blå")
      elif x == y: 
        print("gul")
      else: 
        print("röd")
    else:
      print("grön")
#l(4,4)

def l1():
    i = 0
    while i < 5:
      v = i * 2
      print(v, end=" ")
      i += 1
#l1()
def l3():
    v = 5
    while v > 5:
      print("hej")
      v += 1
    print("hej")
#l3()

def l4():
    i = 3
    while i < 8:
      print("a", end=" ")
      if i > 5:
        print("b", end=" ")
      i += 1
#l4()

def l5():
    a = -1
    b = -11
    if a <= b:
      print("r", end=" ")
      print("s", end=" ")
    else:
      print("t", end=" ")
#l5()

def l6():
    a = -5
    MITTEN = 6

    if a <= MITTEN:
      print("e", end=" ")
      print("f", end=" ")
    else:
      print("g", end=" ")
    print("h", end=" ")
#l6()

def l7():
    mn = 5
    mx = 10
    b = 0
    a = 12

    if a < mn:
      mn = a
      print(mn, mx, b, sep=" ")
    elif a > mx:
      mx = a
      print(mn, mx, b, sep=" ")
    else:
      b += 1
      print(mn, mx, b, sep=" ")
#l7()

def l8():
    a = -5
    mn = 10
    mx = 55
    b = 0

    if a == mn:
      mn = a
      print(mn, mx, b, sep=" ")
    elif a > mx:
      mx = a
      print(mn, mx, b, sep=" ")
    else:
      b += 1
      print(mn, mx, b, sep=" ")
#l8()

def loop():
    j = 1 
    namn=["a","a","a"]
    s = namn[0]
    while j < 3: 
        s += namn[j] 
        j += 1 
    print(s)
#loop()

def l9():
    a = -2
    b = a
    c = a + b + 3
    d = c - b
    print(d)

l9()
