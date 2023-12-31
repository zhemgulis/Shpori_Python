
-- 1.7 Таблица НАРУШЕНИЯ ПДД, ЗАПРОСЫ, КОРРЕКТИРОВКИ

-- Структура и наполнение таблиц

DROP TABLE fine;

CREATE TABLE fine (
    fine_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    number_plate VARCHAR(6),
    violation VARCHAR(50),
    sum_fine DECIMAL(8, 2),
    date_violation DATE,
    date_payment DATE);
    
INSERT INTO fine(name, number_plate, violation, sum_fine, date_violation, date_payment)
VALUES    
    ('Баранов П.Е.', 'Р523ВТ', 'Превышение скорости (от 40 до 60)', 500.00, '2020-01-12', '2020-01-17'),
    ('Абрамова К.А.', 'О111АВ', 'Проезд на запрещающий сигнал', 1000.00, '2020-01-14', '2020-02-27'),
    ('Яковлев Г.Р.', 'Т330ТТ', 'Превышение скорости (от 20 до 40)', 500.00,	'2020-01-23', '2020-02-23'),
    ('Яковлев Г.Р.', 'М701АА', 'Превышение скорости (от 20 до 40)', NULL, '2020-01-12', NULL),
    ('Колесов С.П.', 'К892АХ', 'Превышение скорости (от 20 до 40)', NULL, '2020-02-01', NULL),
    ('Баранов П.Е.', 'Р523ВТ', 'Превышение скорости (от 40 до 60)', NULL, '2020-02-14', NULL),
    ('Абрамова К.А.', 'О111АВ', 'Проезд на запрещающий сигнал', NULL, '2020-02-23', NULL),
    ('Яковлев Г.Р.', 'Т330ТТ', 'Проезд на запрещающий сигнал', NULL, '2020-03-03', NULL);
       
SELECT * FROM fine;

DROP TABLE traffic_violation;

CREATE TABLE traffic_violation (
    violation_id INT PRIMARY KEY AUTO_INCREMENT,
    violation VARCHAR(50),
    sum_fine DECIMAL(8, 2));
    
INSERT INTO traffic_violation (violation, sum_fine)
VALUES
    ('Превышение скорости (от 20 до 40)', 500.00),
    ('Превышение скорости (от 40 до 60)', 1000.00),
    ('Проезд на запрещающий сигнал', 1000.00);
    
SELECT * FROM traffic_violation;

-- ***************************************************************************************************************
-- ИСПОЛЬЗОВАНИЕ ВРЕМЕННОГО ИМЕНИ ТАБЛИЦЫ (алиаса)

-- Чтобы не писать название таблицы каждый раз, удобно использовать алиасы.
-- Алиас, это псевдоним, который мы присваивали столбцам после ключевого слова AS(шаг). Алиасы так же можно использовать и для таблиц. Это становится актуальным, при увеличении числа используемых таблиц, их иногда может быть и 5 и 10 и более. Псевдонимы помогают сделать запрос чище и читабельнее.

--                  Для присваивания псевдонима существует 2 варианта: 
--                      I                   |               II
-- ---------------------------------------------------------------------------------
-- с использованием ключевого слова AS:     |   а так же и без него:
-- FROM fine AS f, traffic_violation AS tv  |   FROM fine f, traffic_violation tv

-- После присвоения таблице алиаса, он используется во всех разделах запроса, в котором алиас задан. Например:
-- WHERE f.violation = tv.violation

-- Пример
-- Для тех, кто уже оплатил штраф, вывести информацию о том, изменялась ли стандартная сумма штрафа.

SELECT f.name, f.number_plate, f.violation, 
    IF(f.sum_fine = tv.sum_fine, "Стандартная сумма штрафа", 
        IF(f.sum_fine < tv.sum_fine, "Уменьшенная сумма штрафа", "Увеличенная сумма штрафа")
    ) AS description               
FROM  fine f, traffic_violation tv
WHERE tv.violation = f.violation and f.sum_fine IS NOT Null;

