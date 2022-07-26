import telebot
from telebot import types
import re
#sum_ks_bot

# Создаем экземпляр бота
bot = telebot.TeleBot('5444247357:AAFnioMrj4x6OLDT9UzVbI8RPopICpVlKf8')

@bot.message_handler(content_types=['text']) #Срабатывание на text
def start(message): #Начало
  if message.text.lower() == 'вычисли сумму чисел' or message.text.lower() == '/sum':#Команда для начала. message.text - получаемый текст. lower(), значит не учитывается регистр, т.е. и /SUM и /SuM будет считаться за один и тот же текст
    bot.send_message(message.from_user.id, 'Хорошо. Введи два числа которые ты хочешь суммировать. К примеру "1 и 5".')
    bot.register_next_step_handler(message, sumcalc)#"Перенаправляет" на след.функцию
  else:
    bot.send_message(message.from_user.id, 'Введи /sum, или напиши "Вычисли сумму чисел", чтобы продолжить.')

def sumcalc(message):#После "перенаправления" функция сработает, лишь после получения message
  try: #try юзаю, чтоб делать проверки каких-то действий. И в случае ошибки, программа не крашнется, а просто выполнит заданные в except действие.
    number1, number2 = re.split(' и ', message.text, maxsplit = 1)#Разделяет полученный текст по слову " и "
    try:
      number1 = int(number1) #Проверка "числа ли?" полученные данные. Если без такой проверки. То при попытке сделать сумму, а там не числа - то краш
      try:
        number2 = int(number2)
        bot.send_message(message.from_user.id, 'Сумма двоих введённых тобой чисел равна - ' + str(number1 + number2))
      except Exception:
        bot.send_message(message.from_user.id, 'Вы ввели данные не в правильном формате.\nВы ввели не число. /sum - Чтоб повторить сначала.')
    except Exception:
      bot.send_message(message.from_user.id, 'Вы ввели данные не в правильном формате.\nВы ввели не число. /sum - Чтоб повторить сначала.')
  except Exception:
    bot.send_message(message.from_user.id, 'Вы ввели данные не в правильном формате.\n*Будьте внимательны*, ввод должен быть формата *"*число *и* число*"*. /sum - Чтоб повторить сначала.', parse_mode= 'Markdown')

bot.polling( none_stop = True, interval=0 )#Чтоб программа не закрывалась никогда