run2=0 #сколько проехали туземцы
run1=25 #сколько проехал разбiйнiк
jajda=0 #склько жажды у разбойника,если жажда будет равна 8 ,то ты умрешь!
energy=8 #энергия верблюда ,если будет 0 ты умрешь
a=1
b=1
import telebot
import random
import time

bot = telebot.TeleBot('1932260026:AAFH7x2nMEFNxvkv6w92VzrBuo_FT4r3qaA')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True,True)


keyboard1.row('Начать игру', 'Об игре','/restart','Правила')
keyboard1.row('A','B','C','D','Q')
keyboard2.row('Начать дуэль!','Сдатьса')


@bot.message_handler(commands=['restart'])
def tytyty(message):
    global run1,run2,jajda,energy,a
    run2 = 0
    run1 = 25
    jajda = 0
    energy = 8
    bot.send_message(message.chat.id, 'нажмите что-бы пройти игру заново:')
    bot.send_message(message.chat.id, '/start')
    a=1


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
    bot.send_photo(message.chat.id, open('/Users/apple/Downloads/1кjpg.jpg', 'rb'))
    bot.send_message(message.chat.id, 'Добро пожаловать в игру -на верблюдах! Вы украли верблюда, чтобы пробраться через великую пустыню Моби(169 миль). Туземцы хотят вернуть своего верблюда и гонятся за тобой! Выживите убегаю по пустыне и опередите туземцев.'
                                          'Скорость туземцев равна 15 миль, а разбойника равна 16 милям в час,энергия верблюда равна 8,жажда разбойника в начале игры=0,но потом она увеличивается и если она достигнет 8 то ты труп,и да у тебя есть фора равная 25 милям!Вообщем удачи')
    bot.send_message(message.chat.id,'Нажмите Начать Игру!')



def vopros(message):
    bot.send_message(message.chat.id, "A)Пейте из фляги")
    bot.send_message(message.chat.id, "B)вперед на полной скорости.")
    bot.send_message(message.chat.id, "C)Остановитесь и отдохните.")
    bot.send_message(message.chat.id, "D)Проверка состояния.")
    bot.send_message(message.chat.id, "Q) Выйти из игры")
    bot.send_message(message.chat.id, "Твой выбор?")

@bot.message_handler(content_types=['text'])

