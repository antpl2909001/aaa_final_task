import pytest
from click.testing import CliRunner
from cli import cli, menu, order


def test_menu():
    runner = CliRunner()
    result = runner.invoke(menu)

    expected_output = "- Margherita: tomato sauce, mozzarella, tomatoes\n" \
                      "- Pepperoni: tomato sauce, mozzarella, pepperoni\n" \
                      "- Hawaiian: tomato sauce, mozzarella, chicken, pineapples\n" \
                      "Possible pizza sizes: L, XL\n"

    assert result.stdout == expected_output


def test_order_declaration():
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'pepperoni'])

    assert result.stdout.startswith('Your order is:')


def test_order_hawaiian():
    runner = CliRunner()
    result = runner.invoke(order, 'hawaiian')

    assert result.stdout.find('Hawaiian: tomato sauce, mozzarella, chicken, pineapples') != -1


@pytest.mark.parametrize('flag, pattern', [('--delivery', 'Delivered by'),
                                           ('--pickup', 'Taken away for')])
def test_order_delivery(flag, pattern):
    runner = CliRunner()
    result = runner.invoke(order, ['hawaiian', flag])

    assert result.stdout.find(pattern) != -1


@pytest.mark.parametrize('size, pattern', [('L', '(size: L)'),
                                           ('XL', '(size: XL)'),
                                           ('XXL', 'Error: Invalid value for \'--size\'')])
def test_order_size(size, pattern):
    runner = CliRunner()
    result = runner.invoke(order, ['hawaiian', f'--size={size}'])

    assert result.stdout.find(pattern) != -1


def test_order_empty_arguments():
    runner = CliRunner()
    result = runner.invoke(order)

    assert result.stdout.find('Error: Missing argument \'PIZZA_TITLE\'.') != -1


def test_order_pizza_out_from_menu():
    runner = CliRunner()
    result = runner.invoke(order, 'cheese')

    assert result.stdout == 'There is no pizza with title \"cheese\" in our menu.\n'
