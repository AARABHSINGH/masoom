import os

API_ID = API_ID = 25434657

API_HASH = os.environ.get("API_HASH", "22cfc54f94cf17360dc1475a51e38518")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7177547553:AAE_kNvhIJyMjhPeaAR0ygj_9_Rk-BP0btM")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6950434272))

LOG = -1002092747701
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6950434272").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


