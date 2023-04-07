import os
from deta import Deta
from dotenv import load_dotenv
# https://docs.deta.sh/docs/base/sdk
load_dotenv(".env")   # DETA_KEY dans un fichier .env
# exemple le fichier .env contient
# DETA_KEY = lkhjgjgkfjfjdkd12334
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
db_ = deta.Base('data_position')  # acces a la base de donnees


def fetch_all(database_):
    res = database_.fetch()
    return res.items


def update_database(database_, update_values_, key_):
    d = get_database(database_, key_)  # lecture {}
    d.update(update_values_)  # update {}
    database_.put(d)


def put_database(database_, dict_):
    database_.put(dict_)


def get_database(database_, key_):
    return database_.get(key_)


a = fetch_all(db_)
# [{'key': 'john', 'position': '126.3456'}]
print(a)

a = get_database(db_, 'john')
# 126.3456
print(a['position'])

update_database(db_, {'position': '125'}, 'john')

a = fetch_all(db_)
# [{'key': 'john', 'position': '125'}]
print(a)