-- Результат:
-- +---------------+--------------+----------------------------------+--------------------------+
-- | name          | number_plate | violation                        | description              |
-- +---------------+--------------+----------------------------------+--------------------------+
-- | Баранов П.Е.  | Р523ВТ       | Превышение скорости(от 40 до 60) | Уменьшенная сумма штрафа |
-- | Абрамова К.А. | О111АВ       | Проезд на запрещающий сигнал     | Стандартная сумма штрафа |
-- | Яковлев Г.Р.  | Т330ТТ       | Превышение скорости(от 20 до 40) | Стандартная сумма штрафа |
-- +---------------+--------------+----------------------------------+--------------------------+

-- ЗАДАНИЕ
-- Занести в таблицу fine суммы штрафов, которые должен оплатить водитель, в соответствии с данными из таблицы traffic_violation. При этом суммы заносить только в пустые поля столбца  sum_fine.
-- Таблица traffic_violation создана и заполнена.

-- ВАЖНО !!! 
-- Сравнение значения столбца с пустым значением осуществляется с помощью оператора IS NULL.

-- Пояснение
-- 1. После ключевого слова UPDATE кроме обновляемой таблицы fine укажите таблицу traffic_violation, для того чтобы запрос видел таблицы источники.  Сначала перечисляем все источники, потом выполняем необходимые действия.
-- 2.Обновляйте только те записи таблицы fine, у которых значение столбца violation совпадает со значением соответствующего столбца таблицы traffic_violation, а также значение столбца sum_fine пусто.


UPDATE fine f, traffic_violation tv
SET f.sum_fine = tv.sum_fine
WHERE f.violation = tv.violation AND f.sum_fine IS NULL
LIMIT 1000;

-- можно заморочиться через IF:

UPDATE fine f, traffic_violation tv
SET f.sum_fine = IF(f.sum_fine IS NULL, tv.sum_fine, f.sum_fine)
WHERE f.violation = tv.violation
LIMIT 1000;

SELECT * FROM fine;

-- ***************************************************************************************************************
-- ГРУППИРОВКА ДАННЫХ ПО НЕСКОЛЬКИМ СТОЛБЦАМ

-- В разделе GROUP BY можно указывать несколько столбцов, разделяя их запятыми. Тогда к одной группе будут относиться записи, у которых значения столбцов, входящих в группу, равны. Рассмотрим группировку по нескольким столбцам на примере следующего запроса:

SELECT name, number_plate, violation, count(*)
FROM fine
GROUP BY name, number_plate, violation;

-- 1. Сначала записи таблицы  fine разделяются на группы. В каждую группу включаются строки, у которых равны значения в столбцах name, number_plate и violation  соответственно. Получается 6 групп. 
-- 2. Затем вычисляется функция count(*), которая определяет количество записей в каждой группе. Получается, что к первым двум группам относятся по две записи, ко всем остальным - по одной.

-- ВАЖНО !!!
-- В разделе GROUP BY нужно перечислять все НЕАГРЕГИРОВАННЫЕ столбцы (к которым не применяются групповые функции) из SELECT.

-- ЗАДАНИЕ
-- Вывести фамилию, номер машины и нарушение только для тех водителей, которые на одной машине нарушили одно и то же правило два и более раз. При этом учитывать все нарушения, независимо от того оплачены они или нет. Информацию отсортировать в алфавитном порядке, сначала по фамилии водителя, потом по номеру машины и, наконец, по нарушению.

-- Пояснение
-- Под увеличение  штрафа в два раза подходит водитель «Абрамова К.А.», который на машине с государственным номером «О111АВ» совершил повторное нарушение «Проезд на запрещающий сигнал», а также водитель  «Баранов П.Е.» , который на машине с номером  «Р523ВТ» дважды совершил нарушение «Превышение скорости(от 40 до 60)».

SELECT name, number_plate, violation
FROM fine
GROUP BY name, number_plate, violation
HAVING COUNT(number_plate) > 1
ORDER BY name, number_plate, violation;

