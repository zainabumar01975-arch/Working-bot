from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8672600900:AAE3-uxZBLkuTncdprtNV6Nmn9MKvzBn7hA"
ADMIN_ID = 8273206128

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Start"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Welcome!\n\nThis bot helps you unlock rewards by completing simple steps.",
        reply_markup=reply_markup
    )

# Handle "Start" button
async def handle_start_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Yes", "No"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Were you referred by someone?",
        reply_markup=reply_markup
    )

# Handle referral response
async def handle_referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Step 1:\nDownload Cardcosmic app\n"
        "Use invite code: JSEXD8\n\n"
        "🎁 Reward: 10GB data + 3000 trading bonus\n\n"
        "📌 Step 2:\nSend a screenshot of your dashboard after signup."
    )

# Handle screenshot
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]

    # Forward to admin
    await context.bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

    await update.message.reply_text(
        "✅ Screenshot received.\nVerification in progress.\n\n"
        "📢 Final Step:\nInvite 5 friends to unlock your reward."
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex("^Start$"), handle_start_button))
app.add_handler(MessageHandler(filters.TEXT & (filters.Regex("^Yes$") | filters.Regex("^No$")), handle_referral))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

app.run_polling()
