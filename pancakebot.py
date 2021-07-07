import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from pancaketracker import get_prices

print("Bot started...")
telegram_bot_token = "1860286149:AAF-lcSCq6FUxyjxZdYDrPhdzSK63yEnNNI"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def price(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    bnbprice = float(crypto_data["PriceBNB"])
    usdprice = float(crypto_data["PriceUSD"])
    message += f"1 SFUND = \n{bnbprice:.8f} BNB\n{usdprice:,.8f} USD\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("price", price))
updater.start_polling()