-- ну или опять вспомним COUNT(*):

SELECT name, number_plate, violation
FROM fine
GROUP BY name, number_plate, violation
HAVING COUNT(*) > 1
ORDER BY name, number_plate, violation;

-- ***************************************************************************************************************
-- ЗАДАНИЕ
-- В таблице fine увеличить в два раза сумму неоплаченных штрафов для отобранных на предыдущем шаге записей. 

-- Пояснение !!!  Если не получается запрос или валидатор выдает ошибки, раскройте это пояснение!!!

--    1. Для всех нарушений, по которым штраф еще не оплачен, (тех, у которых date_payment имеет пустое значение Null), необходимо проверить, является ли данное нарушение для водителя и машины повторным, если да –  увеличить штраф в два раза.
--    2. Если водитель совершил нарушение на другой машине, ему увеличивать штраф не нужно.
--    3. Если несколько повторных нарушений не оплачены, то штраф увеличить для всех.
--    4. Этот запрос реализован на предыдущем шаге.

-- При реализации можно использовать вложенный запрос как отдельную таблицу, записанную после ключевого слова UPDATE, при этом вложенному запросу необходимо присвоить имя, например query_in:
-- UPDATE fine, 
    -- (
     -- SELECT ...
    -- ) query_in
-- SET ...
-- WHERE указать, что совпадают нарушение, фамилия водителя и номер машины в таблицах fine и вложенном запросе query_in соответственно, а также дата оплаты в таблице fine пуста

-- Другим способом решения является использование двух запросов: сначала создать временную таблицу, например query_in, в которую включить информацию о тех штрафах, сумму которых нужно увеличить в два раза, а затем уже обновлять информацию в таблице fine:
-- CREATE TABLE query_in ...;

-- UPDATE fine, query_in
-- SET ...
-- WHERE ...;

-- После ключевого слова WHERE  указывается условие, при котором нужно обновлять данные. В нашем случае  данные обновляются, если и фамилия, и государственный номер, и нарушение совпадают в таблице fine и в результирующей таблице запроса query_in. -- Например, для связи по фамилии используется запись fine.name = query_in.name. Также в условии нужно учесть, что данные обновляются только для тех записей, у которых в столбце date_payment пусто.

-- ВАЖНО !!!
-- Если в запросе используется несколько таблиц или запросов, включающих одинаковые поля, то применяется полное имя столбца, включающего название таблицы через символ «.». Например,  fine.name  и  query_in.name.

SELECT * FROM traffic_violation;

UPDATE fine f, (
    SELECT name, number_plate, violation
    FROM fine
    GROUP BY name, number_plate, violation
    HAVING COUNT(name) > 1) qi
SET sum_fine = sum_fine * 2
WHERE f.name = qi.name 
    AND f.number_plate = qi.number_plate 
    AND f.violation = qi.violation 
    AND date_payment IS Null
LIMIT 1000;

-- или используя СТЕ (англ.СТЕ = рус.ОТВ - общее табличное выражение, по сути временная таблица):

WITH t AS (
    SELECT name, number_plate, violation
    FROM fine
    GROUP BY name, number_plate, violation
    HAVING COUNT(*) > 1
    )

UPDATE fine f, t
SET sum_fine = sum_fine * 2
WHERE date_payment IS NULL
    AND t.name = f.name
    AND t.number_plate = f.number_plate
    AND t.violation = f.violation
LIMIT 1000;

SELECT * FROM fine;

-- ***************************************************************************************************************
-- Водители оплачивают свои штрафы. В таблице payment занесены даты их оплаты:

DROP TABLE payment;

CREATE TABLE payment (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    number_plate VARCHAR(6),
    violation VARCHAR(50),    
    date_violation DATE,
    date_payment DATE);
    
