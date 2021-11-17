def get_name_list(project_id):
    req = "SELECT name_list FROM list WHERE project_id = '{}'".format(project_id)
    return req


def get_id_list(name):
    req = "SELECT id FROM list WHERE name_list = '{name}'".format(name=name)
    return req


def create_list(project_id):
    name_list = input('Enter list name')
    req = "INSERT INTO list (name_list, project_id) VALUES ('{name_list}', '{project_id}')".format(name_list=name_list, project_id=project_id)
    return req
