#! /Users/yuu/repos/line-messaging-api/venv/bin/python3.12
import os
import random
import datetime
from dotenv import load_dotenv
from linebot.v3.messaging import MessagingApi
from linebot.v3.messaging.models import TextMessage
from messages import MESSAGES

# Load environment variables
load_dotenv(dotenv_path=os.getenv('DOTENV_PATH'))

channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
user_id = os.getenv('USER_ID')

if channel_access_token is None or user_id is None:
    raise ValueError("please set .env file")

messaging_api = MessagingApi(channel_access_token)

def send_message(message):
    try:
        # Send message using MessagingApi (v3)
        messaging_api.push_message(
            to=[user_id],
            messages=[TextMessage(text=message)]
        )
        print(f"message sent: {message}")
    except Exception as e:
        print(f"message send error: {e}")

def main():
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    messages = MESSAGES
    if not messages:
        raise ValueError("MESSAGES env variable is not set")
    chosen_message = random.choice(messages)
    send_message(chosen_message)
    print(f"Initial message sent: {chosen_message}")

    if now.hour >= 4:
        wait_seconds = random.randint(3600, 43200)  # between 1 and 12 hours
        next_run_time = now + datetime.timedelta(seconds=wait_seconds)
        next_day_7am = (now + datetime.timedelta(days=1)).replace(hour=7, minute=0, second=0, microsecond=0)
        if next_run_time >= next_day_7am:
            print("Skipping message today, next run will be after 7 AM tomorrow.")
            return
        second_message = random.choice(messages)
        send_message(second_message)
        print("Next message will be sent after", wait_seconds, "seconds.")
    else:
        print("It's before 7 AM JST, skipping additional message.")

if __name__ == "__main__":
    main()
