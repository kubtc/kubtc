import Constants_ls as keys
from telegram.ext import *
import Responses_ls as R
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# import os
# PORT = int(os.environ.get('PORT', 5000))


print("Bot started...")


def start_command(update,context):
	update.message.reply_text('Type something random to get started')


def help_command(update, context):
	update.message.reply_text('Google')

def buy_command(update, context):
	update.message.reply_text('https://koffeeswap.exchange/#/pro/KCS/0x1f884a77ce343d599a139aa03c0305bc5566a84c')

def chart_command(update, context):
	update.message.reply_text('https://koffeeswap.exchange/#/pro/KCS/0x1f884a77ce343d599a139aa03c0305bc5566a84c')

def address_command(update, context):
	update.message.reply_text('0x1f884a77ce343d599a139aa03c0305bc5566a84cs')	

def kcc_command(update, context):
	update.message.reply_text('https://explorer.kcc.io/en/token/0x1f884a77ce343d599a139aa03c0305bc5566a84c')	


def tutorial_command(update, context):
	update.message.reply_text('https://kubtc.site/#tutorial')


def whitepaper_command(update, context):
	update.message.reply_text('https://kubtc.site/#whitepaper')


def roadmap_command(update, context):
	update.message.reply_text('https://kubtc.site/#roadmap')



def handle_message(update, context):
	text = str(update.message.text).lower()
	response = R.sample_responses(text)

	update.message.reply_text(response)


def error(update, context):
	print(f"Update {update} caused error {context.error}")








############################### Bot ############################################
def start(bot, update):
  bot.message.reply_text(main_menu_message(),
                         reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  bot.callback_query.message.edit_text(main_menu_message(),
                          reply_markup=main_menu_keyboard())

# def first_menu(bot, update):
#   bot.callback_query.message.edit_text(first_menu_message(),
#                           reply_markup=first_menu_keyboard())

# def second_menu(bot, update):
#   bot.callback_query.message.edit_text(second_menu_message(),
#                           reply_markup=second_menu_keyboard())

# def first_submenu(bot, update):
#   pass

# def second_submenu(bot, update):
#   pass

def error(update, context):
    print(f'Update {update} caused error {context.error}')

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Buy/Chart', url='https://koffeeswap.exchange/#/pro/KCS/0x1f884a77ce343d599a139aa03c0305bc5566a84c')],
  			  [InlineKeyboardButton('KCC Explorer', url='https://explorer.kcc.io/en/token/0x1f884a77ce343d599a139aa03c0305bc5566a84c')],
              [InlineKeyboardButton('Tutorial', url='https://kubtc.site/#tutorial')],
              [InlineKeyboardButton('Whitepaper', url='https://kubtc.site/#whitepaper')]]
  return InlineKeyboardMarkup(keyboard)

# def first_menu_keyboard():
#   keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
#               [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
#               [InlineKeyboardButton('Main menu', callback_data='main')]]
#   return InlineKeyboardMarkup(keyboard)

# def second_menu_keyboard():
#   keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
#               [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
#               [InlineKeyboardButton('Main menu', callback_data='main')]]
#   return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

# def first_menu_message():
#   return 'Choose the submenu in first menu:'

# def second_menu_message():
#   return 'Choose the submenu in second menu:'





def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher

	#dp.add_handler(CommandHandler("start", start_command))
	#dp.add_handler(CommandHandler("help", help_command))
	dp.add_handler(CommandHandler("buy", buy_command))
	dp.add_handler(CommandHandler("chart", chart_command))
	dp.add_handler(CommandHandler("kcc", kcc_command))
	dp.add_handler(CommandHandler("address", address_command))
	dp.add_handler(CommandHandler("tutorial", tutorial_command))
	dp.add_handler(CommandHandler("whitepaper", whitepaper_command))
	dp.add_handler(CommandHandler("roadmap", roadmap_command))




	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('info', start))
	dp.add_handler(CommandHandler('help', start))
	dp.add_handler(CommandHandler('links', start))
	dp.add_handler(CommandHandler('link', start))
	dp.add_handler(CommandHandler('menu', start))
	dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
	# dp.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
	# dp.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
	# dp.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
	# dp.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))


	dp.add_handler(MessageHandler(Filters.text, handle_message))

	dp.add_error_handler(error)

	updater.start_polling(0)
	# updater.start_webhook(listen="0.0.0.0",
 #                          port=int(PORT),
 #                          url_path=keys.API_KEY)
	# updater.bot.setWebhook('https://secret-escarpment-10009.herokuapp.com/' + keys.API_KEY)
	updater.idle()



# def print_hi(name):
# 	print(f'Hi, {name}')



# if __name__ == '__main__':
# 	print_hi('PyCharm')

main()