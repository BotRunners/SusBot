from telebot import TeleBot, types
from decouple import config as key
from os import system as cmd
from manager import genero, show_all
from random import choice
tocken = key("TK")

bot = TeleBot(tocken)


@bot.message_handler(["start", "help"])
def start(msg):
    uid = msg.chat.id

    info = """
[ ANIMES SUSPEITOS ]
Escolha un gênero
    """
    counter = 0
    markup = types.InlineKeyboardMarkup(row_width=2)
    mark = types.InlineKeyboardMarkup(row_width=1)
    h = types.InlineKeyboardButton("Todos Hentai", callback_data="h")
    e = types.InlineKeyboardButton("Todos Ecchi", callback_data="e")
    rand = types.InlineKeyboardButton("Random", callback_data="random")
    
    markup.add(h, e)
    mark.add(rand)


    bot.send_message(uid, info, reply_markup=markup)
    bot.send_message(uid, "Ou selecione 1 aleatório", reply_markup=mark)
cmd("clear && echo -e '\e[01;36m' && figlet Running... && echo '\e[01;0m Status:\e[01;32m Online \e[0m'")

@bot.callback_query_handler()
def aswer(callback):
    uid = callback.message.chat.id
    text = callback.data

    ecchi = genero("ecchi")
    hentai = genero("hentai")
 # Listar todos os Ecchi registrados no DB
    if text == "e":
        for link in ecchi:
            data = f"{link} \n{ecchi[link]}"
            bot.send_message(uid, data)

 # Listar todos os Hentai registrados no DB
    if text == "h":
        for anime in hentai:
            data = f"{anime} \n{hentai[anime]}"
            bot.send_message(uid, data)

 # Escolhe aleatoriamente 1 dentro todos registrados no DB
    if text == "random":
        todos = show_all()
        escolhido = choice(list(todos))
        nome = escolhido
        link = todos[escolhido]
        bot.send_message(uid, f"{nome} \n{link}")

bot.infinity_polling()
