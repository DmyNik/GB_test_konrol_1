
from logger import input_data, print_data, find_data

# Главный интерфейс программы
def interface(param = 0):
    
    if param == 1:
        print('> Доброго времени суток!\n'
              '> Вы находитесь в программе "Заметки"!')
    
    print('> Меню программы:\n'
          '> 1 - Добавить заметку\n'
          '> 2 - Вывести все заметки на экран\n'
          '> 3 - Найти / изменить / удалить заметку\n'
          '> 0 - Выйти из программы')
    
    comand = int(input('> '))

    while comand < 0 or 3 < comand:
        print('> Неправильный ввод')
        comand = int(input('> Введите число: '))

    if comand == 1:
        input_data()
    elif comand == 2:
        print_data()
    elif comand == 3:
        find_data_ui()
    elif comand == 0:
        print('> До новых встречь!')

# Интерфейс поиска заметок
def find_data_ui():
    
    print('> Как будем искать заметки: \n'
          '> 1 - По номеру\n'
          '> 2 - По дате\n'
          '> 3 - По заголовку\n'
          '> 4 - По содержанию\n'
          '> ', end='')
    
    comand_1 = int(input(''))

    while comand_1 < 1 or 4 < comand_1:
        print('> Неправильный ввод')
        comand_1 = int(input('> Введите число: '))
    
    find_data(comand_1)

