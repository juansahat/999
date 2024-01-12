from telegram.update import Update
from telegram.ext import CommandHandler, CallbackContext

def module1_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Module 1 command executed.')

def setup(dp):
    dp.add_handler(CommandHandler("module1", module1_command))