# Pizza

*Финальное задание по курсу Python от Академии Аналитиков Авито. <br>*

В данном репозитории находится консольное мини-приложение, написанное 
на языке Python3 с использованием библиотеки click.

****

В приложении доступны следующие команды:
- Вывод меню (список доступных пицц и их ингредиентов): ``python cli.py menu``
- Заказ пиццы: ``python cli.py order [PIZZA_NAME]``. 


В меню доступны следующие пиццы:
- Margherita
- Pepperoni
- Hawaiian

Для команды `order` доступны флаги `--delivery` и `--pickup` 
(доставка и самовывоз заказа соответственно), а также опциональный аргумент `--size` со значениями 
`L`, `XL` (размер пиццы; по умолчанию `L`). <br>
При вызове команды `order` в консоли также выводятся текстовые сообщения
о времени приготовления пиццы и времени доставки/самовывоза.

Пример допустимых команд:
1) `python cli.py menu`
2) `python cli.py order hawaiian --pickup --size=XL`
3) `python cli.py order pepperoni --delivery`


### Тестирование:

Все функции и классы были протестированы с помощью 
библиотеки pytest (модуль `pizzas.py`) и click.testing (модуль `cli.py`)

Модуль `pizzas.py`: 100% покрытие кода тестами. <br>
Модуль `cli.py`: 98% покрытие кода тестами (100% за исключением `if __name__ == '__main__':...`)