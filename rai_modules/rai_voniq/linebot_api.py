from .linebot import LineBotApi
from .linebot.models import TextSendMessage
from .linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('u3JVrkr6x3AB/lsonyzpLFP7reE7fXZvD1xCRGz8PeJ56O/VnpE3f68bVCTOUQZVIs9AAskrVFCKjqVeBTocN8ymBx6OcF6cfExIJfX0Y4xmUqDcqPbDyuX8LQPxMu16J5m1wSbRLEo8SLpPBY6dkQdB04t89/1O/w1cDnyilFU=')
def pushmsg(userId, message):
    try:
        line_bot_api.push_message(userId, TextSendMessage(text=message), notification_disabled=False, timeout=5)
    except LineBotApiError as e:
        # error handle
        print("error from line push msg")