from name_function import get_formatted_name

def test_first_last_name():
    """Do names like Diego Trinidad Work?"""
    formatted_name = get_formatted_name('Diego', 'Trinidad')
    assert formatted_name == "Diego Trinidad"

def test_first_last_middle_name():
    """Do names like Marcus Alejandro Trinidad Work?"""
    formatted_name = get_formatted_name('Marcus', 'Trinidad', 'Alejandro')
    assert formatted_name == "Marcus Alejandro Trinidad"