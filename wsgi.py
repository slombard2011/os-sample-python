from flask import Flask
import psycopg2
import os
application = Flask(__name__)

USER = os.environ.get("POSTGRESQL_USER")
PASSWORD = os.environ.get("POSTGRESQL_PASSWORD")
HOST = "127.0.0.1"
PORT = "5432"
DATABASE = os.environ.get("POSTGRESQL_DATABASE")

@application.route('/')
def health_check():
    try:
        connection = psycopg2.connect(user = USER,
                                      password = PASSWORD,
                                      host = HOST,
                                      port = PORT,
                                      database = DATABASE)
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        return "Database connexion is ok "
    except ( psycopg2.Error) as error :
        return ('Unable to connect to the database!\n{0}').format(error)

if __name__ == '__main__':
    application.run()
