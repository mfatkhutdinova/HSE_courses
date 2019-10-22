# Telegram_Bot

##### In this project we use VK API, take out the necessary data and create a bot in the Telegram that these data will give. Go!

First you need to obtain an API VK. To do this, we create an application. 
After completion you will receive id_app (id_client) and access_token. About it can be found [here](http://tatet.net/p345-kak-poluchit-app-id-dlya-sotsialnoy-seti-vkontakte.html).

For most of the API methods, You must pass in the access_token request is a special access key. 
It is a string of Latin letters and digits and may correspond to an individual user, a community, or to Your application.

After you create the application you ask permission for the use of all available data, listing all known identifiers rights. You have to agree. Next, you will open the website where your personal data:
https://oauth.vk.com/blank.html#access_token=xxxxxxxx&expires_in=xxxxxxx&user_id=xxxxxxxx
**Their not allowed to tell anyone!**

Detail how to get the access token can be read [here](https://vk.com/dev/access_token).

## Requests
To access a method Vkontakte API, You need to make a POST or GET request like this:
**https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=V**

It consists of several parts:

**METHOD_NAME** (required) — the API method name to which You want to apply. A complete list of methods available on [this page](https://vk.com/dev/methods).

**PARAMETERS** (optional) — input parameters of the corresponding API method, the sequence of pairs name=value separated by ampersand. The list of parameters is listed on the page with the description of the method.

**ACCESS_TOKEN** - (optional) — access key. More information about obtaining a token You can find in [this guide](https://vk.com/dev/authentication).

**V** (optional) — the version of API. Use this option to apply some changes to the format of the response of different methods. At the moment [the current version of the API 5.62](https://vk.com/dev/versions). This parameter should be passed with all requests. To maintain compatibility to existing applications by default use the version 3.0.

All the documentation [here](https://vk.com/dev/).

## News about Python
Our task is to get the news about Python from different groups of Vk. For this we use "groups.search". He searches for communities for a given substring (q = Python).
The output is a json file with **id** and **screen_name** of the desired groups.

Next, we are going in groups from a json file and pulls out all of the posts, which were published in the daily running of the script.
The output is a json file with the necessary information about the posts (text, url, date).
If you run the script twice, the new posts are added to the file, and not duplicated. See **Python_groups.py** and **posts_from_groups.py.**

## Telegram Bot
First you need to [register](http://web.telegram.org.ru).
Then find @BotFather: -> /start -> /newbot -> (write the name of the bot) -> (write the username of your bot).
You will get access token for your bot.

Next, we connect our bot with a script that produces random current news. 
The bot understands the command /start, /help and /python_news. See **Python_news_bot.py**



