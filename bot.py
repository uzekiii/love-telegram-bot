from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8958653969:AAFCLiJqGeQmpKic2dNTUaEX5V4wTUxTp2A"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("❌ Yo'q, sevmayman", callback_data="no1")],
        [InlineKeyboardButton("❤️ Ha, sevaman sizni", callback_data="yes")]
    ]

    await update.message.reply_text(
        "🥰 Meni sevasizmi?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "yes":
        await query.edit_message_text(
            "❤️ Men ham sevaman sizni, jonimdan ortiq ko'raman, hayotimda borligiz uchun shukur ❤️"
        )

    elif query.data == "no1":
        keyboard = [
            [InlineKeyboardButton("❌ Yo'q, sevmayman", callback_data="no2")],
            [InlineKeyboardButton("❤️ Ha, sevaman sizni", callback_data="yes")]
        ]

        await query.edit_message_text(
            "🤔 Aniqmi?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "no2":
        keyboard = [
            [InlineKeyboardButton("❌ Yo'q, sevmayman", callback_data="no3")],
            [InlineKeyboardButton("❤️ Ha, sevaman sizni", callback_data="yes")]
        ]

        await query.edit_message_text(
            "😟 Ishonchingiz komilmi?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "no3":
        keyboard = [
            [InlineKeyboardButton("❤️ Ha, sevaman sizni", callback_data="yes")]
        ]

        await query.edit_message_text(
            "🥺 Haa qo'ymadiz qo'ymadizda...",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Bot ishga tushdi...")

app.run_polling()
