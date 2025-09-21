class Human():
    def __init__(self, name, high, weight,eyes):
        self.name = name
        self.high = high
        self.weight = weight
        self.eyes = eyes

    def printf(self):
        print(self.name, self.high, self.eyes, self.weight)

    def grow(self, high = 1):
        self.high += high

peter = Human("Peter",170 , 60, "blue")

peter.printf()
peter.grow(10)
peter.printf()