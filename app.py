from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
)
from linebot.exceptions import LineBotApiError #新加的

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
    msg = event.message.text
    r = '我看不懂你說甚麼'

    if '圖片' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://cdn.hk01.com/di/media/images/3023738/org/67df85b6f7f06a7624bed0dd5f1f6afa.jpg/WRIzIxRqUxud42IOEObM_e9aHf1qKAWlokR5eqJEeXo?v=w1280.png',
            preview_image_url='https://cdn.hk01.com/di/media/images/3023738/org/67df85b6f7f06a7624bed0dd5f1f6afa.jpg/WRIzIxRqUxud42IOEObM_e9aHf1qKAWlokR5eqJEeXo?v=w1280.png')
        
        line_bot_api.reply_message(
        event.reply_token,
        image_message)

        return    



    if '貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',sticker_id='23')
        
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

        return

    if 'hi' in msg:
        r = 'hi'
    elif '你吃飯了嗎' in msg:
        r = '還沒'
    elif '你是誰' in msg:
        r = '我是line bot'
    elif '訂位' in msg:
        r = '請問您想訂位的時間?'
    


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))
    try: #新加的
        line_bot_api.reply_message('Uf5c869d53bf80b476aeeb21280e7b37f', TextSendMessage(text='Hello World!'))
    except LineBotApiError as e:
   
if __name__ == "__main__":
    app.run()






