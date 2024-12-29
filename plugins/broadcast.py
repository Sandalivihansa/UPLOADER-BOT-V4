# ©️ Tg @yeah_new | YEAR-NEW | @NT_BOT_CHANNEL

import traceback, datetime, asyncio, string, random, time, os, aiofiles, aiofiles.os
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from plugins.database.database import db
from plugins.config import Config

broadcast_ids = {}


async def send_msg(chat_id, message):
    try:
        await message.copy(chat_id=chat_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(chat_id, message)
    except InputUserDeactivated:
        return 400, f"{chat_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{chat_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{chat_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{chat_id} : {traceback.format_exc()}\n"


@Client.on_message(filters.command('broadcast') & filters.reply)
async def broadcast_(c, m):
    if m.from_user.id != Config.OWNER_ID:
        return

    # Fetch all users from the database
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message

    # Generate a unique broadcast ID
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break

    out = await m.reply_text("You will be notified with a log file when all the chats are notified.")
    start_time = time.time()
    total_users = await db.total_users_count()
    done, failed, success = 0, 0, 0

    broadcast_ids[broadcast_id] = dict(
        total=total_users,
        current=done,
        failed=failed,
        success=success
    )

    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            try:
                chat_id = int(user['id'])
                sts, msg = await send_msg(chat_id, broadcast_msg)
                if msg:
                    await broadcast_log_file.write(msg)

                if sts == 200:
                    success += 1
                else:
                    failed += 1

                if sts == 400:
                    await db.delete_user(user['id'])

            except Exception as e:
                failed += 1
                await broadcast_log_file.write(f"{chat_id} : {traceback.format_exc()}\n")

            done += 1
            if not broadcast_ids.get(broadcast_id):
                break
            broadcast_ids[broadcast_id].update(dict(current=done, failed=failed, success=success))

    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)

    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(5)
    await out.delete()

    if failed == 0:
        await m.reply_text(
            text=f"Broadcast completed in `{completed_in}`\n\nTotal chats: {total_users}.\nSuccess: {success}, Failed: {failed}.",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"Broadcast completed in `{completed_in}`\n\nTotal chats: {total_users}.\nSuccess: {success}, Failed: {failed}.",
            quote=True
        )

    await aiofiles.os.remove('broadcast.txt')
