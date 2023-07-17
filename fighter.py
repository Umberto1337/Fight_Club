import random

class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = random.randint(5, 15)
        self.turn = random.choice([True, False])

    def attack(self, opponent):
        if self.turn:
            print(f"{self.name} атакует {opponent.name} и наносит {self.damage} урона.")
            opponent.health -= self.damage
        else:
            print(f"{opponent.name} атакует {self.name} и наносит {opponent.damage} урона.")
            self.health -= opponent.damage

        self.turn = not self.turn

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health
