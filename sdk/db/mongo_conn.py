"""
    MongoDB 连接的客户端
"""

from pymongo import MongoClient


class MongoConnectClient:
    def __init__(self, host="localhost", port=27017, username="root", password="root"):
        """
        :param host: str mongodb地址
        :param port: int 端口，默认为27017
        :param username: str 用户名
        :param password: str 密码
        """
        host = host
        self.port = port
        self.client = MongoClient(host=host, port=port, username=username, password=password)

    def get_db(self):
        """
        获取数据库
        :return: 数据库
        """
        return self.client.list_database_names()

    def insert_one(self, db, collection, dic):
        """
        :param db:
        :param collection: str 数据库中的集合
        :param dic: dict 要插入的字典
        :return: 返回包含一个ObjectId类型的对象
        """
        db = self.client[db]
        collection = db[collection]
        rep = collection.insert_one(dic)
        return rep

    def insert_many(self, db, collection, lists):
        """
        :param db:
        :param lists: 要插入的列表，列表中的元素为字典
        :param collection: str 数据库中的集合
        :return: 返回包含多个ObjectId类型的列表对象
        """
        db = self.client[db]
        collection = db[collection]
        rep = collection.insert_many(lists)
        return rep

    def get_counts(self, db, collection):
        """
        获取表里的数据总数
        :param collection: str 表名称
        """
        db = self.client[db]
        return db[collection].count()

    def get_one(self, db, collection):
        """
        随机获取一条数据
        :param collection: collection
        """
        db = self.client[db]
        return db[collection].find_one()

    def get_all(self, db, collection, query=None, projects=None):
        """
        获取某个 collection 的所有数据
        :param projects: 投影的字段
        :param query: 查询语句
        :param collection: collection名称
        :return: 所有的Object
        """
        db = self.client[db]
        if query is None:
            query = {}
        if projects is None:
            projects = {}
        return db[collection].find(query, projects)

    def get_last(self, db, collection):
        """
        获取插入最晚的一条数据
        :param collection: collection的名称
        :return: 插入最晚的一条数据
        """
        db = self.client[db]
        resp = db[collection].find().sort('_id', -1).limit(1)
        for item in resp:
            return item

    def get_collections(self, db):
        """
        获取所有的collection的名称
        :return: 所有的collection的名称
        """
        return self.client[db].list_collection_names()

    def upsert(self, db, collection, query, update):
        """
        更新数据
        :param collection: collection的名称
        :param query: 查询语句
        :param update: 更新语句
        :return: 更新后的数据
        """
        db = self.client[db]
        return db[collection].update_one(query, update, upsert=True)



if __name__ == '__main__':
    mongo = MongoConnectClient(host="localhost", port=27017)
    res = mongo.get_collections("sock-shop")
    print(res)
