# coding=utf8
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import MYDB


dburl = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (MYDB['user'], MYDB['passwd'], MYDB['host'], MYDB['port'], MYDB['db'])
engine = create_engine(dburl, echo=False)
DBSession = sessionmaker(bind=engine)

# 创建对象的基类:
Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {
        'extend_existing': True,
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
    }


class Video(BaseModel):
    __tablename__ = 'video'
    id = Column("id", Integer, primary_key=True)
    uid = Column(String(32))
    name = Column(String(256))
    url = Column(String(512))
    section = Column(Integer)
    category = Column(Integer)
    pubdate = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)



class DbMgr(object):
    def __init__(self):
        self.session = DBSession()

    def addVideo(self, record={}):
        try:
            if not record:
                return None
            video = Video(**record)
            self.session.add(video)
            self.session.commit()
        except:
            self.session.rollback()
        finally:
            self.session.close()


    def existsVideo(self, uid):
        try:
            ret = False
            exists = self.session.query(Video) \
                .filter(Video.uid == uid).count()
            if exists:
                ret = True
        except:
            pass
        finally:
            self.session.close()
        return ret




