






class Celsius:
    def __init__(self, temperature = 0):
        # We initialize this, and it seems to be used
        # only by to_fahrenheit. However
        # as we wish to update this shit, we will not want to use it
        self.temperature = temperature 
        

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
        
    def bla(self, a):
        print("bla")
    # vad detta gör är att den kommer att länka temperature med get_temperature och set_temperature
    # varav dessa två kommer att run så fort man equatar variabeln med något
    # eller så länge man initialize it. 

    # Tittar man the docs verkar det som att property är konstruerad som följande:
    # property(fget=None, fset=None ...) Det verkar som att fset kommer att kallas
    # när man först settar temperatur för ngt. 
    # å andra sidan, fget kommer att bli run, när variabeln blir kallad ngnstans typ 
    # print(temperature)
    # fget verkar endast fungera om man kallar variabeln genom att göra
    # obj.temperature, och att det inte fungerar from inside of the function. 
    temperature = property(get_temperature, set_temperature)

if __name__ == '__main__':
    a = Celsius(5)
    a.temperature