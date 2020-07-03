import requests
import lxml
from bs4 import BeautifulSoup
import csv
import time

# ключи для последующей сортировки полученных данных считываются из файла keys.txt и записываются в список
keys = []

# Для записи данных в CSV-таблицу используем два списка
titles = []

links = []

# Промежуточный список для сохранения сортированных данных и последующей их записи в таблицу
#list_edited = []

headers = {'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15'}

def get_list(html):
    # формируем объект "Soup" с исходным кодом и отбираем основные данные в переменную projList для дальнейшего парсинга 
    source = BeautifulSoup(html.text, 'lxml')
    projList = source.select('div.b-post')
    
    # Для каждого проекта из списка проектов извлекаем название и ссылку на проект, записываем их в соответствующие списки titles и links

    for project in projList:
        item = project.select_one('a.b-post__link')
        title = item.text
        link = 'https://www.fl.ru' + item.get('href')
        titles.append(title)
        links.append(link)

def csv_write():
    with open('data.csv', 'w') as f:
        wr = csv.writer(f,delimiter=',',  quoting=csv.QUOTE_MINIMAL)
        rows = zip(titles,links)
        for i in rows:
            wr.writerow(i)
        
        f.close()

def keys_reader():
    with open ('keys.txt', 'r') as f:
        
        for key in f:
            keys.append(key.replace('\n', ''))
            
        f.close()
        
def csv_sorter():
    list_edited = []
    with open ('data.csv', 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            for item in row:
                for key in keys:
                    if key in item:
                        list_edited.append(row)
        f.close()
        
    with open('sorted.csv', 'w') as f:
        wr = csv.writer(f,delimiter=',',  quoting=csv.QUOTE_MINIMAL)
        for i in list_edited:
            wr.writerow(i)
        
        f.close()


def main():
    
    parse_rights = input('\nЕсли хотите парсить проекты с FL.ru введите Y, если нужна фильтрация таблицы по новым ключам - введите N : ')


    if parse_rights == 'Y':
        
        page_count = input('\nВведите количество страниц, которые необходимо изучить: ')
        time.sleep(1)
        print('\nСбор информации с сайта запущен, дождитесь его окончания')
        for page_num in range(1, int(page_count)):
            baseUrl = f'https://www.fl.ru/projects/?kind=1&page={page_num}'
            html = requests.get(baseUrl, headers=headers)
            get_list(html)
            csv_write()
        
        
        keys_reader()
        print('\nФильтруем данные по следующим ключам:')
        
        for key in keys:
            print(key)
        print('\nЧтобы изменить ключи, введите новые значения в файле keys.txt (каждый ключ в отдельной строке без запятых, пробелов, пустых строк)')
        time.sleep(1)
        csv_sorter()
    
    elif parse_rights == 'N':
        keys_reader()
        print('\nФильтруем информацию по следующим ключам:')
        
        for key in keys:
            print(key)
        
        print('\nЧтобы изменить ключи, введите новые значения в файле keys.txt (каждый ключ в отдельной строке без запятых, пробелов, пустых строк)')
        time.sleep(1)
        csv_sorter()
    
    else:
        print('\nВы ввели неверные параметры!')
        exit()
    

    
if __name__ == "__main__":
    main()
    time.sleep(1)
    print('\nВсё готово. Отобранные по ключевым словам данные хранятся в файле sorted.csv,\nвсе данные вы найдете в файле data.csv. Спасибо!')
    time.sleep(1)
    exit()
