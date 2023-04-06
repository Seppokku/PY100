"""Готово......."""

NUMBERS_ = list(range(1, 10))

c = input("Приветствую Вас в игре крестики-нолики!\n"
          "Правила Вам известны.\n"
          "Для того, чтобы начать играть, введите сюда что-нибудь: ")


def game_board(numbers_: list):
    print("-" * 13)
    for i in range(3):
        print("|", numbers_[0 + i * 3], "|", numbers_[1 + i * 3], "|", numbers_[2 + i * 3], "|")
        print("-" * 13)


game_board(NUMBERS_)


def win_condition(numbers_: list) -> bool:
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    win = False
    for i in win_coord:
        if numbers_[i[0]] == numbers_[i[1]] == numbers_[i[2]]:
            print(f"Поздравляю с победой, игрок {numbers_[i[0]]}!!!!")
            win = True
            break
        else:
            win = False

    return win


while True:

    a = int(input("Ходит игрок X, введите номер клетки от 1 до 9: "))

    if a > 9 or a <= 0:
        print("Ошибочный ввод, повторите попытку")
        continue

    if str(NUMBERS_[a - 1]) in 'XO':
        print("Клетка уже занята, выберите другую")
        continue

    if a in NUMBERS_:
        NUMBERS_[a - 1] = "X"
        game_board(NUMBERS_)

    if win_condition(NUMBERS_):
        break

    b = int(input("Ходит игрок O, введите номер клетки от 1 до 9: "))

    if b > 9 or b <= 0:
        print("Ошибочный ввод, повторите попытку ")
        b = int(input("Ходит игрок O, введите номер клетки от 1 до 9: "))

    if str(NUMBERS_[b - 1]) in 'XO':
        print("Клетка уже занята, выберите другую")
        b = int(input("Ходит игрок O, введите номер клетки от 1 до 9: "))

    if b in NUMBERS_:
        NUMBERS_[b - 1] = "O"
        game_board(NUMBERS_)

    if win_condition(NUMBERS_):
        break
