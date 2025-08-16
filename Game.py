import random

player_wins = 0
computer_wins = 0
choices = ['камень', 'ножницы', 'бумага']

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
print("Играем до 3 побед. Варианты: камень, ножницы, бумага")

while player_wins < 3 and computer_wins < 3:
    player_choice = input("Ваш выбор: ").lower()
    while player_choice not in choices:
        print("Ошибка! Выберите: камень, ножницы или бумага")
        player_choice = input("Ваш выбор: ").lower()

    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
            (player_choice == 'ножницы' and computer_choice == 'бумага') or \
            (player_choice == 'бумага' and computer_choice == 'камень'):
        player_wins += 1
        print(f"Вы победили! Счет: {player_wins}-{computer_wins}")
    else:
        computer_wins += 1
        print(f"Компьютер победил! Счет: {player_wins}-{computer_wins}")

# Финал с исправленными f-строками
if player_wins == 3:
    print(f"\nПоздравляем! Вы выиграли игру со счетом 3-{computer_wins}!")
else:
    print(f"\nК сожалению, компьютер выиграл игру со счетом {player_wins}-3!")
