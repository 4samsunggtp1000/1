import telebot
from telebot import types  # Для создания кнопок
import random  # Для генерации случайного числа

# Токен вашего бота
token = '7357460650:AAF-jPWZzVVFggQI0d-cRjNQq7QHPCL-eTY'

# Создаем объект бота
bot = telebot.TeleBot(token)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру с одной кнопкой "Гадать"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # resize_keyboard=True делает кнопки меньше
    guess_button = types.KeyboardButton("Гадать")  # Кнопка "Гадать"
    markup.add(guess_button)  # Добавляем кнопку в клавиатуру

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Добро пожаловать! Нажмите кнопку 'Гадать', чтобы получить случайное число.",
                     reply_markup=markup)


# Функция для отправки случайного числа
def send_random_number(chat_id):
    # Генерация случайного числа от 1 до 64
    random_number = random.randint(1, 64)

    # Создаем inline-кнопку "Гадать еще"
    markup = types.InlineKeyboardMarkup()
    guess_again_button = types.InlineKeyboardButton(text="Гадать еще", callback_data="guess_again")
    markup.add(guess_again_button)

    # Отправляем число с inline-кнопкой
    bot.send_message(chat_id, f"  {random_number}", reply_markup=markup)


# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Гадать":
        send_random_number(message.chat.id)
    else:
        bot.send_message(message.chat.id, "Нажмите кнопку 'Гадать', чтобы получить случайное число.")


# Обработчик inline-кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "guess_again":
        # Отправляем новое случайное число, не удаляя предыдущее
        send_random_number(call.message.chat.id)


# Запуск бота
bot.polling(none_stop=True, interval=0)