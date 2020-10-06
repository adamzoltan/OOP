class Plant():
    def __init__(self, color):
        self.color = color
        self.water_level = 0
        self.water_threshold = 0
        self.absorbtion = 0
        self.type = "Plant"

    def needs_water(self):
        return self.water_level < self.water_threshold

    def status(self):
        print(f"The {self.color} {self.type}", "needs water." if self.needs_water() else "doesn't need water.")

class Tree(Plant):
    def __init__(self,color):
        super().__init__(color)
        self.water_threshold = 10
        self.absorbtion = 0.4
        self.type = "Tree"

class Flower(Plant):
    def __init__(self,color):
        super().__init__(color)
        self.color = color
        self.water_threshold = 5
        self.absorbtion = 0.75
        self.type = "Flower"
