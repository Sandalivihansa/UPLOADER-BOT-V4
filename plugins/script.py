from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import RPCError
import asyncio

class Translation:
    START_TEXT = """
    👋 Hᴇʏ {} 

    ⵊ Aᴍ Tᴇʟᴇɢʀᴀᴍ URL Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ.

    **Sᴇɴᴅ ᴍᴇ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴀɴᴅ ɪ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀs ᴀ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ**

    Usᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ
    """
    # Image link to display in the start message
    START_IMAGE = "https://telegra.ph/file/ee7d75a552dd22796807f.jpg"
    
    HELP_TEXT = """
    ʟɪɴᴋ ᴛᴏ ᴍᴇᴅɪᴀ ᴏʀ ꜰɪʟᴇ

    ➠ sᴇɴᴅ ᴀ ʟɪɴᴋ ꜰᴏʀ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ.

    sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ

    ➠ sᴇɴᴅ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴀs ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

    ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴜᴍʙɴᴀɪʟ

    ➠ sᴇɴᴅ /delthumb ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴜᴍʙɴᴀɪʟ.

    sᴇᴛᴛɪɴɢs

    ➠ ᴄᴏɴғɪɢᴜʀᴇ ᴍʏ sᴇᴛᴛɪɴɢs ᴛᴏ ᴄʜᴀɴɢᴇ ᴜᴘʟᴏᴀᴅ ᴍᴏᴅᴇ

    sʜᴏᴡ ᴛʜᴜᴍʙɴᴀɪʟ

    ➠ sᴇɴᴅ /showthumb ᴛᴏ ᴠɪᴇᴡ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ.
    """

    ABOUT_TEXT = """
    **Mʏ ɴᴀᴍᴇ** : [𝐸𝑙𝑖𝑧𝑎𝑏𝑒𝑡𝒽](https://t.me/ElizabethTGram_bot)

    **Cʜᴀɴɴᴇʟ** : [𝑆𝐿 𝑀𝑢𝑆𝑖𝑐](https://t.me/MusicOFHuB)

    **Sᴏᴜʀᴄᴇ** : [𝐶𝑙𝑖𝑐𝑘 𝐻𝑒𝑟𝑒](https://t.me/AboutDeWeNi/7)

    **Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ** : [𝑆𝐿 𝑀𝑢𝑆𝑖𝑐 𝑀𝑎𝑁𝑖𝑎](https://t.me/NT_BOTS_SUPPORT)

    **Dᴀᴛᴀʙᴀsᴇ** : [𝑀𝑜𝑁𝐺𝑜 𝐷𝐵](https://cloud.mongodb.com)

    **Lᴀɴɢᴜᴀɢᴇ :** [𝑃𝑦𝑡𝒉𝑜𝑛 3.12.4](https://www.python.org/)

    **Fʀᴀᴍᴇᴡᴏʀᴋ :** [𝑃𝑦𝑟𝑜𝑔𝑟𝑎𝑚 2.3.45](https://docs.pyrogram.org/)

    **Dᴇᴠᴇʟᴏᴘᴇʀ :** [𝐷𝑒𝑊𝑒𝑁𝑖🇱🇰](https://t.me/deweni2)
    """

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('⚙️ sᴇᴛᴛɪɴɢs', callback_data='OpenSettings')
        ], [
            InlineKeyboardButton('❔ ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('👨‍🚒 ᴀʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('⛔️ ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )

@app.on_message(filters.command("start"))
async def start(client, message):
    try:
        # Send image and text together
        await message.reply_photo(
            photo=Translation.START_IMAGE,
            caption=Translation.START_TEXT.format(message.from_user.first_name),
            reply_markup=Translation.START_BUTTONS
        )
    except Exception as e:
        await message.reply(f"Something went wrong: {str(e)}")

# Run the bot
app.run()
