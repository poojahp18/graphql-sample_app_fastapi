from sqlalchemy import create_engine, MetaData

engine = create_engine(
    "mysql+pymysql://root:root@localhost:3307/test",
)
meta = MetaData()
conn = engine.connect()
