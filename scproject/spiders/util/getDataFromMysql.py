import pymysql.cursors

from scproject.settings import MYSQL_HOST, MYSQL_DBNAME, MYSQL_USER, MYSQL_PASSWD


class mySqlData:
# 连接MySQL数据库
    def __init__(self):
        dbparms = dict(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,  # 指定 curosr 类型
            use_unicode=True,
        )
        self.connection = pymysql.connect(**dbparms)
        # 通过cursor创建游标
        self.cursor = self.connection.cursor()
    def do_select(self,sql):
        # 执行数据查询
        self.cursor.execute(sql)
        # 查询数据库多条数据
        result = self.cursor.fetchall()
        self.con_close()
        return result
    def con_close(self):
        self.cursor.close()
        self.connection.close()
    def get_sc(self):
        pass
