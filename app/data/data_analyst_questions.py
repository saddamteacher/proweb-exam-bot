from app.data.common import bq


DATA_ANALYST_QUESTIONS = [
    bq(
        """x = 5
print(x)

BU YERDA BIRINCHI SATR NIMA BAJARADI?""",
        """x = 5
print(x)

ЧТО ДЕЛАЕТ ПЕРВАЯ СТРОКА?""",
        {"A": "FUNKSIYA YARATADI", "B": "O'ZGARUVCHIGA QIYMAT BERADI", "C": "SIKL ISHLATADI", "D": "SQL SO'ROV YUBORADI"},
        {"A": "СОЗДАЕТ ФУНКЦИЮ", "B": "ПРИСВАИВАЕТ ЗНАЧЕНИЕ ПЕРЕМЕННОЙ", "C": "ЗАПУСКАЕТ ЦИКЛ", "D": "ОТПРАВЛЯЕТ SQL-ЗАПРОС"},
        "B",
    ),
    bq(
        """value = 3.14
print(type(value))

TYPE NATIJASI NIMA BO'LADI?""",
        """value = 3.14
print(type(value))

КАКИМ БУДЕТ РЕЗУЛЬТАТ TYPE?""",
        {"A": "int", "B": "str", "C": "float", "D": "bool"},
        {"A": "int", "B": "str", "C": "float", "D": "bool"},
        "C",
    ),
    bq(
        """for i in range(3):
    print(i)

SIKL NECHA MARTA ISHLAYDI?""",
        """for i in range(3):
    print(i)

СКОЛЬКО РАЗ СРАБОТАЕТ ЦИКЛ?""",
        {"A": "2", "B": "3", "C": "4", "D": "1"},
        {"A": "2", "B": "3", "C": "4", "D": "1"},
        "B",
    ),
    bq(
        """if sales > 100:
    print("bonus")

IF NIMA UCHUN ISHLATILGAN?""",
        """if sales > 100:
    print("bonus")

ДЛЯ ЧЕГО ИСПОЛЬЗУЕТСЯ IF?""",
        {"A": "SHART TEKSHIRISH", "B": "FUNKSIYA YARATISH", "C": "SQL JOIN", "D": "DATAFRAME SAQLASH"},
        {"A": "ПРОВЕРКА УСЛОВИЯ", "B": "СОЗДАНИЕ ФУНКЦИИ", "C": "SQL JOIN", "D": "СОХРАНЕНИЕ DATAFRAME"},
        "A",
    ),
    bq(
        """my_list = [1, 2, 3]
print(my_list[0])

MY_LIST QAYSI TUR?""",
        """my_list = [1, 2, 3]
print(my_list[0])

КАКОЙ ТИП У MY_LIST?""",
        {"A": "dict", "B": "tuple", "C": "list", "D": "set"},
        {"A": "dict", "B": "tuple", "C": "list", "D": "set"},
        "C",
    ),
    bq(
        """text = "data"
print(len(text))

LEN NATIJASI NIMA?""",
        """text = "data"
print(len(text))

КАКИМ БУДЕТ РЕЗУЛЬТАТ LEN?""",
        {"A": "3", "B": "4", "C": "5", "D": "xato"},
        {"A": "3", "B": "4", "C": "5", "D": "ошибка"},
        "B",
    ),
    bq(
        """def calc():
    return 10

CALC NIMA?""",
        """def calc():
    return 10

ЧЕМ ЯВЛЯЕТСЯ CALC?""",
        {"A": "Class", "B": "Function", "C": "SQL table", "D": "Loop"},
        {"A": "Класс", "B": "Функция", "C": "SQL table", "D": "Цикл"},
        "B",
    ),
    bq(
        """if a == b:
    print("equal")

== NIMA QILADI?""",
        """if a == b:
    print("equal")

ЧТО ДЕЛАЕТ == ?""",
        {"A": "TENGLIKNI TEKSHIRADI", "B": "QIYMAT BERADI", "C": "QO'SHADI", "D": "BO'LADI"},
        {"A": "ПРОВЕРЯЕТ РАВЕНСТВО", "B": "ПРИСВАИВАЕТ ЗНАЧЕНИЕ", "C": "СКЛАДЫВАЕТ", "D": "ДЕЛИТ"},
        "A",
    ),
    bq(
        """import pandas as pd

BU SATR NIMA QILADI?""",
        """import pandas as pd

ЧТО ДЕЛАЕТ ЭТА СТРОКА?""",
        {"A": "PANDASNI PD NOMI BILAN IMPORT QILADI", "B": "NUMPYNI OCHADI", "C": "SQL ULANISH YARATADI", "D": "GRAFIK CHIZADI"},
        {"A": "ИМПОРТИРУЕТ PANDAS КАК PD", "B": "ОТКРЫВАЕТ NUMPY", "C": "СОЗДАЕТ SQL-ПОДКЛЮЧЕНИЕ", "D": "СТРОИТ ГРАФИК"},
        "A",
    ),
    bq(
        """df = pd.read_csv("sales.csv")

READ_CSV NIMA UCHUN?""",
        """df = pd.read_csv("sales.csv")

ДЛЯ ЧЕГО НУЖЕН READ_CSV?""",
        {"A": "CSV FAYLNI O'QISH", "B": "GRAFIK CHIZISH", "C": "SQL TABLE YARATISH", "D": "ARRAY YARATISH"},
        {"A": "ЧТЕНИЕ CSV-ФАЙЛА", "B": "ПОСТРОЕНИЕ ГРАФИКА", "C": "СОЗДАНИЕ SQL-ТАБЛИЦЫ", "D": "СОЗДАНИЕ ARRAY"},
        "A",
    ),
    bq(
        """df.head()

HEAD() ODATDA NIMANI KO'RSATADI?""",
        """df.head()

ЧТО ОБЫЧНО ПОКАЗЫВАЕТ HEAD()?""",
        {"A": "OXIRGI 5 QATOR", "B": "BIRINCHI 5 QATOR", "C": "FAQAT USTUNLAR", "D": "FAQAT SHAPE"},
        {"A": "ПОСЛЕДНИЕ 5 СТРОК", "B": "ПЕРВЫЕ 5 СТРОК", "C": "ТОЛЬКО СТОЛБЦЫ", "D": "ТОЛЬКО SHAPE"},
        "B",
    ),
    bq(
        """arr = np.array([1, 2, 3])

ARR NIMA?""",
        """arr = np.array([1, 2, 3])

ЧЕМ ЯВЛЯЕТСЯ ARR?""",
        {"A": "DataFrame", "B": "numpy array", "C": "list", "D": "sql"},
        {"A": "DataFrame", "B": "numpy array", "C": "list", "D": "sql"},
        "B",
    ),
    bq(
        """rows, cols = df.shape

SHAPE NIMA BERADI?""",
        """rows, cols = df.shape

ЧТО ДАЕТ SHAPE?""",
        {"A": "SATR VA USTUN SONI", "B": "MEAN", "C": "JOIN", "D": "CHART"},
        {"A": "КОЛИЧЕСТВО СТРОК И СТОЛБЦОВ", "B": "MEAN", "C": "JOIN", "D": "CHART"},
        "A",
    ),
    bq(
        """plt.plot(x, y)

PLOT QAYSI KUTUBXONAGA TEGISHLI?""",
        """plt.plot(x, y)

К КАКОЙ БИБЛИОТЕКЕ ОТНОСИТСЯ PLOT?""",
        {"A": "seaborn", "B": "matplotlib", "C": "pandas", "D": "sqlalchemy"},
        {"A": "seaborn", "B": "matplotlib", "C": "pandas", "D": "sqlalchemy"},
        "B",
    ),
    bq(
        """sns.heatmap(corr)

HEATMAP NIMA UCHUN?""",
        """sns.heatmap(corr)

ДЛЯ ЧЕГО НУЖЕН HEATMAP?""",
        {"A": "ISSIQLIK XARITASI", "B": "CSV O'QISH", "C": "TOKEN SAQLASH", "D": "JOIN"},
        {"A": "ПОСТРОЕНИЕ HEATMAP", "B": "ЧТЕНИЕ CSV", "C": "ХРАНЕНИЕ ТОКЕНА", "D": "JOIN"},
        "A",
    ),
    bq(
        """df.describe()

DESCRIBE() NIMA QAYTARADI?""",
        """df.describe()

ЧТО ВОЗВРАЩАЕТ DESCRIBE()?""",
        {"A": "STATISTIK SUMMARY", "B": "CHART", "C": "SQL DELETE", "D": "ARRAY"},
        {"A": "СТАТИСТИЧЕСКУЮ СВОДКУ", "B": "CHART", "C": "SQL DELETE", "D": "ARRAY"},
        "A",
    ),
    bq(
        """SELECT * FROM sales;

BARCHA MA'LUMOTNI OLISH UCHUN ASOSIY BUYRUQ QAYSI?""",
        """SELECT * FROM sales;

КАКАЯ ОСНОВНАЯ КОМАНДА ИСПОЛЬЗУЕТСЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ?""",
        {"A": "GET", "B": "SELECT", "C": "SHOW", "D": "ALL"},
        {"A": "GET", "B": "SELECT", "C": "SHOW", "D": "ALL"},
        "B",
    ),
    bq(
        """SELECT * FROM sales
WHERE amount > 100;

WHERE NIMA UCHUN?""",
        """SELECT * FROM sales
WHERE amount > 100;

ДЛЯ ЧЕГО НУЖЕН WHERE?""",
        {"A": "FILTERLASH", "B": "JOIN", "C": "SORT", "D": "GROUP"},
        {"A": "ФИЛЬТРАЦИЯ", "B": "JOIN", "C": "СОРТИРОВКА", "D": "ГРУППИРОВКА"},
        "A",
    ),
    bq(
        """SELECT COUNT(*) FROM users;

COUNT() NIMA QILADI?""",
        """SELECT COUNT(*) FROM users;

ЧТО ДЕЛАЕТ COUNT()?""",
        {"A": "SANAYDI", "B": "QO'SHADI", "C": "UZUNLIKNI O'LCHAYDI", "D": "O'RTACHA OLADI"},
        {"A": "СЧИТАЕТ", "B": "СУММИРУЕТ", "C": "ИЗМЕРЯЕТ ДЛИНУ", "D": "СЧИТАЕТ СРЕДНЕЕ"},
        "A",
    ),
    bq(
        """SELECT * FROM users
ORDER BY created_at DESC;

ORDER BY NIMA UCHUN?""",
        """SELECT * FROM users
ORDER BY created_at DESC;

ДЛЯ ЧЕГО НУЖЕН ORDER BY?""",
        {"A": "SARALASH", "B": "FILTER", "C": "DELETE", "D": "JOIN"},
        {"A": "СОРТИРОВКА", "B": "ФИЛЬТР", "C": "УДАЛЕНИЕ", "D": "JOIN"},
        "A",
    ),
    bq(
        """SELECT *
FROM orders o
JOIN users u ON o.user_id = u.id;

JOIN NIMA UCHUN?""",
        """SELECT *
FROM orders o
JOIN users u ON o.user_id = u.id;

ДЛЯ ЧЕГО НУЖЕН JOIN?""",
        {"A": "IKKI TABLE ULASH", "B": "SATRNI O'CHIRISH", "C": "CSV O'QISH", "D": "FORMULA YASASH"},
        {"A": "СОЕДИНЕНИЕ ДВУХ ТАБЛИЦ", "B": "УДАЛЕНИЕ СТРОКИ", "C": "ЧТЕНИЕ CSV", "D": "СОЗДАНИЕ ФОРМУЛЫ"},
        "A",
    ),
    bq(
        """SELECT region, COUNT(*)
FROM sales
GROUP BY region;

GROUP BY NIMA QILADI?""",
        """SELECT region, COUNT(*)
FROM sales
GROUP BY region;

ЧТО ДЕЛАЕТ GROUP BY?""",
        {"A": "GURUHLAYDI", "B": "SARALAYDI", "C": "O'CHIRADI", "D": "FILTERLAYDI"},
        {"A": "ГРУППИРУЕТ", "B": "СОРТИРУЕТ", "C": "УДАЛЯЕТ", "D": "ФИЛЬТРУЕТ"},
        "A",
    ),
    bq(
        """SELECT MAX(price)
FROM products;

MAX() NIMA QAYTARADI?""",
        """SELECT MAX(price)
FROM products;

ЧТО ВОЗВРАЩАЕТ MAX()?""",
        {"A": "ENG KICHIK QIYMAT", "B": "ENG KATTA QIYMAT", "C": "O'RTACHA QIYMAT", "D": "SATRLAR SONI"},
        {"A": "МИНИМАЛЬНОЕ ЗНАЧЕНИЕ", "B": "МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ", "C": "СРЕДНЕЕ ЗНАЧЕНИЕ", "D": "КОЛИЧЕСТВО СТРОК"},
        "B",
    ),
    bq(
        """INSERT INTO users (name)
VALUES ('Ali');

INSERT INTO NIMA UCHUN?""",
        """INSERT INTO users (name)
VALUES ('Ali');

ДЛЯ ЧЕГО НУЖЕН INSERT INTO?""",
        {"A": "YANGI QATOR QO'SHISH", "B": "USTUNNI O'CHIRISH", "C": "TABLE NOMINI O'ZGARTIRISH", "D": "SELECT QILISH"},
        {"A": "ДОБАВЛЕНИЕ НОВОЙ СТРОКИ", "B": "УДАЛЕНИЕ СТОЛБЦА", "C": "ПЕРЕИМЕНОВАНИЕ ТАБЛИЦЫ", "D": "ВЫПОЛНЕНИЕ SELECT"},
        "A",
    ),
]
