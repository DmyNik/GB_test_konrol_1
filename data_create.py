
import datetime

# Файл, содержащий базу данных заметок
db_file_name = 'data_base.csv'

# Получение наибольшего номера заметки
def get_index():
    
    max_index = 0

    with open(db_file_name, 'r', encoding='utf-8') as f:

        data_first = f.readlines()
        data_first = list(map(lambda x: (x.replace('\n', '')), data_first))
        data_first = list(filter(lambda x: (len(x) != 0), data_first))
        data_first_list = []
        
        for i in range(len(data_first)): 
            data_tuple = tuple(list(data_first[i].split(';')))
            data_first_list.append(data_tuple)
    
    for i in data_first_list:
        if int(i[0]) > max_index:
            max_index = int(i[0])
    
    return max_index

# Генерация нового номера заметки
def generate_new_index(): 
    index = str(get_index() + 1)
    return index

# Получение номера заметки
def index_data(): 
    index = generate_new_index()
    return index

# Получение текущей даты для новой заметки
def date_data():
    dt_now = datetime.datetime.now()
    date_string = dt_now.strftime('%d.%m.%Y %H:%M:%S')
    return date_string

# Ввод данных для темы заметки
def topic_data():
    topic = input('> Введите Тему заметки: ')
    return topic

# Ввод данных для содержания заметки
def content_data():
    content = input('> Введите Содержание заметки: ')
    return content
