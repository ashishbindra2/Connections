import pymysql
import os


class MySqlConnection:
    connection = None

    def get_connection(self):
        try:
            if not self.connection:
                self.connection = pymysql.connect(
                host=os.environ.get("DB_HOST", 'localhost'),
                user=os.environ.get("MYSQL_USER", 'root'),
                password=os.environ.get("MYSQL_PASSWORD", 'root'),
                db=os.environ.get("MYSQL_DATABASE", 'iqaccolleges'),
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("DB connection problem: ",e)    

        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None