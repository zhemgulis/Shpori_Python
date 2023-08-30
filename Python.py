# git init                     - создание нового репозитория
# git add .                    - добаление сразу всех изминений
# git commit -m "..."          - новый коммит с комментарием
# git branch -M main           - создание новой ветки и присвоение ей статуса "основная"
# git remote add origin https://github.com/zhemgulis/Shpori_Python.git - соединение с GH
# git push -u origin main      - команда пуша локального дипозитория на удаленный

# git status                   - посмотреть состояние файлов и папок
# git ls -la                   - просмотр всего содержимого репозитория
# git log                      - команда используется для просмотра истории коммитов

# git pull                     - команда используется для извлечения и загрузки содержимого из удаленного
#                                репозитория и немедленного обновления локального репозитория этим содержимым




print('Hello, World!') # просто вывод на печать
a = 10,                # создание переменной int   - целые числа
b = 23.14              # создание переменной float - дробные числа (c плавающей запятой)

print(type(a))                                             # вывод типа данных переменной
c = 'Я строка'                                             # str     - строка
a = True, b = False, c = 2 < 1                             # bool    - булевые True/False
my_list = [10, 15, 'Что-то еще']                           # list    - спискок
my_dict = {'Вася': 19, 'Оля': 18, 'Артем': 22, 'Вася': 23} # dict    - словарь

b = '5.6', c = float(b)      # изменение типа данных с str на float

d = True, a = 10, print(a + d) # a + d = 11 т.к. True = 1, а False = 0

