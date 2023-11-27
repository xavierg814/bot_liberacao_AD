# arquivo de conexão do AD 
import os
from ldap3 import Connection
from dotenv import load_dotenv

load_dotenv()

AD_SERVER = ""
AD_USERNAME = ""
AD_PASSWORD = ""
TELEGRAM_BOT_TOKEN = "6479101603:AAHb4q4Sc6o_dBjaUVxeOzBISvz_zqmzwX4"
con=Connection(AD_SERVER,AD_USERNAME,AD_PASSWORD, auto_bind=True)
print(con)