# %%
person_1 = {'name': 'john', 'last_name': 'kennedy', 'age': 35, 'city': 'New Jersey'}

person_2 = {'name': 'anna', 'last_name': 'bush', 'age': 21, 'city': 'Londres'}

person_3 = {'name': 'ken', 'last_name': 'jun', 'age': 27, 'city': 'Tokyo'}

people = [person_1, person_2, person_3,]
people
# %%
for person in people:
    print(f'Full name: {person['name'].title()} {person['last_name'].title()}')
    print(f'Age: {person['age']}')
    print(f'City: {person['city'].title()}')
    print()
    
# %%
people[0]['pet'] = 'dog'
people[1]['pet'] = 'cat'
people[2]['pet'] = 'snake'
people
# %%
for person in people:
    print(f'Full name: {person['name'].title()} {person['last_name'].title()}')
    print(f'Age: {person['age']}')
    print(f'City: {person['city'].title()}')
    print(f'Pet: {person['pet']}')
    print()
# %%
cities = {}
sao_paulo = {'city':'São Paulo', 'country':'brazil','continent':'south america'}
new_york = {'city':'New york', 'country':'usa','continent':'north america'}
vancouver = {'city':'vancouver', 'country':'canada','continent':'south america'}
seoul = {'city':'seoul', 'country':'south korea','continent':'asia'}

cities['sao paulo'] = sao_paulo
cities['new york'] = new_york
cities['vancouver'] = vancouver
cities['seoul'] = seoul

for city, value in cities.items():
    print(f'City: {value['city'].title()}')
    print(f'Country: {value['country'].title()}')
    print(f'Continent: {value['continent'].title()}')
    print()
# %%
