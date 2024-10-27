class Employee:
    def __init__(self, id, name, field, project):
        self.__id = id
        self.__name = name
        self.__field = field
        self.__project = project
        self.__project_backlog = [project]

    def assign_project(self, project_backlog):
        self.__project_backlog.append(project_backlog)

    def work(self):
        print(f"Working on {self.__project}",end=" ")

    def swap_project(self, index):
        self.__project = self.__project_backlog[index]

# data = Employee("007", "James Bond", "Intelligence", "Moonraker")
# data.work()
#
# data = Employee("007", "James Bond", "Intelligence", "Moonraker")
# data.assign_project("GoldFinger")
# data.swap_project(1)
# data.work()
#
# data = Employee("007", "James Bond", "Intelligence", "Moonraker").__dict__
# expected_attributes = ['_Employee__id', '_Employee__name', '_Employee__field', '_Employee__project', '_Employee__project_backlog']
# for attribute in expected_attributes:
#     if (not data.__contains__(attribute)):
#         print(f"The class is missing a {attribute} attribute")