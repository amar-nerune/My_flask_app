import pymysql

from sqlalchemy import create_engine, text
from hidden_files.constant import db_connect_string

engine = create_engine(db_connect_string)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    item = result.mappings().all()
    # print(result.mappings().all())
    result_dicts = []
    for val in item:
        result_dicts.append(dict(val))
    print(result_dicts)

    
