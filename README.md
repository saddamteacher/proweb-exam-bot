# Telegram Test Bot

`aiogram` asosidagi o‘quv markazi test boti.

## Ishga tushirish

1. Virtual environment yarating.
2. `pip install -r requirements.txt`
3. `.env.example` faylidan nusxa olib `.env` yarating.
4. `python main.py`

`.env` ichida `RESULTS_CHAT_ID` ga guruh yoki kanal chat ID sini yozing. Bot shu yerga o‘quvchi ismi, telefoni, Telegram useri, kursi va ballini yuboradi.

## Admin formatlari

`/admin` komandasi faqat `ADMIN_IDS` ichidagi foydalanuvchilar uchun ishlaydi.

- Kurs qo‘shish:
  `Kurs nomi | Qisqa izoh`
- Savol qo‘shish:
  `Savol matni | Variant A | Variant B | Variant C | Variant D | To‘g‘ri javob`
