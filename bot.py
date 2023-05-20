import asyncio
import re
from pyrogram import Client, filters, idle
from config import *
from uvloop import install
from contextlib import closing, suppress
from pyrogram.types import Message, MessageEntity
from string import ascii_letters, ascii_uppercase, digits
from base64 import standard_b64encode, standard_b64decode
app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )
app.start()

loop = asyncio.get_event_loop()
def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode('ascii')
    bytes_str = standard_b64decode(bytes_b64)
    __str = bytes_str.decode('ascii')
    return __str
def str_to_b64(__str: str) -> str:

    str_bytes = __str.encode('ascii')

    bytes_b64 = standard_b64encode(str_bytes)

    b64 = bytes_b64.decode('ascii')

    return b64

@app.on_message(filters.command("start") & filters.private)
async def start(bot, cmd: Message):
    usr_cmd = cmd.text.split("_", 1)[-1]
    kay_id = -1001642923224
    if usr_cmd == "/start":
       await cmd.reply_text("Bot seems online! ⚡️")
    else:
        try:
            try:
                file_id = int(b64_to_str(usr_cmd).split("_")[-1])
            except (Error, UnicodeDecodeError):
                file_id = int(usr_cmd.split("_")[-1])
            GetMessage = await app.get_messages(kay_id, message_ids=file_id)
            message_ids = GetMessage.message_id
            await app.copy_message(chat_id=cmd.from_user.id, from_chat_id=kay_id, message_id=message_ids)
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `XXXXXXX`")
            
            
@app.on_message(filters.command("link") & filters.private)

async def link(bot, cmd: Message):
    usr_cmd = cmd.text.split("_", 1)[-1]
    if usr_cmd == "/link":

       await cmd.reply_text("Fuck off!")

    else: 
        try:

       
            fuk_cmd = cmd.text.replace("/link https://t.me/c/1642923224/", "")
            filex_id = str_to_b64(fuk_cmd)
            sendx = await app.send_message(chat_id=cmd.from_user.id, text="https://t.me/somayukibot?start=animxt_" + filex_id)
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `XXXXXXX`")

    
    
async def start_bot():
  print("==================================")
  print("[INFO]: AutoAnimeBot Started Bot Successfully")
  print("==========JOIN @Latest_ongoing_airing_animes=========")
  
  await idle()
  print("[INFO]: BOT STOPPED")
  await app.stop()  
  for task in asyncio.all_tasks():
    task.cancel()

if __name__ == "__main__":
  install()
  with closing(loop):
    with suppress(asyncio.exceptions.CancelledError):
      loop.run_until_complete(start_bot())
      loop.run_until_complete(asyncio.sleep(3.0))
