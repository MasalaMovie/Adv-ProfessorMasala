import random
from pyrogram import Client, filters
import imdb

# Create an instance of the IMDb class
ia = imdb.IMDb()

# Get the top 250 movies
TOP10MV = ia.get_top250_movies()

CMD = ["/", "\."]

@Client.on_message(filters.command("trending", CMD))
async def check_alive(_, message):
    # Display the top 10 movies
    movie_list = "\n".join(movie['title'] for movie in TOP10MV)
    await message.reply_text(f"<b>ᴛᴏᴘ 29 ᴍᴏsᴛ ᴛʀᴇɴᴅɪɴɢ ᴍᴏᴠɪᴇs:\n\n{movie_list}\n\nᴀʟʟ ᴛʜᴇ ʀᴇsᴜʟᴛs sʜᴏᴡɴ ʜᴇʀᴇ ᴀʀᴇ ғʀᴏᴍ ᴛᴏᴘ sᴇᴀʀᴄʜᴇs. ɴᴏᴛ ᴇᴅɪᴛᴇᴅ ʙʏ ᴛʜᴇ ᴀᴅᴍɪɴ</b>")
