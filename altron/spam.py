# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅


import os
from typing import Union, List
import sys
from data import *
import asyncio
import random
from random import choice
from sys import version_info
from pyrogram import __version__ as __pyro_version__
from time import time
from config import *
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import re
from datetime import datetime


LOGGER = [-1001864840905]

# JOIN COMMAND  

@Client.on_message(filters.command(["join"], ["/", "!", "."]) & filters.user(SUDO_USERS))
async def join(client: Client, message: Message):
    op = message.text[6:]
    count = 0
    if not op:
        return await message.reply_text("`Need a chat username or invite link to join.`")
    if op.isnumeric():
        return await message.reply_text("`Can't join a chat with chat id. Give username or invite link.`")
    try:
        await client.join_chat(op)
        await message.reply_text(f"**Joined**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
  
         
# LEAVE COMMAND         
    
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["leave", "remove"], [".", "!", "/"]))
async def leave(pam: Client, e: Message):
    hero = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    if len(e.text) > 7:
        chat = hero[0]
        try:
           await pam.leave_chat(chat)
           await e.reply_text("**Left Successfully ✅**")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
    else:
        chat = e.chat.id
        ok = e.from_user.id
        if int(chat) == int(ok):
            return await e.reply_text(f"Usage: !leave <chat username or id> or !leave [type in Group for Direct leave]")
        if int(chat) == -1001777776331:
              return e.reply_text("**Error**")
        try:
           await pam.leave_chat(chat)
           await e.reply_text("**Left Successfully ✅ **")
        except Exception as ex:
           await e.reply_text(f"**ERROR:** \n\n{str(ex)}")
   

# MEMBERS ADDING

@Client.on_message(filters.command(["addall", "inviteall"], ["/", "!", "."]) & filters.user(SUDO_USERS))
async def inviteall(client: Client, message: Message):
    op = await message.reply_text("`Processing...`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await op.edit_text(f"`Adding Members From` **{chat.username}**")
    
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        kal= ["online", "recently"]
        if user.status in kal:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            print(e)
            pass
        
# ALIVE MESSAGE

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], [".", "!", "/"]))
async def alive(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))   
    reply_msg = f"**🔥 ᴀʟᴛʀᴏɴ ᴏɴ ғɪʀᴇ 🔥**\n"
    reply_msg += f"═══════════════════\n"
    reply_msg += f"🔸 **ᴘʏᴛʜᴏɴ**: `{__python_version__}`\n"
    reply_msg += f"🔹 **ᴘɪɴɢ **: `{delta_ping * 1000:.3f}ms`\n"
    reply_msg += f"🔸 **ᴄʀᴇᴀᴛᴏʀ**: `{OWNER_USERNAME}`\n"
    reply_msg += f"🔹 **ᴘʏʀᴏɢʀᴀᴍ**: `{__pyro_version__}`\n"    
    reply_msg += f"🔸 **ᴜᴘᴛɪᴍᴇ**: `{uptime}`\n"
    reply_msg += f"═══════════════════\n\n"
    reply_msg += f"**ᴊᴏɪɴ** @TheAltron **ғᴏʀ ʜᴇʟᴘ**\n"
    await m.delete()
    await m.reply_text(reply_msg)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], [".", "/", "!"]))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.reply_text("`Checking...`")
   delta_ping = time() - start
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m.delete() 
   await m_reply.edit(f"═══════════════════\n   **ᴀʟᴛʀᴏɴ sᴘᴀᴍ ᴜsᴇʀʙᴏᴛ**   \n═══════════════════\n\n🇵 🇮 🇳 🇬 : `{delta_ping * 1000:.3f}ms`")
   
# HANG FEATURE

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["hang", "hng"], [".", "!", "/"]))
async def statspam(client: Client, message: Message):
    await message.delete()
    hang_text = f"😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟"
    sex = await client.send_message(message.chat.id, hang_text)       
    await asyncio.sleep(0.50)
    
# RAIDING FEATURES

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], ["/", "!", "."]))
async def raid(pam: Client, e: Message):  
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Hero) == 2:
          counts = int(Hero[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await pam.get_users(Hero[1])
          id = ok.id
          if int(id) in OWNERS:
                text = f"I can't raid on ALTRON's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of the Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await pam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.3)
      elif e.reply_to_message:
          counts = int(Hero[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          user_id = e.reply_to_message.from_user.id
          ok = await pam.get_users(user_id)
          id = ok.id
          if int(id) in OWNERS:
                text = f"I can't raid on ALTRON's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of the Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await pam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.3)
      else:
          await e.reply_text("`Wrong Usage`")


RUSERs = []

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], ["/", ".", "!"]))
async def rraid(pam: Client, e: Message):
      global RUSERs
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
      if Hero:
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await pam.get_users(Hero[0])
          id = ok.id
          if int(id) in OWNERS:
                text = f"I can't raid on ALTRON's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              RUSERs.append(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = f"Reply Raid Activated Successfully On User {mention}"
              await e.reply_text(msg)
      elif e.reply_to_message:
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          user_id = e.reply_to_message.from_user.id
          ok = await pam.get_users(user_id)
          id = ok.id
          if int(id) in OWNERS:
                text = f"I can't raid on ALTRON's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              RUSERs.append(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = f"Reply Raid Activated Successfully On User {mention}"
              await e.reply_text(msg)
      else:
          await e.reply_text("`Wrong Usage`")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["drraid", "draid", "dreplyraid"], ["/", ".", "!"]))
