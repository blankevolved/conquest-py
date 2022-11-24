class Currency:
    def __init__(self, name:str):
        self.name = name
        self.amt = 0

class Building:
    def __init__(self, name:str, description:str, *costs:Currency):
        self.name = name
        self.desc = description
        self.costs = costs
        self.amt = 0
    def buy(self):
        amt_true = 0
        for i in self.costs:
            if i['currency'].amt >= i['amt']:
                amt_true = amt_true + 1
            else:
                break
            
        if amt_true == len(self.costs):
            self.amt = self.amt + 1
            
                