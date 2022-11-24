from conquest import Entity, Gender, Profession

class Human(Entity):
    def __init__(self, name: str, gender: Gender, profession: Profession = None):
        super().__init__(name, gender)
        self.profession = profession
        self.inv = {}

    def work(self):
        if self.profession == None:
            return f'{self.name.capitalize()} dosent have a job.'
        elif self.profession.salary_object.sign != None:
            return f'{self.name.capitalize()} made {self.profession.salary_object.sign}{self.profession.salary}'
        else:
            return f'{self.name.capitalize()} made {self.profession.salary} {self.profession.salary_object.name}'