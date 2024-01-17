import unittest
from main import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee1 = Employee('Andrew', 'Kohut', 100000)
        self.custom_increase = 15000
        self.skills = ['Python', 'Java', 'English']
        self.add_already_skills = ['Python', 'Java']

    def test_give_default_raise(self):
        self.employee1.give_rise()
        self.assertEqual(self.employee1.salary, 105000)

    def test_give_custom_raise(self):
        self.employee1.give_rise(self.custom_increase)
        self.assertEqual(self.employee1.salary, 115000)

    def test_add_skills(self):
        self.employee1.add_skill(self.skills)
        self.assertEqual(self.employee1.skills, self.skills)

    def test_add_already_skills(self):
        self.employee1.add_skill(self.skills)
        errors = self.employee1.add_skill(self.add_already_skills)
        self.assertEqual(self.employee1.skills, self.skills)
        self.assertEqual(errors, ['Python is already', 'Java is already'])

    def test_add_mix_skills(self):
        self.employee1.add_skill(self.skills)
        errors = self.employee1.add_skill(self.skills)
        self.assertEqual(self.employee1.skills, self.skills)
        self.assertEqual(errors, ['Python is already', 'Java is already', 'English is already'])

    def test_remove_skills(self):
        self.employee1.add_skill(self.skills)
        self.employee1.remove_skill(self.add_already_skills)
        self.assertNotIn(self.add_already_skills[0], self.employee1.skills)

    def test_error_remove(self):
        self.employee1.add_skill(self.skills)
        errors = self.employee1.remove_skill(['Polish'])
        self.assertEqual(errors, ['Polish is not exist'])

    def test_error(self):
        with self.assertRaises(Exception):
            self.employee1.add_skill('Polish')


if __name__ == '__main__':
    unittest.main()
