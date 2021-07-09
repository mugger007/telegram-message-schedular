from sqlalchemy import *
from config import host, port, database, user, password

class DBHelper:

    def __init__(self):
        conn_str = f"postgresql://{user}:{password}@{host}/{database}"
        global engine
        engine = create_engine(conn_str)
        metadata = MetaData(bind = engine)
        global cheesy_tb
        cheesy_tb = Table('cheesy_shit', metadata, autoload = True)

    def get_items(self):
        # query = select(cheesy_tb.c.insta_url, cheesy_tb.c.caption).where(cheesy_tb.c.index == index)
        query = select(cheesy_tb.c.insta_url, cheesy_tb.c.caption, cheesy_tb.c.index).order_by(func.random()).limit(1)
        connection = engine.connect()
        result = connection.execute(query)
        return [r for r in result]

    def delete_item(self, index):
        query = delete(cheesy_tb).where(cheesy_tb.c.index == index)
        connection = engine.connect()
        ResultProxy = connection.execute(query)
"""
    def get_items(self):
        query = select(cheesy_tb).order_by(func.random())
        # query = select(cheesy_tb.c.ticker).where(cheesy_tb.c.user_id == user_id)
        connection = engine.connect()
        result = connection.execute(query)
"""
