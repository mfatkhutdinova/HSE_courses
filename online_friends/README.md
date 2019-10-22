# online_friends

### A site that allows you to see a list of online friends from an arbitrary VKontakte user. The site will run on Heroku.

## Api Vk
First you need to get an API VK. To do this, we create an application. 
After completion you will receive id_app (id_client) and access_token. About it can be found [here]( http://tatet.net/p345-kak-poluchit-app-id-dlya-sotsialnoy-seti-vkontakte.html). 

After you create the application you ask permission for the use of all available data, listing all known identifiers rights.
You have to agree. Next, you will open the website where your personal data: 
https://oauth.vk.com/blank.html#access_token=xxxxxxxx&expires_in=xxxxxxx&user_id=xxxxxxxx 

Detail how to get the access token can be read [here](https://vk.com/dev/access_token).

## check_vk_online.py
When you enter an id with an API request, create a list of friends online. 
It should be run like this: **python check_vk_online.py** 1 (1 - user's ID), after launching to give out a list of friends online: **name, surname, link to the page.**

## Flask
The [Flask]( http://flask.pocoo.org) library is used to write the site. The **[tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)** will help you. 
You will need the basic layout: **HTML and CSS.**
