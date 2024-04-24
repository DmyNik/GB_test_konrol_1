
from data_create import content_data, date_data, index_data, topic_data

# Файл, содержащий базу данных заметок
db_file_name = 'data_base.csv'

# Перезапись файла 1
def write_file(strings): 
    
    with open(db_file_name, 'w', encoding='utf-8') as f:
        
        for i in strings:
            
            flg = False
            str = ''
            
            for j in i:
                if flg:
                    str += ';' + j
                else:
                    str += j
                    flg = True
            
            f.write(str)
            f.write('\n')
    
        print('> Внимание: файл "' + db_file_name + '" был перезаписан!')

    from ui import interface
    interface()   

# Манипуляции с заметками (на основе найденных в файле)
def edit_data(data_list, cmd, data_find): 

    cnt = 0 # Счетчик совпадений
    coincidence_list = list() # Список совпадений
    
    for i in data_list:
        if cmd == 1: # Поиск по номеру
            if i[0] == data_find:
                cnt += 1
                coincidence_list.append(i)
        elif cmd == 2: # Поиск по дате
            if data_find.lower() in i[1].lower():
                cnt += 1
                coincidence_list.append(i)
        elif cmd == 3: # Поиск по заголовку
            if data_find.lower() in i[2].lower():
                cnt += 1
                coincidence_list.append(i)
        elif cmd == 4: # Поиск по содержанию
            if data_find.lower() in i[3].lower():
                cnt += 1
                coincidence_list.append(i)

    print(f'> Найдено {cnt} совпадени(е/й):')
    
    if cnt < 1: 
        print('> Поэтому вернемся в главное меню.')
        from ui import interface
        interface()

    else:

        # Вывод списка совпадений
        for i in range(0, len(coincidence_list)):
            print('#' + str(i+1) + ':\t', end='')
            for j in range(0, len(coincidence_list[i])):
                if j != 0:
                    print('; ' + coincidence_list[i][j], end='')
                else:
                    print(coincidence_list[i][j], end='')
            print('')
        
        print('> Выберите одну заметку.\n'
              '> (Ведите порядковый номер совпадения или 0 для выхода в главное меню.)')
        edtNum = int(input('> '))

        while edtNum < 0 or cnt < edtNum:
            print('> Неправильный ввод')
            edtNum = int(input('> Введите число: '))

        # Если выбрана команда не "Выход в главное меню"
        if edtNum != 0:
            
            print('> Что-нибудь сделать с заметкой?\n'
                  '> (Подсказка: 1 - Вывести на экран в деталях, 2 - Изменить, 3 - Удалить, 0 - Выход в главное меню.)')
            edtNum2 = int(input('> '))

            while edtNum2 < 0 or 3 < edtNum2:
                print('> Неправильный ввод')
                edtNum2 = int(input('> Введите число: '))

            # Если не выбрана команда "Выход в главное меню"
            if edtNum2 != 0:

                tupleToEdit = coincidence_list[edtNum-1]
                
                # Если выбрана команда "Вывести на экран"
                if edtNum2 == 1:
                    print('> ----------------------------------------------------- ')
                    print('> Заметка № ' + tupleToEdit[0] + ' от ' +  tupleToEdit[1])
                    print('> Тема: ' + tupleToEdit[2])
                    print('> Содержание: ')
                    print('> ' + tupleToEdit[3])
                    print('> ----------------------------------------------------- ')

                    from ui import interface
                    interface()
                
                # Если выбрана команда "Изменить"
                if edtNum2 == 2:
                    
                    edit_date = date_data()
                    edit_topic = topic_data()
                    edit_content = content_data()
                
                    tupleNew = tuple([tupleToEdit[0], edit_date, edit_topic, edit_content])

                    print('> Записать: "', *tupleToEdit, '"')
                    print('> Будет заменена на: "', *tupleNew, '"')

                # Если выбрана команда "Изменить" или "Удалить"
                if edtNum2 == 2 or edtNum2 == 3:
                    
                    cnt = 0 # Еще раз считаем совпадения

                    for i in range(len(data_list)):                
                        
                        if cmd == 1: # Поиск по номеру
                            if data_list[i][0] == data_find:
                                cnt += 1
                                if cnt == edtNum:
                                    if edtNum2 == 2:
                                        data_list[i] = tupleNew
                                    elif edtNum2 == 3:
                                        ii = i

                        elif cmd == 2: # Поиск по дате
                            if data_find in data_list[i][1]:
                                cnt += 1
                                if cnt == edtNum:
                                    if edtNum2 == 2:
                                        data_list[i] = tupleNew
                                    elif edtNum2 == 3:
                                        ii = i

                        elif cmd == 3: # Поиск по заголовку
                            if data_find in data_list[i][2]:
                                cnt += 1
                                if cnt == edtNum:
                                    if edtNum2 == 2:
                                        data_list[i] = tupleNew
                                    elif edtNum2 == 3:
                                        ii = i

                        elif cmd == 4: # Поиск по содержанию
                            if data_find in data_list[i][3]:
                                cnt += 1
                                if cnt == edtNum:
                                    if edtNum2 == 2:
                                        data_list[i] = tupleNew
                                    elif edtNum2 == 3:
                                        ii = i

                # Если выбрана команда "Удалить"
                if edtNum2 == 3:
                    data_list.pop(ii)
                
                # Если выбрана команда "Изменить" или "Удалить"
                if edtNum2 == 2 or edtNum2 == 3:
                    write_file(data_list)

                    from ui import interface
                    interface()

            else:
                from ui import interface
                interface()   
            
        else:
            from ui import interface
            interface()    

