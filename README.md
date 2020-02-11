## Flask Example

An example usage of Flask with webhook on Heroku.  

## Requirements

- botapitamtam
- requests
- Flask
- gunicorn

## Heroku

For full job, you need to do a few things on the [Heroku](https://www.heroku.com/) itself:

- Create new app on Heroku.
- Deploy your code. I'am used github.
- Copy url your new app. (Button: Open App)  

After all job, you need add webhook in TamTam to PrimeBot.  
If did everythined right, you see welcome message: "Hello!".  
If you don't see this message, check second method. (Deploy your code on Heroku)  

## TamTam

Okay, let's go to TamTam in PrimeBot:
- If you have bot, then write command: `/set_webhook`.  
- Choose your bot.
- Now you need paste copyed url.  

If everything right, bot answer on you command.
