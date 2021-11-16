import mysql.connector
from mysql.connector import Error

from utils.project import get_name_project, create_project, get_id_project
from utils.list import get_id_list, get_name_list, create_list
from utils.cards import create_card, get_name_card, get_id_card, get_details_card, update_card, get_member_card, update_member


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
            rows = cursor.fetchall()
            if not rows:
                print("No Project")
                select_or_create_project(cursor)
            else:
                print("Enter project name to access")
                print(rows)
                project_name = input()
                project_id = get_id_project(project_name)
                select_or_create_list_in_project(cursor, project_id, project_id)
        else:
            select_or_create_project(cursor)


def select_or_create_list_in_project(cursor, project_id, project_name):
    while True:
        print("   __________   ")
        print("LIST MENU of {} PROJECT".format(project_name))
        print("")
        print("Enter 'c' to create list")
        print("      's' to select list")
        print("      'b' to return to project menu")

        key = input()

        if key == 'c':
            new_list = create_list(project_id)
            cursor.execute(new_list)
        elif key == 's':
            list_list_req = get_name_list(project_id)
            cursor.execute(list_list_req)
            rows = cursor.fetchall()
            if not rows:
                print("No List")
                select_or_create_list_in_project(cursor, project_id, project_name)
            else:
                print("Enter list name to access")
                print(rows)
                list_name = input()
                list_id = get_id_list(list_name)
                select_or_create_card_in_list(cursor, list_id, list_name, project_id, project_name)
        elif key == 'b':
            select_or_create_project(cursor)
        else:
            select_or_create_list_in_project(cursor, project_id, project_name)


def select_or_create_card_in_list(cursor, list_id, list_name, project_id, project_name):
    while True:
        print("   __________   ")
        print("CARDS MENU of {} LIST".format(list_name))
        print("")
        print("Enter 'c' to create card")
        print("      's' to select card")
        print("      'b' to return to list menu")

        key = input()

        if key == 'c':
            new_card = create_card(list_id)
            cursor.execute(new_card)
        elif key == 's':
            list_card_req = get_name_card(list_id)
            cursor.execute(list_card_req)
            rows = cursor.fetchall()
            if not rows:
                print("No Card")
                select_or_create_card_in_list(cursor, list_id, list_name, project_id, project_name)
            else:
                print("Enter card name to access")
                print(rows)
                card_name = input()
                card_id = get_id_card(card_name)
                card_details(cursor, list_id, list_name, project_id, project_name, card_id, card_name)
        elif key == 'b':
            select_or_create_list_in_project(cursor, project_id, project_name)
        else:
            select_or_create_card_in_list(cursor, list_id, list_name, project_id, project_name)


def card_details(cursor, list_id, list_name, project_id, project_name, card_id, card_name):
    print("   __________   ")
    print("CARDS DETAILS of {} card".format(card_name))
    print("")
    print("Enter 'v' to views card details")
    print("      'u' to update card")
    print("      'm' to add member to card")
    print("      'b' to return to card menu")

    key = input()

    if key == 'v':
        details_card = get_details_card(card_id)
        cursor.execute(details_card)
        details = cursor.fetchone()
        print(details)
    elif key == 'u':
        req_update = update_card(id)
        for req in req_update:
            cursor.execute(req)
    elif key == 'm':
        req_member = get_member_card(card_id)
        cursor.execute(req_member)
        member = cursor.fetchone()
        req_new_member = update_member(id, member)
        for req in req_new_member:
            cursor.execute(req)
    elif key == 'b':
        select_or_create_card_in_list(cursor, list_id, list_name, project_id, project_name)
    else:
        card_details(cursor, list_id, list_name, project_id, project_name, card_id, card_name)


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
            req_project = "CREATE TABLE IF NOT EXISTS project (id INT UNSIGNED NOT NULL AUTO_INCREMENT, admin TEXT NOT NULL, name_project VARCHAR(255) NOT NULL, update_date TIMESTAMP, date_creation DATETIME DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));"
            req_card = "CREATE TABLE IF NOT EXISTS card (id INT UNSIGNED NOT NULL AUTO_INCREMENT, list_id INT NOT NULL, name_card TEXT NOT NULL, member TEXT NOT NULL, description TEXT, tag TEXT, checklist TEXT, update_date DATETIME, deadline DATETIME, date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));"
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
