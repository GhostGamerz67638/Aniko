import dotenv
import logging
from os import getenv
dotenv.load_dotenv()



class BaseConfig(object):
    BOT_TOKEN = getenv("BOT_TOKEN", "8267726453:AAGaMshUPP1AEkJUUFeI4u1uFsB7WjLEzco")
    OWNER_ID = int(getenv("OWNER_ID", 1207066133))
    API_ID = int(getenv("API_ID", "32461689"))
    API_HASH = getenv("API_HASH", "1049552a00c9134e1c93e6580289261e
")
    LOG_CHAT_ID = int(getenv("LOG_CHAT_ID", "-1001482059289"))
    LOG_LEVEL = getenv("LOG_LEVEL") or "INFO"
    CHNL_NAME = getenv("UPDATES_CHANNEL", "bots_universe")
    STRT_IMG = getenv("ALIVE_IMG", "https://c.tenor.com/uCVosr0dhnQAAAAC/anime-hello.gif")
