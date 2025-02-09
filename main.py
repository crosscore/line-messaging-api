#! /Users/yuu/repos/line-messaging-api/venv/bin/python3.12
import os
import random
import datetime
from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

load_dotenv(dotenv_path=os.getenv('DOTENV_PATH'))

channel_secret = os.getenv('CHANNEL_SECRET')
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
user_id = os.getenv('USER_ID')


if channel_secret is None or channel_access_token is None or user_id is None:
    raise ValueError("please set .env file")

line_bot_api = LineBotApi(channel_access_token)

def send_message(message):
    try:
        line_bot_api.push_message(user_id, TextSendMessage(text=message))
        print(f"message sent: {message}")
    except LineBotApiError as e:
        print(f"message send error: {e}")

def main():
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))  # set JST
    messages = os.getenv('MESSAGES').split(',')
    send_message(random.choice(messages))
    print(f"message sent: {random.choice(messages)}")

    if now.hour >= 7:
        wait_seconds = random.randint(3600, 43200) # 3600 * 12 = 43200 seconds
        next_run_time = now + datetime.timedelta(seconds=wait_seconds)

        next_day_7am = (now + datetime.timedelta(days=1)).replace(hour=7, minute=0, second=0, microsecond=0)
        if next_run_time >= next_day_7am:
            print("Skipping message today, next run will be after 7 AM tomorrow.")
            return

        send_message(random.choice(messages))
        print("Next message will be sent after", wait_seconds, "seconds.")

    else:
        print("It's before 7 AM JST, skipping additional message.")


if __name__ == "__main__":
    main()