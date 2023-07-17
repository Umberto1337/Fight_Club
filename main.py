from fighter import Fighter

# Создаем экземпляры бойцов
fighter1 = Fighter("Анакин")
fighter2 = Fighter("Бастиан")

# Начинаем бой до тех пор, пока один из бойцов не умрет
while fighter1.is_alive() and fighter2.is_alive():
    fighter1.attack(fighter2)
    if not fighter2.is_alive():
        break
    fighter2.attack(fighter1)

# Определяем победителя
if fighter1.is_alive():
    print(f"{fighter1.name} победил!")
elif fighter2.is_alive():
    print(f"{fighter2.name} победил!")
else:
    print("Ничья!")
