from app.data.common import bq


MS_OFFICE_QUESTIONS = [
    bq(
        """=SUM(A1:A10)

BU FORMULA NIMA QILADI?""",
        """=SUM(A1:A10)

ЧТО ДЕЛАЕТ ЭТА ФОРМУЛА?""",
        {"A": "O'RTACHANI OLADI", "B": "ENG KATTASINI TOPADI", "C": "YIG'INDINI HISOBLAYDI", "D": "SATRLARNI SANAYDI"},
        {"A": "СЧИТАЕТ СРЕДНЕЕ", "B": "ИЩЕТ МАКСИМУМ", "C": "СЧИТАЕТ СУММУ", "D": "СЧИТАЕТ СТРОКИ"},
        "C",
    ),
    bq(
        """=AVERAGE(B1:B5)

AVERAGE FORMULASI NIMA UCHUN?""",
        """=AVERAGE(B1:B5)

ДЛЯ ЧЕГО НУЖНА ФОРМУЛА AVERAGE?""",
        {"A": "O'RTACHA QIYMAT", "B": "YIG'INDI", "C": "MINIMUM", "D": "FILTER"},
        {"A": "СРЕДНЕЕ ЗНАЧЕНИЕ", "B": "СУММА", "C": "МИНИМУМ", "D": "ФИЛЬТР"},
        "A",
    ),
    bq(
        """=MAX(C1:C10)

MAX NIMA QAYTARADI?""",
        """=MAX(C1:C10)

ЧТО ВОЗВРАЩАЕТ MAX?""",
        {"A": "ENG KICHIK QIYMAT", "B": "ENG KATTA QIYMAT", "C": "O'RTACHA", "D": "SONI"},
        {"A": "МИНИМАЛЬНОЕ ЗНАЧЕНИЕ", "B": "МАКСИМАЛЬНОЕ ЗНАЧЕНИЕ", "C": "СРЕДНЕЕ", "D": "КОЛИЧЕСТВО"},
        "B",
    ),
    bq(
        """Sheet ichida yangi varaq qo'shish kerak.
Qaysi tugmalar odatda ishlatiladi?

ENG TO'G'RI JAVOBNI TANLANG.""",
        """Нужно добавить новый лист в Excel.
Какая комбинация чаще всего используется?

ВЫБЕРИТЕ ПРАВИЛЬНЫЙ ОТВЕТ.""",
        {"A": "Ctrl + N", "B": "Shift + F11", "C": "Ctrl + S", "D": "Alt + F4"},
        {"A": "Ctrl + N", "B": "Shift + F11", "C": "Ctrl + S", "D": "Alt + F4"},
        "B",
    ),
    bq(
        """Jadvaldagi yozuvlarni saralab ko'rish kerak.
FILTER QAYSI BO'LIMDA KO'P ISHLATILADI?""",
        """Нужно отфильтровать записи в таблице.
В КАКОМ РАЗДЕЛЕ ЧАЩЕ ВСЕГО ИСПОЛЬЗУЕТСЯ FILTER?""",
        {"A": "Insert", "B": "Data", "C": "View", "D": "Home"},
        {"A": "Insert", "B": "Data", "C": "View", "D": "Home"},
        "B",
    ),
    bq(
        """Savdo ma'lumotlaridan tez summary olish kerak.
PIVOT TABLE NIMA UCHUN?""",
        """Нужно быстро сделать сводку по продажам.
ДЛЯ ЧЕГО НУЖЕН PIVOT TABLE?""",
        {"A": "DIZAYN", "B": "DATA ANALIZ VA SUMMARY", "C": "RASM", "D": "FORMULA YOZISH"},
        {"A": "ДИЗАЙН", "B": "АНАЛИЗ ДАННЫХ И СВОДКА", "C": "КАРТИНКА", "D": "НАПИСАНИЕ ФОРМУЛЫ"},
        "B",
    ),
    bq(
        """=VLOOKUP(A2, D2:F20, 2, FALSE)

VLOOKUP NIMA QILADI?""",
        """=VLOOKUP(A2, D2:F20, 2, FALSE)

ЧТО ДЕЛАЕТ VLOOKUP?""",
        {"A": "GRAFIK CHIZADI", "B": "QIYMATNI QIDIRADI", "C": "SHEET YARATADI", "D": "RANG BERADI"},
        {"A": "СТРОИТ ГРАФИК", "B": "ИЩЕТ ЗНАЧЕНИЕ", "C": "СОЗДАЕТ ЛИСТ", "D": "ЗАДАЕТ ЦВЕТ"},
        "B",
    ),
    bq(
        """Hisobotni saqlash kerak.
EXCEL NING ASOSIY FAYL FORMATI QAYSI?""",
        """Нужно сохранить отчет.
КАКОЙ ОСНОВНОЙ ФОРМАТ ФАЙЛА EXCEL?""",
        {"A": ".docx", "B": ".xlsx", "C": ".pptx", "D": ".csv"},
        {"A": ".docx", "B": ".xlsx", "C": ".pptx", "D": ".csv"},
        "B",
    ),
    bq(
        """Cell address: B3

BU NIMANI BILDIRADI?""",
        """Cell address: B3

ЧТО ЭТО ОЗНАЧАЕТ?""",
        {"A": "3-USTUN, B-SATR", "B": "B USTUN, 3-SATR", "C": "SHEET NOMI", "D": "FORMULA NOMI"},
        {"A": "3-Й СТОЛБЕЦ, СТРОКА B", "B": "СТОЛБЕЦ B, СТРОКА 3", "C": "ИМЯ ЛИСТА", "D": "ИМЯ ФОРМУЛЫ"},
        "B",
    ),
    bq(
        """Word hujjatida matnni qalin qilish kerak.
QAYSI BUYRUQ ENG MOS?""",
        """В документе Word нужно сделать текст жирным.
КАКАЯ КОМАНДА ПОДХОДИТ ЛУЧШЕ ВСЕГО?""",
        {"A": "Bold", "B": "Italic", "C": "Underline", "D": "Replace"},
        {"A": "Bold", "B": "Italic", "C": "Underline", "D": "Replace"},
        "A",
    ),
]
