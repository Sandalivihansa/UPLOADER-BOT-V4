from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import RPCError

class Translation:
    START_TEXT = """
👋 Hᴇʏ {} 

ⵊ Aᴍ Tᴇʟᴇɢʀᴀᴍ URL Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ.

**Sᴇɴᴅ ᴍᴇ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴀɴᴅ ɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀs ᴀ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ**

Usᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ
"""
    START_IMAGE = "https://telegra.ph/file/ee7d75a552dd22796807f.jpg"
    
    HELP_TEXT = """
ʟɪɴᴋ ᴛᴏ ᴍᴇᴅɪᴀ ᴏʀ ꜰɪʟᴇ

➠ sᴇɴᴅ ᴀ ʟɪɴᴋ ꜰᴏʀ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ.

sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴀs ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ

➠ sᴇɴᴅ /delthumb ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ.
"""
    
    ABOUT_TEXT = """
**Mʏ ɴᴀᴍᴇ** : [𝐸𝑙𝑖𝑧𝑎𝑏𝑒𝑡𝒽](https://t.me/ElizabethTGram_bot)

**Cʜᴀɴɴᴇʟ** : [𝑆𝐿 𝑀𝑢𝑆𝑖𝑐](https://t.me/MusicOFHuB)

**Sᴏᴜʀᴄᴇ** : [𝐶𝑙𝑖𝑐𝑘 𝐻𝑒𝑟𝑒](https://t.me/AboutDeWeNi/7)

**Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ** : [𝑆𝐿 𝑀𝑢𝑆𝑖𝑐 𝑀𝑎𝑁𝑖𝑎](https://t.me/NT_BOTS_SUPPORT)
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙️ sᴇᴛᴛɪɴɢs', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('❔ ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('👨‍🚒 ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 ʜᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('👨‍🚒 ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )

# Initialize the Pyrogram Client
app = Client("my_bot")  # Define the app instance first

@app.on_message(filters.command("start"))
async def start(client, message):
    try:
        # Send image and text together
        await message.reply_photo(
            photo=Translation.START_IMAGE,
            caption=Translation.START_TEXT.format(message.from_user.first_name),
            reply_markup=Translation.START_BUTTONS
        )
    except RPCError as e:
        print(f"An error occurred: {e}")

@app.on_message(filters.command("help"))
async def help(client, message):
    try:
        await message.reply_text(
            Translation.HELP_TEXT,
            reply_markup=Translation.HELP_BUTTONS
        )
    except RPCError as e:
        print(f"An error occurred: {e}")

@app.on_message(filters.command("about"))
async def about(client, message):
    try:
        await message.reply_text(
            Translation.ABOUT_TEXT,
            reply_markup=Translation.HELP_BUTTONS
        )
    except RPCError as e:
        print(f"An error occurred: {e}")

@app.on_callback_query()
async def button(client, callback_query):
    try:
        if callback_query.data == 'help':
            await callback_query.message.edit_text(
                Translation.HELP_TEXT,
                reply_markup=Translation.HELP_BUTTONS
            )
        elif callback_query.data == 'about':
            await callback_query.message.edit_text(
                Translation.ABOUT_TEXT,
                reply_markup=Translation.HELP_BUTTONS
            )
        elif callback_query.data == 'close':
            await callback_query.message.delete()
    except RPCError as e:
        print(f"An error occurred: {e}")

# Use an asynchronous function to start the bot in environments with an active event loop
async def main():
    await app.start()  # Use app.start() instead of app.run()
    print("Bot is now running...")
    await app.idle()  # Keeps the bot running until it is manually stopped

# If running in a script, ensure you start the bot with an asyncio event loop
import asyncio
asyncio.run(main())
