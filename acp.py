class Robots:
    species = "robot"

    def __init__(self, name):
        self.name = name
    
tom = Robots("Tom")
jerry = Robots("Jerry")

print("Hi, my name is {} and i am a robot.".format(tom.name))
print("Hi, my name is {} and i am also a robot.".format(jerry.name))