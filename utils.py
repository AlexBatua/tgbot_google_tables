import re
from datetime import datetime


def split_message(message) -> tuple | None:
    date = str(datetime.now())[:-7]
    try:
        price = round(count_filter(message))
        percent = round(check_percent(message, price))
        purchase_type = str(check_purchase_type(message))
    except TypeError:
        return
    else:
        return price, percent, purchase_type, date


def answer_with_params(message, bot, data):
    try:
        price, percent, purchase_type, _ = data
    except TypeError:
        bot.reply_to(message, "параметры не распознаны")
    else:
        text = f"Покупка на сумму: {price} \U0001F4B0 \nПроцент с покупки: {percent} \U0001F4C8 \nТип оплаты: " + str(
            purchase_type)
        bot.reply_to(message, text)


def check_purchase_type(message):
    purchase_type = ''
    purchase_types = ['Карта', 'Перевод', 'Наличные', 'Безнал']
    for payment_type in purchase_types:
        if payment_type.lower() in message.text.lower():
            if payment_type.lower() == 'перевод':
                purchase_type = str(payment_type) + ' \U0001F4B8'
            elif payment_type.lower() == 'наличные':
                purchase_type = str(payment_type) + ' \U0001F4B5'
            elif payment_type.lower() == 'безнал':
                purchase_type = str(payment_type) + ' \U0001F4B3'
            elif payment_type.lower() == 'карта':
                purchase_type = str(payment_type) + ' \U0001F4B3'
            else:
                return purchase_type
            return purchase_type


def count_filter(message):
    try:
        purchase = re.search(r'(\d+\.?\d*)', message.text)
        count = float(purchase.group(1))
        return count
    except:
        pass


def check_percent(message, price):
    percent = price * 0.05
    product_types = ['Латте', 'Чай', 'Американо', 'Эспрессо']
    for product in product_types:
        if product.lower() in message.text.lower():
            percent = 0
            break
    return percent
