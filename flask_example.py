# import

# from
from flask import jsonify
from flask import request
from flask import Flask
from botapitamtam import BotHandler

# settings
bot = BotHandler('token_from_prime_bot')
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello!'


@app.route('/', methods=['POST'])
def main():
    update = request.get_json()
    if update:
        message = bot.get_text(update)
        chat_id = bot.get_chat_id(update)
        mid = bot.get_message_id(update)
        if message == '/hello':
            bot.send_reply_message('Hello!', mid, chat_id)
    return jsonify(update)


if __name__ == '__main__':
    app.run()

