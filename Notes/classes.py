# CB 1st Classes

class Stats:
    def __init__(self,health,offense,defense,speed):
        self.health = health
        self.offense = offense
        self.defense = defense
        self.speed = speed

    def print_stats(self):
        print(f"Health: {self.health}")
        print(f"Offense: {self.offense}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        

player = Stats(100,10,10,10)
player.print_stats()

player.health -= 99
player.print_stats()


if player.health <= 0:
    print("You died!")
else:
    pass


