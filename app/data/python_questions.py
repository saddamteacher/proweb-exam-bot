from app.data.common import bq


PYTHON_QUESTIONS = [
    bq(
        """a = "hello"
b = "world"
print(a, b)

BU KOD NIMA CHIQARADI?""",
        """a = "hello"
b = "world"
print(a, b)

ЧТО ВЫВЕДЕТ ЭТОТ КОД?""",
        {"A": "HELLOWORLD", "B": "hello world", "C": "['hello', 'world']", "D": "XATO"},
        {"A": "HELLOWORLD", "B": "hello world", "C": "['hello', 'world']", "D": "ОШИБКА"},
        "B",
    ),
    bq(
        """x = 10
if x > 5:
    print("katta")

IF BU YERDA NIMA ISH BAJARADI?""",
        """x = 10
if x > 5:
    print("bolshe")

ЧТО ДЕЛАЕТ IF В ЭТОМ ПРИМЕРЕ?""",
        {"A": "SIKL ISHLATADI", "B": "SHARTNI TEKSHIRADI", "C": "FUNKSIYA YARATADI", "D": "RO'YXAT TUZADI"},
        {"A": "ЗАПУСКАЕТ ЦИКЛ", "B": "ПРОВЕРЯЕТ УСЛОВИЕ", "C": "СОЗДАЕТ ФУНКЦИЮ", "D": "СОЗДАЕТ СПИСОК"},
        "B",
    ),
    bq(
        """for i in range(3):
    print(i)

BU SIKL NECHA MARTA ISHLAYDI?""",
        """for i in range(3):
    print(i)

СКОЛЬКО РАЗ СРАБОТАЕТ ЦИКЛ?""",
        {"A": "2", "B": "3", "C": "4", "D": "CHEKSIZ"},
        {"A": "2", "B": "3", "C": "4", "D": "БЕСКОНЕЧНО"},
        "B",
    ),
    bq(
        """def salom():
    print("Salom")

SALOM BU YERDA NIMA?""",
        """def salom():
    print("Привет")

ЧЕМ ЯВЛЯЕТСЯ SALOM В ЭТОМ КОДЕ?""",
        {"A": "KLASS", "B": "FUNKSIYA", "C": "MODUL", "D": "OBYEKT"},
        {"A": "КЛАСС", "B": "ФУНКЦИЯ", "C": "МОДУЛЬ", "D": "ОБЪЕКТ"},
        "B",
    ),
    bq(
        """text = "python"
print(len(text))

NATIJA QANCHA BO'LADI?""",
        """text = "python"
print(len(text))

КАКИМ БУДЕТ РЕЗУЛЬТАТ?""",
        {"A": "5", "B": "6", "C": "7", "D": "XATO"},
        {"A": "5", "B": "6", "C": "7", "D": "ОШИБКА"},
        "B",
    ),
    bq(
        """items = ["olma", "anor"]
print(items[0])

ITEMS QAYSI TURGA KIRADI?""",
        """items = ["apple", "pomegranate"]
print(items[0])

К КАКОМУ ТИПУ ОТНОСИТСЯ ITEMS?""",
        {"A": "DICT", "B": "SET", "C": "LIST", "D": "TUPLE"},
        {"A": "DICT", "B": "SET", "C": "LIST", "D": "TUPLE"},
        "C",
    ),
    bq(
        """user = {"ism": "Ali", "yosh": 20}
print(user["ism"])

USER QAYSI TURDAGI MA'LUMOT?""",
        """user = {"name": "Ali", "age": 20}
print(user["name"])

КАКОЙ ТИП ДАННЫХ У USER?""",
        {"A": "DICT", "B": "LIST", "C": "STRING", "D": "INT"},
        {"A": "DICT", "B": "LIST", "C": "STRING", "D": "INT"},
        "A",
    ),
    bq(
        """# test kodi
print("start")

BIRINCHI QATOR NIMA VAZIFA BAJARADI?""",
        """# test code
print("start")

ЧТО ДЕЛАЕТ ПЕРВАЯ СТРОКА?""",
        {"A": "IMPORT QILADI", "B": "IZOH", "C": "FUNKSIYANI CHAQIRADI", "D": "XATOLIK BERADI"},
        {"A": "ИМПОРТИРУЕТ", "B": "КОММЕНТАРИЙ", "C": "ВЫЗЫВАЕТ ФУНКЦИЮ", "D": "ВЫДАЕТ ОШИБКУ"},
        "B",
    ),
    bq(
        """x = 10
y = 5

BIRINCHI SATR NIMA BAJARADI?""",
        """x = 10
y = 5

ЧТО ДЕЛАЕТ ПЕРВАЯ СТРОКА?""",
        {"A": "TAQQOSLAYDI", "B": "QIYMAT TAYINLAYDI", "C": "SIKL BOSHLAYDI", "D": "XATOLIK BERADI"},
        {"A": "СРАВНИВАЕТ", "B": "ПРИСВАИВАЕТ ЗНАЧЕНИЕ", "C": "ЗАПУСКАЕТ ЦИКЛ", "D": "ВЫДАЕТ ОШИБКУ"},
        "B",
    ),
    bq(
        """if x == 10:
    print("ok")

== OPERATORI NIMA UCHUN?""",
        """if x == 10:
    print("ok")

ДЛЯ ЧЕГО НУЖЕН ОПЕРАТОР == ?""",
        {"A": "TENGLIKNI TEKSHIRISH", "B": "QIYMAT BERISH", "C": "LIST YARATISH", "D": "IMPORT"},
        {"A": "ПРОВЕРКА РАВЕНСТВА", "B": "ПРИСВАИВАНИЕ", "C": "СОЗДАНИЕ СПИСКА", "D": "ИМПОРТ"},
        "A",
    ),
    bq(
        """class Car:
    pass

BU KODDA NIMA YARATILGAN?""",
        """class Car:
    pass

ЧТО СОЗДАНО В ЭТОМ КОДЕ?""",
        {"A": "FUNKSIYA", "B": "MODUL", "C": "KLASS", "D": "OBYEKT"},
        {"A": "ФУНКЦИЯ", "B": "МОДУЛЬ", "C": "КЛАСС", "D": "ОБЪЕКТ"},
        "C",
    ),
    bq(
        """class Car:
    pass

obj = Car()

OBJ NIMA?""",
        """class Car:
    pass

obj = Car()

ЧЕМ ЯВЛЯЕТСЯ OBJ?""",
        {"A": "KLASSDAN OLGAN NUSXA", "B": "MODUL", "C": "IMPORT", "D": "DEKORATOR"},
        {"A": "ЭКЗЕМПЛЯР КЛАССА", "B": "МОДУЛЬ", "C": "ИМПОРТ", "D": "ДЕКОРАТОР"},
        "A",
    ),
    bq(
        """class User:
    def __init__(self, name):
        self.name = name

__init__ NIMA UCHUN KERAK?""",
        """class User:
    def __init__(self, name):
        self.name = name

ДЛЯ ЧЕГО НУЖЕН __init__?""",
        {"A": "OBYEKTNI BOSHLANG'ICH HOLATDA YARATISH", "B": "SIKL", "C": "IMPORT", "D": "DELETE"},
        {"A": "ДЛЯ ИНИЦИАЛИЗАЦИИ ОБЪЕКТА", "B": "ДЛЯ ЦИКЛА", "C": "ДЛЯ ИМПОРТА", "D": "ДЛЯ УДАЛЕНИЯ"},
        "A",
    ),
    bq(
        """class User:
    def show(self):
        return self.name

SELF NIMANI BILDIRADI?""",
        """class User:
    def show(self):
        return self.name

ЧТО ОЗНАЧАЕТ SELF?""",
        {"A": "KLASS NOMI", "B": "JORIY OBYEKT", "C": "MODUL", "D": "SERVER"},
        {"A": "ИМЯ КЛАССА", "B": "ТЕКУЩИЙ ОБЪЕКТ", "C": "МОДУЛЬ", "D": "СЕРВЕР"},
        "B",
    ),
    bq(
        """class Animal:
    pass

class Cat(Animal):
    pass

BU MISOLDA QANDAY G'OYA BOR?""",
        """class Animal:
    pass

class Cat(Animal):
    pass

КАКОЙ ПРИНЦИП ПОКАЗАН В ЭТОМ ПРИМЕРЕ?""",
        {"A": "INHERITANCE", "B": "DEBUG", "C": "LOOP", "D": "IMPORT"},
        {"A": "НАСЛЕДОВАНИЕ", "B": "ОТЛАДКА", "C": "ЦИКЛ", "D": "ИМПОРТ"},
        "A",
    ),
    bq(
        """class Bird:
    def sound(self):
        return "tweet"

class Dog:
    def sound(self):
        return "woof"

ASOSIY G'OYA NIMA?""",
        """class Bird:
    def sound(self):
        return "tweet"

class Dog:
    def sound(self):
        return "woof"

КАКАЯ ОСНОВНАЯ ИДЕЯ ЗДЕСЬ?""",
        {"A": "POLYMORPHISM", "B": "ENCAPSULATION", "C": "MIGRATION", "D": "INDEXING"},
        {"A": "ПОЛИМОРФИЗМ", "B": "ИНКАПСУЛЯЦИЯ", "C": "МИГРАЦИЯ", "D": "ИНДЕКСАЦИЯ"},
        "A",
    ),
    bq(
        """class User:
    def __init__(self):
        self.__password = "1234"

BU YERDA QAYSI OOP G'OYASI BOR?""",
        """class User:
    def __init__(self):
        self.__password = "1234"

КАКОЙ ПРИНЦИП OOP ПОКАЗАН ЗДЕСЬ?""",
        {"A": "ENCAPSULATION", "B": "POLYMORPHISM", "C": "INHERITANCE", "D": "DEBUGGING"},
        {"A": "ИНКАПСУЛЯЦИЯ", "B": "ПОЛИМОРФИЗМ", "C": "НАСЛЕДОВАНИЕ", "D": "ОТЛАДКА"},
        "A",
    ),
    bq(
        """class Product:
    def __str__(self):
        return "Book"

__str__ NIMA UCHUN KERAK?""",
        """class Product:
    def __str__(self):
        return "Book"

ДЛЯ ЧЕГО НУЖЕН __str__?""",
        {"A": "OBYEKTNI MATN KO'RINISHIDA CHIQARISH", "B": "CLASS OCHISH", "C": "SIKL ISHLATISH", "D": "IMPORT"},
        {"A": "ТЕКСТОВОЕ ПРЕДСТАВЛЕНИЕ ОБЪЕКТА", "B": "СОЗДАНИЕ КЛАССА", "C": "ЗАПУСК ЦИКЛА", "D": "ИМПОРТ"},
        "A",
    ),
    bq(
        """try:
    x = 1 / 0
except ZeroDivisionError:
    print("xato")

TRY/EXCEPT NIMA UCHUN?""",
        """try:
    x = 1 / 0
except ZeroDivisionError:
    print("error")

ДЛЯ ЧЕГО НУЖЕН TRY/EXCEPT?""",
        {"A": "XATOLARNI USHLASH", "B": "HTML CHIQARISH", "C": "BOT YARATISH", "D": "URL OCHISH"},
        {"A": "ОБРАБОТКА ОШИБОК", "B": "ВЫВОД HTML", "C": "СОЗДАНИЕ БОТА", "D": "ОТКРЫТИЕ URL"},
        "A",
    ),
    bq(
        """while x > 0:
    x -= 1

WHILE NIMA BAJARADI?""",
        """while x > 0:
    x -= 1

ЧТО ДЕЛАЕТ WHILE?""",
        {"A": "SHARTLI SIKL YARATADI", "B": "CLASS OCHADI", "C": "IMPORT QILADI", "D": "URL TUZADI"},
        {"A": "СОЗДАЕТ УСЛОВНЫЙ ЦИКЛ", "B": "СОЗДАЕТ КЛАСС", "C": "ИМПОРТИРУЕТ", "D": "СОЗДАЕТ URL"},
        "A",
    ),
    bq(
        """for i in range(10):
    if i == 5:
        break

BREAK NIMA QILADI?""",
        """for i in range(10):
    if i == 5:
        break

ЧТО ДЕЛАЕТ BREAK?""",
        {"A": "SIKLNI TO'XTATADI", "B": "KEYINGI ITERATSIYAGA O'TADI", "C": "XATONI USHLAYDI", "D": "PRINT QILADI"},
        {"A": "ОСТАНАВЛИВАЕТ ЦИКЛ", "B": "ПЕРЕХОДИТ К СЛЕДУЮЩЕЙ ИТЕРАЦИИ", "C": "ЛОВИТ ОШИБКУ", "D": "ПЕЧАТАЕТ"},
        "A",
    ),
    bq(
        """for i in range(5):
    if i == 2:
        continue
    print(i)

CONTINUE NIMA QILADI?""",
        """for i in range(5):
    if i == 2:
        continue
    print(i)

ЧТО ДЕЛАЕТ CONTINUE?""",
        {"A": "JORIY ITERATSIYANI O'TKAZIB YUBORADI", "B": "DASTURNI TUGATADI", "C": "IMPORTNI O'CHIRADI", "D": "SIKLNI TESKARI QILADI"},
        {"A": "ПРОПУСКАЕТ ТЕКУЩУЮ ИТЕРАЦИЮ", "B": "ЗАВЕРШАЕТ ПРОГРАММУ", "C": "УДАЛЯЕТ ИМПОРТ", "D": "РАЗВОРАЧИВАЕТ ЦИКЛ"},
        "A",
    ),
    bq(
        """from aiogram import Bot, Dispatcher

QAYSI KUTUBXONA ISHLATILYAPTI?""",
        """from aiogram import Bot, Dispatcher

КАКАЯ БИБЛИОТЕКА ИСПОЛЬЗУЕТСЯ?""",
        {"A": "DJANGO", "B": "AIOGRAM", "C": "NUMPY", "D": "PANDAS"},
        {"A": "DJANGO", "B": "AIOGRAM", "C": "NUMPY", "D": "PANDAS"},
        "B",
    ),
    bq(
        """@dp.message(Command("start"))
async def cmd_start(message):
    await message.answer("Salom")

HANDLER QAYSI BUYRUQDA ISHLAYDI?""",
        """@dp.message(Command("start"))
async def cmd_start(message):
    await message.answer("Privet")

НА КАКОЙ КОМАНДЕ СРАБАТЫВАЕТ HANDLER?""",
        {"A": "/HELP", "B": "/START", "C": "/STOP", "D": "/PING"},
        {"A": "/HELP", "B": "/START", "C": "/STOP", "D": "/PING"},
        "B",
    ),
    bq(
        """@dp.message()
async def echo(message):
    await message.answer("ok")

HANDLER BU YERDA NIMA VAZIFA BAJARADI?""",
        """@dp.message()
async def echo(message):
    await message.answer("ok")

ЧТО ДЕЛАЕТ HANDLER В ЭТОМ ПРИМЕРЕ?""",
        {"A": "SO'ROVNI USHLAYDI", "B": "DATABASE YARATADI", "C": "RASMLARNI SAQLAYDI", "D": "CSS O'ZGARTIRADI"},
        {"A": "ОБРАБАТЫВАЕТ ЗАПРОС", "B": "СОЗДАЕТ БАЗУ ДАННЫХ", "C": "СОХРАНЯЕТ ИЗОБРАЖЕНИЯ", "D": "МЕНЯЕТ CSS"},
        "A",
    ),
    bq(
        """await message.answer("Salom")

BU SATR NIMA QILADI?""",
        """await message.answer("Privet")

ЧТО ДЕЛАЕТ ЭТА СТРОКА?""",
        {"A": "USERGA JAVOB YUBORADI", "B": "FAYL OCHADI", "C": "BOTNI O'CHIRADI", "D": "TOKENNI O'ZGARTIRADI"},
        {"A": "ОТПРАВЛЯЕТ ОТВЕТ ПОЛЬЗОВАТЕЛЮ", "B": "ОТКРЫВАЕТ ФАЙЛ", "C": "ВЫКЛЮЧАЕТ БОТА", "D": "МЕНЯЕТ ТОКЕН"},
        "A",
    ),
    bq(
        """await state.set_state(Form.name)

FSM ASOSAN NIMA UCHUN KERAK?""",
        """await state.set_state(Form.name)

ДЛЯ ЧЕГО В ОСНОВНОМ НУЖЕН FSM?""",
        {"A": "HOLATLARNI BOSHQARISH", "B": "DATABASE SAQLASH", "C": "RASM CHIZISH", "D": "SERVER YOPISH"},
        {"A": "УПРАВЛЕНИЕ СОСТОЯНИЯМИ", "B": "ХРАНЕНИЕ В БАЗЕ", "C": "РИСОВАНИЕ", "D": "ОСТАНОВКА СЕРВЕРА"},
        "A",
    ),
    bq(
        """builder.button(text="NEXT")

INLINE TUGMALARNING VAZIFASI NIMA?""",
        """builder.button(text="NEXT")

ДЛЯ ЧЕГО НУЖНЫ INLINE-КНОПКИ?""",
        {"A": "ICHKI TUGMALAR CHIQARISH", "B": "DATABASE ULASH", "C": "AUDIO YOZISH", "D": "SERVER YOPISH"},
        {"A": "ПОКАЗ ВСТРОЕННЫХ КНОПОК", "B": "ПОДКЛЮЧЕНИЕ БАЗЫ", "C": "ЗАПИСЬ АУДИО", "D": "ОСТАНОВКА СЕРВЕРА"},
        "A",
    ),
    bq(
        """@dp.message()
async def get_text(message):
    pass

@dp.message() NIMA?""",
        """@dp.message()
async def get_text(message):
    pass

ЧЕМ ЯВЛЯЕТСЯ @dp.message()?""",
        {"A": "DECORATOR", "B": "MODEL", "C": "URL", "D": "LIST"},
        {"A": "ДЕКОРАТОР", "B": "МОДЕЛЬ", "C": "URL", "D": "СПИСОК"},
        "A",
    ),
    bq(
        """from aiogram import Bot

BU IMPORT NIMA QILADI?""",
        """from aiogram import Bot

ЧТО ДЕЛАЕТ ЭТОТ ИМПОРТ?""",
        {"A": "BOT KLASSINI IMPORT QILADI", "B": "BOTNI O'CHIRADI", "C": "DATABASE YOPADI", "D": "FAYL YARATADI"},
        {"A": "ИМПОРТИРУЕТ КЛАСС BOT", "B": "УДАЛЯЕТ БОТА", "C": "ЗАКРЫВАЕТ БАЗУ ДАННЫХ", "D": "СОЗДАЕТ ФАЙЛ"},
        "A",
    ),
    bq(
        """await bot.send_message(chat_id, "Hello")

ASOSIY NATIJA NIMA?""",
        """await bot.send_message(chat_id, "Hello")

КАКОЙ ОСНОВНОЙ РЕЗУЛЬТАТ?""",
        {"A": "CHATGA XABAR YUBORADI", "B": "USERNI O'CHIRADI", "C": "TOKEN YANGILAYDI", "D": "FAYL OCHADI"},
        {"A": "ОТПРАВЛЯЕТ СООБЩЕНИЕ В ЧАТ", "B": "УДАЛЯЕТ ПОЛЬЗОВАТЕЛЯ", "C": "ОБНОВЛЯЕТ ТОКЕН", "D": "ОТКРЫВАЕТ ФАЙЛ"},
        "A",
    ),
    bq(
        """@router.message(F.text == "hi")
async def hello(message):
    await message.answer("ok")

BU FILTER NIMANI TEKSHIRADI?""",
        """@router.message(F.text == "hi")
async def hello(message):
    await message.answer("ok")

ЧТО ПРОВЕРЯЕТ ЭТОТ ФИЛЬТР?""",
        {"A": "MATN 'hi' GA TENGLIGINI", "B": "USER IDNI", "C": "CHAT TURINI", "D": "TOKENNI"},
        {"A": "ЧТО ТЕКСТ РАВЕН 'hi'", "B": "ID ПОЛЬЗОВАТЕЛЯ", "C": "ТИП ЧАТА", "D": "ТОКЕН"},
        "A",
    ),
    bq(
        """from django.shortcuts import render

DJANGO NIMA?""",
        """from django.shortcuts import render

ЧТО ТАКОЕ DJANGO?""",
        {"A": "PYTHON WEB FRAMEWORK", "B": "MESSENGER", "C": "VIDEO EDITOR", "D": "OS"},
        {"A": "PYTHON WEB FRAMEWORK", "B": "МЕССЕНДЖЕР", "C": "ВИДЕОРЕДАКТОР", "D": "ОС"},
        "A",
    ),
    bq(
        """python manage.py startapp blog

BU KOMANDA NIMA QILADI?""",
        """python manage.py startapp blog

ЧТО ДЕЛАЕТ ЭТА КОМАНДА?""",
        {"A": "YANGI APP YARATADI", "B": "SERVERNI TO'XTATADI", "C": "HTML SAQLAYDI", "D": "TOKEN OLADI"},
        {"A": "СОЗДАЕТ НОВОЕ ПРИЛОЖЕНИЕ", "B": "ОСТАНАВЛИВАЕТ СЕРВЕР", "C": "СОХРАНЯЕТ HTML", "D": "ПОЛУЧАЕТ ТОКЕН"},
        "A",
    ),
    bq(
        """class Post(models.Model):
    title = models.CharField(max_length=100)

POST BU YERDA NIMA?""",
        """class Post(models.Model):
    title = models.CharField(max_length=100)

ЧЕМ ЯВЛЯЕТСЯ POST ЗДЕСЬ?""",
        {"A": "MODEL", "B": "TEMPLATE", "C": "VIEW", "D": "URL"},
        {"A": "МОДЕЛЬ", "B": "ШАБЛОН", "C": "ПРЕДСТАВЛЕНИЕ", "D": "URL"},
        "A",
    ),
    bq(
        """def home(request):
    return render(request, "home.html")

HOME BU YERDA NIMA?""",
        """def home(request):
    return render(request, "home.html")

ЧЕМ ЯВЛЯЕТСЯ HOME ЗДЕСЬ?""",
        {"A": "VIEW", "B": "MODEL", "C": "MIGRATION", "D": "ADMIN"},
        {"A": "ПРЕДСТАВЛЕНИЕ", "B": "МОДЕЛЬ", "C": "МИГРАЦИЯ", "D": "АДМИН"},
        "A",
    ),
    bq(
        """return render(request, "home.html")

HOME.HTML QAYSI TURGA KIRADI?""",
        """return render(request, "home.html")

К КАКОМУ ТИПУ ОТНОСИТСЯ HOME.HTML?""",
        {"A": "TEMPLATE", "B": "MODEL", "C": "FORM", "D": "MIDDLEWARE"},
        {"A": "ШАБЛОН", "B": "МОДЕЛЬ", "C": "ФОРМА", "D": "MIDDLEWARE"},
        "A",
    ),
    bq(
        """urlpatterns = [
    path("", home),
]

URLLAR ODATDA QAYSI FAYLDA BO'LADI?""",
        """urlpatterns = [
    path("", home),
]

В КАКОМ ФАЙЛЕ ОБЫЧНО ХРАНЯТСЯ URL?""",
        {"A": "urls.py", "B": "views.py", "C": "models.py", "D": "apps.py"},
        {"A": "urls.py", "B": "views.py", "C": "models.py", "D": "apps.py"},
        "A",
    ),
    bq(
        """python manage.py runserver

BU KOMANDA NIMA BAJARADI?""",
        """python manage.py runserver

ЧТО ДЕЛАЕТ ЭТА КОМАНДА?""",
        {"A": "SERVERNI ISHGA TUSHIRADI", "B": "MIGRATION YARATADI", "C": "BOTNI TO'XTATADI", "D": "APP O'CHIRADI"},
        {"A": "ЗАПУСКАЕТ СЕРВЕР", "B": "СОЗДАЕТ МИГРАЦИЮ", "C": "ОСТАНАВЛИВАЕТ БОТА", "D": "УДАЛЯЕТ ПРИЛОЖЕНИЕ"},
        "A",
    ),
    bq(
        """python manage.py makemigrations

BU NIMA UCHUN KERAK?""",
        """python manage.py makemigrations

ДЛЯ ЧЕГО НУЖНА ЭТА КОМАНДА?""",
        {"A": "MODEL O'ZGARISHLARINI TAYYORLAYDI", "B": "CSS BUILD", "C": "BOT TOKEN OCHADI", "D": "ADMIN YOPADI"},
        {"A": "ГОТОВИТ ИЗМЕНЕНИЯ МОДЕЛЕЙ", "B": "СОБИРАЕТ CSS", "C": "ОТКРЫВАЕТ ТОКЕН БОТА", "D": "ЗАКРЫВАЕТ АДМИНКУ"},
        "A",
    ),
    bq(
        """python manage.py migrate

BU KOMANDA NIMA QILADI?""",
        """python manage.py migrate

ЧТО ДЕЛАЕТ ЭТА КОМАНДА?""",
        {"A": "O'ZGARISHLARNI DATABASEGA YOZADI", "B": "RASM CHIQARADI", "C": "IMPORT TOZALAYDI", "D": "BOTNI START QILADI"},
        {"A": "ПРИМЕНЯЕТ ИЗМЕНЕНИЯ К БАЗЕ ДАННЫХ", "B": "ВЫВОДИТ ИЗОБРАЖЕНИЕ", "C": "ЧИСТИТ ИМПОРТЫ", "D": "ЗАПУСКАЕТ БОТА"},
        "A",
    ),
    bq(
        """queryset = Post.objects.all()

OBJECTS.ALL() NIMA QAYTARADI?""",
        """queryset = Post.objects.all()

ЧТО ВОЗВРАЩАЕТ OBJECTS.ALL()?""",
        {"A": "BARCHA YOZUVLAR", "B": "BITTA YOZUV", "C": "SERVER STATUSI", "D": "TOKEN"},
        {"A": "ВСЕ ЗАПИСИ", "B": "ОДНУ ЗАПИСЬ", "C": "СТАТУС СЕРВЕРА", "D": "ТОКЕН"},
        "A",
    ),
    bq(
        """async def fetch_data():
    return 1

ASYNC DEF NIMANI BILDIRADI?""",
        """async def fetch_data():
    return 1

ЧТО ОЗНАЧАЕТ ASYNC DEF?""",
        {"A": "ASINXRON FUNKSIYA", "B": "ODDIY CLASS", "C": "DJANGO MODEL", "D": "HTML TEG"},
        {"A": "АСИНХРОННАЯ ФУНКЦИЯ", "B": "ОБЫЧНЫЙ КЛАСС", "C": "МОДЕЛЬ DJANGO", "D": "HTML-ТЕГ"},
        "A",
    ),
    bq(
        """async def main():
    await fetch_data()

AWAIT QAYERDA ISHLATILADI?""",
        """async def main():
    await fetch_data()

ГДЕ ИСПОЛЬЗУЕТСЯ AWAIT?""",
        {"A": "ASYNC ICHIDA", "B": "CLASS ICHIDA", "C": "HTMLDA", "D": "MIGRATEDA"},
        {"A": "ВНУТРИ ASYNC", "B": "ВНУТРИ CLASS", "C": "В HTML", "D": "В MIGRATE"},
        "A",
    ),
    bq(
        """python manage.py createsuperuser

BU KOMANDA NIMA YARATADI?""",
        """python manage.py createsuperuser

ЧТО СОЗДАЕТ ЭТА КОМАНДА?""",
        {"A": "DJANGO ADMIN USER", "B": "BOT TOKEN", "C": "HTML TEMPLATE", "D": "CSS FAYL"},
        {"A": "ПОЛЬЗОВАТЕЛЯ АДМИНКИ DJANGO", "B": "ТОКЕН БОТА", "C": "HTML-ШАБЛОН", "D": "CSS-ФАЙЛ"},
        "A",
    ),
]