print(10 // 3)               # результат деления без остатка (3)
print(10 % 3)                # остаток от деления            (1)
2 ** 3                       # возведение в степень          (8)
c = - 1.14456, print(abs(c)) # abs - модуль числа            (1.14456)
round(c, 2)                  # округление                    (-1.14)

# КОНКАТЕНАЦИЯ
a = 'Hello, ', b = 'World!', c = a + b, print(c)
# Получим:
Hello, World!
# еще пример:
print('Ваш коэффициент' + ' - ' + str(number)) # меняем тип данных для 0.23789012 с float на str
# Получим:
Ваш коэффициент - 0.23789012

# РАЗБИВКА СПИСКА на составные части .split() или с аргументом .split(',') для разделения используется запятая (по умолчанию - пробел)
single = 'Съешь булок, выпей чаю'
result = single.split()
print(result) # получим: ['Съешь', 'булок,', 'выпей', 'чаю']

# Результат как логическое выражение которое может быть False или True
single = 'Съешь еще булок'
print('бул' in single)          # получим: True
print('бул' in single.split())  # получим: False т.к. слова 'бул" там нет
print('еще' in single.split())  # получим: True т.к. слово 'еще" есть
print('выпей' in single)        # получим: False

# УСЛОВНЫЕ ОПЕРАТОРЫ - if, else, (elif)
student_name = 'Вася'
price = 15000
discount = 0.11
if student_name == 'Вася' and discount <= 0.1:     # заголовок условного оператора
    print('Васе положена скидка')                  # тело условного оператора
    price = price * 0.95
else:                                              # else (еще) т.е. все другое или отличное от Вася
    print('Это не Вася ИЛИ слишком большая скидка')
print(price)  # получим: Это не Вася ИЛИ слишком большая скидка  15000

# СПИСОК      0       1       2
students = ['Вася', 'Оля', 'Алефтина']
students[0]                           # выведет: 'Вася' т.к. задан индекс [0]
students[1] = 'Ольга'                 # заменит в списке Оля на Ольга: ['Вася', 'Ольга', 'Алефтина']
students.count('Оля')                 # выведет кол-во уникальных значений: 'Оля' в списке
students.append('Артем')              # добавит в список Артем: ['Вася', 'Ольга', 'Алефтина', 'Артем']
deleted_student = students.pop(1)     # удалит из списка Ольга: ['Вася', 'Алефтина', 'Артем'] .pop(1)

# СЛОВАРЬ       Вася        Оля        Алефтина                                                
students = {'Вася':4.8, 'Оля':4.9, 'Алефтина':4.6}
students['Остап'] = 4.75              # добавит в словарь: Остап: 4.75 {'Вася': 4.8, 'Оля': 4.9, 'Алефтина': 4.6, 'Остап': 4.75}
students.pop('Вася')                  # удалит из словаря Вася : 4.8 по индексу: 'Вася'

# ЦИКЛЫ
for i in students: # заголовок цикла
    print(i)       # тело цикла            получим: Вася Алефтина Артем
    
numbers = [10, 4, -5]
new_list = []
for i in numbers:
    new_list.append(i ** 2)  
new_list   # получим: [100, 16, 25]

list(range(0, len(numbers)))     # получим: [0, 1, 2]

for i in range(0, len(numbers)):
    numbers[i] = numbers[i] ** 2
numbers                          # получим: [100, 16, 25]

# Так же в ЦИКЛе мы можем обрабатывать и СЛОВАРИ через - items, keys, values:
students = {'Вася' : 3.5, 'Оля' : 4.9, 'Алефтина': 4.6, 'Коля': 4.1}
print(students)            # {'Вася': 3.5, 'Оля': 4.9, 'Алефтина': 4.6, 'Коля': 4.1}
print(students.keys())     # dict_keys(['Вася', 'Оля', 'Алефтина', 'Коля'])
print(students.values())   # dict_values([3.5, 4.9, 4.6, 4.1])
print(students.items())    # dict_items([('Вася', 3.5), ('Оля', 4.9), ('Алефтина', 4.6), ('Коля', 4.1)])

students = {'Вася' : 3.5, 'Оля' : 4.9, 'Алефтина': 4.6, 'Коля': 4.1}
for key, value in students.items():
    if value > 4.5: 
        print(key, '- отличный студент.') 
# получим: 
Оля - отличный студент. 
Алефтина - отличный студент.
        
# ФУНКЦИИ
def montly_payment(S, n, annual):       # заголовок функции; S, n, annual - входные параметры
    i = annual / 12                     # тело фунции
    P =  S * (i + i/((1 + i)**n-1)) 
    return round(P, 2)                  # то что возвращает функция: Р с округлением до двух знаков после запятой
    
# Задаем ПАРАМЕТРЫ ФУНКЦИИ:    
montly_payment(50000, 12, 0.22)         # получаем ответ: 4679.72 (при 50000 рублей на 12 месяцев под 22% годовых)

# Пример функции с ФАКТОРИАЛом числа:
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i             # данное равенство можно записать и так:   result *= i
    return result
    
# ИМПОРТ БИБЛИОТЕК
import pandas as pd # pd - алиас для pandas, чтобы каждый раз не писать название библиотеки целиком
from random import randint
import random
random.randint(0, 10)

# Некоторые библиотеки не будут входить в стандартный дистрибутиы Анаконды, их придется ставить дополнительно с помощью команды:
!pip install pandas

# Series (набор значений с индексами) в Pandas:
Series в Pandas это такие списки, которые включают в себя набор значений (например, значения возрастов)
и "адреса" значений (в нашем случае - имена студентов).
Набор "адресов" назвается ИНДЕКСОМ:

# Series СОЗДАНИЕ на основе списков:
student_names = ['Вася', 'Оля', 'Петя', 'Даша', 'Катя']                # задаем список имен студентов
age_list = [23, 21, 26, 19, 30]                                        # задаем список возрастов
age = pd.Series(age_list, index = student_names, name = 'Возраст')     # собираем Series возрастов, даем название Series
age
# Получаем:
Вася    23
Оля     21
Петя    26
Даша    19
Катя    30

print(type(age)) # смотрим полученный тип данных: <class 'pandas.core.series.Series'>

# Series СОЗДАНИЕ на основе списка и другого Series (student_names - у нас уже создан ранее)
# созадаем список оценок:
score_list = [4, 5, 3.5, 4.5, 5]
# создаем Series используя созданные ранее переменные: 
score = pd.Series(score_list, index = student_names, name = 'Оценка по тесту')
score
# Получаем:
Вася    4.0
Оля     5.0
Петя    3.5
Даша    4.5
Катя    5.0

# DataFrame (таблицы) в Pandas
Для создания таблиц в Pandas существует специальная конструкция - DataFrame (аналог таблицы в Excel).
Каждая колонка датафрейма - это отдельная Series (так же как и каждая строка).
DataFrame можно создать несколькими способами. Самый простой - конвертировать Series в DataFrame с одной колонкой:
students = age.to_frame()
students
# Получаем:
        Возраст
Вася	23
Оля 	21
Петя	26
Даша	19
Катя	30

# Тип данных переменной students:
print(type(students)) # <class 'pandas.core.frame.DataFrame'>

# DataFrame ДОБАВЛЕНИЕ столбцов:
Получилась симпатичная таблица с одной колонкой. Давайте добавим в нее еще одну - колонку оценок.
Для этого возьмем нашу Series для оценок:
students['Оценка по тесту'] = score # Назоваем новую колонку 'Оценка по тесту' и добавляем в нее значения из Series 'score'
students
# Получаем:
      Возраст   Оценка по тесту
Вася	23	     4.0
Оля 	21	     5.0
Петя	26	     3.5
Даша	19	     4.5
Катя	30	     5.0

# DataFrame ВЫВОД значения конкретной строки:
Раз у фрейма есть индекс, то мы можем получить по нему значения в строке фрейма. Это делается с помощью функции - loc:
students.loc['Вася']
# Получаем:
Возраст            23.0
Оценка по тесту     4.0

# DataFrame ВЫВОД значения нескольких строк:
Чтобы получить оценку для нескольких студентов, поступим вот так:
students.loc[['Вася', 'Катя'], 'Оценка по тесту']
# Получаем:
Вася    4.0
Катя    5.0

# DataFrame ВЫВОД строк по индексам (выводит все столбцы):
print(youtube_channels.loc[[20, 21]])

# DataFrame ВЫВОД целого столбца:
students['Оценка по тесту']

# DataFrame ВЫВОД диапазона строк по индексам (выводим только нужные столбцы):
print(youtube_channels.loc[15:25, ['category', 'language']])

# DataFrame ВЫВОД через создание переменных:
perem_1 = [15,25]
perem_2 = ['category', 'language']
print(youtube_channels.loc[perem_1, perem_2])

# DataFrame ВЫВОД при помощи .iloc (выводит все столбцы):
print(youtube_channels.iloc[[0, 1, 2]]) # можно и так: .iloc[0:3]

# DataFrame ВЫВОД при помощи .iloc (выводит 2 и 3 строки с 1 и 4 столбцами):
print(youtube_channels.iloc[[2,3], [0,3]])
print(youtube_channels.iloc[2:9, 0:3]) # тоже самое но через срезы

# DataFrame ВЫВОД строк ПО УСЛОВИЮ
# рассмотрим новую таблицу:
	Color   Shape       Price
0   Green   Rectangle   10
1   Green   Rectangle   15
2   Green   Square      5
4   Blue    Square      10
5   Red     Square      15
6   Red     Square      15

print(Tablica_1.loc[Tablica_1.Color == 'Green']) # выберем только строки с Green
print(Tablica_1.loc[Tablica_1.Price >= 10]) # выберем только строки где цена >= 10
Tablica_1.loc[(Tablica_1.Color == 'Green') & (Tablica_1.Price >= 10)] # выберем строки где верно первое условие И(&) второе
Tablica_1.loc[(Tablica_1.Color == 'Green') | (Tablica_1.Price >= 10)] # выберем где верно первое условие ИЛИ(|) второе

# DataFrame ФИЛЬТРАЦИЯ данных по НАИМЕНОВАНИЮ СТОБЛЦОВ
# regex (регулярные выражения)
  df. filter (regex = 'regex') ПРИМЕРЫ ФИЛЬТРОВ:
# рассмотрим новую таблицу:
   aph1  aph2  bph3  aph3
1  aa    bb    cc    dd
2  x     y     z     k
3  ax    by    cz    dk
  
display(df.filter(regex ='1'))             # Фильтрация столбцов, которые содержат в названии "1"
display(df.filter(regex ='3$'))            # Фильтрация столбцов, которые заканчиваются на "h3"
display(df.filter(regex ='^ap'))           # Фильтрация столбцов, которые начинаются с "ap"
display(df.filter(regex ='^ap.*h3$'))      # Фильтрация столбцов, которые начинаются с "ap" и заканчиваются на "h3"
display(df.filter(regex ='^ap.*[1-3]$'))   # Фильтрация столбцов, которые начинаются c "ap" и заканчиваются на значение в промежутке от 1 до 3
display(df.filter(regex ='^ap.*[2,3]$'))   # Фильтрация столбцов, которые начинаются с "ap" и заканчиваются на "3" или "2"
display(df.filter(regex ='^(?!.*ph3$).*')) # Фильтрация столбцов, которые НЕ содержат "ph3"

# DataFrame ФИЛЬТРАЦИЯ данных по ЗНАЧЕНИЯМ данных ОПРЕДЕЛЕННЫХ СТОЛБЦОВ
# Выбрать n НАИБОЛЬШИХ значений определенного столбца:
youtube_channels.nlargest(3, 'like_to_view_ratio')
# Выбрать n НАИМЕНЬШИХ значений определенного столбца:
youtube_channels.nsmallest(3, 'like_to_view_ratio')

# DataFrame ФИЛЬТРАЦИЯ данных в соответствии со списком из другой переменной
# Этот метод возвращает булевую Series, где каждый элемент указывает, принадлежит ли значение элемента к переданному списку:
import pandas as pd
# Создадим новый DataFrame
data = {'fruits': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']}
df = pd.DataFrame(data)
# ОТФИЛЬТРУЕМ из data фрукты, которые принадлежат к списку values:
values = ['apple', 'cherry', 'kiwi']
mask = df['fruits'].isin(values)
print(mask)
# Получим:
0     True
1    False
2     True
3    False
...

# DataFrame СОЗДАНИЕ прямо из массива значений:
import pandas as pd
students_data = [[23, 4], [21, 5], [26, 3.5], [19, 4.5], [30, 4]]
students = pd.DataFrame(students_data,
                        index = student_names,
                        columns = ['Возраст', 'Оценка по тесту']) # Получим тот же датафрейм с возростом и оценками.

# DataFrame СОЗДАНИЕ из словаря:
import pandas as pd
students = {'Вася' : 3.5, 'Оля' : 4.9, 'Алефтина': 4.6, 'Коля': 4.1}
students = pd.DataFrame(students.values(),
                        index = students.keys(),
                        columns = ['Оценка по тесту'])

# DataFrame СОЗДАНИЕ из файлов:
import pandas as pd
Для открытия файлов с расширением .csv используем функцию read_csv
heights = pd.read_csv('lesson02_heights.csv')
heights.head()

# ОТКРЫТИЕ файлов с расширением .xlsx
Для открытия файлов используем функцию read_excel и указываем лист, который хотим
открыть: sheet_name = 'data' (если не укажем откроется первый лист в книге)
# (иногда возникают сбои, может помочь загрузка библиотеки: !pip install openpyxl)
youtube_channels = pd.read_excel('lesson02_wiki_top_youtube_channels.xlsx', sheet_name = 'data')
youtube_channels.head(5)
# Получаем:
      name             subscribers_mln language    category  in_russian  like_to_view_ratio
0   T-Series                    171.0   Hindi    Music          False     0.430178
1   PewDiePie                   109.0   English  Entertainment  False     0.444065
2   Cocomelon - Nursery Rhymes  104.0   English  Education      False     0.573531
3   SET India                   94.0    Hindi    Entertainment  False     0.426803
4   Kids Diana Show             73.0    English  Entertainment  False     0.410649

# DataFrame СОХРАНЕНИЕ файлов:
# Для сохранения датафрейма используем функцию: .to_csv или .to_excel
# Параметр index может быть True или False, в зависимости от того хотим или нет сохранить значение индексов
# index = False - нет, index = True - да:
most_trusted.to_csv('most_trusted.csv', index = False)
most_trusted.to_excel('most_trusted.xlsx')

# DataFrame СОСТАВ и СВОЙСТВА:
heights.info()
# Получаем:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50 entries, 0 to 49
Data columns (total 6 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   name                50 non-null     object 
 1   subscribers_mln     50 non-null     float64
 2   language            50 non-null     object 
 3   category            50 non-null     object 
 4   in_russian          50 non-null     bool   
 5   like_to_view_ratio  50 non-null     float64
dtypes: bool(1), float64(2), object(3)
memory usage: 2.1+ KB

# ТИПЫ ПЕРЕМЕННЫХ. На практике, чаще всего встречаются переменные 4-х типов:
- Категориальные (object)                        # например имена, названия языков, категории тематики каналов.
- Числовые       (int, int64, float64 и другие)  # например рост, количество подписчиков, соотношение лайков к просмотрам и т.д.
- Логические     (bool)                          # например, факт того, вещает ли канал на русском или нет.
- Временные      (datetime)                      # дата.
                    
# Кол-во УНИКАЛЬНЫХ значений
# Можно посчитать частоту повторения значений роста при помощи value_counts:
heights['Рост'].value_counts()
# Получаем:
166    4
171    4
174    3
185    3
178    3
183    2
...

# ФУНКЦИИ для вывода данных для определенного столбца фрейма (Рост):
heights['Рост'].min()           # минимальное значение значение столбца,
heights['Рост'].max()           # максимальное значение значение столбца,
heights['Рост'].count()         # кол-во непустых значений (для DataFrame и Series не принимает аргументов),
heights['Рост'].unique()        # вывод значений без повторения = уникальных значений (аналог DISTINCT),
heights['Рост'].nunique()       # вывод одной цифрой кол-ва уникальных значений,
heights['Рост'].value_counts()  # выведет таблицу где индексом будут уникальные значения, а рядом частота их появления,
heights['Рост'].value_counts().get(174, 0)) # вывыведет кол-во уник-ых значений для 174, а если таких не будет то "0",
heights['Рост'].mean()          # среднее значение в столбце,
heights['Рост'].std()           # дисперсия (среднее квадратное отклонение, СКО),
heights['Рост'].median()        # медиана значений столбца,

# Получить УНИКАЛЬНЫЕ КОМБИНАЦИИ значений по НЕСКОЛЬКИМ СТОЛБЦАМ
# можем использовать drop_duplicates()
# создадим новую таблицу:
df = pd.DataFrame({
    'A': [1, 2, 2, 4, 4],
    'B': ['x', 'y', 'y', 'z', 'z']})
# Получим:   
   A  B
0  1  x
1  2  y
2  2  y
3  4  z
4  4  z

# Выведем только уникальные комбинации в столбцах:
unique_combinations = df[['A', 'B']].drop_duplicates()
# Получим:
   A  B
0  1  x
1  2  y
3  4  z

# ЦЕПОЧКА МЕТОДОВ (Method Chaining) в Pandas — это мощная концепция, которая позволяет объединять множество операций в одну строку.
# Это может улучшить читаемость кода и уменьшить количество временных переменных.
# Создадим новый дата фрейм:
import pandas as pd
df = pd.DataFrame({
    'date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'A': [100, 150, 200, 250],
    'B': [50, 210, 300, 400]})
# Получим:
   date         A    B
0  2021-01-01  100  50
1  2021-01-01  150  210
2  2021-01-02  200  300
3  2021-01-02  250  400   

# Теперь применим в одном коде цепочку методов:
  1. pd.melt(df) - преобразует датафрейм из широкого формата в длинный.
  2. rename(columns={'variable' : 'var', 'value' : 'val'}) - переименовывает столбцы в "var" и "val".
  3. query('val >= 200') - фильтрует строки, где значение в столбце 'val' больше или равно 200.
# Эти три операции объединены в одну строку, что делает код более чистым и компактным:
df_transformed = (df.melt(id_vars=['date'])
                  .rename(columns={'variable': 'var', 'value': 'val'})
                  .query('val >= 200')) # данную последнюю часть кода можно убрать и тогда получим все 8 значений полностью.
# Получим:
    date        var  val
2   2021-01-02   A   200
3   2021-01-02   A   250
5   2021-01-01   B   210
6   2021-01-02   B   300
7   2021-01-02   B   400

# СОРТИРОВКА с помощью функции sort_values().
# По умолчанию сортировка идет по ВОЗРАСТАНИЮ:
youtube_channels['subscribers_mln'].sort_values()
# Получаем:
49     36.0
48     36.0
47     36.0
46     37.0
45     37.0
44     38.0
...
# по УБЫВАНИЮ: 
youtube_channels['subscribers_mln'].sort_values(ascending=False)

# СОРТИРОВКА с выводом НЕСКОЛЬКИХ столбцов (например наименование и его значение):
youtube_channels[['name','subscribers_mln']].sort_values(by='subscribers_mln')

# ГИСТОГРАММА - это график, у которого по оси X отложены значения переменной, а по оси Y - частота (или вероятность) их появления. 
# Построить гистограмму можно с помощью функции hist:
from matplotlib import pyplot as plt # импортируем библиотеку matplotlib
heights['Рост'].hist(bins = 10)      # Значение (bins = 10) кол-во значений в еденице по оси координат "Рост" (корзина)
plt.xlabel('Рост'), plt.ylabel('Частота появления'), plt.title('Распределение роста взрослых мужчин') # задаем подписи осей и заголовок
plt.show()

# Диаграмма размаха (BOXPLOT):
heights.boxplot('Рост') # можно повернуть по горизонтали добавив аргумент: , vert=False
plt.xlabel('Рост'), plt.title('Диаграмма размаха роста взрослых мужчин') # добавим подписи данных
plt.show() 

# Функци QUANTILE
heights['Рост'].quantile(0.5), heights['Рост'].quantile(0.75), heights['Рост'].quantile(0.95)
(174.5, 181.75, 189.95)

# можно задать переменные и с их помощью выводить развернутый ответ (функция .format):
criteria_value = heights['Рост'].quantile(0.95)
criteria_column = 'Рост'
print('95-ти процентный квантель для колонки {} равен {:.2f}'.format(criteria_column, criteria_value))
# Получим:
95-ти процентный квантель для колонки Рост равен 189.95
# в {} -ки при помощи функции .format вставляем: 1.criteria_column = 'like_to_view_ratio' и 2.значение колонки criteria_value
# {:.2f} - показывает, что у числа тип длжен быть float с 2-мя знаками после запятой.

# можно вывести строки таблицы у которых значения стобца Рост >= quantile(0.95)
criteria_value = heights['Рост'].quantile(0.95)
criteria_column = 'Рост'
most_trusted = heights.query('{} > {}'.format(criteria_column, criteria_value))
most_trusted

# еще примеры:
number = 0.23789012
print('Ваш коэффициент, {:.2f}'.format(number))
# Получим:
Ваш коэффициент, 0.24

print('Привет {}, и тебе доброе утрое {}'.format('Вася', 'Ира'))
# Получим:
Привет Вася, и тебе доброе утрое Ира


# DataFrame СОХРАНЕНИЕ в файл
# для сохранения используем функцию: .to_csv или .to_excel
# в зависимости от того хотим или нет сохранить значение индексов ставим:
# index = False - нет, index = True - да:
most_trusted.to_csv('most_trusted.csv', index = False)
most_trusted.to_excel('most_trusted.xlsx')


# DataFrame ИЗМЕНЕНИЕ ТИПА ДАННЫХ с object на datetime (для данных с датами)
# просто отобразить при помощи функции pd.to_datetime столбец date в формате datetime,
# это не приведет к изменению фрейма (таблицы):
pd.to_datetime(name_df['date'])
# код для изменения типа данных столбца 'date' в name_df:
name_df['date'] = pd.to_datetime(name_df['date'])
# Вот теперь формат столбца date изменен и сохранен под новым типом данных (datetime) в таблице.

При изменении типа данных столбца date на datetime добвится время
т.к. ранее его не было, то добавится просто - 00:00:00
# функция loc поможет нам увидеть полное значение ячейки:
name_df.loc[0, 'date']
# Получим:
Timestamp('2021-02-01 00:00:00')
# Можно убрать время и оставить только дату добавив в конце: .dt.date:
name_df['date_only'] = name_df['date'].dt.date


# Бизнес показатели: DAU, WAU и MAU (ежедневные активные пользователи, еженедельные, ежемесячные)
# Добавим новый столбец в котором оставим только год и месяц:
# тип данных столбца 'date_month' будет: period[M] (разновидность типа datetime)
# можно оставить только год заменив ('M') на ('Y')
user_activity['date_month'] = user_activity['date'].dt.to_period('M')
# Получим:
   user_id           device   date        date_only   date_month
0  74793686a6268281  iPhone   2021-02-01  2021-02-01  2021-02
1  6986c3d2188caf4b  Android  2021-02-01  2021-02-01  2021-02
2  d9a79c634cc6df36  iPhone   2021-02-01  2021-02-01  2021-02
3  b3b0c361708b69a9  PC       2021-02-01  2021-02-01  2021-02
4  48ddcd54a6844b70  Mac      2021-02-01  2021-02-01  2021-02

# DataFrame ГРУППИРОВКА ДАННЫХ
# Теперь когда мы добавили необходимые столбцы - можно по ним группировать данные:
  - при помощи функции 'groupby' группируем по столбцу 'date_only'
  - '.agg' агрегируем данные в столбце 'user_id' при помощи функции 'nunique',
# получаем кол-во уникальных user_id на дату date_only
dau = user_activity.groupby('date_only').agg({'user_id': 'nunique'})
# Получим:
	user_id
date_only	
2021-02-01	1727
2021-02-02	1899
2021-02-03	1994
...

# ПЕРЕИМЕНУЕМ все КОЛОНКИ фрейма dau (dau.columns) в название "DAU".
# Все колонки потому, что у нас всего одна колонка user_id:
# - date это название столбца по которому идет группировка из фрейма-источника (индекс)
dau = user_activity.groupby('date').agg({'user_id': 'nunique'})
dau.columns = ['DAU']
dau.head(3)
# Получим:
	DAU
date	
2021-02-01	1727
2021-02-02	1899
2021-02-03	1994
...

# DataFrame ГРУППИРОВКА сразу ПО НЕСКОЛЬКИМ ФУНКЦИЯМ например nunique и count:
# - nunique кол-во уникальных пользователей на дату и count посчитать общее кол-во на дату
# - ['nunique', 'count'] скобки указывают, на список функций применяемых к 'user_id'
# - сгруппируем в этот раз по столбцу date_month и списком дадим название столбцам - ['MAU', 'Число посещений']
mau = user_activity.groupby('date_month').agg({'user_id': ['nunique', 'count']})
mau.columns = ['MAU', 'Число посещений']
mau.head(3)
# Получим:
	MAU	Число посещений
date_month		
2021-02	44419	68537
2021-03	45849	72061
2021-04	41995	67397
...

# DataFrame ИЗМЕНЕНИЕ НАИМЕНОВАНИЯ одной колонки во фрейме,
# inplace=True - сразу сохраняет изменения во фрейме mau.
mau.rename(columns={'Число посещений': 'Кол-во посещений'}, inplace=True)
mau
# Получим:
	MAU	Кол-во посещений
date_month		
2021-02	44419	68537
2021-03	45849	72061
2021-04	41995	67397
...

# К списку функций применяемых для user_id, можно добавить функцию для device
# - функция first просто выбирает первое значение в столбце из заданной группы:
mau = user_activity.groupby('date_month').agg({'user_id': ['nunique', 'count'],'device': 'first'})
mau
# Получим:
              user_id      device
           nunique  count  first
date_month			
2021-02    44419	68537  iPhone
2021-03    45849	72061  iPhone
2021-04    41995	67397  Android
...

# ГРАФИКИ
# функция .plot добавляет график для фрейма dau:
from matplotlib import pyplot as plt
dau.plot()

# При помощи функции figsize можем изменить размер графика:
dau.plot(figsize = (15, 5)) # измеряется в дюймах

# Установим заголовоки и подписи осей:
dau.plot(figsize = (15, 5))
plt.title('Изменение DAU'), plt.xlabel('Дата'), plt.ylabel('Уникальные пользователи')

# Изображение графиков можно сохранить в виде картинки (например с разрешением PNG):
mau.plot()
plt.title('Изменение MAU'), plt.xlabel('Дата'), plt.ylabel('Уникальные пользователи')
plt.savefig('test_plot.png') # данная строка сохраняет изображение графика в папеке с данным ноутбуком


# pivot_table
data.head()
# Получим:
       user_id       device      date
0  74793686a6268281  iPhone   2021-02-01
1  6986c3d2188caf4b  Android  2021-02-01
2  d9a79c634cc6df36  iPhone   2021-02-01
...
#подсчет всех девайсов во фрейме data без группировки по датам
data['device'].value_counts()
# Получим:
iPhone     101838
Android     78984
Mac         51376
PC          47265

# В pandas мы можем с помощью функции pivot_table построить сводную таблицу, где у нас будет не одна группировка, а две:
# -  первая группировка по индексу (колонка date): index = 'date'
# -  вторая группировка по колонке device: columns = 'device'
# -  значения для группировки берем из колонки user_id: values = 'user_id'
# -  агрегирующая функция для уникальных значений: aggfunc = 'nunique'

# DataFrame СГРУППИРУЕМ ДАННЫЕ по дате и устройству:
dau = data.pivot_table(index = 'date', columns = 'device', values = 'user_id', aggfunc = 'nunique')
# Получим:
device    Android  Mac  PC  iPhone
  date				
2021-02-01	472    303  312  640
2021-02-02	549    325  328  697
2021-02-03	593    349  336  716
...

# DataFrame МОДИФИКАЦИЯ ДАННЫХ
# Операции над столбцами - самый быстрый вариант работы с данными в pandas

# DataFrame 4 ОСНОВНЫХ МЕТОДА МОДИФИКАЦИИ данных в фреймах
# Вот они в порядке скорости выполнения:
# -  Операции над столбцами;
# -  Работа с функцией apply;
# -  Прямая модификация даннах в ячейках с помощью .loc.

# Скопируем DAU в новую переменную:
test_dau = dau.copy()
# DataFrame СОЗДАНИЕ НОВОГО столбца:
dau['total_dau'] = 1
# DataFrame СЛОЖЕНИЕ столбцов (вариант 1):
dau['total_dau'] = dau['Android'] + dau['Mac'] + dau['PC'] + dau['iPhone']
# Получим:
device    Android  Mac  PC  iPhone  total_dau
  date				
2021-02-01	472    303  312  640    1727
2021-02-02	549    325  328  697    1899
2021-02-03	593    349  336  716    1994
...

import numpy as np
test_02 = dau_channel
numeric_cols = test_02.select_dtypes(include=[np.number]) # Выберает только числовые столбцы перед суммированием
test_02['Total'] = numeric_cols.sum(axis=1)


# DataFrame СЛОЖЕНИЕ столбцов (вариант 2):
# сложение по оси Х: sum(axis = 1)
# сложение по оси Y: sum(axis = 0)
dau['total_dau'] = 0
dau['total_dau'] = dau.sum(axis = 1)
# или так (не будет ошибки скрасным фоном):
import numpy as np
numeric_cols = dau.select_dtypes(include=[np.number]) # ВЫБЕРАЕТ ТОЛЬКО ЧИСЛОВЫЕ СТОЛБЦЫ перед суммированием
dau['total_dau'] = numeric_cols.sum(axis=1)

# DataFrame ДЕЛЕНИЕ столбцов:
dau['perc_pc'] = dau['PC'] / dau['total_dau']

# DataFrame ФУНКЦИЯ apply
# Apply - это второй по скорости метод массовой модификации данных в фреймах.

# ПРИМЕР 1
# Предположим, мы хотим посчитать сколько процентов от общего DAU составляют все 
# платформы кроме PC. Каким образом мы можем это посчитать? Мы можем задать функцию:
def get_perc_except_pc(cell_value):
    return 1 - cell_value
    
dau['perc_except_pc'] = dau['perc_pc'].apply(get_perc_except_pc)

# cell_value - значение столбца
# Что здесь происходит? По сути дела, apply просто берет последовательно КАЖДУЮ ЯЧЕЙКУ В СТОЛБЦЕ perc_pc,
# применяетк ней функцию get_perc_except_pc (которая из 1 вычетает cell_value - значение ячейки perc_pc)
# и сохраняет результат в столбец perc_except_pc.

# ПРИМЕР 2
# Если вы хотите вычислить значение столбца, используя значения НЕСКОЛЬКИХ СТОЛБЦОВ,
# то apply нужно применять по-другому:

# Допустим, вы хотете вычислить, какой процент от общего DAU составляет сумма DAU для платформ Android и Mac.
# Для этого напишем функцию:
def get_perc_android_mac(row_values):
    return (row_values['Android'] + row_values['Mac']) / row_values['total_dau']

dau['perc_android_mac'] = dau.apply(get_perc_android_mac, axis = 1)

# row values - значения в строках
# Обратите внимание на то, как применяется команда apply в этом случае:

#    apply применяется не к конкретному столбцу, а к ФРЕЙМУ ЦЕЛИКОМ: dau.apply(...)
#    При вызове apply указывается axis = 1. Это означает, что внуть функции get_perc_android_mac
#    будет переданы все ЗНАЧЕНИЯ ТЕКУЩЕГО РЯДА.

# (axis = 0 - будет указывать на значения в столбце)

# DataFrame ПРЯМАЯ МОДИФИКАЦИЯ данных в ЯЧЕЙКАХ с помощью .loc

# Функция loc меняет (перезаписывает) значения в самой таблице!!!

# Изменим значения ячеек в строке: '2021-02-04' для столбцов 'iPhone' и 'Mac' на 0:
dau.loc['2021-02-04', ['iPhone', 'Mac']] = 0

# Можем сделать ИЗМЕНЕНИЯ сразу МНОГИХ строк ПО УСЛОВИЮ, например:
# -  для всех строк с индексом (здесь индекс = дата) равным или меньшим'2021-02-03':
dau.loc[dau.index <= '2021-02-03'] = -1

# НЕ ПУТАТЬ с функцией query которая только показывает, но не изменяет значение ячеек:
dau.query("date <= '2021-02-03'")

# Давайте ИСПОЛЬЗУЕМ навыки МОДИФИКАЦИИ ДАННЫХ в фреймах для того, чтобы посчитать
# какой % от DAU составляют пользователи мобильных устройств (это Android + iPhone):
dau_perc = dau.copy() # создадим копию фрейма dau
dau_perc['Total'] =  dau_perc.sum(axis = 1) # суммируем данные в строках dau
mobile_types = ['Android', 'iPhone'] # создаем список моб. устройств
dau_perc['Mobile'] = dau_perc[mobile_types].sum(axis = 1) # сумма моб.уст-тв
dau_perc['Others'] = dau_perc['Total'] - dau_perc['Mobile'] # считаем разницу
dau_perc.head()
# Получим:
device   Android Mac  PC iPhone Total Mobile Others
date							
2021-02-01  472  303  312  640  1727   1112   615
2021-02-02  549  325  328  697  1899   1246   653
2021-02-03  593  349  336  716  1994   1309   685
...
# Переводим значения интересующих столбцов в проценты:
dau_perc['Mobile'] = dau_perc['Mobile'] / dau_perc['Total']
dau_perc['Others'] = dau_perc['Others'] / dau_perc['Total']
# Получим:
device  Android  Mac  PC iPhone Total  Mobile    Others
date							
2021-02-01  472  303  312  640  1727  0.643891  0.356109
2021-02-02  549  325  328  697  1899  0.656135  0.343865
2021-02-03  593  349  336  716  1994  0.656469  0.343531
...

