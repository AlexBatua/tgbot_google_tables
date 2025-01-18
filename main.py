import telebot 
import utils
import test

token = '8197686575:AAGtgCPPmN9ag0DJsfqEZBoAUTHn_1N_iQ4'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def reply_to_user(message):
    data = utils.split_message(message)
    test.insert_purchase(data)
    utils.answer_with_params(message, bot, data)


if __name__ == '__main__':
    bot.infinity_polling()
