import random

class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        

    def attack(self, opponent):
        damage = random.randint(5, 15)
        if self.is_blocked():
            damage = damage // 2  # Наносим половину урона при блокировке
            print('=' * 30)
            print(f"{self.name} атакует, но {opponent.name} блокирует атаку.\nПоловина урона нанесена: {damage}")
            print()
        else:
            print('=' * 30)
            print(f"{self.name} атакует {opponent.name} и наносит {damage} урона.")
        opponent.health -= damage
        
    def is_blocked(self):
        return random.random() < 0.3 # 30% шанс блокировки

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health