
from mysql import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func, VARCHAR


class Test(Base):

    __talbename__ = 'test'

    id = Column(Integer, primary_key=True)
    content = Column(VARCHAR(128), nullable=True, default='hello world')
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="update time")


# 创建表
Base.metadata.create_all()
