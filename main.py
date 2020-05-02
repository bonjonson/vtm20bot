import telebot
from telebot import types
import maneurs
import credential
bot = credential.connectto

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('Правила')
	btn2 = types.KeyboardButton('Маневры ближнего боя')
	btn3 = types.KeyboardButton('Маневры дистанционного боя')
	btn4 = types.KeyboardButton('Защитные маневры')
	btn5 = types.KeyboardButton('Общие маневры')
	btn6 = types.KeyboardButton('Оружие ближнего боя')
	btn7 = types.KeyboardButton('Дистанционное оружие')
	markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

	send_message = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакая информация тебя интересует?"
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = "" #переменная для финального сообщения
	get_message_bot = message.text.strip().lower() #считывает ввод в нижнем регистре

#главное меню
	if get_message_bot == "главное меню": #возврат в главное меню
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Правила')
		btn2 = types.KeyboardButton('Маневры ближнего боя')
		btn3 = types.KeyboardButton('Маневры дистанционного боя')
		btn4 = types.KeyboardButton('Защитные маневры')
		btn5 = types.KeyboardButton('Общие маневры')
		btn6 = types.KeyboardButton('Оружие ближнего боя')
		btn7 = types.KeyboardButton('Дистанционное оружие')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
		final_message = "Хочешь узнать что-то еще?:"

	elif get_message_bot == "правила": #ссылка на сайт с книгами правил
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://wod.su"))
		bot.send_message(message.chat.id, "Вы можете самостоятельно ознакомиться с книгами правил на сайте wod.su", parse_mode='html', reply_markup=markup)

# защитные маневры	
	elif get_message_bot == "защитные маневры":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Блок')
		btn2 = types.KeyboardButton('Парирование')
		btn3 = types.KeyboardButton('Уклонение')
		btn4 = types.KeyboardButton('Поглощение урона')
		btn5 = types.KeyboardButton('Главное меню')
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Выбери один из вариантов:"

# общие маневры
	elif get_message_bot == "общие маневры":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Атака с фланга и с тыла')
		btn2 = types.KeyboardButton('Засада')
		btn3 = types.KeyboardButton('Множественные действия')
		btn4 = types.KeyboardButton('Отмена действия')
		btn5 = types.KeyboardButton('Перемещение')
		btn6 = types.KeyboardButton('Прицеливание')
		btn7 = types.KeyboardButton('Удар или выстрел вслепую')
		btn8 = types.KeyboardButton('Главное меню')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
		final_message = "Выбери один из вариантов:"
		
# маневрый ближнего боя
	elif get_message_bot == "маневры ближнего боя":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
		btn1 = types.KeyboardButton('Бросок')
		btn2 = types.KeyboardButton('Длинное оружие')
		btn3 = types.KeyboardButton('Захват')
		btn4 = types.KeyboardButton('Клинч')
		btn5 = types.KeyboardButton('Подсечка')
		btn6 = types.KeyboardButton('Разоружение')
		btn7 = types.KeyboardButton('Удар когтями')
		btn8 = types.KeyboardButton('Удар ногой')
		btn9 = types.KeyboardButton('Удар оружием')
		btn10 = types.KeyboardButton('Удар рукой')
		btn11 = types.KeyboardButton('Укус')
		btn12 = types.KeyboardButton('Численное превосходство')
		btn13 = types.KeyboardButton('Главное меню')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13)
		final_message = "Выбери один из вариантов:"

# маневры дистанционного боя
	elif get_message_bot == "маневры дистанционного боя":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
		btn1 = types.KeyboardButton('Беглый огонь')
		btn2 = types.KeyboardButton('Дистанция')
		btn3 = types.KeyboardButton('Длинная очередь')
		btn4 = types.KeyboardButton('Короткая очередь')
		btn5 = types.KeyboardButton('Наведение')
		btn6 = types.KeyboardButton('Обстрел')
		btn7 = types.KeyboardButton('Перезарядка')
		btn8 = types.KeyboardButton('Стрельба по-македонски')
		btn9 = types.KeyboardButton('Укрытие')
		btn10 = types.KeyboardButton('Главное меню')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
		final_message = "Выбери один из вариантов:"
		return(final_message)

# обработка исключений
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Правила')
		btn2 = types.KeyboardButton('Маневры ближнего боя')
		btn3 = types.KeyboardButton('Маневры дистанционного боя')
		btn4 = types.KeyboardButton('Защитные маневры')
		btn5 = types.KeyboardButton('Общие маневры')
		btn6 = types.KeyboardButton('Оружие ближнего боя')
		btn7 = types.KeyboardButton('Дистанционное оружие')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
		final_message = "Хочешь узнать что-то еще?:"
		
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

	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup) #отправляет final_message
bot.polling(none_stop=True)