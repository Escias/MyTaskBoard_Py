import datetime
import mysql.connector
from mysql.connector import Error


def connect_to_mysqldb(connection):
    try:
        connection
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
    except Error as e:
        print("Error while connecting to MySQL", e)


if __name__ == '__main__':
    connection = mysql.connector.connect(host='localhost',
                                         port='8889',
                                         database='trello',
                                         user='root',
                                         password='root')
    connect_to_mysqldb(connection)
