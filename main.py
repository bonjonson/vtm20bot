"""Основной код"""
from telebot import types
import advanced
import credential
import maneurs
import tables
#import logging
import menu
# from menu import *menu.

bot = credential.connectto
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def start(message):
    """Стартовое меню и приветствие"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(*menu.start_btn_list.values())

    send_message = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}\
        </b>!\nКакая информация " \
                   f"тебя интересует? "
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    """Оглавление и полезные ссылки"""
    final_message = ""  # переменная для финального сообщения
    get_message_bot = message.text.strip().lower()  # считывает ввод в нижнем регистре

    _lookup = {
        "главное меню": [*menu.main_menu.values()],
        "защитные маневры": [*menu.def_maneurs.values()],
        "общие маневры": [*menu.usual_maneurs.values()],
        "маневры ближнего боя": [*menu.range_maneurs.values()],
        "маневры дистанционного боя": [*menu.def_maneurs.values()],
        "различные подсказки": [*menu.tips.values()],
        "таблицы": [*menu.graph_tables.values()]
    }.get(get_message_bot)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(_lookup.get(get_message_bot,
                           final_message = "Неправильное значение, \
                            пожалуйста выбери одно из меню:"))

    # Ссылки
    if get_message_bot == "ссылки":  # ссылка на сайт с книгами правил
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на wod.su", url="https://wod.su"))
        markup.add(types.InlineKeyboardButton("Перейти на studio101.ru", \
                                              url="https://studio101.ru"))
        bot.send_message(message.chat.id,
                         'Вы можете самостоятельно ознакомиться с книгами \
                            правил на сайте wod.su или приобрести официальную \
                                книгу правил на сайте studio101.ru',
                         parse_mode='html', reply_markup=markup)

    # главное меню
    if get_message_bot == "главное меню":  # возврат в главное меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(*menu.main_menu.values())
        final_message = "Хочешь узнать что-то еще?:"

    # # защитные маневры
    # elif get_message_bot == "защитные маневры":
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    #     markup.add(*menu.def_maneurs.values(), menu.MAIN_BTN)
    #     final_message = "Выбери один из вариантов:"

    # # общие маневры
    # elif get_message_bot == "общие маневры":
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    #     markup.add(*menu.usual_maneurs.values(), menu.MAIN_BTN)
    #     final_message = "Выбери один из вариантов:"

    # # маневрый ближнего боя
    # elif get_message_bot == "маневры ближнего боя":
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    #     markup.add(*menu.melee_maneurs.values(), menu.MAIN_BTN)
    #     final_message = "Выбери один из вариантов:"

    # # маневры дистанционного боя
    # elif get_message_bot == "маневры дистанционного боя":
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    #     markup.add(*menu.range_maneurs.values(), menu.MAIN_BTN)
    #     final_message = "Выбери один из вариантов:"

    # # различные подсказки
    # elif get_message_bot == "различные подсказки":
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    #     markup.add(*menu.tips.values(), menu.MAIN_BTN)
    #     final_message = "Выбери один из вариантов:"

    # # графические таблицы
    # elif get_message_bot == "таблицы":
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    #     markup.add(*menu.graph_tables.values(), menu.MAIN_BTN)
    #     final_message = "Выбери один из вариантов:"


    if get_message_bot in maneurs.def_man:
        markup = types.InlineKeyboardMarkup()
        final_message = maneurs.def_man[get_message_bot]

    elif get_message_bot in maneurs.usual:
        markup = types.InlineKeyboardMarkup()
        final_message = maneurs.usual[get_message_bot]

    elif get_message_bot in maneurs.at_man:
        markup = types.InlineKeyboardMarkup()
        final_message = maneurs.at_man[get_message_bot]

    elif get_message_bot in maneurs.rang_man:
        markup = types.InlineKeyboardMarkup()
        final_message = maneurs.rang_man[get_message_bot]

    elif get_message_bot in advanced.adv:
        markup = types.InlineKeyboardMarkup()
        final_message = advanced.adv[get_message_bot]

    if get_message_bot in tables.graph_tab:
        markup = types.InlineKeyboardMarkup()
        with open(tables.graph_tab.get(get_message_bot), 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

    # обработка исключений
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(*menu.main_menu.values(), menu.MAIN_BTN)
        final_message = "Неправильное значение, пожалуйста выбери одно из меню:"

    bot.send_message(message.chat.id, final_message, parse_mode='html', \
                     reply_markup=markup)  # отправляет final_message



if __name__ == "__main__":
    bot.polling(none_stop=True)
