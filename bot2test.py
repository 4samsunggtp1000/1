import telebot
from telebot import types  # Для создания кнопок
import random  # Для выбора случайного слова
import os  # Для работы с файловой системой

# Токен вашего бота
token = '7357460650:AAF-jPWZzVVFggQI0d-cRjNQq7QHPCL-eTY'

# Создаем объект бота
bot = telebot.TeleBot(token)

# Путь к вашей картинке
image_path = r"C:\pythonProject2\100055355046b0.webp"

# Список слов (все слова используют одну и ту же картинку)
words = ["Яблоко", "Солнце", "Книга", "Океан", "Гитара", "Радость", "Город", "Звезда", "Ветер", "Мечта"]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру с кнопками "Старт" и "Рандом"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # resize_keyboard=True делает кнопки меньше
    start_button = types.KeyboardButton("Старт")  # Кнопка "Старт"
    random_button = types.KeyboardButton("Рандом")  # Кнопка "Рандом"
    markup.add(start_button, random_button)  # Добавляем кнопки в клавиатуру

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=markup)

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Старт":
        # Действия при нажатии кнопки "Старт"
        bot.send_message(message.chat.id, "Привет! Чем я могу тебе помочь?")
    elif message.text == "Рандом":
        # Действия при нажатии кнопки "Рандом"
        random_word = random.choice(words)  # Выбираем случайное слово

        # Проверяем, существует ли файл
        if os.path.exists(image_path):
            # Отправляем картинку и текст
            with open(image_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo, caption=f"Случайное слово: {random_word}")
        else:
            bot.send_message(message.chat.id, "Изображение не найдено.")
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Напиши 'Старт', чтобы начать, или 'Рандом', чтобы получить случайное слово и картинку.")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")

# Запуск бота
bot.polling(none_stop=True, interval=0)