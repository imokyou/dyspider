# -*- coding: utf-8 -*-
from dyspider.models import DbMgr

class DyspiderPipeline(object):
    def process_item(self, item, spider):
        return item



class MysqlDyttPipeline(object):
    def __init__(self):
        self.dbmgr = DbMgr()

    def _connectdb(self):
        if not self.dbsession:
            self.dbsession = DBSession()
        return self.dbsession

    def _closedb(self):
        if self.dbsession:
            self.dbsession.close()

    def process_item(self, item, spider):
        if spider.name == 'dytt':

            record = {
                'uid':item['uid'],
                'name':item['name'],
                'url':item['url'],
                'section':item['section'],
                'category':item['category'],
                'pubdate':item['pubdate']
            }
            if not self.dbmgr.existsVideo(record['uid']):
                self.dbmgr.addVideo(record)
        else:
            pass
        return item