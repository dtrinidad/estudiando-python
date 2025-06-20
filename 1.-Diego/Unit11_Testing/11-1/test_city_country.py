import city_functions

def test_city_country():
    assert city_functions.cuntry_city("Republica Dominicana", "Santo Domingo") == "Republica Dominicana, Santo Domingo"