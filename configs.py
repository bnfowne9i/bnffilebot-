import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "24782172"))
  API_HASH = os.environ.get("API_HASH", "ec1ef9cce1c4d852365e55e3139b72d8")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8095299226:AAGhMq1eSF6yDydQwfgAaCzeE53BHe7Gu44")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "@FileTo_LinkBot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002299322267"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "mdisk.pro")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "8df317bff1977ef01061b3c3b31fde785f4811e5")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6434831584"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://bharathkalladi38:4TDnaR1dZqAEshQq@cluster0.ps5ucul.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002478941535")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002250961481"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1002389880858").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/FileTo_LinkBot)
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/TK_Mob_TY)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Tamil_Mob_TY)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
