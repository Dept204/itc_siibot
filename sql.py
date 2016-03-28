from pymysql import cursors, connect
import os


class SQL:
    def __init__(self):
        self.user = os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
        self.password = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
        self.host = os.environ['OPENSHIFT_MYSQL_DB_HOST']
        self.database = os.environ['OPENSHIFT_APP_NAME']
        self.charset = 'utf8mb4'
        self.cursorclass = cursors.DictCursor
        self.connection = None
        self.result = None

    def _create_connection_(self):
        self.connection = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.database,
                charset=self.charset,
                cursorclass=self.cursorclass
        )

    def function(self, query):
        self._query_(query)
        return self.get_last_result()[self.result.keys()[0]]

    def _query_(self, query):
        self._create_connection_()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
                self.result = cursor.fetchone()
        finally:
            self.connection.close()

    def get_last_result(self):
        return self.result
