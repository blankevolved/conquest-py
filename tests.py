from civ import Building, Currency

wood = Currency('Wood')
stone = Currency('Stone')

building = Building('hi', 'none', {'currency':wood, 'amt':100}, {'currency':stone, 'amt': 30})

wood.amt = 150
stone.amt = 40

print(building.buy())

print(building.amt)