# Поиск записи в файле (предварительное чтение файла)
def find_data_in_file(cmd, data_find): 
    
    with open(db_file_name, 'r', encoding='utf-8') as f:

        data_first = f.readlines()
        data_first = list(map(lambda x: (x.replace('\n', '')), data_first))
        data_first = list(filter(lambda x: (len(x) != 0), data_first))
        data_first_list = []
        
        for i in range(len(data_first)): 
            data_tuple = tuple(list(data_first[i].split(';')))
            data_first_list.append(data_tuple)

    edit_data(data_first_list, cmd, data_find)

# Ввод новых данных в файл
def input_data():    
    
    index = index_data()
    date = date_data()
    topic = topic_data()
    content = content_data()
    
    with open(db_file_name, 'a', encoding='utf-8') as f:
            f.write(f'{index};{date};{topic};{content}\n')

    print('> Внимание: заметка была добавлена в файл "' + db_file_name + '"!')
    
    from ui import interface
    interface()

# Вывод данных из файла
def print_data(): 

    print('> Вывожу все данные из файла: \n')
    
    with open(db_file_name, 'r', encoding='utf-8') as f:
        
        data_first = f.readlines()
        data_first = list(map(lambda x: (x.replace('\n', '')), data_first))
        data_first = list(filter(lambda x: (len(x) != 0), data_first))
        data_first_list = []
        
        for i in range(len(data_first)): 
            data_tuple = tuple(list(data_first[i].split(';')))
            data_first_list.append(data_tuple)
        
        for i in data_first_list:
            for j in range(len(i)): 
                if j != 0: print(';' + i[j], end='') 
                else: print(i[j], end='')    
            print('')

        print('')
    
    print('> Вывод из файла "' + db_file_name + '" завершен!')
    
    from ui import interface
    interface()

# Поиск заметок в файле
def find_data(cmd = 1):
    
    if cmd == 1:
        data_find = input('> Введите номер: ')
    elif cmd == 2:
        data_find = input('> Введите дату: ')
    elif cmd == 3:
        data_find = input('> Введите заголовок: ')
    elif cmd == 4:
        data_find = input('> Введите фразу из содержания: ')
        
    find_data_in_file(cmd, data_find)