def send_text(message):
    global run1
    global jajda
    global run2
    global energy
    global a
    global b

    if message.text.lower() == 'начать игру':
        bot.send_message(message.chat.id,"A)Пейте из фляги")
        bot.send_message(message.chat.id,"B)вперед на полной скорости.")
        bot.send_message(message.chat.id,"C)Остановитесь и отдохните.")
        bot.send_message(message.chat.id,"D)Проверка состояния.")
        bot.send_message(message.chat.id,"Q) Выйти из игры")
        bot.send_message(message.chat.id,"Твой выбор?")
    if message.text.lower() == 'об игре':
        bot.send_message(message.chat.id,'Создал сие чудо Ю.Наумов')
    if message.text.lower() == 'правила':
        bot.send_message(message.chat.id,'Чувак,правил нет!')

    if a==1:
        if message.text.lower() == 'a':
            if jajda==0:
                bot.send_message(message.chat.id,"У тебя нет жажды ,она равна 0,ты просто остановил верблюда,за это время туземцы прошли еще 5 миль !")
                run2+=10
            else:
                bot.send_message(message.chat.id,f"Жажда равна {jajda-1} пока ты пил туземцы проехали 5 миль")
                jajda-=1
                run2 +=5


            if jajda == 8:
                bot.send_message(message.chat.id,"Ты проиграл!Ты умер от не хватка воды")
                bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECyHVhICzgK1FQt_OUtNNX1FSHK_-0JgACJAQAAj-VzArPrlf2wHO8CyAE')
                a=0
                bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
                bot.send_message(message.chat.id,'/restart')


            vopros(message)

        if message.text.lower() == 'b':
            energy -= 1
            bot.send_message(message.chat.id,f"Ты прошел в итоге  {run1+16} миль(полная скорость равна 16 миль в час ,кстати из за этого энергия верблюда уменьшилась на 1 и жажда прибавилась на 1)")
            run1+=16
            run2+=15
            jajda+=1
            if run1 >= 169:
                bot.send_message(message.chat.id,"*Ты победил(проехал пустныню Моби) !Молодец, уделал туземцев!! *", parse_mode= "Markdown")
                bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECyHlhIDWMJmR2cKzipOO-8iBa4LS4IwAC0gQAAs7Y6AsRtfrQUJZpBiAE')
                a=0
                bot.send_message(message.chat.id, 'Нажмите для того что-бы начать сначала:')
                bot.send_message(message.chat.id,'/restart')
            if jajda==8 and run1<169:
                bot.send_message(message.chat.id,f"Ты умер от жажды!!!Покеда!Она у тебя равна максимальному значению {jajda}")
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECyHVhICzgK1FQt_OUtNNX1FSHK_-0JgACJAQAAj-VzArPrlf2wHO8CyAE')
                a=0
                bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
                bot.send_message(message.chat.id,'/restart')
            if run2 >= run1:
                bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECyQthINoHhu55a4MOmaylz5URplqWJgAC7gQAAs7Y6Av7yana3PIwiSAE')
                bot.send_message(message.chat.id, "Тебя догнали туземцы,и сейчас тебя съедят!Так что ты проиграл!!!")
                a=0
                bot.send_message(message.chat.id,'Нажмите что-бы начать с начала:')
                bot.send_message(message.chat.id,'/restart')
            if a==1:
                vopros(message)

            if energy==0 and jajda!=8:
                bot.send_message(message.chat.id,"Энергия верблюда равна 0, он умер от измождения")
                bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
                bot.send_message(message.chat.id, '/restart')
                a=0
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECyH1hIDYusgngP0fBp63R4vGBf5OZMAAC7wUAApb6EgXN5022CloLmiAE')
        if message.text.lower()  == 'd':
            bot.send_message(message.chat.id,f"Энергия верблюда равна {energy}.Твоя жажда равна {jajda}.Ты проехал всего {run1}. Кстати если жажда будет равна 8 то ты умрешь ,Туземцы от вас на расстояние {run1-run2-5} из-за того что ты остановился что бы проверить состояние, туземцы проехали еще 5 миль" )
            run2+=5
            if run2 >= run1:
                bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECyfBhIihFCQvJGipsQpAWiQk2lif58gACzQQAAs7Y6Auz8ca_WShKkSAE')
                bot.send_message(message.chat.id, "Тебя догнали туземцы,но может есть еще шанс?",reply_markup=keyboard2)
        if message.text.lower() == 'начать дуэль!':
            b=0
            bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECygphIir_0dLQZvGaYzj2uxa3wY9mggACKAQAAj-VzApCEo_PLa7NvCAE')
            bot.send_message(message.chat.id,'Дуэль началась,теперь все зависит от твоего везения...')
            my_number = random.randrange(0,8)
            time.sleep(5)
            if my_number == 1:
                bot.send_message(message.chat.id,'*О,а ты везунчик,тебе повезло!Ты сумел выиграть дуэль!Теперь тебе ничего не угрожает!*',parse_mode= "Markdown")
                a = 0
                bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
                bot.send_message(message.chat.id, '/restart')
            else:
                bot.send_message(message.chat.id,'*Вот ты уже достал свой пистолет,но вдруг раздался выстрел и  ты труп!*',parse_mode= "Markdown")
                bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECyfZhIij4bPCi__Ve-hU2MxCe9mH1YAAC_wAD5bkIGvo7MX3nUJ5VIAQ')
                a = 0
                bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
                bot.send_message(message.chat.id, '/restart')

        if message.text.lower() == 'сдатьса' and b==1:
            bot.send_message(message.chat.id, 'Ты сдался,а значит нв всю жизнь будешь рабом')
            a = 0
            bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
            bot.send_message(message.chat.id, '/restart')


        if message.text.lower() == 'c':
            if energy<=7:
                energy += 1
                bot.send_message(message.chat.id,f"Верблюд отдохнул его энергия теперь равна {energy+1}  за это время туземцы проехали еще 5 миль,а ты в это время отдыхал..." )
            elif energy==8:
                bot.send_message(message.chat.id,"Ты потерял время в пустую так как энергия равна макс 8,туземцы за это время прошли еще 5 миль")
            run2+=5

            if run2>=run1:
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECyfBhIihFCQvJGipsQpAWiQk2lif58gACzQQAAs7Y6Auz8ca_WShKkSAE')
                bot.send_message(message.chat.id, "Тебя догнали туземцы,но может есть еще шанс?",reply_markup=keyboard2)
            if message.text.lower() == 'начать дуэль!':
                b = 0
                bot.send_sticker(message.chat.id,
                                 'CAACAgIAAxkBAAECygphIir_0dLQZvGaYzj2uxa3wY9mggACKAQAAj-VzApCEo_PLa7NvCAE')
                bot.send_message(message.chat.id, 'Дуэль началась,теперь все зависит от твоего везения...')
                my_number = random.randrange(0, 8)
                time.sleep(5)
                if my_number == 1:
                    bot.send_message(message.chat.id,'*О,а ты везунчик,тебе повезло!Ты сумел выиграть дуэль!Теперь тебе ничего не угрожает!*',parse_mode="Markdown")
                    a = 0
                    bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
                    bot.send_message(message.chat.id, '/restart')
                else:
                    bot.send_message(message.chat.id,'*Вот ты уже достал свой пистолет,но вдруг раздался выстрел и  ты труп!*',parse_mode="Markdown")
                    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAECyfZhIij4bPCi__Ve-hU2MxCe9mH1YAAC_wAD5bkIGvo7MX3nUJ5VIAQ')
                    a = 0
                    bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
                    bot.send_message(message.chat.id, '/restart')

            if message.text.lower() == 'сдатьса' and b == 1:
                bot.send_message(message.chat.id, 'Ты сдался,а значит нв всю жизнь будешь рабом')
                a = 0
                bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
                bot.send_message(message.chat.id, '/restart')

            if a==1:
                vopros(message)
        if message.text.lower() =='q':
            bot.send_message(message.chat.id,"Да ,я надеялся ,что ты пройдешь больше ,пока!!!")
            a=0
            bot.send_message(message.chat.id, 'Нажмите что-бы начать с начала:')
            bot.send_message(message.chat.id, '/restart')

bot.polling()

