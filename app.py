# ایجاد دکمه شیشه ای در بات  یا 
# inline keyboard buttons

from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , CallbackQueryHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup 

token = Updater("6012975729:AAF94oYNvkK4-Bz5qHx8ZR4rrKLAAuKAqxE",use_context=True) 
# Required BOT...

# Action BOT...
def sayhello(update , context):
    mykey = [[InlineKeyboardButton('پروفایل من',callback_data='myprofile'),InlineKeyboardButton('لینک کانال',callback_data='channellink')]]  # دو دکمه کنار همدیگر
    # mykey = [[InlineKeyboardButton('کانال تلگرام',callback_data='mykey1')],[InlineKeyboardButton('آدرس سایت',callback_data='mykey2')]]  # دو دکمه به زیر همدیگر

    showmykey = InlineKeyboardMarkup(mykey) #نمایش دکمه ها
    context.bot.send_message(chat_id=update.message.chat.id,text='به ربات ما خوش آمدید!',reply_markup=showmykey)

def sayaction(update,context):
    update = update.callback_query

    # print(btn)
    # {'id': '8429586604848317616', 'chat_instance': '-8782027423401440810', 'message': {'message_id': 544, 'date': 1679119602, 'chat': {'id': 6257633370, 'type': 'private', 'username': 'shusyin', 'first_name': 'husyin'}, 'text': 'به ربات ما خوش آمدید!', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'reply_markup': {'inline_keyboard': [[{'text': 'پروفایل من', 'callback_data': 'mykey1'}, {'text': 'لینک کانال', 'callback_data': 'mykey2'}]]}, 'from': {'id': 6012975729, 'first_name': 'بوت تست', 'is_bot': True, 'username': 'husyintest_bot'}}, 'data': 'mykey2', 'from': {'id': 6257633370, 'first_name': 'husyin', 'is_bot': False, 'username': 'shusyin', 'language_code': 'en'}}

    if update.data == 'myprofile':
        context.bot.send_message(text=update.message.chat.username,chat_id=update.message.chat.id)
    elif update.data == 'channellink':
        context.bot.send_message(text="@aksdjjl",chat_id=update.message.chat.id)

           

# RUN BOT...

# جواب به پیام هایی که کاربر با کامند ارسال کرده
token.dispatcher.add_handler(CommandHandler('start',sayhello))

# جواب به پیام هایی که کاربر به صورت متن ارسال میکنه
token.dispatcher.add_handler(CallbackQueryHandler(sayaction))


token.start_polling()
token.idle()