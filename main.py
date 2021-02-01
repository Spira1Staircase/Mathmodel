import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.exceptions import (
    InvalidSignatureError
)

app = Flask(__name__)

#GET EnvironmentVariable
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["impbzBGXjvI96ybIJoFNrnHaUykB708pkP/OZGpCdXhR1KIdMf0K/PxePgXBB6az3l+qgivCw3gaa/zkJ0IpvwIc8GPvS6bDXqW9hxpIdwiaOP3f/ztUzi8Kij6vhPUi7jaG/tWYnd/F6AKpL5HlJAdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["a68af942c456b4c1ec27f830b1d6dc3a"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "Hello World!"

#GET post sentence
@app.route("/callback", methods=['POST'])
def callback():
    # GET header value
    signature = request.headers['X-Line-Signature']

    # GET text at request body
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#GET text and response
@handler.add(MassageEvent, message=TextMassage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

#Exclude execution from import
if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)