INSERT INTO payment (name, number_plate, violation, date_violation, date_payment)
VALUES    
    ('Яковлев Г.Р.', 'М701АА', 'Превышение скорости (от 20 до 40)', '2020-01-12', '2020-01-22'),
    ('Баранов П.Е.', 'Р523ВТ', 'Превышение скорости (от 40 до 60)', '2020-02-14', '2020-03-06'),
    ('Яковлев Г.Р.', 'Т330ТТ', 'Проезд на запрещающий сигнал', '2020-03-03', '2020-03-23');    
       
SELECT * FROM payment;

-- ЗАДАНИЕ
--    в таблицу fine занести дату оплаты соответствующего штрафа из таблицы payment; 
--    уменьшить начисленный штраф в таблице fine в два раза (только для тех штрафов, информация о которых занесена в таблицу payment), если оплата произведена не позднее 20 дней со дня нарушения.

-- ПОЯСНЕНИЕ К ЗАДАНИЮ
-- 1. Для уменьшения суммы штрафа в два раза в зависимости от условия можно использовать функцию if().  Синтаксис раздела SET при использовании функции if() следующий:
-- SET столбец = IF(условие, выражение_1, выражение_2)

-- Выполняется этот оператор так:
--    сначала вычисляется условие;
--    если условие ИСТИНА, то вычисляется выражение_1, в противном случае (если условие ЛОЖНО) вычисляется выражение_2;
--    в столбец заносится результат выполнения функции (либо значение выражения_1, либо значение выражения_2 в зависимости от условия).

-- Например, чтобы обнулить штрафы, меньшие или равные 500 рублей, а остальные оставить без изменения, используется запрос:

UPDATE fine
SET sum_fine = IF(sum_fine <= 500, 0, sum_fine);

-- 2. Количество дней между датой нарушения и датой оплаты считается по формуле:
-- количество_дней = дата_оплаты - дата_нарушения

-- ПОЯСНЕНИЕ К РЕШЕНИЮ  !!! раскройте пояснение, если не получается решить или ошибка в запросе !!!
-- UPDATE 
    -- fine, payment
-- SET 
    -- fine.date_payment = дата оплаты из payment,
    -- fine.sum_fine = сравнить разницу между датой нарушения и датой оплаты (из payment) 
                    -- и при необходимости уменьшить размер штрафа (использовать IF)
-- WHERE
    -- указать условие, что совпадают и номера машин, и нарушения, и 
    -- фамилия водителя в таблицах fine и payment, а также, что
    -- дата оплаты в fine должна быть пуста

SELECT * FROM payment;

UPDATE fine f, payment p
SET f.date_payment = p.date_payment,
    sum_fine = IF(DATEDIFF(p.date_payment, p.date_violation) <= 20,
				  sum_fine / 2,
                  sum_fine)
WHERE (f.date_violation, f.name, f.number_plate, f.violation) =
      (p.date_violation, p.name, p.number_plate, p.violation)
LIMIT 1000;

SELECT * FROM fine;

-- ***************************************************************************************************************
-- ЗАДАНИЕ
-- Создать новую таблицу back_payment, куда внести информацию о неоплаченных штрафах (Фамилию и инициалы водителя, номер машины, нарушение, сумму штрафа и дату нарушения) из таблицы fine.

-- Пояснение
-- Для неоплаченных штрафов столбец date_payment имеет пустое значение.

-- Важно !!! 
-- На этом шаге необходимо создать таблицу на основе запроса! Не нужно одним запросом создавать таблицу, а вторым в нее добавлять строки.

CREATE TABLE back_payment
SELECT name, number_plate, violation, sum_fine, date_violation
FROM fine
WHERE fine.date_payment IS NULL
LIMIT 1000;

SELECT * FROM back_payment;

-- ***************************************************************************************************************
-- ЗАДАНИЕ
-- Удалить из таблицы fine информацию о нарушениях, совершенных раньше 1 февраля 2020 года.

DELETE FROM fine
WHERE date_violation < '2020-02-01'
LIMIT 1000;

-- можно приколоться и так))

DELETE FROM fine
WHERE DATEDIFF('2020.02.01', date_violation) > 0
LIMIT 1000;

SELECT * FROM fine;





















  
    