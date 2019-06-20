class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def eat(self, food):
        if(food == "apple"):
            self.health -= 100
        elif (food == "ham"):
            self.health += 20
Bob = Hero("Bob")
print(__main__.Hero)
print (Bob.name)
print (Bob.health)
Bob.eat("apple")
print (Bob.health)
