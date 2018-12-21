from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):  # 6面的骰子
        x = randint(1, self.sides)
        print(x)


die6 = Die()
die6.roll_die()
die10 = Die(10)
die10.roll_die()
die20 = Die(20)
die20.roll_die()
