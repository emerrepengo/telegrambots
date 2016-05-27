#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Bot de servicio para VideoShock
# This program is dedicated to the public domain under the CC0 license.
"""
Basado en los ejemplos de https://github.com/python-telegram-bot/python-telegram-bot
"""
from uuid import uuid4

import re

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging

# Activamos el logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#Reemplazo simple de caracteres
def replace_all(texto, dic):
    for i, j in dic.items():
        texto = texto.replace(i, j)
    return texto
#MIMIMIzador para usar inline
def mimimi2(text):
    mimimimi2 = text
    iiii = {'a':'i', 'e':'i', 'o':'i', 'u':'i','A':'I','E':'I','O':'I','U':'I','á':'í','é':'í','ó':'í','ú':'í','Á':'Í','É':'Í','Ó':'Í','Ú':'Í'}
    trad = replace_all(mimimimi2, iiii)
    return trad
#Limonizador para usar inline
def limon(text):
    limonizado = text
    limondic = {'grim':'me', 'fandango':'toco', 'aventura':'patata'}
    limontrad = replace_all(limonizado, limondic)
    limontrad += ' ME CAGO EN SU PUTA MADRE'
    return limontrad

#MIMIMIzador con comando
def mimimi(bot, update):
    mimimimi = update.message.text
    mimimimi = mimimimi[7:]
    mimimimi += ' MIMIMIMIMIMIMI'
    iiii = {'a':'i', 'e':'i', 'o':'i', 'u':'i','A':'I','E':'I','O':'I','U':'I','á':'í','é':'í','ó':'í','ú':'í','Á':'Í','É':'Í','Ó':'Í','Ú':'Í'}
    trad = replace_all(mimimimi, iiii)
    bot.sendMessage(update.message.chat_id, text=trad)

#Comandos inline
def inlinequery(bot, update):
    query = update.inline_query.query
    results = list()
 
    results.append(InlineQueryResultArticle(id=uuid4(),
                                            title="MIMIMIzador",
                                            input_message_content=InputTextMessageContent(
                                                mimimi2(query))))
                                            
    results.append(InlineQueryResultArticle(id=uuid4(),
                                            title="Limonizador",
                                            input_message_content=InputTextMessageContent(
                                                limon(query))))
                                            
    bot.answerInlineQuery(update.inline_query.id, results=results)

#Salida del logger
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Lanzamos el updater y lo asignamos al TOKEN
    updater = Updater("TOKEN_AQUI")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Comandos a los que responder
    dp.add_handler(CommandHandler("mimimi", mimimi))

    # sin comando respondemos inline
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log de errores
    dp.add_error_handler(error)

    # arranque del bot
    updater.start_polling()

    # El bot correrá hasta que pulsemo Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()
