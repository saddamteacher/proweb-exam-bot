import re

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.config import Settings
from app.database.db import Database
from app.keyboards.inline import admin_courses_keyboard, admin_panel_keyboard
from app.states.test_states import AdminPanel

router = Router()


def is_admin(user_id: int, settings: Settings) -> bool:
    return user_id in settings.admin_ids


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9\s-]", "", value.lower()).strip()
    return re.sub(r"[\s-]+", "_", cleaned)


@router.message(Command("admin"))
async def admin_entry(message: Message, state: FSMContext, settings: Settings) -> None:
    if not is_admin(message.from_user.id, settings):
        await message.answer("⛔ Sizda admin huquqi yo‘q.")
        return
    await state.clear()
    await message.answer(
        "🛠 <b>Admin panel</b>\nKerakli bo‘limni tanlang:",
        reply_markup=admin_panel_keyboard(),
    )


@router.callback_query(F.data == "admin:menu")
async def admin_menu(callback: CallbackQuery, state: FSMContext, settings: Settings) -> None:
    if not is_admin(callback.from_user.id, settings):
        await callback.answer("Ruxsat yo‘q", show_alert=True)
        return
    await state.clear()
    await callback.message.edit_text(
        "🛠 <b>Admin panel</b>\nKerakli bo‘limni tanlang:",
        reply_markup=admin_panel_keyboard(),
    )
    await callback.answer()


@router.callback_query(F.data == "admin:add_course")
async def admin_add_course(callback: CallbackQuery, state: FSMContext, settings: Settings) -> None:
    if not is_admin(callback.from_user.id, settings):
        await callback.answer("Ruxsat yo‘q", show_alert=True)
        return
    await state.set_state(AdminPanel.waiting_course)
    await callback.message.edit_text(
        "➕ Yangi kurs yuboring.\n\nFormat:\n<code>Kurs nomi | Qisqa izoh</code>"
    )
    await callback.answer()


@router.message(AdminPanel.waiting_course)
async def process_new_course(message: Message, state: FSMContext, db: Database, settings: Settings) -> None:
    if not is_admin(message.from_user.id, settings):
        return
    if not message.text:
        await message.answer("Matn ko‘rinishida kurs yuboring.")
        return
    if "|" not in message.text:
        await message.answer("Format noto‘g‘ri. Namuna: <code>UI/UX Design | Dizayn asoslari</code>")
        return
    title, description = [part.strip() for part in message.text.split("|", 1)]
    slug = slugify(title)
    existing = await db.get_course_by_slug(slug)
    if existing:
        await message.answer("Bu kurs allaqachon mavjud. Boshqa nom kiriting.")
        return
    await db.add_course(slug, title, description)
    await state.clear()
    await message.answer(
        f"✅ <b>{title}</b> kursi qo‘shildi.\nSlug: <code>{slug}</code>",
        reply_markup=admin_panel_keyboard(),
    )


@router.callback_query(F.data == "admin:add_question")
async def admin_select_course_for_question(
    callback: CallbackQuery, settings: Settings, db: Database
) -> None:
    if not is_admin(callback.from_user.id, settings):
        await callback.answer("Ruxsat yo‘q", show_alert=True)
        return
    courses = await db.get_courses()
    await callback.message.edit_text(
        "🧩 Qaysi kursga savol qo‘shmoqchisiz?",
        reply_markup=admin_courses_keyboard(courses),
    )
    await callback.answer()


@router.callback_query(F.data.startswith("admin_course:"))
async def admin_course_picked(
    callback: CallbackQuery, state: FSMContext, settings: Settings, db: Database
) -> None:
    if not is_admin(callback.from_user.id, settings):
        await callback.answer("Ruxsat yo‘q", show_alert=True)
        return
    course_id = int(callback.data.split(":", 1)[1])
    course = await db.get_course_by_id(course_id)
    if not course:
        await callback.answer("Kurs topilmadi", show_alert=True)
        return
    await state.set_state(AdminPanel.waiting_question)
    await state.update_data(admin_course_id=course_id, admin_course_title=course["title"])
    await callback.message.edit_text(
        "✍️ Savol yuboring.\n\n"
        "Format:\n"
        "<code>Savol matni | Variant A | Variant B | Variant C | Variant D | To‘g‘ri javob</code>\n\n"
        "Masalan:\n"
        "<code>HTML nima? | Dasturlash tili | Belgilash tili | Database | Framework | B</code>"
    )
    await callback.answer()


@router.message(AdminPanel.waiting_question)
async def process_new_question(
    message: Message, state: FSMContext, db: Database, settings: Settings
) -> None:
    if not is_admin(message.from_user.id, settings):
        return
    if not message.text:
        await message.answer("Savolni matn ko‘rinishida yuboring.")
        return
    parts = [part.strip() for part in message.text.split("|")]
    if len(parts) != 6:
        await message.answer("Format noto‘g‘ri. 6 ta bo‘lim yuboring.")
        return
    question_text, option_a, option_b, option_c, option_d, correct = parts
    correct = correct.upper()
    if correct not in {"A", "B", "C", "D"}:
        await message.answer("To‘g‘ri javob faqat A/B/C/D bo‘lishi kerak.")
        return
    data = await state.get_data()
    await db.add_question(
        course_id=data["admin_course_id"],
        question_text=question_text,
        options={"A": option_a, "B": option_b, "C": option_c, "D": option_d},
        correct_option=correct,
    )
    await state.clear()
    await message.answer(
        f"✅ <b>{data['admin_course_title']}</b> kursiga yangi savol qo‘shildi.",
        reply_markup=admin_panel_keyboard(),
    )


@router.callback_query(F.data == "admin:stats")
async def admin_stats(callback: CallbackQuery, settings: Settings, db: Database) -> None:
    if not is_admin(callback.from_user.id, settings):
        await callback.answer("Ruxsat yo‘q", show_alert=True)
        return
    stats = await db.get_statistics()
    lines = [
        "📈 <b>Bot statistikasi</b>",
        f"Umumiy urinishlar: <b>{stats['total_attempts']}</b>",
        f"Unikal foydalanuvchilar: <b>{stats['unique_users']}</b>",
        f"O‘rtacha natija: <b>{stats['average_percentage']}%</b>",
        "",
        "Kurslar kesimida:",
    ]
    for item in stats["courses"]:
        lines.append(
            f"• <b>{item['title']}</b> — urinishlar: {item['attempts']}, o‘rtacha: {item['avg_score']}%"
        )
    await callback.message.edit_text("\n".join(lines), reply_markup=admin_panel_keyboard())
    await callback.answer()
