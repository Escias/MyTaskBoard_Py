import datetime


def get_name_card(list_id):
    req = "SELECT C.name_card FROM card AS C WHERE C.list_id = '{}'".format(list_id)
    return req


def get_id_card(name):
    req = "SELECT C.id FROM card AS C WHERE C.name_card = '{name}'".format(name=name)
    return req


def get_details_card(id):
    req = "SELECT * FROM card WHERE id = '{}'".format(id)
    return req


def get_member_card(id):
    req = "SELECT member FROM card WHERE id = '{id}'".format(id)
    return req


def update_card(id):
    check = False
    req = []
    print('/!\ just press enter without enter anything to not upgrade indicated value')
    new_name = input("name : ")
    if new_name != "":
        req_name = "UPDATE card SET name_card = '{name}' WHERE id = '{id}'".format(name=new_name, id=id)
        req.append(req_name)
        check = True
    new_description = input("description : ")
    if new_description != "":
        req_description = "UPDATE card SET description = '{desc}' WHERE id = '{id}'".format(desc=new_description, id=id)
        req.append(req_description)
        check = True
    new_tag = input("tag : ")
    if new_tag != "":
        req_tag = "UPDATE card SET tag = '{tag}' WHERE id = '{id}'".format(tag=new_tag, id=id)
        req.append(req_tag)
        check = True
    new_checklist = input("checklist : ")
    if new_checklist != "":
        req_checklist = "UPDATE card SET checklist = '{check}' WHERE id = '{id}'".format(check=new_checklist, id=id)
        req.append(req_checklist)
        check = True
    new_deadline = input("deadline : ")
    if new_deadline != "":
        req_deadline = "UPDATE card SET deadline = '{dl}' WHERE id = '{id}'".format(dl=new_deadline, id=id)
        req.append(req_deadline)
        check = True
    if check:
        date = datetime.datetime.now()
        update_date = date.strftime("%Y-%m-%d %H:%M:%S")
        req_update_time = "UPDATE card SET update_date = '{update}' WHERE id = '{id}'".format(update=update_date, id=id)
        req.append(req_update_time)
    return req


def update_member(id, member):
    req = []
    new_add_member = input("Enter member name")
    new_member = member + ', ' + new_add_member
    req_member = "UPDATE card SET member = {member} WHERE id = {id}".format(member=new_member, id=id)
    req.append(req_member)
    date = datetime.datetime.now()
    update_date = date.strftime("%Y-%m-%d %H:%M:%S")
    req_update_time = "UPDATE card SET update_date = '{update}' WHERE id = {id}".format(update=update_date, id=id)
    req.append(req_update_time)
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
