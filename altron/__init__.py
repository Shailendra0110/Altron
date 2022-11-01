# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅


from config import *
import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = API_ID
API_HASH = API_HASH
SUDO_USERS = SUDO_USERS
OWNER_ID = OWNER_ID
ALIVE_PIC = ALIVE_PIC

STRING1 = STRING1
STRING2 = STRING2
STRING3 = STRING3
STRING4 = STRING4
STRING5 = STRING5 
STRING6 = STRING6
STRING7 = STRING7
STRING8 = STRING8
STRING9 = STRING9
STRING10 = STRING10

if ALIVE_PIC:
    ALIVE_PIC = ALIVE_PIC
else: 
    ALIVE_PIC = "https://telegra.ph/file/a9b56319322553da4b240.jpg"

if not STRING1:
    logging.error("No STRING Found")
    quit(1)

if not API_ID:
    logging.error("No API_ID Found")
    quit(1)

if not API_HASH:
    logging.error("No API_HASH Found")
    quit(1)


if STRING1:
    print("[INFO] STRING1 Found") 
    alt1 = Client(STRING1, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt1 = None

if STRING2:
    print("[INFO] STRING2 Found") 
    alt2 = Client(STRING2, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt2 = None


if STRING3:
    print("[INFO] STRING3 Found") 
    alt3 = Client(STRING3, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt3 = None

if STRING4:
    print("[INFO] STRING4 Found") 
    alt4 = Client(STRING4, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt4 = None

if STRING5:
    print("[INFO] STRING5 Found") 
    alt5 = Client(STRING5, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt5 = None

if STRING6:
    print("[INFO] STRING6 Found") 
    alt6 = Client(STRING6, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt6 = None

if STRING7:
    print("[INFO] STRING7 Found") 
    alt7 = Client(STRING7, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt7 = None

if STRING8:
    print("[INFO] STRING8 Found") 
    alt8 = Client(STRING8, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt8 = None

if STRING9:
    print("[INFO] STRING9 Found") 
    alt9 = Client(STRING9, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt9 = None

if STRING10:
    print("[INFO] STRING10 Found") 
    alt10 = Client(STRING10, API_ID, API_HASH, plugins=dict(root=f"altron"))
else:
    alt10 = None



scheduler = AsyncIOScheduler()
START_TIME = datetime.now()
