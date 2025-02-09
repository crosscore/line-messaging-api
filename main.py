#! /Users/yuu/repos/line-messaging-api/venv/bin/python3.12
import os
import random
import datetime
import time
from dotenv import load_dotenv
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from messages import MESSAGES

load_dotenv(dotenv_path=os.getenv('DOTENV_PATH'))

channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
user_id = os.getenv('USER_ID')

if channel_access_token is None or user_id is None:
    raise ValueError("please set .env file")

line_bot_api = LineBotApi(channel_access_token)

def send_message(message):
    try:
        line_bot_api.push_message(user_id, [TextSendMessage(text=message)])
        print(f"Message sent: {message}")
    except LineBotApiError as e:
        print(f"Message send error: {e}")

def main():
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

    if not MESSAGES:
        raise ValueError("MESSAGES is not set")

    chosen_message = random.choice(MESSAGES)
    send_message(chosen_message)
    print(f"Initial message sent: {chosen_message}")

    if now.hour >= 4:
        wait_seconds = random.randint(3600, 43200)
        next_run_time = now + datetime.timedelta(seconds=wait_seconds)
        next_day_7am = (now + datetime.timedelta(days=1)).replace(hour=7, minute=0, second=0, microsecond=0)
        if next_run_time >= next_day_7am:
            print("Skipping additional message today, next run will be after 7 AM tomorrow.")
            return
        print(f"Waiting for {wait_seconds} seconds before sending the next message.")
        time.sleep(wait_seconds)
        second_message = random.choice(MESSAGES)
        send_message(second_message)
        print(f"Second message sent: {second_message}")
    else:
        print("It's before 4 AM JST, skipping additional message.")

if __name__ == "__main__":
    main()
