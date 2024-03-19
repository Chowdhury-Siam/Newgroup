import json
import os


def get_user_list(config, key):
    with open("{}/EnmuBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    TEMP_DOWNLOAD_DIRECTORY = "/tmp"
    API_ID = 28986163  
    API_HASH = "07225d0de9bee70666517315d2174171"
    ARQ_API = "SLFPTV-GTODAB-OBSWXL-IDKRKC-ARQ"
    TOKEN = "7033370307:AAHiO5Wnk18cUXUjgAykvDUkcqKzbZ2JcEM"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    BOT_ID = 7033370307
    OWNER_ID = 5971676967  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Chowdhury_Siam"
    SUPPORT_CHAT = "AnimeKunChannel"  # Your own group for support, do not add the @
    BOT_USERNAME = "AnimeKunChannel_Bot"
    JOIN_LOGGER = (
        -1001999743881
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001999743881
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOGS = (
        -1001999743881
    )  # Prints information Error
    REDIS_URL = ""
    MONGO_DB_URI = "mongodb+srv://GPN:lUAID1xlk9Yo9ykY@gpnyt.vghzopa.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = ""  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = "-QcoQXCAXyhAxeLN2eD86LeFa"
    OPENWEATHERMAP_ID = "887da2c60d9f13fe78b0f9d0c5cbaade"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
