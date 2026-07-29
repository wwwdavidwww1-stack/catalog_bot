from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from flask import Flask
import threading

flask_app = Flask('')

@flask_app.route('/')
def home():
    return "Бот работает! ✅"

def run_flask():
    flask_app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_flask).start()
print("✅ Flask-заглушка запущена на порту 10000")

TOKEN = "8752978380:AAGE4HDcV_SnK9c4Qy6BDF_4WN3USDmUmkU"

# --- ДАННЫЕ ---
iphone_versions = {
    "Обычная": {
        "11": {"photo": "AgACAgIAAxkBAAIBFGpkq9eQc1nMOMyr3YfYXhed5ktNAALJGGsbgcwoSymI9AvGAAEDQQEAAwIAA3kAAz0E", "price": "30 000 ₽", "specs": "6.1″ LCD, A13 Bionic, 64GB"},
        "12": {"photo": "AgACAgIAAxkBAAIBHmpks4ksgSEaK6uNHaZFdFcUaNNmAAINGWsbgcwoS9DedA9JLMoDAQADAgADeAADPQQ", "price": "40 000 ₽", "specs": "6.1″ OLED, A14 Bionic, 64GB"},
        "13": {"photo": "AgACAgIAAxkBAAIBOGpoj5N9UkLRxGeijAlAfBRqHcUZAAIOGWsbZzJIS50hlrZXX4rAAQADAgADeAADPQQ", "price": "50 000 ₽", "specs": "6.1″ OLED, A15 Bionic, 128GB"},
        "14": {"photo": "AgACAgIAAxkBAAIBPmpoj_NUGgY-XwAB6gcZL5puIToI5QACEhlrG2cySEsEUxKBLaxB2wEAAwIAA3gAAz0E", "price": "60 000 ₽", "specs": "6.1″ OLED, A15 Bionic, 128GB"},
        "15": {"photo": "AgACAgIAAxkBAAIBQGpokLSyYFqYchenqVEPy110Rh1GAAIVGWsbZzJIS_k7rqFJbjG4AQADAgADeAADPQQ", "price": "70 000 ₽", "specs": "6.1″ OLED, A16 Bionic, 128GB, USB-C"},
        "16": {"photo": "AgACAgIAAxkBAAIBQmpokOpPWkPeZFv1P6hx2O40kiaHAAIXGWsbZzJIS1rBR1biI_UsAQADAgADeAADPQQ", "price": "80 000 ₽", "specs": "6.1″ OLED, A18 Bionic, 128GB"},
        "17": {"photo": "AgACAgIAAxkBAAIBRGpokRAQzBlM-Dw_md96Ko1EdHXfAAIYGWsbZzJIS61bguC_94SaAQADAgADeQADPQQ", "price": "90 000 ₽", "specs": "6.1″ OLED, A19 Bionic, 128GB"}
    },
    "Pro": {
        "11 Pro": {"photo": "AgACAgIAAxkBAAIBUmpokcqMrQhpR4KmBOn6uNsCV1NBAAIbGWsbZzJIS4UvF_rdisFzAQADAgADeAADPQQ", "price": "45 000 ₽", "specs": "5.8″ OLED, A13 Bionic, 64GB"},
        "12 Pro": {"photo": "AgACAgIAAxkBAAIBVGpokeskzm9FIrm5xO65ccnrKVcmAAIeGWsbZzJIS39JQEUryCJNAQADAgADeAADPQQ", "price": "55 000 ₽", "specs": "6.1″ OLED, A14 Bionic, 128GB"},
        "13 Pro": {"photo": "AgACAgIAAxkBAAIBVmpokhPXLNwrdsDokGuo5cisRtpyAAIfGWsbZzJISzbFL4zjRNbmAQADAgADeAADPQQ", "price": "65 000 ₽", "specs": "6.1″ OLED, A15 Bionic, 128GB, 120Hz"},
        "14 Pro": {"photo": "AgACAgIAAxkBAAIBWGpoklpsdCR_oTHDOM-gPAG4PmOzAAIhGWsbZzJIS4Qa9jchxlQUAQADAgADeAADPQQ", "price": "75 000 ₽", "specs": "6.1″ OLED, A16 Bionic, 128GB, 48MP"},
        "15 Pro": {"photo": "AgACAgIAAxkBAAIBWmpoktipnM4Eio-wCfe0E4qtCHJ1AAIlGWsbZzJIS5AQPi0jhErDAQADAgADeAADPQQ", "price": "85 000 ₽", "specs": "6.1″ OLED, A17 Pro, 128GB, 48MP"},
        "16 Pro": {"photo": "AgACAgIAAxkBAAIBXGpokyXWqlQ7IQpWtJK0AAEpxtrj_gACJhlrG2cySEufFV9VYSrScQEAAwIAA3gAAz0E", "price": "95 000 ₽", "specs": "6.3″ OLED, A18 Pro, 256GB"},
        "17 Pro": {"photo": "AgACAgIAAxkBAAIBXmpok0kTU9iy1QABDo7XnDBeCu577QACKRlrG2cySEtXKJaSjgkKzwEAAwIAA3gAAz0E", "price": "105 000 ₽", "specs": "6.3″ OLED, A19 Pro, 256GB"}
    },
    "Pro Max": {
        "11 Pro Max": {"photo": "AgACAgIAAxkBAAIBUmpokcqMrQhpR4KmBOn6uNsCV1NBAAIbGWsbZzJIS4UvF_rdisFzAQADAgADeAADPQQ", "price": "55 000 ₽", "specs": "6.5″ OLED, A13 Bionic, 64GB"},
        "12 Pro Max": {"photo": "AgACAgIAAxkBAAIBVGpokeskzm9FIrm5xO65ccnrKVcmAAIeGWsbZzJIS39JQEUryCJNAQADAgADeAADPQQ", "price": "65 000 ₽", "specs": "6.7″ OLED, A14 Bionic, 128GB"},
        "13 Pro Max": {"photo": "AgACAgIAAxkBAAIBVmpokhPXLNwrdsDokGuo5cisRtpyAAIfGWsbZzJISzbFL4zjRNbmAQADAgADeAADPQQ", "price": "75 000 ₽", "specs": "6.7″ OLED, A15 Bionic, 128GB, 120Hz"},
        "14 Pro Max": {"photo": "AgACAgIAAxkBAAIBWGpoklpsdCR_oTHDOM-gPAG4PmOzAAIhGWsbZzJIS4Qa9jchxlQUAQADAgADeAADPQQ", "price": "85 000 ₽", "specs": "6.7″ OLED, A16 Bionic, 128GB, 48MP"},
        "15 Pro Max": {"photo": "AgACAgIAAxkBAAIBWmpoktipnM4Eio-wCfe0E4qtCHJ1AAIlGWsbZzJIS5AQPi0jhErDAQADAgADeAADPQQ", "price": "95 000 ₽", "specs": "6.7″ OLED, A17 Pro, 256GB"},
        "16 Pro Max": {"photo": "AgACAgIAAxkBAAIBXGpokyXWqlQ7IQpWtJK0AAEpxtrj_gACJhlrG2cySEufFV9VYSrScQEAAwIAA3gAAz0E", "price": "105 000 ₽", "specs": "6.9″ OLED, A18 Pro, 256GB"},
        "17 Pro Max": {"photo": "AgACAgIAAxkBAAIBXmpok0kTU9iy1QABDo7XnDBeCu577QACKRlrG2cySEtXKJaSjgkKzwEAAwIAA3gAAz0E", "price": "115 000 ₽", "specs": "6.9″ OLED, A19 Pro, 256GB"}
    },
    "Plus": {
        "14 Plus": {"photo": "AgACAgIAAxkBAAIBPmpoj_NUGgY-XwAB6gcZL5puIToI5QACEhlrG2cySEsEUxKBLaxB2wEAAwIAA3gAAz0E", "price": "70 000 ₽", "specs": "6.7″ OLED, A15 Bionic, 128GB"},
        "15 Plus": {"photo": "AgACAgIAAxkBAAIBQGpokLSyYFqYchenqVEPy110Rh1GAAIVGWsbZzJIS_k7rqFJbjG4AQADAgADeAADPQQ", "price": "80 000 ₽", "specs": "6.7″ OLED, A16 Bionic, 128GB"},
        "16 Plus": {"photo": "AgACAgIAAxkBAAIBQmpokOpPWkPeZFv1P6hx2O40kiaHAAIXGWsbZzJIS1rBR1biI_UsAQADAgADeAADPQQ", "price": "90 000 ₽", "specs": "6.7″ OLED, A18 Bionic, 128GB"},
        "17 Plus": {"photo": "AgACAgIAAxkBAAIBRGpokRAQzBlM-Dw_md96Ko1EdHXfAAIYGWsbZzJIS61bguC_94SaAQADAgADeQADPQQ", "price": "100 000 ₽", "specs": "6.7″ OLED, A19 Bionic, 128GB"}
    },
    "Mini": {
        "12 Mini": {"photo": "AgACAgIAAxkBAAIBHmpks4ksgSEaK6uNHaZFdFcUaNNmAAINGWsbgcwoS9DedA9JLMoDAQADAgADeAADPQQ", "price": "35 000 ₽", "specs": "5.4″ OLED, A14 Bionic, 64GB"},
        "13 Mini": {"photo": "AgACAgIAAxkBAAIBOGpoj5N9UkLRxGeijAlAfBRqHcUZAAIOGWsbZzJIS50hlrZXX4rAAQADAgADeAADPQQ", "price": "45 000 ₽", "specs": "5.4″ OLED, A15 Bionic, 128GB"}
    }
}

