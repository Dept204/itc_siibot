import pymysql.cursors
import os


class SQL:
    def __init__(self):
        self.user = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
        self.password = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
        self.host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
        self.database = os.environ['OPENSHIFT_APP_NAME']
        self.charset = 'utf8mb4'
        self.cursorclass = pymysql.cursors.DictCursor
        self.connection = None
        self.result = None

    def _create_connection_(self):
        self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.database,
                charset=self.charset,
                cursorclass=self.cursorclass
        )

    def funcion(self, query):
        self._query_(query)
        print 'Resultado', type(self.result), self.result
        return self.get_last_result()

    def _query_(self, query):
        self._create_connection_()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.result = cursor.fetchone()
        finally:
            self.connection.close()

    def insert_update(self, query):
        self._create_connection_()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        finally:
            self.connection.close()
            return True

    def get_last_result(self):
        return self.result
