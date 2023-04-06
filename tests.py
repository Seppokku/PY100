"""Вот самый тестовый вариант,
Я сейчас пытаюсь реализовать то, что как только будет выявлен хоть 1 победитель, программа будет останавливаться,
но она ждет пока их не будет двое, а только потом выдает имя первого победителя,
программа так же не останавливается после нахождения победителя, видимо, где-то не там стоит break,
так же я не понимаю, почему функции и их вызовы подчеркнуты желтой линией """

NUMBERS_ = list(range(1, 10))
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))



def game_board(NUMBERS_):
    print("-" * 13)
    for i in range(3):
        print("|", NUMBERS_[i], "|", NUMBERS_[i + 3], "|", NUMBERS_[i + 6], "|")
        print("-" * 13)
game_board(NUMBERS_)

def win_condition(NUMBERS_):
    for i in win_coord:
        if NUMBERS_[i[0]] == NUMBERS_[i[1]] == NUMBERS_[i[2]]:
            print(f"Поздравляю с победой, игрок {NUMBERS_[i[0]]}!!!!")
            break
            return True


#def step(x):


#all(isinstance(item, str) for item in NUMBERS_):


while not win_condition(NUMBERS_):
    counter = 0

    a = int(input("Ходит игрок X, введите номер клетки: "))
    if a in NUMBERS_:
        NUMBERS_[a - 1] = "X"
        counter += 1
        game_board(NUMBERS_)

    b = int(input("Ходит игрок O, введите номер клетки: "))

    if b in NUMBERS_:
        NUMBERS_[b - 1] = "O"
        counter += 1
        game_board(NUMBERS_)

    if counter == 9:
        print("Больше некуда ходить..")
        break










































# def game_start():
#     game_board(NUMBERS_)
#     counter = 0
#     win = False
#     while not win:
#         game_board(NUMBERS_)
#         if counter % 2 == 0:
#             step("X")
#         else:
#             step("O")
#         counter += 1
#         if counter > 4:
#             tmp = win_condition(NUMBERS_)
#             if tmp:
#                 print
#                 tmp, "выиграл!"
#                 win = True
#                 break
#         if counter == 9:
#             print
#             "Ничья!"
#             break
#     game_board(NUMBERS_)
#
#
# game_start()



























