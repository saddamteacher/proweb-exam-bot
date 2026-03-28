from app.data.common import bq


FRONTEND_QUESTIONS = [
    bq(
        """<!DOCTYPE html>
<html>
<body>
    <h1>Salom</h1>
</body>
</html>

HTML ASOSAN NIMA UCHUN ISHLATILADI?""",
        """<!DOCTYPE html>
<html>
<body>
    <h1>Hello</h1>
</body>
</html>

ДЛЯ ЧЕГО В ОСНОВНОМ ИСПОЛЬЗУЕТСЯ HTML?""",
        {"A": "BACKEND YOZISH", "B": "WEB SAHIFA STRUKTURASI", "C": "DATABASE BOSHQARISH", "D": "SERVER OCHISH"},
        {"A": "ДЛЯ BACKEND", "B": "ДЛЯ СТРУКТУРЫ ВЕБ-СТРАНИЦЫ", "C": "ДЛЯ УПРАВЛЕНИЯ БАЗОЙ", "D": "ДЛЯ ЗАПУСКА СЕРВЕРА"},
        "B",
    ),
    bq(
        """<a href="https://example.com">
    Saytga o'tish
</a>

BU TEG NIMA QILADI?""",
        """<a href="https://example.com">
    Перейти на сайт
</a>

ЧТО ДЕЛАЕТ ЭТОТ ТЕГ?""",
        {"A": "RASM CHIQARADI", "B": "HAVOLA YARATADI", "C": "FORMA OCHADI", "D": "JADVAL CHIZADI"},
        {"A": "ПОКАЗЫВАЕТ КАРТИНКУ", "B": "СОЗДАЕТ ССЫЛКУ", "C": "ОТКРЫВАЕТ ФОРМУ", "D": "СТРОИТ ТАБЛИЦУ"},
        "B",
    ),
    bq(
        """<img src="photo.png" alt="avatar">

BU TEG QAYSI VAZIFANI BAJARADI?""",
        """<img src="photo.png" alt="avatar">

КАКУЮ ЗАДАЧУ ВЫПОЛНЯЕТ ЭТОТ ТЕГ?""",
        {"A": "HAVOLA YARATADI", "B": "MATNNI QALIN QILADI", "C": "RASM KO'RSATADI", "D": "FORMA YUBORADI"},
        {"A": "СОЗДАЕТ ССЫЛКУ", "B": "ДЕЛАЕТ ТЕКСТ ЖИРНЫМ", "C": "ПОКАЗЫВАЕТ ИЗОБРАЖЕНИЕ", "D": "ОТПРАВЛЯЕТ ФОРМУ"},
        "C",
    ),
    bq(
        """<h1>Frontend</h1>

H1 NIMA UCHUN ISHLATILADI?""",
        """<h1>Frontend</h1>

ДЛЯ ЧЕГО ИСПОЛЬЗУЕТСЯ H1?""",
        {"A": "ENG MUHIM SARLAVHA", "B": "LINK", "C": "RO'YXAT", "D": "BUTTON"},
        {"A": "ГЛАВНЫЙ ЗАГОЛОВОК", "B": "ССЫЛКА", "C": "СПИСОК", "D": "КНОПКА"},
        "A",
    ),
    bq(
        """<form>
    <input type="text">
</form>

FORM TEGINING ASOSIY MAQSADI NIMA?""",
        """<form>
    <input type="text">
</form>

КАКОВА ОСНОВНАЯ ЦЕЛЬ ТЕГА FORM?""",
        {"A": "FAYLNI YUKLASH", "B": "MA'LUMOT YUBORISH UCHUN FORMA", "C": "VIDEO OCHISH", "D": "STIL BERISH"},
        {"A": "ЗАГРУЗКА ФАЙЛА", "B": "ФОРМА ДЛЯ ОТПРАВКИ ДАННЫХ", "C": "ОТКРЫТИЕ ВИДЕО", "D": "ДОБАВЛЕНИЕ СТИЛЯ"},
        "B",
    ),
    bq(
        """<input type="text" value="Ali">

VALUE ATTRIBUTI NIMA UCHUN?""",
        """<input type="text" value="Ali">

ДЛЯ ЧЕГО НУЖЕН АТРИБУТ VALUE?""",
        {"A": "RASMDAGI MANZIL", "B": "HAVOLA MANZILI", "C": "MAYDONNING ICHKI QIYMATI", "D": "RANG BERISH"},
        {"A": "ПУТЬ К КАРТИНКЕ", "B": "АДРЕС ССЫЛКИ", "C": "ЗНАЧЕНИЕ ПОЛЯ", "D": "ЗАДАНИЕ ЦВЕТА"},
        "C",
    ),
    bq(
        """<ol>
    <li>Birinchi</li>
</ol>

OL QANDAY RO'YXAT?""",
        """<ol>
    <li>Первый</li>
</ol>

КАКОЙ ТИП СПИСКА СОЗДАЕТ OL?""",
        {"A": "TARTIBSIZ", "B": "TARTIBLI", "C": "JADVAL", "D": "NAVBAR"},
        {"A": "НЕУПОРЯДОЧЕННЫЙ", "B": "УПОРЯДОЧЕННЫЙ", "C": "ТАБЛИЦУ", "D": "NAVBAR"},
        "B",
    ),
    bq(
        """<table>
    <tr><td>1</td></tr>
</table>

TABLE ICHIDA TR VA TD NIMA UCHUN KERAK?""",
        """<table>
    <tr><td>1</td></tr>
</table>

ЗАЧЕМ В TABLE НУЖНЫ TR И TD?""",
        {"A": "FORMA YUBORISH", "B": "QATOR VA KATAK YARATISH", "C": "CSS ULANISH", "D": "SCRIPT YOZISH"},
        {"A": "ОТПРАВКА ФОРМЫ", "B": "СОЗДАНИЕ СТРОКИ И ЯЧЕЙКИ", "C": "ПОДКЛЮЧЕНИЕ CSS", "D": "НАПИСАНИЕ SCRIPT"},
        "B",
    ),
    bq(
        """<header>
    <nav>Menu</nav>
</header>

HEADER QANDAY TEG HISOBLANADI?""",
        """<header>
    <nav>Menu</nav>
</header>

КАКИМ ТЕГОМ СЧИТАЕТСЯ HEADER?""",
        {"A": "SEMANTIK TEG", "B": "FORM TEGI", "C": "SCRIPT TEGI", "D": "STYLE TEGI"},
        {"A": "СЕМАНТИЧЕСКИЙ ТЕГ", "B": "ТЕГ FORM", "C": "ТЕГ SCRIPT", "D": "ТЕГ STYLE"},
        "A",
    ),
    bq(
        """<!-- izoh -->
<p>Text</p>

HTML COMMENT QANDAY YOZILADI?""",
        """<!-- comment -->
<p>Text</p>

КАК ПИШЕТСЯ HTML-КОММЕНТАРИЙ?""",
        {"A": "// comment", "B": "# comment", "C": "<!-- -->", "D": "/* */"},
        {"A": "// comment", "B": "# comment", "C": "<!-- -->", "D": "/* */"},
        "C",
    ),
    bq(
        """p {
    color: red;
}

COLOR XOSSASI NIMANI O'ZGARTIRADI?""",
        """p {
    color: red;
}

ЧТО МЕНЯЕТ СВОЙСТВО COLOR?""",
        {"A": "ORQA FON", "B": "MATN RANGI", "C": "ELEMENT ENI", "D": "BORDER"},
        {"A": "ФОН", "B": "ЦВЕТ ТЕКСТА", "C": "ШИРИНУ ЭЛЕМЕНТА", "D": "BORDER"},
        "B",
    ),
    bq(
        """body {
    background-color: #f5f5f5;
}

BU XOSSA NIMA UCHUN?""",
        """body {
    background-color: #f5f5f5;
}

ДЛЯ ЧЕГО НУЖНО ЭТО СВОЙСТВО?""",
        {"A": "ORQA FON RANGI", "B": "MATN O'LCHAMI", "C": "BORDER RANGI", "D": "MARGIN"},
        {"A": "ЦВЕТ ФОНА", "B": "РАЗМЕР ШРИФТА", "C": "ЦВЕТ ГРАНИЦЫ", "D": "MARGIN"},
        "A",
    ),
    bq(
        """.card {
    display: flex;
}

DISPLAY: FLEX NIMA QILADI?""",
        """.card {
    display: flex;
}

ЧТО ДЕЛАЕТ DISPLAY: FLEX?""",
        {"A": "ELEMENTNI YASHIRADI", "B": "FLEX KONTEYNERGA AYLANTIRADI", "C": "RANG BERADI", "D": "ANIMATSIYA YOQADI"},
        {"A": "СКРЫВАЕТ ЭЛЕМЕНТ", "B": "ДЕЛАЕТ ЕГО FLEX-КОНТЕЙНЕРОМ", "C": "ЗАДАЕТ ЦВЕТ", "D": "ВКЛЮЧАЕТ АНИМАЦИЮ"},
        "B",
    ),
    bq(
        """.wrap {
    display: flex;
    justify-content: center;
}

JUSTIFY-CONTENT: CENTER NIMA BAJARADI?""",
        """.wrap {
    display: flex;
    justify-content: center;
}

ЧТО ДЕЛАЕТ JUSTIFY-CONTENT: CENTER?""",
        {"A": "TEPASIGA OLIB CHIQADI", "B": "GORIZONTAL MARKAZGA OLIB KELADI", "C": "VERTIKAL CHO'ZADI", "D": "RANGNI O'ZGARTIRADI"},
        {"A": "ПОДНИМАЕТ ВВЕРХ", "B": "ЦЕНТРИРУЕТ ПО ГОРИЗОНТАЛИ", "C": "РАСТЯГИВАЕТ ПО ВЕРТИКАЛИ", "D": "МЕНЯЕТ ЦВЕТ"},
        "B",
    ),
    bq(
        """.title {
    font-size: 24px;
}

FONT-SIZE NIMA UCHUN?""",
        """.title {
    font-size: 24px;
}

ДЛЯ ЧЕГО НУЖЕН FONT-SIZE?""",
        {"A": "MATN O'LCHAMI", "B": "RASM O'LCHAMI", "C": "BACKGROUND", "D": "MARGIN"},
        {"A": "РАЗМЕР ТЕКСТА", "B": "РАЗМЕР КАРТИНКИ", "C": "BACKGROUND", "D": "MARGIN"},
        "A",
    ),
    bq(
        """.btn-primary {
    padding: 12px;
}

.BTN-PRIMARY BU YERDA NIMA?""",
        """.btn-primary {
    padding: 12px;
}

ЧТО ТАКОЕ .BTN-PRIMARY В ЭТОМ ПРИМЕРЕ?""",
        {"A": "ID SELECTOR", "B": "CLASS SELECTOR", "C": "TAG SELECTOR", "D": "ATTRIBUTE"},
        {"A": "ID-СЕЛЕКТОР", "B": "CLASS-СЕЛЕКТОР", "C": "TAG-СЕЛЕКТОР", "D": "АТРИБУТ"},
        "B",
    ),
    bq(
        """#hero {
    min-height: 400px;
}

#HERO QANDAY SELECTOR?""",
        """#hero {
    min-height: 400px;
}

КАКОЙ ЭТО СЕЛЕКТОР?""",
        {"A": "CLASS", "B": "ID", "C": "TAG", "D": "UNIVERSAL"},
        {"A": "CLASS", "B": "ID", "C": "TAG", "D": "UNIVERSAL"},
        "B",
    ),
    bq(
        """.box {
    margin: 20px;
}

MARGIN NIMA?""",
        """.box {
    margin: 20px;
}

ЧТО ТАКОЕ MARGIN?""",
        {"A": "ICHKI JOY", "B": "TASHQI BO'SH JOY", "C": "RANG", "D": "BORDER"},
        {"A": "ВНУТРЕННИЙ ОТСТУП", "B": "ВНЕШНИЙ ОТСТУП", "C": "ЦВЕТ", "D": "ГРАНИЦА"},
        "B",
    ),
    bq(
        """.box {
    padding: 20px;
}

PADDING NIMA?""",
        """.box {
    padding: 20px;
}

ЧТО ТАКОЕ PADDING?""",
        {"A": "ICHKI JOY", "B": "TASHQI JOY", "C": "WIDTH", "D": "HEIGHT"},
        {"A": "ВНУТРЕННИЙ ОТСТУП", "B": "ВНЕШНИЙ ОТСТУП", "C": "WIDTH", "D": "HEIGHT"},
        "A",
    ),
    bq(
        """@media (max-width: 768px) {
    .card { width: 100%; }
}

@MEDIA NIMA UCHUN?""",
        """@media (max-width: 768px) {
    .card { width: 100%; }
}

ДЛЯ ЧЕГО НУЖЕН @MEDIA?""",
        {"A": "RESPONSIVE DESIGN", "B": "DATABASE", "C": "ANIMATION", "D": "FORM SUBMIT"},
        {"A": "АДАПТИВНЫЙ ДИЗАЙН", "B": "БАЗА ДАННЫХ", "C": "АНИМАЦИЯ", "D": "ОТПРАВКА ФОРМЫ"},
        "A",
    ),
    bq(
        """let count = 0;

LET BU YERDA NIMA UCHUN ISHLATILGAN?""",
        """let count = 0;

ДЛЯ ЧЕГО ЗДЕСЬ ИСПОЛЬЗУЕТСЯ LET?""",
        {"A": "O'ZGARUVCHI YARATISH", "B": "FUNKSIYA YARATISH", "C": "CLASS OCHISH", "D": "STYLE BERISH"},
        {"A": "СОЗДАНИЕ ПЕРЕМЕННОЙ", "B": "СОЗДАНИЕ ФУНКЦИИ", "C": "СОЗДАНИЕ КЛАССА", "D": "ДОБАВЛЕНИЕ СТИЛЯ"},
        "A",
    ),
    bq(
        """function sum(a, b) {
    return a + b;
}

BU QANDAY KONSTRUKSIYA?""",
        """function sum(a, b) {
    return a + b;
}

ЧТО ЭТО ЗА КОНСТРУКЦИЯ?""",
        {"A": "FUNKSIYA", "B": "CLASS", "C": "OBJECT", "D": "PROMISE"},
        {"A": "ФУНКЦИЯ", "B": "КЛАСС", "C": "ОБЪЕКТ", "D": "PROMISE"},
        "A",
    ),
    bq(
        """const title = document.getElementById("title");

GETELEMENTBYID NIMA QILADI?""",
        """const title = document.getElementById("title");

ЧТО ДЕЛАЕТ GETELEMENTBYID?""",
        {"A": "ELEMENTNI ID BO'YICHA OLADI", "B": "SQL SO'ROV YUBORADI", "C": "CSS YARATADI", "D": "FETCH QILADI"},
        {"A": "ПОЛУЧАЕТ ЭЛЕМЕНТ ПО ID", "B": "ОТПРАВЛЯЕТ SQL-ЗАПРОС", "C": "СОЗДАЕТ CSS", "D": "ДЕЛАЕТ FETCH"},
        "A",
    ),
    bq(
        """button.onclick = () => {
    alert("ok");
};

ONCLICK NIMA UCHUN?""",
        """button.onclick = () => {
    alert("ok");
};

ДЛЯ ЧЕГО НУЖЕН ONCLICK?""",
        {"A": "SCROLLNI BOSHQARISH", "B": "CLICK HODISASINI USHLASH", "C": "RANGNI O'ZGARTIRISH", "D": "SERVERGA ULASH"},
        {"A": "УПРАВЛЕНИЕ СКРОЛЛОМ", "B": "ОБРАБОТКА КЛИКА", "C": "СМЕНА ЦВЕТА", "D": "ПОДКЛЮЧЕНИЕ К СЕРВЕРУ"},
        "B",
    ),
    bq(
        """const nums = [1, 2, 3];

BU MA'LUMOT TURI NIMA?""",
        """const nums = [1, 2, 3];

ЧТО ЭТО ЗА ТИП ДАННЫХ?""",
        {"A": "OBJECT", "B": "ARRAY", "C": "STRING", "D": "SET"},
        {"A": "OBJECT", "B": "ARRAY", "C": "STRING", "D": "SET"},
        "B",
    ),
    bq(
        """if (a === b) {
    console.log("ok");
}

=== NIMA QILADI?""",
        """if (a === b) {
    console.log("ok");
}

ЧТО ДЕЛАЕТ === ?""",
        {"A": "QIYMAT BERADI", "B": "QATTIQ TENGLIKNI TEKSHIRADI", "C": "QO'SHADI", "D": "AYIRADI"},
        {"A": "ПРИСВАИВАЕТ", "B": "ПРОВЕРЯЕТ СТРОГОЕ РАВЕНСТВО", "C": "СКЛАДЫВАЕТ", "D": "ВЫЧИТАЕТ"},
        "B",
    ),
    bq(
        """const user = JSON.parse(data);

JSON.PARSE NIMA QILADI?""",
        """const user = JSON.parse(data);

ЧТО ДЕЛАЕТ JSON.PARSE?""",
        {"A": "JSON MATNNI OBJECTGA AYLANTIRADI", "B": "OBJECTNI STRINGGA AYLANTIRADI", "C": "RASM CHIZADI", "D": "API YOPADI"},
        {"A": "ПРЕВРАЩАЕТ JSON-СТРОКУ В ОБЪЕКТ", "B": "ПРЕВРАЩАЕТ ОБЪЕКТ В СТРОКУ", "C": "РИСУЕТ КАРТИНКУ", "D": "ЗАКРЫВАЕТ API"},
        "A",
    ),
    bq(
        """const result = fetch("/api/users");

PROMISE NIMA BILAN BOG'LIQ?""",
        """const result = fetch("/api/users");

С ЧЕМ СВЯЗАН PROMISE?""",
        {"A": "ASYNC NATIJA", "B": "CSS GRID", "C": "HTML COMMENT", "D": "FORM"},
        {"A": "АСИНХРОННЫЙ РЕЗУЛЬТАТ", "B": "CSS GRID", "C": "HTML-КОММЕНТАРИЙ", "D": "FORM"},
        "A",
    ),
    bq(
        """async function load() {
    await fetch("/api");
}

ASYNC/AWAIT NIMA UCHUN?""",
        """async function load() {
    await fetch("/api");
}

ДЛЯ ЧЕГО НУЖНЫ ASYNC/AWAIT?""",
        {"A": "STILLASH", "B": "ASINXRON KODNI O'QISH OSON QILISH", "C": "HTML YOZISH", "D": "SQL QUERY"},
        {"A": "СТИЛИЗАЦИЯ", "B": "УДОБНАЯ РАБОТА С АСИНХРОННЫМ КОДОМ", "C": "НАПИСАНИЕ HTML", "D": "SQL-ЗАПРОС"},
        "B",
    ),
    bq(
        """console.log("debug");

CONSOLE.LOG NIMA QILADI?""",
        """console.log("debug");

ЧТО ДЕЛАЕТ CONSOLE.LOG?""",
        {"A": "UI CHIZADI", "B": "KONSOLGA CHIQARADI", "C": "ALERT KO'RSATADI", "D": "SAVE QILADI"},
        {"A": "РИСУЕТ UI", "B": "ВЫВОДИТ В КОНСОЛЬ", "C": "ПОКАЗЫВАЕТ ALERT", "D": "СОХРАНЯЕТ"},
        "B",
    ),
    bq(
        """const user = { name: "Ali" };
console.log(user.name);

DOT NOTATION NIMA UCHUN?""",
        """const user = { name: "Ali" };
console.log(user.name);

ДЛЯ ЧЕГО НУЖНА DOT NOTATION?""",
        {"A": "OBJECT PROPERTY OLISH", "B": "CSS CLASS YARATISH", "C": "RO'YXAT SARALASH", "D": "TOKEN SAQLASH"},
        {"A": "ДОСТУП К СВОЙСТВУ ОБЪЕКТА", "B": "СОЗДАНИЕ CSS-КЛАССА", "C": "СОРТИРОВКА СПИСКА", "D": "ХРАНЕНИЕ ТОКЕНА"},
        "A",
    ),
    bq(
        """const ids = [1, 2, 3];
ids.map((id) => id * 2);

MAP NIMA QILADI?""",
        """const ids = [1, 2, 3];
ids.map((id) => id * 2);

ЧТО ДЕЛАЕТ MAP?""",
        {"A": "ARRAYNI O'ZGARTIRIB YANGI MASSIV QAYTARADI", "B": "BITTA ELEMENTNI O'CHIRADI", "C": "SERVERNI ISHGA TUSHIRADI", "D": "HTML YASAYDI"},
        {"A": "СОЗДАЕТ НОВЫЙ МАССИВ ПО РЕЗУЛЬТАТУ ПРЕОБРАЗОВАНИЯ", "B": "УДАЛЯЕТ ОДИН ЭЛЕМЕНТ", "C": "ЗАПУСКАЕТ СЕРВЕР", "D": "СТРОИТ HTML"},
        "A",
    ),
    bq(
        """import { useState } from "react";

REACT NIMA?""",
        """import { useState } from "react";

ЧТО ТАКОЕ REACT?""",
        {"A": "PYTHON FRAMEWORK", "B": "JS KUTUBXONASI", "C": "SQL SERVER", "D": "CSS PREPROCESSOR"},
        {"A": "PYTHON-ФРЕЙМВОРК", "B": "JS-БИБЛИОТЕКА", "C": "SQL-СЕРВЕР", "D": "CSS-ПРЕПРОЦЕССОР"},
        "B",
    ),
    bq(
        """function Button() {
    return <button>Save</button>;
}

BUTTON BU YERDA NIMA?""",
        """function Button() {
    return <button>Save</button>;
}

ЧЕМ ЯВЛЯЕТСЯ BUTTON ЗДЕСЬ?""",
        {"A": "QAYTA ISHLATILADIGAN UI BLOK", "B": "SQL TABLE", "C": "API ROUTE", "D": "STYLE FILE"},
        {"A": "ПЕРЕИСПОЛЬЗУЕМЫЙ UI-БЛОК", "B": "SQL-ТАБЛИЦА", "C": "API-ROUTE", "D": "STYLE-ФАЙЛ"},
        "A",
    ),
    bq(
        """const [count, setCount] = useState(0);

STATE NIMANI SAQLAYDI?""",
        """const [count, setCount] = useState(0);

ЧТО ХРАНИТ STATE?""",
        {"A": "COMPONENT ICHIDAGI O'ZGARUVCHAN DATA", "B": "FAQAT CSS", "C": "FAQAT HTML", "D": "TOKEN"},
        {"A": "ИЗМЕНЯЕМЫЕ ДАННЫЕ ВНУТРИ КОМПОНЕНТА", "B": "ТОЛЬКО CSS", "C": "ТОЛЬКО HTML", "D": "ТОКЕН"},
        "A",
    ),
    bq(
        """function Card({ title }) {
    return <h2>{title}</h2>;
}

TITLE BU YERGA QANDAY KELADI?""",
        """function Card({ title }) {
    return <h2>{title}</h2>;
}

КАК СЮДА ПОПАДАЕТ TITLE?""",
        {"A": "PROPS ORQALI", "B": "SQL ORQALI", "C": "MIGRATION ORQALI", "D": "CSS ORQALI"},
        {"A": "ЧЕРЕЗ PROPS", "B": "ЧЕРЕЗ SQL", "C": "ЧЕРЕЗ МИГРАЦИЮ", "D": "ЧЕРЕЗ CSS"},
        "A",
    ),
    bq(
        """const [open, setOpen] = useState(false);

USESTATE NIMA?""",
        """const [open, setOpen] = useState(false);

ЧТО ТАКОЕ USESTATE?""",
        {"A": "HOOK", "B": "SQL METHOD", "C": "CLASS", "D": "API ROUTE"},
        {"A": "ХУК", "B": "SQL-МЕТОД", "C": "КЛАСС", "D": "API-ROUTE"},
        "A",
    ),
    bq(
        """useEffect(() => {
    document.title = "App";
}, []);

USEEFFECT NIMA UCHUN?""",
        """useEffect(() => {
    document.title = "App";
}, []);

ДЛЯ ЧЕГО НУЖЕН USEEFFECT?""",
        {"A": "SIDE EFFECTLAR", "B": "CSS YAZISH", "C": "SQL SO'ROV", "D": "SVG CHIZISH"},
        {"A": "ПОБОЧНЫЕ ЭФФЕКТЫ", "B": "НАПИСАНИЕ CSS", "C": "SQL-ЗАПРОС", "D": "РИСОВАНИЕ SVG"},
        "A",
    ),
    bq(
        """npm install react

NPM NIMA?""",
        """npm install react

ЧТО ТАКОЕ NPM?""",
        {"A": "PACKAGE MANAGER", "B": "CSS ENGINE", "C": "BROWSER", "D": "SERVER"},
        {"A": "МЕНЕДЖЕР ПАКЕТОВ", "B": "CSS-ДВИЖОК", "C": "БРАУЗЕР", "D": "СЕРВЕР"},
        "A",
    ),
    bq(
        """npm create vite@latest

VITE KO'PROQ NIMA UCHUN ISHLATILADI?""",
        """npm create vite@latest

ДЛЯ ЧЕГО ЧАЩЕ ВСЕГО ИСПОЛЬЗУЮТ VITE?""",
        {"A": "BUILD TOOL VA DEV SERVER", "B": "SQL DATABASE", "C": "TELEGRAM BOT", "D": "WORD PROCESSOR"},
        {"A": "BUILD-TOOL И DEV-СЕРВЕР", "B": "SQL-БАЗА", "C": "TELEGRAM-БОТ", "D": "ТЕКСТОВЫЙ РЕДАКТОР"},
        "A",
    ),
    bq(
        """fetch("/api/users")
    .then((res) => res.json());

FETCH NIMA UCHUN?""",
        """fetch("/api/users")
    .then((res) => res.json());

ДЛЯ ЧЕГО НУЖЕН FETCH?""",
        {"A": "API CHAQIRISH", "B": "HTML SAQLASH", "C": "FONT O'RNATISH", "D": "CSS PARSE"},
        {"A": "ВЫЗОВ API", "B": "СОХРАНЕНИЕ HTML", "C": "УСТАНОВКА ШРИФТА", "D": "ПАРСИНГ CSS"},
        "A",
    ),
    bq(
        """const app = document.getElementById("app");

SPA NIMA DEGANI?""",
        """const app = document.getElementById("app");

ЧТО ОЗНАЧАЕТ SPA?""",
        {"A": "SINGLE PAGE APPLICATION", "B": "SERVER PAGE APP", "C": "SQL PAGE APP", "D": "STATIC PHP APP"},
        {"A": "SINGLE PAGE APPLICATION", "B": "SERVER PAGE APP", "C": "SQL PAGE APP", "D": "STATIC PHP APP"},
        "A",
    ),
]
