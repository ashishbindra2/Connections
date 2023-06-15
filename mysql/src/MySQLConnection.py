import os
from flask import current_app
import mysql.connector


class MySQLConnection:

    def __init__(self):
        self.connection = None

    def get_connection(self):
        if not self.connection:
            db_config = current_app.config['DATABASE']
            self.connection = mysql.connector.connect(
                host=os.environ.get("DB_HOST",db_config['HOST']),
                user=os.environ.get("DB_USER",db_config['USER']),
                password=os.environ.get("DB_PASSWORD",db_config['PASSWORD']),
                database=os.environ.get("DB_NAME",db_config['NAME']),
                port=os.environ.get("DB_PORT", "3308"),
            )
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
