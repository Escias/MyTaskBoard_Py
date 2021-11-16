import mysql.connector
from mysql.connector import Error

from utils.project import get_name_project, create_project, get_id_project
from utils.list import get_id_list, get_name_list, create_list


def select_or_create_project(cursor):
    while True:
        print("   __________   ")
        print("PROJECT MENU")
        print("")
        print("Enter 'c' to create project")
        print("      's' to select project")

        key = input()

        if key == 'c':
            new_project = create_project()
            cursor.execute(new_project)
        elif key == 's':
            list_project_req = get_name_project()
            cursor.execute(list_project_req)
            print("Enter project name to access")
            rows = cursor.fetchall()
            if not rows:
                print("No Project")
                select_or_create_project(cursor)
            else:
                print(rows)
                name = input()
                project_id = get_id_project(name)
                select_or_create_list_in_project(cursor, project_id)


def select_or_create_list_in_project(cursor, project_id):
    while True:
        print("   __________   ")
        print("LIST MENU")
        print("")
        print("Enter 'c' to create list")
        print("      's' to select list")
        print("      'b' to return to project menu")

        key = input()

        if key == 'c':
            new_list = create_list(project_id)
            cursor.execute(new_list)
        elif key == 's':
            print()
        elif key == 'b':
            print()


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
            req_card = "CREATE TABLE IF NOT EXISTS card (id INT UNSIGNED NOT NULL AUTO_INCREMENT, list_id INT NOT NULL, member TEXT NOT NULL, description TEXT, tag TEXT, checklist TEXT, update_date DATETIME, deadline DATETIME, date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));"
            req_list = "CREATE TABLE IF NOT EXISTS list (id INT UNSIGNED NOT NULL AUTO_INCREMENT, project_id INT NOT NULL, name_list TEXT, card INT, date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));"
            cursor.execute(req_project)
            cursor.execute(req_card)
            cursor.execute(req_list)
            select_or_create_project(cursor)
    except Error as e:
        print("Error while connecting to MySQL", e),





if __name__ == '__main__':
    connection = mysql.connector.connect(host='localhost',
                                         port='8889',
                                         database='trello',
                                         user='root',
                                         password='root')
    connect_to_mysqldb(connection)
