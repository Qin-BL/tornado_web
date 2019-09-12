
from sqlalchemy.ext.declarative import declarative_base


class BaseModel(object):

    # 告诉sqlalchemy是基类
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


Base = declarative_base(cls=BaseModel)
