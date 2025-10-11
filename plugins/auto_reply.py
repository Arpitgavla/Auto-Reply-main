import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_GRP

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

lock = asyncio.Lock()

# Changed line below 👇
@Client.on_message(~filters.bot)
async def auto_reply(bot, message):
    try:
        reply = await message.reply_text(
            '''Yₒᵤᵣ ₘₒᵥᵢₑ ᵢₛ ᵢₙ ₘy ₚᵣₒfᵢₗₑ ₚₗₑₐₛₑ Cₕₑcₖ ₘy Bᵢₒ''',
            reply_to_message_id=message.id
        )
        await asyncio.sleep(60)
        try:
            await asyncio.sleep(10)
            await reply.delete()
        except:
            pass
    except FloodWait as e:
        logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
        await asyncio.sleep(e.value + 2)
        logger.info("Floodwait ended")
