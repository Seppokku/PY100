prof = ['Азарт', 'Активность', 'Внимательность', 'Дисциплина',
        'Знания', 'Карьера', 'Квалификация', 'Компетентность', 'Ловкость',
        'Мастерство', 'Навык','Надежность', 'Независимость' , 'Образованность',
        'Определившийся', 'Опыт', 'Ответственность', 'Преданность делу', 'Признание',
        'Профессионализм', 'Радость', 'Самостоятельность', 'Собранность', 'Совершенствование',
         'Творчество', 'Труд', 'Уважение', 'Уверенность', 'Удача', 'Удовлетворенность', 'Ум',
        'Умение', 'Упорство', 'Успешность', 'Цель', 'Четкость', 'Энтузиазм','Эффективность']
nonprof = ['Безволие', 'Безделушки', 'Безработица', 'Дилетантство', 'Зануда', 'Запросы', 'Кризис', 'Лень', 'Медлительность',
           'Наивность', 'Начинающий', 'Неопытность', 'Неразборчивость', 'Нереализованность', 'Неспособность',
           'Обучающийся', 'Общение', 'Ошибки', 'Переоценка своих возможностей', 'Пессимизм', 'Подготовка',
           'Поддержка', 'Похвала', 'Претензии', 'Проба', 'Промахи', 'Работяга', 'Разноплановость', 'Растерянность',
           'Самолюбие', 'Скука', 'Сравнение', 'Старания', 'Тревога', 'Усердие', 'Ученичество', 'Хобби', 'Экзамен']
a = str(input())
count_prof = 0
count_non_prof = 0
for i in a.split(', '):
    if i in prof:
        count_prof += 1
    else:
        count_non_prof+= 1


print(round((count_prof/count_non_prof), 1))
#fgds