async def draid(pam: Client, e: Message):
      global RUSERs
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if Hero:
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await pam.get_users(Hero[0])
          id = ok.id
          if int(id) in OWNERS:
                text = f"I can't raid on ALTRON's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              RUSERs.remove(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = "Reply Raid Deactivated Successfully"
              await e.reply_text(msg)
      elif e.reply_to_message:
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          user_id = e.reply_to_message.from_user.id
          ok = await pam.get_users(user_id)
          id = ok.id
          if int(id) in OWNERS:
                text = f"I can't raid on ALTRON's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              RUSERs.remove(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = "Reply Raid Deactivated Successfully"
              await e.reply_text(msg)
      else:
          await e.reply_text("`Wrong Usage`")
    

@Client.on_message( ~filters.me & filters.incoming)
async def watcher(_, msg: Message):
    global RUSERs
    id = msg.from_user.id
    if int(id) in RUSERs:
       reply = choice(RAID)
       await msg.reply_text(reply)
       
# REBOOT FEATURE

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart", "stop"], ["/", "!", "."]))
async def restart(client, m: Message):
    reply = await m.reply_text("`Restarting....`")     
    await m.delete() 
    await reply.edit(
        "<b>Reboot has been initiated successfully Wait for 1-2 minutes.</b>"
    )
    os.system(f"kill -9 {os.getpid()} && python3 main.py")
   
# ADDING SUDO

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["addsudo", "addrandi"], ["/", ".", "!"]))
async def aid(pam: Client, e: Message):
      global SUDO_USERS
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
      if Hero:
          ok = await pam.get_users(Hero[0])
          id = ok.id
          if int(id) == OWNER_ID:
                text = f"This Guy Is My Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This Guy Is Already A Sudo User"
                await e.reply_text(text)
          else:
              fname = ok.first_name
              SUDO_USERS.append(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = f"**{mention} Is Now My Sudo User** "
              await e.reply_text(msg)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await pam.get_users(user_id)
          id = ok.id
          if int(id) == OWNER_ID:
                text = f"This Guy Is My Owner"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This Guy Is Already A Sudo User"
                await e.reply_text(text)
          else:
              fname = ok.first_name
              SUDO_USERS.append(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = f"**{mention} Is Now My Sudo User** "
              await e.reply_text(msg)
      else:
          await e.reply_text("`Wrong Usage`")
       
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dsudo", "delsudo", "deletesudo"], ["/", ".", "!"]))
async def draid(pam: Client, e: Message):
      global SUDO_USERS
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if Hero:
          ok = await pam.get_users(Hero[0])
          id = ok.id
          if int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif not int(id) in SUDO_USERS:
                text = f"This guy is not a sudo user"
                await e.reply_text(text)
          else:
              fname = ok.first_name
              SUDO_USERS.remove(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = "Sudo Deleted Successfully On {mention}"
              await e.reply_text(msg)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await pam.get_users(user_id)
          id = ok.id
          if int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif not int(id) in SUDO_USERS:
                text = f"This guy is not a sudo user."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              SUDO_USERS.remove(id)
              mention = f"[{fname}](tg://user?id={id})"
              msg = "Sudo Deleted Successfully On {mention}"
              await e.reply_text(msg)
      else:
          await e.reply_text("`Wrong Usage`")


# HIGH LEVEL COMMAND


other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded

def commandpro(commands: Union[str, List[str]]):
    return filters.command(commands,"")
    

@Client.on_message(commandpro(["op", "nice", "cute", "hot", "!save", "x", "kid"]) & filters.me)
async def downloader(client: Client, message: Message):
    targetcontent = message.reply_to_message
    load = await client.download_media(targetcontent)
    send = await client.send_document("me", load)
    if LOGGER:
       try:
            await client.send_document(LOGGER, load)
       except Exception as a:
         print(a)
         pass        
    os.remove(load)

# DM RAID

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], ["/", "!", "."]))
async def dmraid(pam: Client, e: Message):
      """ Module: Dm Raid """
      Hero = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Hero) == 2:
          ok = await pam.get_users(Hero[1])
          id = ok.id
          if int(id) in OWNERS:
                text = f"I can't raid on ALTRON's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is The Owner Of these Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is sudo user."
                await e.reply_text(text)
          else:
              counts = int(Hero[0])
              await e.reply_text("⚜️ Dm Raid Started Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await pam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await pam.get_users(user_id)
          id = ok.id
          if int(id) in OWNERS:
                text = f"I can't raid on @ALTRON's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is The Owner Of these Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is sudo user."
                await e.reply_text(text)
          else:
              counts = int(Hero[0])
              await e.reply_text("⚜️ Dm Raid Started Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await pam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await pam.reply_text("`Wrong Usage`")
             
             
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["spam", "fspam", "fastspam"], [".", "!", "/"]))
async def fastspam(client: Client, message: Message):
    sex  = await message.reply_text("⚡ Usage:\n /fastspam 10 LODA ")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if int(message.chat.id) in GROUP:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.001)
        return
    
    for _ in range(quantity):
        await sex .delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.001)


