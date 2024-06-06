from telegram import Update, ChatMember
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext



from telegram import Update, ChatMember
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

user_messages_count = {}

def count_messages(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id in user_messages_count:
        user_messages_count[user_id] += 1
    else:
        user_messages_count[user_id] = 1

def get_user_info(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_id = user.id
    username = user.username
    full_name = user.full_name
    message_count = user_messages_count.get(user_id, 0)

    try:
        chat_member = context.bot.get_chat_member(update.effective_chat.id, user_id)
        status = chat_member.status
    except Exception as e:
        status = "غير معروف"

    response = (f"معرف المستخدم: {user_id}\n"
                f"الاسم: {full_name}\n"
                f"اسم المستخدم: @{username}\n"
                f"عدد الرسائل: {message_count}\n"
                f"الرتبة: {status}")

    update.message.reply_text(response)

def main() -> None:

    
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    /userinfo get_user_info
    dispatcher.add_handler(CommandHandler('userinfo', get_user_info))
    count_messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, count_messages))

    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()
