from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from helpers import get_object_from_file_txt, get_object_from_file
from posts_from_groups import todays_date
from random import choice

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text('Hi, I am Milla\'s bot! Say \'/python_news\' to get news about Python!')

def help(bot, update):
    update.message.reply_text('Don\'t worry! :) Say \'/python_news\' to get news about Python!')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def python_news(bot, update):
    date_today = todays_date()
    todays_posts = []

    posts_in_file = get_object_from_file('Python_posts.json')
    for post in posts_in_file:
        try:
            if post['date'] == date_today:
                todays_posts.append(post)
        except:
            continue
    if len(todays_posts) != 0:
        post = choice(todays_posts)
        update.message.reply_text(post['text'] + post['url'])
    else:
        update.message.reply_text('Today no news :/')

def main():
    access_token_bot = get_object_from_file_txt('access_token_bot.txt')
    updater = Updater(access_token_bot)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("python_news",python_news))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()