#SLOWSPAM HANDLER
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dspam", "slowspam"], [".", "!", "/"]))
async def slowspam(client: Client, message: Message):
    sex = await message.reply_text("⚡ Usage:\n /slowspam 10 LODA ")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if int(message.chat.id) in GROUP:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(1)
        return

    for _ in range(quantity):
        await sex.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(1)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return

    if int(message.chat.id) in GROUP:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if message.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)
                
             
WORD = ["AJA", "TERI", "MAA", "KI", "CHUT", "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP", "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA", "MADARCHOD", "AAGYA", "TERI", "MAA ", "CHODNE", "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE", "ME", "TEAM ALTRON", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI", "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE", "BOOBS", "DABAUNGA", "XXX", "TERI", "MAA", "KAA", "CHUT", "MARU", "RANDI", "KEE", "PILLE", "TERI", "MAA", "KAA", "BHOSDAA", "MARU", "SUAR", "KEE", "CHODE", "TERI", "MAAA", "KEEE", "NUDES", "BECHUNGA", "RANDI", "KEE", "PILLE", "TERI", "MAAA", "CHODU", "SUAR", "KEEE", "PILLE", "TERIII", "MAAA", "DAILYY", "CHUDTTI", "HAII", "MADHARCHOD", "AUKAT", "BANAA", "LODE", "TERAA", "BAAP", "HUU", "TERI", "GFF", "KAA", "BHOSDAA", "MARUU", "MADARCHOD", "TERI", "NANI", "KIII", "CHUTT", "MARU", "TERII", "BEHEN", "KAAA", "BHOSDAA", "MARU", "RANDII", "KEEE", "CHODE", "TERI", "DADI", "KAAA", "BOOR", "GARAM", "KARR", "TERE", "PUREE", "KHANDAN", "KOOO", "CHODUNGAA", "BAAP", "SEE", "BAKCHODI", "KAREGAA", "SUARR", "KEEE", "PILLEE", "BETAA", "CHUSS", "LEEE", "MERAA", "LODAA", "JAISE", "AALU", "KAAA", "PAKODAA", "TERI", "MAAA", "BEHEN", "GFF", "NANI", "DIN", "RAAT", "SOTEE", "JAGTEE", "PELTAA", "HUUU", "LODEE", "CHAAR", "CHAWNII", "GHODEE", "PEEE", "TUMM", "MEREE", "LODEE", "PEE", "TERI", "MAA", "KAAA", "BOOBS", "DABATA HU"]

             
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["oword", "ospam", "uspam", "abuse"], ["/", ".", "!"]))
@Client.on_message(filters.me & filters.command(["oword", "ospam", "uspam", "abuse"], ["/", ".", "!"]))
async def abuse(am: Client, e: Message): 
     sex = e.text[7:]
     if sex:
          counts = int(sex)
          if int(e.chat.id) in GROUP:
              return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          for _ in range(counts):
              msg = choice(WORD)
              await am.send_message(e.chat.id, msg)
              await asyncio.sleep(0.2)
     else:
          global infinite
          infinite = True
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          try:
             while infinite == True:
                 msg = choice(WORD)
                 await am.send_message(e.chat.id, msg)
          except Exception as ex:
              print(ex)
              await e.reply_text(f" Error -! \n\n {ex}")
             
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["pspam", "pornspam"], ["/", ".", "!"]))
@Client.on_message(filters.me & filters.command(["pspam", "pornspam"], ["/", ".", "!"]))
async def pornspam(am: Client, e: Message): 
    xx = e.text[9:]
    if xx:
       counts = int(xx)
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       hero = "**#𝙿𝚘𝚛𝚗𝚜𝚙𝚊𝚖**"
       count = int(counts)
       for _ in range(count):
           prn = choice(PORM)
           if ".jpg" in prn or ".png" in prn:
              await am.send_photo(e.chat.id, prn, caption=hero)
              await asyncio.sleep(0.4)
           if ".mp4" in prn or ".MP4," in prn:
              await am.send_video(e.chat.id, prn, caption=hero)
              await asyncio.sleep(0.4)
    else:
         await e.reply_text("`Wrong Usage Of Command`")             
         
