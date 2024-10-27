from employee import Employee

class SoftwareDeveloper(Employee):
    def __init__(self, id, name, field, project, language):
        super().__init__(id, name, field, project)
        self.__language = language
        self.__programming_languages = [language]

    def work(self):
        super().work()
        print(f"in {self.__language}.")

    def learn_language(self, language):
        self.__programming_languages.append(language)

employee_1 = SoftwareDeveloper(1, "Ash Ketchum", "Pokemon Trainer", "Beat the Elite Four", "Python")
employee_1.work()
employee_1.learn_language("C++")
employee_1.assign_project("Be the very best, like no one ever was.")
employee_1.swap_project(1)
employee_1.work()
