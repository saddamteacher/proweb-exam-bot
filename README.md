# Telegram Test Bot

`aiogram` asosidagi o'quv markazi test boti.

## Local ishga tushirish

1. Virtual environment yarating.
2. `pip install -r requirements.txt`
3. `.env.example` dan `.env` yarating.
4. `python main.py`

Asosiy env:

- `BOT_TOKEN`
- `ADMIN_IDS`
- `RESULTS_CHAT_ID`

## Render free workaround

Loyiha endi 2 rejimda ishlaydi:

- `WEBHOOK_BASE_URL` bo'lmasa: `polling`
- `WEBHOOK_BASE_URL` bo'lsa: `webhook + /health`

Render uchun:

1. Repo'ni Render'ga ulang.
2. `render.yaml` bo'yicha deploy qiling.
3. Env kiriting:
   `BOT_TOKEN`, `ADMIN_IDS`, `RESULTS_CHAT_ID`, `WEBHOOK_BASE_URL`
4. `WEBHOOK_BASE_URL` ga Render service URL yozing.
   Misol: `https://proweb-exam-bot.onrender.com`
5. UptimeRobot yoki shunga o'xshash servis bilan
   `https://your-service.onrender.com/health`
   endpointini har `10-14` minutda urib turing.

Muhim:

- Bu workaround, 100% kafolat emas.
- Free Render local fayllarni saqlab qolmaydi.
- Ishonchli production uchun paid worker yoki VPS yaxshiroq.

## Admin formatlari

`/admin` komandasi faqat `ADMIN_IDS` ichidagi foydalanuvchilar uchun ishlaydi.

- Kurs qo'shish:
  `Kurs nomi | Qisqa izoh`
- Savol qo'shish:
  `Savol matni | Variant A | Variant B | Variant C | Variant D | To'g'ri javob`
