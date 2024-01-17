class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.skills = []

    def give_rise(self, salary_increase=5000):
        self.salary += salary_increase

    def add_skill(self, skill_data):
        if type(skill_data) is not list or not set:
            raise Exception('Error')
        error_data = []
        for skill in skill_data:
            if skill not in self.skills:
                self.skills.append(skill)
            else:
                error_data.append(f"{skill} is already")

        return error_data

    def remove_skill(self, skill_data):
        if type(skill_data) is not list or not set:
            raise Exception('Error')
        error_data = []
        for skill in skill_data:
            if skill in self.skills:
                self.skills.remove(skill)
            else:
                error_data.append(f"{skill} is not exist")

        return error_data
