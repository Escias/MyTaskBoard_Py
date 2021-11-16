def get_name_project():
    req = "SELECT P.name_project FROM project AS P"
    return req


def get_id_project(name):
    req = "SELECT P.id FROM project AS P WHERE P.name_project = '{name}'".format(name=name)
    return req


def create_project():
    admin = input("Enter admin's name of project")
    name_project = input('Enter project name : ')
    req = "INSERT INTO project (admin, name_project) VALUES ('{admin}', '{name_project}')".format(admin=admin, name_project=name_project)
    return req
