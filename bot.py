
import logging
from pathlib import Path
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(level=logging.INFO)

TOKEN = "7305986179:AAE31gHW35n4g1rMcvdC9e-sGOr_3E2RO8E"

main_menu = ReplyKeyboardMarkup([
    ["Нові мотоцикли", "Б/у мотоцикли"],
    ["Шоломи", "Питання щодо покупки"]
], resize_keyboard=True)

moto_menu = ReplyKeyboardMarkup([
    ["Kovi Advance 300"],
    ["Kovi Advance 250"],
    ["Mustang Alpha 125"],
    ["Mustang Delta 110"],
    ["Mustang Challenge 250"],
    ["Fada Рута"],
    ["Назад"]
], resize_keyboard=True)

helmet_menu = ReplyKeyboardMarkup([
    ["Шолом 1", "Шолом 2"],
    ["Назад"]
], resize_keyboard=True)

project_dir = Path(__file__).resolve().parent

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вітаємо у магазині мотоциклів!", reply_markup=main_menu)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Нові мотоцикли":
        await update.message.reply_text("Оберіть модель:", reply_markup=moto_menu)

    elif text == "Назад":
        await update.message.reply_text("Повертаємось до головного меню.", reply_markup=main_menu)

    elif text == "Б/у мотоцикли":
        await update.message.reply_text("Каталог б/у мотоциклів ще не доданий.", reply_markup=main_menu)

    elif text == "Питання щодо покупки":
        await update.message.reply_text("З питань покупки звертайтесь до: @Fon4ik10")

    elif text == "Шоломи":
        await update.message.reply_text("Оберіть шолом:", reply_markup=helmet_menu)

    elif text == "Шолом 1":
        with open(project_dir / "helmet1.jpg", "rb") as f:
            await update.message.reply_photo(f)

    elif text == "Шолом 2":
        with open(project_dir / "helmet2.jpg", "rb") as f:
            await update.message.reply_photo(f)

    elif text == "Kovi Advance 300":
        for photo in ["kovi3001.jpg", "kovi3002.jpg", "kovi3003.jpg"]:
            with open(project_dir / photo, "rb") as f:
                await update.message.reply_photo(f)
        await update.message.reply_text(
            """Характеристики Kovi Advance 300:
"
            "- Довжина: 2045 мм
"
            "- Висота по сідлу: 938 мм
"
            "- Маса: 112,5 кг
"
            "- Двигун: 279 см³, 28 к.с.
"
            "- Карбюратор: Nibbi Racing PWK NBR 34
"
            "- КПП: 5-ступінчаста
"
            "- Підвіска: регульована
"
            "- Гальма: дискові
"
            "- Швидкість: ≥109 км/год
"
            "- Бак: 7,5 л
"
            "- Ціна: 98000 Грн"""
        )

    elif text == "Kovi Advance 250":
        for photo in ["kovi2501.jpg", "kovi2502.jpg", "kovi2503.jpg"]:
            with open(project_dir / photo, "rb") as f:
                await update.message.reply_photo(f)
        await update.message.reply_text(
            """Характеристики Kovi Advance 250:
"
            "- Довжина: 2045 мм
"
            "- Висота по сідлу: 940 мм / 910 мм
"
            "- Маса: 123 кг
"
            "- Двигун: 249 см³, повітряне охолодження
"
            "- Карбюратор: Nibbi Racing NBR PWK32
"
            "- КПП: 6-ступінчаста
"
            "- Підвіска: передня вилка + задня стійка
"
            "- Гальма: дискові
"
            "- Швидкість: ≥114 км/год
"
            "- Бак: 7,5 л
"
            "- Ціна: 87800 Грн"""
        )

    elif text == "Mustang Alpha 125":
        for photo in ["must1251.jpg", "must1252.jpg", "must1253.jpg"]:
            with open(project_dir / photo, "rb") as f:
                await update.message.reply_photo(f)
        await update.message.reply_text(
            """Характеристики Mustang Alpha 125:
"
            "- Довжина: 1900 мм
"
            "- Висота: 1030 мм
"
            "- Маса: 92 кг
"
            "- Двигун: 119.7 см³
"
            "- КПП: 4-ступінчаста
"
            "- Підвіска: телескопічна + маятникова
"
            "- Гальма: переднє дискове, заднє барабанне
"
            "- Швидкість: до 80 км/год
"
            "- Бак: 11,5 л
"
            "- Ціна: 28380 Грн"""
        )

    elif text == "Mustang Delta 110":
        for photo in ["delt1101.jpg", "delt1102.jpg", "delt1103.jpg"]:
            with open(project_dir / photo, "rb") as f:
                await update.message.reply_photo(f)
        await update.message.reply_text(
            """Характеристики Mustang Delta 110:
"
            "- Довжина: 1850 мм
"
            "- Висота: 1120 мм
"
            "- Маса: 92 кг
"
            "- Двигун: 110 см³, 4-тактний
"
            "- КПП: 4-ступінчаста
"
            "- Гальма: переднє/заднє барабанне
"
            "- Швидкість: до 80 км/год
"
            "- Бак: 3,6 л
"
            "- Ціна: 26450 Грн"""
        )

    elif text == "Mustang Challenge 250":
        for photo in ["chal1.jpg", "chal2.jpg", "chal3.jpg"]:
            with open(project_dir / photo, "rb") as f:
                await update.message.reply_photo(f)
        await update.message.reply_text(
            """Характеристики Mustang Challenge 250:
"
            "- Довжина: 2100 мм
"
            "- Висота: 1400 мм
"
            "- Маса: 143 кг
"
            "- Двигун: 249 см³, повітряно-олійне охолодження
"
            "- КПП: 6-ступінчаста
"
            "- Гальма: дискові
"
            "- Бак: 13,6 л
"
            "- Швидкість: ≥118 км/год
"
            "- Ціна: 70800 Грн"""
        )

    elif text == "Fada Рута":
        for photo in ["fad1.jpg", "fad2.jpg", "fad3.jpg"]:
            with open(project_dir / photo, "rb") as f:
                await update.message.reply_photo(f)
        await update.message.reply_text(
            """Характеристики Fada Рута:
"
            "- Двигун: електро
"
            "- АКБ: свинцево-кислотна
"
            "- Привід: мотор-колесо
"
            "- Вантажопідйомність: до 150 кг
"
            "- Запас ходу: 40-60 км"""
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
