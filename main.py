import telebot
from telebot import types
#from conection import TELEGRAM_BOT_TOKEN

#chave do bot do telegram 
#Key provisória


key = ""
bot = telebot.TeleBot(key)
mensagem_text = "insira a matricula do usuário"

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    markup = types.ForceReply(selective=False)
    user = types.InputTextMessageContent()
    bot.send_message(mensagem.chat.id, mensagem_text , entities= user, reply_markup=markup)
    user = mensagem.text.text
    print(user)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.reply_to(mensagem, "Função ainda não criada")

@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.reply_to(mensagem, "Função ainda não criada")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def resposta_padrao(mensagem):
    menu = f"""
    Olá {mensagem.chat.first_name} {mensagem.chat.last_name}, Seja bem vindo ao bot de auxilio do Tech bar. Favor escolha alguma das opções pra continuar:
    /opcao1 Verficiar dados referente a um usuário especifico
    /opcao2 Desbloquear um usuário
    /opcao3 Bloquear um usuário
    """
    bot.reply_to(mensagem, menu)

bot.polling()