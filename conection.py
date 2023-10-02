# arquivo de conexão do AD 

from ldap3 import Connection

AD_SERVER = ""
AD_USERNAME = ""
AD_PASSWORD = ""
TELEGRAM_BOT_TOKEN = ""
con=Connection(AD_SERVER,AD_USERNAME,AD_PASSWORD, auto_bind=True)
print(con)