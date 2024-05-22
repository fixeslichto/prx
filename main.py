import telebot
from telebot import types

bot = telebot.TeleBot("7040949031:AAHy2EAyaezDxO8y0tqEP4CzyVsrc_k-0C0")
PRX_Balance = float(0)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}\n"
                                      f"/Button")

@bot.message_handler(commands=['Button'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("PRX")
    Shop = types.KeyboardButton("Магазин")
    markup.add(item1, Shop)
    bot.send_message(message.chat.id, "Отлично!", reply_markup=markup)

@bot.message_handler(commands=['shop'])
def button_shop(message):
    markup_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Shop = types.KeyboardButton("Магазин")
    Up = types.KeyboardButton("Улучшение")
    Exit = types.KeyboardButton("Выход")
    markup_shop.add(Shop, Up, Exit)
    bot.send_message(message.chat.id, "Магазин", reply_markup=markup_shop)


@bot.message_handler(content_types=['text'])
def PRX(message):
    global PRX_Balance
    if message.text == "PRX":
        bot.send_message(message.chat.id, "+ 0001 PRX'token")
        PRX_Balance += 0.0001
        bot.send_message(message.chat.id, f"Твой баланс: {PRX_Balance} PRX'token")
    if message.text == "Выход":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("PRX")
        Shop = types.KeyboardButton("Магазин")
        markup.add(item1, Shop)
        bot.send_message(message.chat.id, "Отлично!", reply_markup=markup)
        bot.send_message(message.chat.id, f"Твой баланс: {PRX_Balance} PRX'token")
    if message.text == "Магазин":
        markup_shop = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Shop = types.KeyboardButton("Магазин")
        Up = types.KeyboardButton("Улучшение")
        Exit = types.KeyboardButton("Выход")
        markup_shop.add(Shop, Up, Exit)
        bot.send_message(message.chat.id, 'Магазин - здесь вы сможете купить улучшения для вашего бота', reply_markup=markup_shop)






bot.polling(none_stop=True)