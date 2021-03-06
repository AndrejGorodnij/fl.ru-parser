# fl.ru-parser
## Парсер вакансий на портале FL.RU | Python 

Программа парсит все вакансии из указанного количества страниц, и при необходимости фильтрует интересующие по ключевым словам.

Чтобы изменить ключевые слова, добавьте нужные в файл keys.txt, каждое слово должно занимать отдельную строку, не содержать лишних пробелов и знаков.

В результате парсинга вы получаете общий CSV-файл c полным списком вакансий из выбранного количества страниц, и отдельный CSV-файл, содержащий отфильтрованные данные по ключевым словам.

*Для упрощения использования парсера был создан текстовый интерфейс для работы в терминале.*

![alt text](https://github.com/AndrejGorodnij/fl.ru-parser/blob/master/screen.png "Скриншот работы парсера")

Кроме функции парсинга "свежих" вакансий, программа позволяет выполнять сортировку уже собранной базы по новым ключам, без необходимости повторного парсинга.

**Для запуска необходимо:**
1. OS - Windows|MacOS|Linux
2. Python - 3.6+
3. Пакеты из **requirements.txt**

**Перед запуском обязательно выполните команду  `pip install -r requirements.txt`**

**Запустить парсер можно при помощи команды - `python3 start.py`**
