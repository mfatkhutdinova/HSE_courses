import telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    RegexHandler, ConversationHandler
from helpers import load_txt_data, get_api_key
from DB import add_user
import logging
import re

logging.basicConfig(format='%(asctime)s - %(name)s - '
                           '%(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [
    ['Возраст', 'Имя'],
    ['Фамилия', 'Должность'],
    ['Компания', 'Знакомство'],
    ['Done']
]

markup_keyboard = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data: dict) -> str:
    facts = ""
    for key, value in user_data.items():
        facts += f"{key}:\t{value}\n"
    return facts


def set_to_str(categories: set) -> str:
    categories_str = ""
    for category in categories:
        categories_str += f"{category}, "
    return categories_str[:-2]  # remove last ', '


# @TODO: store messages in json
def start(bot, update):
    update.message.reply_text(
        "Здравствуй! Мы рады знать, что Ты сейчас с нами! "
        "Давай, познакомимся? :) Расскажи немного о себе.",
        reply_markup=markup_keyboard)
    return CHOOSING


def stop(bot, update):
    update.message.reply_text(f"До свидания!",
                              reply_markup=telegram.ReplyKeyboardRemove())
    done(bot, update, None)  # stop conversation


def configure_bot(bot, update):
    update.message.reply_text(
        "Настраивать пока нечего.",
        reply_markup=markup_keyboard)
    return CHOOSING


def get_help(bot, update):
    update.message.reply_text(
        "Пожалуйста, следуйте просьбам бота: заполните информацию о Вас.",
        reply_markup=markup_keyboard)
    return CHOOSING


# @TODO: store messages in json
def regular_choice(bot, update, user_data):
    request_text = update.message.text
    user_data['choice'] = request_text
    if request_text.lower() == "знакомство":
        update.message.reply_text('С кем бы Вы хотели познакомиться?')
    else:
        update.message.reply_text(f"Ваш(а/е) {request_text.lower()}?")
    return TYPING_REPLY


# @TODO: store messages in json
def received_information(bot, update, user_data):
    lower_border, higher_border = 17, 90
    choice_text = update.message.text
    category = user_data['choice'].lower()

    correct_info = True
    if category.lower() == "возраст":
        try:
            user_age = int(choice_text)
            if user_age < lower_border or user_age > higher_border:
                correct_info = False
        except ValueError:
            correct_info = False
        if not correct_info:
            update.message.reply_text(f"Вы ввели неверную информацию о "
                                      f"возрасте!\nПожалуйста, введите число "
                                      f"от {lower_border} до {higher_border}.",
                                      reply_markup=markup_keyboard)

    if category.lower() == "имя" or category.lower() == "фамилия":
        if re.search(r"[^а-яА-Я ]", choice_text) \
                or len(choice_text.lower().strip()) < 2:
            correct_info = False
        if not correct_info:
            update.message.reply_text(f"Вы неверно ввели поле '{category}'!\n"
                                      f"Пожалуйста, введите корректную "
                                      f"информацию о себе.",
                                      reply_markup=markup_keyboard)

    del user_data['choice']  # remove current request message
    if not correct_info:
        return CHOOSING
    user_data[category] = choice_text
    update.message.reply_text(f"Записал: {facts_to_str(user_data)}",
                              reply_markup=markup_keyboard)
    return CHOOSING


# @TODO: store messages in json
# @TODO: add name, surname and other str fields verifications
def done(bot, update, user_data):
    if not user_data:
        return ConversationHandler.END
    if 'choice' in user_data:
        del user_data['choice']
    
    user_data['chat_id'] = update.message.chat.id
        
    user_data['chat_id'] = update.message.chat.id

    if 'возраст' not in user_data or 'имя' not in user_data \
            or 'фамилия' not in user_data or 'должность' not in user_data:
        mentioned = set(user_data.keys())
        required = {"имя", "фамилия", "возраст", "должность"} - mentioned
        update.message.reply_text(f"Но Вы пока еще не рассказали нам о себе!\n"
                                  f"Пожалуйста, запоните обязательные поля: "
                                  f"{set_to_str(required)}.",
                                  reply_markup=markup_keyboard)
        return CHOOSING
    else:
        update.message.reply_text("Спасибо! Мы желаем Вам отличного "
                                  "времяпровождения!\n",
                                  reply_markup=telegram.ReplyKeyboardRemove())
        users = add_user(user_data)
        if isinstance(users, str):
            update.message.reply_text(users)
        else:
            update.message.reply_text("Список людей, которые хотят с Вами "
                                      "познакомиться:\n" )
            for user in users:
                update.message.reply_text(facts_to_str(user))
    user_data.clear()
    return ConversationHandler.END


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def add_events_handlers(dispatcher, handlers, error_handler=None):
    for handler in handlers:
        dispatcher.add_handler(handler)
    if error_handler:
        dispatcher.add_error_handler(error_handler)


if __name__ == '__main__':
    access_token = get_api_key("API_KEY_TELEGRAM_NETWORK_BOT", "Telegram")
    if not access_token:
        access_token = load_txt_data("token.txt")
    updater = Updater(access_token)

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            CHOOSING: [
                RegexHandler(
                    '^(Возраст|Фамилия|Имя|Должность|Компания|Знакомство)$',
                    regular_choice, pass_user_data=True
                ),
            ],
            TYPING_REPLY: [
                MessageHandler(
                    Filters.text, received_information, pass_user_data=True
                ),
            ],
        },
        fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
    )

    add_events_handlers(
        updater.dispatcher,
        handlers=[
            CommandHandler('help', get_help),
            CommandHandler('settings', configure_bot),
            CommandHandler('stop', stop),
            conversation_handler
        ],
        error_handler=error
    )

    updater.start_polling()
    updater.idle()
