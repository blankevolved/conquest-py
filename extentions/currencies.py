from conquest import Currency_Object

class Money(Currency_Object):
    def __init__(self, name: str, sign:str=''):
        super().__init__(name, sign)

DOLLARS = Money('dollars', '$')
EUROS = Money('euros', '€')

class Material(Currency_Object):
    def __init__(self, name: str):
        super().__init__(name)