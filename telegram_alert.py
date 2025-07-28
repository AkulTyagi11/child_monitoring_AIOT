import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Store your bot token in a .env file

# Initialize the bot
app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Command: /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I am your AIoT Monitoring Bot. How can I assist you?")

# Command: /help
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Commands:\n/start - Start bot\n/help - Get help\n/alert - Send an alert")

# Command: /alert
async def send_alert(update: Update, context: CallbackContext):
    await update.message.reply_text("🚨 Alert triggered! Please check your system.")

# Reply to any text message
async def handle_message(update: Update, context: CallbackContext):
    await update.message.reply_text(f"You said: {update.message.text}")

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("alert", send_alert))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Start the bot
print("Bot is running...")
app.run_polling()