async def start(update: Update, context):
    # Проверяем, откуда пришёл вызов: из сообщения или из кнопки
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        message = query.message
    else:
        message = update.message

    # Удаляем старое сообщение (если есть)
    if "last_message_id" in context.user_data:
        try:
            await context.bot.delete_message(
                chat_id=message.chat_id,
                message_id=context.user_data["last_message_id"]
            )
        except:
            pass

    # Главное меню (Inline-кнопки)
    keyboard = [
        [InlineKeyboardButton("📱 Каталог iPhone", callback_data="main_catalog")],
        [InlineKeyboardButton("💰 Оценить iPhone", callback_data="main_assess")],
        [InlineKeyboardButton("📞 Связаться с нами", callback_data="main_contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    sent_message = await message.reply_text(
        "📱 *iPhone Hub*\n\n"
        "Добро пожаловать! Выберите действие:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    context.user_data["last_message_id"] = sent_message.message_id

async def handle_callback(update: Update, context):
    query = update.callback_query
    await query.answer()

    data = query.data
    print(f"🔍 Получен callback: {data}")

    # --- Удаляем старое сообщение ---
    if "last_message_id" in context.user_data:
        try:
            await context.bot.delete_message(
                chat_id=update.effective_chat.id,
                message_id=context.user_data["last_message_id"]
            )
        except:
            pass

    # --- ГЛАВНОЕ МЕНЮ (КАТАЛОГ) ---
    if data == "main_catalog":
        keyboard = []
        for version in iphone_versions.keys():
            keyboard.append([InlineKeyboardButton(version, callback_data=f"version_{version}")])
        keyboard.append([InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        sent_message = await query.message.reply_text(
            "📱 *Каталог iPhone*\n\nВыберите версию:",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        context.user_data["last_message_id"] = sent_message.message_id

    # --- ГЛАВНОЕ МЕНЮ (ОЦЕНКА) ---
    elif data == "main_assess":
        sent_message = await query.message.reply_text(
            "💰 *Оценка iPhone*\n\nСкоро здесь будет опросник!",
            parse_mode="Markdown"
        )
        context.user_data["last_message_id"] = sent_message.message_id

    # --- ГЛАВНОЕ МЕНЮ (КОНТАКТЫ) ---
    elif data == "main_contact":
        text = (
            "📞 *Связь с нами*\n\n"
            "📱 Telegram: @pet_rycho\n"
            "📞 Телефон 1: 89621962960\n"
            "📞 Телефон 2: 89605872096\n"
            "О наличии: @APPLESHOPRFRF"
        )

        keyboard = [[InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        sent_message = await query.message.reply_text(
            text,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        context.user_data["last_message_id"] = sent_message.message_id

    # --- ВОЗВРАТ В ГЛАВНОЕ МЕНЮ ---
    elif data == "main_menu":
        await start(update, context)
        return

    # --- ВЫБОР ВЕРСИИ ---
    elif data.startswith("version_"):
        version = data.replace("version_", "")
        models = iphone_versions[version]

        keyboard = []
        for model in models.keys():
            keyboard.append([InlineKeyboardButton(model, callback_data=f"model_{version}_{model}")])

        keyboard.append([
            InlineKeyboardButton("⬅️ Назад к версиям", callback_data="main_catalog"),
            InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")
        ])

        reply_markup = InlineKeyboardMarkup(keyboard)
        sent_message = await query.message.reply_text(
            f"📱 Вы выбрали *{version}*. Выберите модель:",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        context.user_data["last_message_id"] = sent_message.message_id

    # --- ВЫБОР МОДЕЛИ ---
    elif data.startswith("model_"):
        parts = data.replace("model_", "").split("_", 1)
        version = parts[0]
        model_name = parts[1]

        model = iphone_versions[version][model_name]

        text = f"📱 *{model_name}*\n\n"
        text += f"💰 Цена: {model['price']}\n"
        text += f"📋 Характеристики: {model['specs']}"

        if "photo" in model:
            sent_message = await query.message.reply_photo(
                photo=model["photo"],
                caption=text,
                parse_mode="Markdown"
            )
        else:
            sent_message = await query.message.reply_text(
                text,
                parse_mode="Markdown"
            )
        context.user_data["last_message_id"] = sent_message.message_id

        # Кнопки после карточки
        keyboard = []
        for model in iphone_versions[version].keys():
            keyboard.append([InlineKeyboardButton(model, callback_data=f"model_{version}_{model}")])

        keyboard.append([


InlineKeyboardButton("⬅️ Назад к моделям", callback_data=f"version_{version}"),
            InlineKeyboardButton("🏠 Главное меню", callback_data="main_menu")
        ])

        reply_markup = InlineKeyboardMarkup(keyboard)
        sent_message = await query.message.reply_text(
            f"📱 Выберите модель *{version}*:",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        context.user_data["last_message_id"] = sent_message.message_id

    # --- НЕИЗВЕСТНАЯ КОМАНДА ---
    else:
        sent_message = await query.message.reply_text("❌ Неизвестная команда.")
        context.user_data["last_message_id"] = sent_message.message_id
        print(f"❌ Неизвестный callback: {data}")
        
async def get_file_id(update: Update, context):
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        await update.message.reply_text(f"📸 `{file_id}`", parse_mode="Markdown")
    else:
        await update.message.reply_text("Отправь мне фото!")

async def pin_message(update: Update, context):
    # Если пользователь написал /start — закрепляем сообщение с меню
    if update.message and update.message.text == "/start":
        try:
            # Ждём, пока бот отправит сообщение, потом закрепляем его
            await update.message.pin()
        except:
            pass

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_callback))
app.add_handler(MessageHandler(filters.PHOTO,get_file_id))
app.add_handler(MessageHandler(filters.COMMAND, pin_message))


print("✅ Бот запущен...")
app.run_polling()
