import telegram
import os
from dotenv import load_dotenv


load_dotenv()
token = os.environ['TELEGRAM_BOT_TOKEN']
bot = telegram.Bot(token=token)
print(bot.get_me())
bot.send_message(chat_id='@AlmazNuriakhmetov', text="I'm sorry Dave I'm afraid I can't do that.")
# bot.send_message(chat_id='-1001874718165', text="I'm sorry Dave I'm afraid I can't do that.")