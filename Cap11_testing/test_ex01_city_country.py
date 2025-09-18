# %%
from ex01_city_country import city_country

def test_city_country_pop():
    get_city_country = city_country('guarulhos','brazil', 50000)
    assert get_city_country == 'Guarulhos, Brazil - population: 50000'
    
def test_city_country():
    get_city_country = city_country('guarulhos','brazil')
    assert get_city_country == 'Guarulhos, Brazil'