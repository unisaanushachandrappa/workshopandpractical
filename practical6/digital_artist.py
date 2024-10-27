from practical6.employee import Employee

class DigitalArtist(Employee):
    def __init__(self, id, name, field, project, software):
        super().__init__(id, name, field, project)
        self.__software = software
        self.__suite = [software]

    def work(self):
        super().work()
        print(f"using {self.__software}.")

    def learn_software(self, software):
        self.__suite.append(software)

employee_1 = DigitalArtist(4, "Professor Oak", "Professor", "Let children do his research", "Blender")
employee_1.work()
employee_1.learn_software("C++")
employee_1.assign_project("Be the very best, like no one ever was.")
employee_1.swap_project(1)
employee_1.work()