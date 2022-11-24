class Currency_Object:
    def __init__(self, name:str, sign:str=''):
        self.name = name
        self.amt = 0
        self.sign = sign

class Profession:
    def __init__(self, name:str, salary:int, salary_object:Currency_Object):
        self.name = name
        self.salary = salary
        self.salary_object = salary_object

class Gender:
    def __init__(self, pronoun:str, past_pronoun:str):
        self.pronoun = pronoun
        self.past_pronoun = past_pronoun

class Entity:
    def __init__(self, name:str, gender:Gender):
        self.name = name
        self.gender = gender
        

class Buildable_Object:
    def __init__(self, name:str, description:str, *costs:Currency_Object):
        self.name = name
        self.desc = description
        self.costs = costs
        self.amt = 0
    
    def build(self):
        amt_true = 0
        for i in self.costs:
            if i['currency'].amt >= i['amt']:
                amt_true = amt_true + 1
            else:
                break
            
        if amt_true == len(self.costs):
            self.amt = self.amt + 1
            return f'Built {self.name}'
            

