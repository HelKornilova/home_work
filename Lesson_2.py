#Задание 1

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - завершение программы.
"""

tasks = []

while True:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks)
    elif command == 'add':
        task = input('Введите название задачи: ')
        tasks.append(task)
        print('Задача добавлена!')
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда.')
        print('До свидания!')
        break

#print('До свидания!')

#Задание 2

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - завершение программы.
"""
from datetime import datetime  #получение текущей даты с помощью библиотеки datetime
date_today = datetime.now()

tasks_today = []
tasks_tomorrow = []
tasks_other = []

while True:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print('Задачи на сегодня: ', tasks_today)
        print('Задачи на завтра: ', tasks_tomorrow)
        print('Другие задачи: ', tasks_other)
    elif command == 'add':
        task = input('Введите название задачи: ')
        date = input('Введите дату выполнения задачи (в формате день-месяц-год): ')
        try:  # использование try-except для обработки ошибок при неправильном формате даты
            date = datetime.strptime(date, '%d-%m-%Y')  # переводим сразу в 'datetime.datetime'
        except ValueError:  # в случае неверного ввода сообщаем об ошибке и запускаем цикл заново
            print('Убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024.')
            print('Пожалуйста, попробуйте еще раз!')
            continue
        time_difference = date - date_today  # получение разницы в днях, <class 'datetime.timedelta'>
        days_difference = time_difference.days + 1  # получение разницы в днях, <class 'int'>
        if days_difference == 0:
            tasks_today.append(task)
            print('Задача добавлена!')
        elif days_difference == 1:
            tasks_tomorrow.append(task)
            print('Задача добавлена!')
        else:
            tasks_other.append(task)
            print('Задача добавлена!')
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команда.')
        print('До свидания!')
        break