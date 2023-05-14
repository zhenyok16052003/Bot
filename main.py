from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json


def get_tender(update, context):
    # Виконуємо GET-запит до сторінки тендерів з вказаною фільтрацією
    url = "https://prozorro.gov.ua/api/search/tenders"
    params = {
        "filterType": "tenders",
        "sort_by": "tenderID",
        "order": "desc",
        "buyer[0]": "40108578"
    }
    response = requests.post(url, data=params)
    parsed_data = json.loads(response.content.decode('utf-8'))
    first_tender = parsed_data["data"][0]
    title = first_tender["title"]
    tender_id = first_tender["tenderID"]

    # Creating a dictionary with the extracted data
    data = {
        "title": title,
        "tenderID": tender_id
    }

    # Converting the dictionary to JSON format
    json_data = json.dumps(data, ensure_ascii=False)

    # Sending the JSON data as a message
    context.bot.send_message(chat_id=update.message.chat_id, text=json_data)


def start(update, context):
    # Создаем клавиатуру с кнопкой "Get Tender"
    keyboard = [['Get Tender']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    # Отправляем приветственное сообщение и клавиатуру
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Hello! I can help you get the latest tender. Press the button to continue.",
                             reply_markup=reply_markup)


def main():
    # Встановлюємо зв'язок з Telegram API
    updater = Updater(token='5696482840:AAEXkqsCmAwl0pk85CjQa_WkVA5XJbudIPk')
    dispatcher = updater.dispatcher

    # Додаємо команду /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Додаємо обробник повідомлень з кнопками
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), get_tender))

    # Запускаємо бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
