import logging
import utils
import test
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

token = '8197686575:AAGtgCPPmN9ag0DJsfqEZBoAUTHn_1N_iQ4'


async def google_table_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    data = utils.split_message(message)
    test.insert_purchase(data)
    await utils.answer_with_params(message, context.bot, data)


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    google_table_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, google_table_handler)
    application.add_handler(google_table_handler)

    application.run_polling()
