# import

# from
from flask import jsonify
from flask import request
from flask import Flask
from tamtamapi import Bot

# settings
bot = BotHandler('token_from_prime_bot')
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello!'


@app.route('/', methods=['POST'])
def main():
    update = request.get_json()
    if updates:
        message = bot.get_message_text(updates)
        chat_id = bot.get_chat_id(updates)
        mid = bot.get_mid(updates)
        if message == '/hello':
            bot.reply_message(chat_id, 'Hello!', mid)
    return jsonify(update)


if __name__ == '__main__':
    app.run()

