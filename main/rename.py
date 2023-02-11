import time
import os
from pyrogram import Client, filters, enums
from config import temp, CAPTION, ADMIN
from main.utils import progress_message, humanbytes

@Client.on_message(filters.private & filters.document & filters.user(ADMIN))             
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    cos = msg.id
    new_namex = "hello"
    sts = await msg.reply_text("Trying to Downloading.....")
    c_time = time.time()
    downloaded = await msg.download(progress=progress_message, progress_args=("Download Started.....", sts, c_time))                 
    file_name = downloaded.file.name
    if CAPTION:
        try:
            cap = CAPTION.format(file_name=file_name)
        except Exception as e:            
            await sts.edit(text=f"Your caption Error unexpected keyword ●> ({e})")
            return
    else:
        cap = f"{new_namex}"
    await sts.edit("Trying to Uploading")
    c_time = time.time()
    try:
        await bot.send_document(msg.chat.id, document=downloaded, file_name=file_name, caption=cap, progress=progress_message, progress_args=("Uploade Started.....", sts, c_time))        
    except Exception as e:  
        await sts.edit(f"Error {e}") 
        return               
    try:
        os.remove(downloaded)
    except:
        pass
    await sts.delete()
