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
            req_project = "CREATE TABLE IF NOT EXISTS project (id INT UNSIGNED NOT NULL AUTO_INCREMENT, name_project VARCHAR(255) NOT NULL, update_date TIMESTAMP, date_creation DATETIME DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));"
            req_card = "CREATE TABLE IF NOT EXISTS card (id INT UNSIGNED NOT NULL AUTO_INCREMENT, member TEXT NOT NULL, description TEXT, tag TEXT, checklist TEXT, update_date DATETIME, deadline DATETIME, date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));"
            req_crud = "CREATE TABLE IF NOT EXISTS crud (id INT UNSIGNED NOT NULL AUTO_INCREMENT, card INT, date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));"
            cursor.execute(req_project)
            cursor.execute(req_card)
            cursor.execute(req_crud)
    except Error as e:
        print("Error while connecting to MySQL", e),





if __name__ == '__main__':
    connection = mysql.connector.connect(host='localhost',
                                         port='8889',
                                         database='trello',
                                         user='root',
                                         password='root')
    connect_to_mysqldb(connection)
