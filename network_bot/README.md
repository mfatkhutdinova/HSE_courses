# network_bot

### A bot that helps people find new acquaintances. 

**The immediate task** is to create a bot that asks the user for the surname, name, age, position and whom he is looking for (just text).
Save all the data in the SQLite. In the interests of the user are selected by other people.

### Usage:
**Python 3.6 required!**
```shell
# update dependences
> pip install requirements.txt

# create database if you don't have
> python DB.py

# start the bot
> python event_bot.py
```
Valid telegram bot access token is required to run the bot, so some bot should be registered with [BotFather](https://telegram.me/botfather) (**[how to](https://core.telegram.org/bots#3-how-do-i-create-a-bot)**).

Then there are 3 options:

* add resieved token to `API_KEY_TELEGRAM_NETWORK_BOT` environment variable,
* enter token manually each time bot starts,
* save token to `token.txt` file and place it near the code (depreciated). 
