# %%
def city_state(city, state):
    print(f'{city.title()}, {state.title()}')
# %%
city_state('São Paulo','São Paulo')
city_state('Makinohara','Shizuoka')
city_state('Ouro Preto','Minas Gerais')
# %%
def city_country():
    count = 1
    while count < 4:
        city = input('Digit a city')
        country = input('Digit its country')
        print(f'{city.title()}, {country.title()}')
        count += 1
# %%
city_country()
# %%
def country_city(country, city, state = None):
    if state:
        info = {'country':country.title(), 'state':state.title(), 
                'city':city.title()}
    else:
        info = {'country':country.title(), 'state':None, 'city':city.title()}
    return info
# %%
city_infos = []
city_infos.append(country_city('brazil','são paulo','são paulo'))
city_infos.append(country_city('brazil','ouro preto',))
city_infos.append(country_city('brazil','niteroi','rio de janeiro'))
city_infos
# %%
