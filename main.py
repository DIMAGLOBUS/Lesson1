import random
class  Humanoid:
    def __init__(self, name = 'Sim', job = None, home = None, car = None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.glladness = 50
        self.satiety = 50