import datetime


def get_name_card(list_id):
    req = "SELECT C.name_card FROM card AS C WHERE C.list_id = {}".format(list_id)
    return req


def get_id_card(name):
    req = "SELECT C.id FROM card AS C WHERE C.name_card = '{name}'".format(name=name)
    return req


def create_card(list_id):
    member = input("Enter member")
    description = input("Enter description")
    tag = input("Enter tag")
    checklist = input("Enter checklist")
    date = datetime.datetime.now()
    update_date = date.strftime("%Y-%m-%d %H:%M:%S")
    req = "INSERT INTO card (list_id, member, description, tag, checklist, update_date) VALUES ('{list_id}', '{member}', '{description}', '{tag}', '{checklist}', '{update_time}')".format(list_id=list_id, member=member, description=description, tag=tag, checklist=checklist, update_date=update_date)
    return req
