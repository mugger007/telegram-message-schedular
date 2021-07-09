from sqlalchemy import *
from config import host, port, database, user, password

class DBHelper:

    def __init__(self):
        conn_str = f"postgresql://{user}:{password}@{host}/{database}"
        global engine
        engine = create_engine(conn_str)
        metadata = MetaData(bind = engine)
        global cheesy_tb
        cheesy_tb = Table('TABLE_NAME', metadata, autoload = True)

    def get_items(self):
        query = select(cheesy_tb.c.insta_url, cheesy_tb.c.caption, cheesy_tb.c.index).order_by(func.random()).limit(1)
        connection = engine.connect()
        result = connection.execute(query)
        return [r for r in result]

    def delete_item(self, index):
        query = delete(cheesy_tb).where(cheesy_tb.c.index == index)
        connection = engine.connect()
        ResultProxy = connection.execute(query)
