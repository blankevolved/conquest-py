from conquest import Buildable_Object, Currency_Object, Entity, Profession
from extentions.genders import MALE
from extentions.entites import Human
from extentions.currencies import DOLLARS, Material


wood = Material('Wood')
stone = Material('Stone')

building = Buildable_Object('hi', 'none', {'currency':wood, 'amt':100}, {'currency':stone, 'amt': 30})

teacher = Profession('Teacher', 100, DOLLARS)

bob = Human('Bob', MALE, teacher)


print(bob.work())

wood.amt = 150
stone.amt = 40

print(building.build())

print(building.amt)