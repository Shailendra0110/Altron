import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID")) 

API_HASH = getenv("API_HASH") 

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

OWNER_ID = int(getenv("OWNER_ID")) 

OWNER_USERNAME = getenv("OWNER_USERNAME")

ALIVE_PIC = getenv("ALIVE_PIC") 


STRING1 = getenv("STRING1", None) 

STRING2 = getenv("STRING2", None) 

STRING3 = getenv("STRING3", None) 

STRING4 = getenv("STRING4", None) 

STRING5 = getenv("STRING5", None) 

STRING6 = getenv("STRING6", None) 

STRING7 = getenv("STRING7", None) 

STRING8 = getenv("STRING8", None) 

STRING9 = getenv("STRING9", None) 

STRING10 = getenv("STRING10", None) 
