from fighter import Fighter

# Создаем экземпляры бойцов
fighter1 = Fighter("Боец 1")
fighter2 = Fighter("Боец 2")

# Начинаем бой до тех пор, пока один из бойцов не умрет
while fighter1.is_alive() and fighter2.is_alive():
    fighter1.attack(fighter2)
    fighter2.attack(fighter1)

# Определяем победителя
if fighter1.is_alive():
    print(f"{fighter1.name} победил!")
elif fighter2.is_alive():
    print(f"{fighter2.name} победил!")
else:
    print("Ничья!")
