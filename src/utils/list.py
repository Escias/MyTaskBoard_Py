def get_name_list():
    req = "SELECT L.name_list FROM list AS L"
    return req


def get_id_list():
    req = "SELECT L.id FROM list AS L"
    return req


def create_list(project_id):
    name_list = input('Enter list name')
    req = "INSERT INTO list (name_list, project_id) VALUES ('{name_list}', '{project_id}')".format(name_list=name_list, project_id=project_id)
    return req
