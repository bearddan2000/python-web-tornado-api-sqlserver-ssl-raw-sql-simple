from tornado_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import db.settings as s

engine = create_engine('{engine}://{username}:{password}@{host}/{db_name}'.format(
        **s.SQLSERVER
    )
)

session_local = sessionmaker(
    bind=engine,
    autoflush=s.SQLALCHEMY['autoflush'],
    autocommit=s.SQLALCHEMY['autocommit']
)

sql_instance=SQLAlchemy(engine)

def get_db():
    db: sessionmaker = session_local()
    try:
        yield db
    finally:
        db.close()