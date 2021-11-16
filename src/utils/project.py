class Project:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_project(self):
        req = "SELECT P.name_project FROM project AS P"
        return self.cursor.execute(req)

    def create_project(self):
        name_project = input('Enter project name')
        req = "INSERT INTO project (name_project) VALUES {name_project}".format(name_project=name_project)
        self.cursor.execute(req)
        print("project {} created".format(name_project))
