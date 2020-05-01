import telebot
from telebot import types
import defence_maneurs
import melee_maneurs
import ranged_maneurs
import maneurs

bot = telebot.TeleBot('API KEY')

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
	
	elif get_message_bot == "блок":
		markup = types.InlineKeyboardMarkup()
		final_message = defence_maneurs.def_man['блок']

	elif get_message_bot == "парирование":
		markup = types.InlineKeyboardMarkup()
		final_message = defence_maneurs.def_man['парирование']

	elif get_message_bot == "уклонение":
		markup = types.InlineKeyboardMarkup()
		final_message = defence_maneurs.def_man['уклонение']

	elif get_message_bot == "поглощение урона":
		markup = types.InlineKeyboardMarkup()
		final_message = defence_maneurs.def_man['поглощение урона']

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
	
	elif get_message_bot == "атака с фланга и с тыла":
		markup = types.InlineKeyboardMarkup()
		final_message = maneurs.usual['атака с фланга и с тыла']

	elif get_message_bot == "засада":
		markup = types.InlineKeyboardMarkup()
		final_message = maneurs.usual['засада']
	
	elif get_message_bot == "множественные действия":
		markup = types.InlineKeyboardMarkup()
		final_message = maneurs.usual['множественные действия']
	
	elif get_message_bot == "перемещение":
		markup = types.InlineKeyboardMarkup()
		final_message = maneurs.usual['перемещение']

	elif get_message_bot == "прицеливание":
		markup = types.InlineKeyboardMarkup()
		final_message = maneurs.usual['прицеливание']
	
	elif get_message_bot == "отмена действия":
		markup = types.InlineKeyboardMarkup()
		final_message = maneurs.usual['отмена действия']
	
	elif get_message_bot == "удар или выстрел вслепую":
		markup = types.InlineKeyboardMarkup()
		final_message = maneurs.usual['удар или выстрел вслепую']

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

	elif get_message_bot == "бросок":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['бросок']
	elif get_message_bot == "длинное оружие":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['длинное оружие']
	elif get_message_bot == "захват":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['захват']
	elif get_message_bot == "клинч":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['клинч']
	elif get_message_bot == "подсечка":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['подсечка']
	elif get_message_bot == "разоружение":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['разоружение']
	elif get_message_bot == "удар когтями":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['удар когтями']
	elif get_message_bot == "удар ногой":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['удар ногой']
	elif get_message_bot == "удар оружием":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['удар оружием']
	elif get_message_bot == "удар рукой":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['удар рукой']
	elif get_message_bot == "укус":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['укус']
	elif get_message_bot == "численное превосходство":
		markup = types.InlineKeyboardMarkup()
		final_message = melee_maneurs.at_man['численное превосходство']
	
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

	elif get_message_bot == "беглый огонь":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['беглый огонь']
	elif get_message_bot == "дистанция":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['дистанция'] 
	elif get_message_bot == "длинная очередь":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['длинная очередь'] 
	elif get_message_bot == "короткая очередь":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['короткая очередь'] 
	elif get_message_bot == "наведение":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['наведение'] 
	elif get_message_bot == "обстрел":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['обстрел'] 
	elif get_message_bot == "перезарядка":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['перезарядка']
	elif get_message_bot == "стрельба по-македонски":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['стрельба по-македонски']  
	elif get_message_bot == "укрытие":
		markup = types.InlineKeyboardMarkup()
		final_message = ranged_maneurs.rang_man['укрытие']   

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

		final_message = "Что-то пошло не так, выбери один из существующих пунктов меню:"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup) #отправляет final_message
bot.polling(none_stop=True)