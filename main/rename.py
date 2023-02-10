import time
import os
from pyrogram import Client, filters, enums
from config import temp, CAPTION, ADMIN
from main.utils import progress_message, humanbytes

@Client.on_message(filters.private & filters.command("rename") & filters.user(ADMIN))             
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    media = msg.document or msg.audio or msg.video
    og_media = getattr(reply, reply.media.value)
    new_name = "hell.mkv"
    new_namex = new_name.replace(".mkv", "")
    sts = await media.reply_text("Trying to Downloading.....")
    c_time = time.time()
    downloaded = media.download(file_name=new_name, progress=progress_message, progress_args=("Download Started.....", sts, c_time)) 
    filesize = humanbytes(og_media.file_size)                
    if CAPTION:
        try:
            cap = CAPTION.format(file_name=new_name, file_size=filesize)
        except Exception as e:            
            await sts.edit(text=f"Your caption Error unexpected keyword ●> ({e})")
            return
    else:
        cap = f"{new_namex}"
    await sts.edit("Trying to Uploading")
    c_time = time.time()
    try:
        await bot.send_document(msg.chat.id, document=downloaded, caption=cap, progress=progress_message, progress_args=("Uploade Started.....", sts, c_time))        
    except Exception as e:  
        await sts.edit(f"Error {e}") 
        return               
    try:
        os.remove(downloaded)
        os.remove(og_thumbnail)
    except:
        pass
    await sts.delete()
