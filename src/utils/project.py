def get_name_project():
    req = "SELECT P.name_project FROM project AS P"
    return req


def get_id_project(name):
    req = "SELECT P.id FROM project AS P WHERE P.name_project = {name}".format(name=name)
    return req


def create_project():
    name_project = input('Enter project name')
    req = "INSERT INTO project (name_project) VALUES ('{name_project}')".format(name_project=name_project)
    return req
