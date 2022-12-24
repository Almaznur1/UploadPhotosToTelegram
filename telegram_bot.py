import telegram
import os
from dotenv import load_dotenv


load_dotenv()
token = os.environ['TELEGRAM_BOT_TOKEN']
bot = telegram.Bot(token=token)
bot.send_document(chat_id='-1001874718165', document=open('images/spacex_1.jpg', 'rb'))
bot.send_message(chat_id='-1001874718165', text="I'm sorry Dave I'm afraid I can't do that.")