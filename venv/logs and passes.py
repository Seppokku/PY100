log = ["Pam", "Angela", "Dwight", "Jim"]
pas = [12345, 23456, 34567, 45678]
user_log = input()
if user_log in log:
    print("Введите пароль, ", user_log)
    user_pas = int(input())
    if user_pas in pas and log.index(user_log) == pas.index(user_pas):
        print("Доступ получен")
    else:
        print("Логин или пароль введен неверно")
else:
    print("Такого пользователя нет")
