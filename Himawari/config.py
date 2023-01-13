"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f'{os.getcwd()}/Himawari/{config}', 'r') as json_file:
        return json.load(json_file)[key]

class Config(object):

    ##dont change
    LOGGER=True
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY="./"
    DEL_CMDS=False
    BAN_STICKER="kans" 
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="Himawari"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"

    #you can change these 
    INFOPIC=True #picture while doing /info
    STRICT_GBAN=True
    API_ID=21927988 ##api id from my.telegram.org
    APP_ID=21927988 #same as API_ID
    API_HASH="e18f720acdff1e5b0ec80616aecd8a5a" ##api hash from my.telegram.org
    APP_HASH="e18f720acdff1e5b0ec80616aecd8a5a" #same as API_HASH
    BL_CHATS=[1] #chats to be blacklisted
    MONGO_DB_URL="mongodb+srv://plumblossmsword:ndXbDlCy7Zn71beD@komi.yg1o2ub.mongodb.net/?retryWrites=true&w=majority" ##mongo database link (necessary)
    DB_URL2="mongodb+srv://plumblossomsword:Qn57AqxG3GRIu9IP@komi.zc6e9si.mongodb.net/?retryWrites=true&w=majority" #mongo db (not necessary)
    DB_URL="postgresql://plumblossomsword:YOHMSYTKcjYLaqioWlyCDRrJZSkSmvQ3@dpg-cevf5782i3mntl1sh6q0-a.frankfurt-postgres.render.com/telegram_postgresql" #postgres sql database link
    REDIS_URL="rediss://red-cf0rlmirrk05t6t5p3qg:RniRsIOnT6UPiAxVD2QcdaIkwRj7RUye@frankfurt-redis.render.com:6379" #redis database url from redislabs.com
    TOKEN="5932946559:AAHY4nAVk_wRxhgslfeTi-53zn28cLhLJew" #bot token from @BotFather
    DEV_USERS=[2064735436] #developers id
    DRAGONS=[] #sudo users id
    DEMONS=[] #support user ids
    TIGERS=[] #commas for multiple ids
    WOLVES=[] #commas for multiple ids 
    DONATION_LINK="https://t.me/plumblossomsword" #u can change with yours
    EVENT_LOGS=-1001859171071 #channel id for gban logs
    JOIN_LOGGER=-1001859171071  #log channel/group id
    OWNER_ID=2064735436 #owner id in integer
    ERROR_LOGS=-1001859171071 #support group id
    BOT_ID =5932946559 #id of bot in integer value
    BOT_NAME="Shouko" #your bot name
    ARQ_API_KEY="QOYIDT-TJPPDA-JVVIZH-BTHMBB-ARQ" #ARQ api key from @ARQRobot
    ARQ_API_URL="arq.hamker.dev" #arq link
    SUPPORT_CHAT="theoneandonlymurim" #support group username without @
    OWNER_USERNAME="plumblossomsword" #owner username without @
    UPDATES_CHANNEL="rimurubotsnetwork" #Updates/News Channel username without @
    BOT_USERNAME="ShoukoX_Bot" #bot username without @
    REM_BG_API_KEY="K2dsdsYma6cZx" #not necessary
    GENIUS_API_TOKEN="e-8UdRQNrIssPyM" # api token from genius.com (not necessary)
    TIME_API_KEY="4ID9HHBVU5L8" #not necessary
    SPAMWATCH_API="zKSTO8g_x3qmaMrU_tiTRXibTb532qbmTKXYW3RdyW8Pq0qk1oEtqddo7HqxRp~1" #spamwatch api token from @SpamWatchBot
    WALL_API="6950f5ds6a3" #wall api (not necessary)
    CASH_API_KEY="6HZ09C7DZYKWBCCE"
    OPENWEATHERMAP_ID="687af7aaae4f454314ca54bfd8cddceb"
    
    
class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
