from os import environ

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
ADMIN = int(environ.get("ADMIN", ""))          
CAPTION = environ.get("CAPTION", "")

class temp(object):
    THUMBNAIL = environ.get("THUMBNAIL", "")
from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "10247139"

API_HASH = "96b46175824223a33737657ab943fd6a"

BOT_TOKEN = "5222572158:AAENHtTOnhWBh4UUZKTjq5ruMtil_4zRA_0"
