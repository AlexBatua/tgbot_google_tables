import logging
import utils
import google_table
from config import get_tg_token
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def google_table_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    data = utils.split_message(message)
    google_table.insert_purchase(data)
    await utils.answer_with_params(message, context.bot, data)


if __name__ == '__main__':
    token = get_tg_token()
    application = ApplicationBuilder().token(token).build()

    google_table_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, google_table_handler)
    application.add_handler(google_table_handler)

    application.run_polling()
