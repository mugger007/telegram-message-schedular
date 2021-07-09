from sqlalchemy import *
from config import host, port, database, user, password

conn_str = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()
cheesy_tb = Table('cheesy_shit', metadata,
    Column('index', Integer, nullable=False),
    Column('insta_url', String(255), nullable=False),
    Column('caption', String(255), nullable=False)
)

metadata.create_all(engine)

query = insert(cheesy_tb).values(index=1, insta_url='INSTA_URL', caption='CHEESY_CAPTION')
connection = engine.connect()
ResultProxy = connection.execute(query)
