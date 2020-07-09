from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('XmdwMzwlp8A16AFbXDu/NS13TkOtqK9hW6cexxBH5fT4t4lc8h5El/QuLNslHXhhCxFCwzsrrvBO/K7A3Qtvsn+IocQxhV0N8R+BGxJJQykYYbuOit67eJ5oabwTMFvw5QRhqNSGy81oC0fOIHhFUgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e1ee4aeb28f481b626a62607ab11b146')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()