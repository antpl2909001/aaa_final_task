import pytest
from pizzas import Pizza, Margherita, Pepperoni, Hawaiian


def test_pizza_dict_method():
    ingredients = ['mozzarella', 'cheddar', 'parmesan']
    pizza = Pizza(ingredients, size='L')
    assert pizza.dict() == {"Pizza": ingredients}


def test_valid_pizza_size():
    ingredients = ['mozzarella', 'cheddar', 'parmesan']
    pizza = Pizza(ingredients, size='XL')
    assert pizza.size == 'XL'


def test_invalid_pizza_size():
    ingredients = ['mozzarella', 'cheddar', 'parmesan']
    size_value = 'XXL'
    with pytest.raises(ValueError) as exception_info:
        Pizza(ingredients, size=size_value)
    assert f'Size of pizza must be L or XL, not {size_value}.' == str(exception_info.value)


@pytest.mark.parametrize('pizza_title, dict_result',
                         [('margherita', {'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']}),
                          ('pepperoni',  {'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni']}),
                          ('hawaiian',   {'Hawaiian': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']})],
                         )
def test_pizzas_from_menu(pizza_title, dict_result):
    menu = {
        'margherita': Margherita,
        'pepperoni': Pepperoni,
        'hawaiian': Hawaiian,
    }
    assert menu[pizza_title]().dict() == dict_result


def test_equal_pizzas():
    assert Margherita(size='XL') == Margherita(size='XL')


def test_not_equal_pizzas():
    assert Margherita() != Pepperoni()
