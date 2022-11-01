from typing import Callable, Union
from random import randint
import click

from pizzas import Pizza, Margherita, Pepperoni, Hawaiian


MENU = {
    'margherita': Margherita,
    'pepperoni': Pepperoni,
    'hawaiian': Hawaiian,
}


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery/--pickup', 'to_deliver', default=True,
              help="If flag --delivery is set, pizza will be delivered. "
                   "If flag --pickup is set, pizza should be picked up. "
                   "Default value is --delivery.")
@click.option('--size', type=click.Choice(['L', 'XL'], case_sensitive=False),
              default='L', help="Pizza size. Possible values: L, XL")
@click.argument('pizza_title', nargs=1)
def order(pizza_title: str, to_deliver: bool, size: str) -> None:
    """Cooks and delivers pizza"""

    if pizza_title not in MENU:
        click.echo(f'There is no pizza with title \"{pizza_title}\" in our menu.')
    else:
        pizza = MENU[pizza_title](size)
        item, ingredients = list(pizza.dict().items())[0]
        click.echo('Your order is:')
        click.echo(f'- {item}: {", ".join(ingredients)} (size: {pizza.size})')

        bake(pizza)
        if to_deliver:
            delivery(pizza)
        else:
            pickup(pizza)


@cli.command()
def menu() -> None:
    """Displays menu"""
    for title in MENU:
        pizza = MENU[title]()
        item, ingredients = list(pizza.dict().items())[0]
        click.echo(f'- {item}: {", ".join(ingredients)}')
    click.echo('Possible pizza sizes: L, XL')


def log(arg: Union[Callable, str]) -> Callable:
    """
    Universal decorator-logger: generates time of function executing
    (optionally, it's possible to set the output format)
    """
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            # use ordinary decorator
            if callable(arg):
                print(f'{func.__name__} - {randint(0, 10)} c!')
            # use parametric decorator
            else:
                print(arg.format(randint(0, 10)))
            return func(*args, **kwargs)
        return inner_wrapper

    return outer_wrapper if not callable(arg) else outer_wrapper(arg)


@log
def bake(pizza: Pizza) -> None:
    """Cooks pizza"""
    pass


@log('Delivered by {}с!')
def delivery(pizza: Pizza) -> None:
    """Delivers pizza"""
    pass


@log('Taken away for {}с!')
def pickup(pizza: Pizza) -> None:
    """Pickup of pizza"""
    pass


if __name__ == '__main__':
    cli()
