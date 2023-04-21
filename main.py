import telebot

# импортируем библиотеку для работы с Telegram API
import requests  # импортируем библиотеку для работы с HTTP-запросами

# получаем токен нашего бота
TOKEN ="6033053374:AAFIDvLpXY0S9RGbGqOY0faxzB4mfhsJUOI"
# создаем соединение с Telegram API, используя наш токен
bot = telebot.TeleBot(TOKEN)

# создаем клавиатуру с кнопками
markup = telebot.types.ReplyKeyboardMarkup(row_width=2)  # создаем объект клавиатуры
weather_button = telebot.types.KeyboardButton('Погода в рідному місті')  # создаем кнопку 'Погода'
weather_button1 = telebot.types.KeyboardButton('Погода в Києві')  # создаем кнопку 'Погода'
weather_button2 = telebot.types.KeyboardButton('Погода в Дніпрі')  # создаем кнопку 'Погода'
markup.add(weather_button)  # добавляем кнопку 'Погода' на клавиатуру
markup.add(weather_button1)  # добавляем кнопку 'Погода' на клавиатуру
markup.add(weather_button2)  # добавляем кнопку 'Погода' на клавиатуру

# логика для обработки сообщений, отправленных боту
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == 'Погода в рідному місті':  # если пользователь нажал на кнопку 'Погода'
        # получаем данные о погоде в городе Миколаїв с помощью API
        url = 'https://api.openweathermap.org/data/2.5/weather?q=Mykolayiv&appid=4aaf7a05ddf42bfb2b2c91ac74065990&units=metric&lang=ua'
        response = requests.get(url)  # отправляем запрос к API
        weather_data = response.json()  # получаем данные о погоде в формате JSON
        # проверяем наличие ошибок в ответе
        if 'main' in weather_data:  # если данные о погоде успешно получены
            temp = weather_data['main']['temp']  # получаем температуру
            description = weather_data['weather'][0]['description']  # получаем описание погоды

            # отправляем ответ пользователю с информацией о погоде
            reply = f'Погода в рідному місті: {temp} °C, {description}'
            bot.send_message(message.chat.id, reply)

        else:  # если возникла ошибка при получении данных о погоде
            bot.send_message(message.chat.id, 'Помилка при отриманні погоди. Спробуйте пізніше.')
    elif message.text=='Погода в Дніпрі':
        url1='https://api.openweathermap.org/data/2.5/weather?q=Dnipro&appid=4aaf7a05ddf42bfb2b2c91ac74065990&units=metric&lang=ua'
        response=requests.get(url1)
        weather_data=response.json()
        if 'main' in weather_data:  # если данные о погоде успешно получены
            temp = weather_data['main']['temp']  # получаем температуру
            description = weather_data['weather'][0]['description']  # получаем описание погоды

            # отправляем ответ пользователю с информацией о погоде
            reply = f'Погода в Дніпрі: {temp} °C, {description}'
            bot.send_message(message.chat.id, reply)

        else:  # если возникла ошибка при получении данных о погоде
            bot.send_message(message.chat.id, 'Помилка при отриманні погоди. Спробуйте пізніше.')
    elif message.text=='Погода в Києві':
        url2='https://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=4aaf7a05ddf42bfb2b2c91ac74065990&units=metric&lang=ua'
        response=requests.get(url2)
        weather_data=response.json()
        if 'main' in weather_data:  # если данные о погоде успешно получены
            temp = weather_data['main']['temp']  # получаем температуру
            description = weather_data['weather'][0]['description']  # получаем описание погоды

            # отправляем ответ пользователю с информацией о погоде
            reply = f'Погода в Києві: {temp} °C, {description}'
            bot.send_message(message.chat.id, reply)

        else:  # если возникла ошибка при получении данных о погоде
            bot.send_message(message.chat.id, 'Помилка при отриманні погоди. Спробуйте пізніше.')
    else:  # если пользователь отправил другое сообщение
        bot.send_message(message.chat.id, 'Виберіть опцію:', reply_markup=markup)  # отправляем сообщение с кнопками на клавиатуре

# запускаем бота
bot.polling()  # бот начинает прослушивание сообщений от пользователей и ответ на них




