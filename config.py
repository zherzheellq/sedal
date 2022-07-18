## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu5X4gou9M9LJgx8zU0TJh1GEYW2hEyi_QLu_8sXjiJo511KU4wlWxfMwHxGHTPSW_VW3S5dZokE2kSBPfjo--1MUggAsPaF9UMNIo5XAep2l8bULLGMqTtTjSVTiaRc_qDD3DZm2IYiPIkHooh5dvlkYnQtR05CEwpu-D3u417HZTeRyY62fJ1zAnHa19S25XIyNrW_6vIV3IRKyowFu0bcJ-RQ_TbrsA8aKE57hAxLD5619tK0VrnLbJSeRcCdW-AaNw-tXD16ueAiNYbfF9Ha-ab-UmYo1zS8SqRbKmWZBIGAUHI8Tpwcs0MEYAjZZfj1GowWVW5wv2eSeEp7xf2c=")
BOT_TOKEN = getenv("BOT_TOKEN", "5560311108:AAHRRiNy3YZ9XG1QdQSNRXI3OBoFr0hiZzY")
BOT_NAME = getenv("BOT_NAME", "Meusec")
API_ID = int(getenv("API_ID", "12652221"))
API_HASH = getenv("API_HASH", "296195e8e3ed7849d34d640e9ce940e5")
OWNER_NAME = getenv("OWNER_NAME", "AL Rmethe")
OWNER_USERNAME = getenv("OWNER_USERNAME", "lllllk30")
ALIVE_NAME = getenv("ALIVE_NAME", "AL Rmethe")
BOT_USERNAME = getenv("BOT_USERNAME", "YY_I6bot")
OWNER_ID = getenv("OWNER_ID", "5174719843")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AL Rmethe")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "YY_I2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "YY_I3")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
