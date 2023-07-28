from os import environ

from dotenv import load_dotenv



load_dotenv()


TOKEN = environ.get("TOKEN")
PG_URL = environ.get("PG_URL")


AUTH_BOT_LINK = "https://api.telegram.org/bot{token}/getMe"


