from product_utils import (
    print_products,
    print_order_products
)

from db_utils import (
    read_products,
    get_products_below_stock,
    find_product_by_name,
    add_product,
    update_product_stock,
    delete_product
)

from input_utils import get_int_input, get_float_input

MIN_STOCK = 10
DB_NAME = 'warehouse.db'


def show_menu():
    print()
    print("1. Показать все товары")
    print("2. Добавить товар")
    print("3. Показать товары с низким остатком")
    print("4. Показать товары для дозаказа")
    print("5. Обновить остаток товара")
    print("6. Удалить товар")
    print("0. Выйти")


def add_product_from_input(db_name):
    name = input('Название товара: ')

    product = find_product_by_name(db_name, name)

    if product is None:
        stock = get_int_input('Остаток: ')
        price = get_float_input('Цена: ')

        add_product(db_name, name, stock, price)

        print(f"Товар '{name}' добавлен в базу.")
    else:
        print(f"Товар '{name}' уже есть в базе.")


def update_stock_from_input(db_name):
    name = input('Название товара: ')

    product = find_product_by_name(db_name, name)

    if product is None:
        print('Ошибка: товар не найден.')
    else:
        new_stock = get_int_input('Новый остаток: ')

        update_product_stock(db_name, name, new_stock)

        print(f"Остаток товара '{name}' обновлён")


def delete_product_from_input(db_name):
    name = input('Название товара: ')

    product = find_product_by_name(db_name, name)

    if product is None:
        print(f"Ошибка: товар '{name}' не найден")
    else:
        delete_product(DB_NAME, name)
        print(f"Товар '{name}' удалён из базы")


while True:
    show_menu()

    choice = input('Выберите действие: ')

    if choice == '1':
        products = read_products(DB_NAME)

        print('Все товары:')
        print_products(products)
        print()
    elif choice == '2':
        add_product_from_input(DB_NAME)    
    elif choice == '3':
        products_below_stock = get_products_below_stock(DB_NAME, MIN_STOCK)
        
        print('Товары с низким остатком:')
        print_products(products_below_stock)
        print()
    elif choice == '4':
        products_below_stock = get_products_below_stock(DB_NAME, MIN_STOCK)

        print('Товары для дозаказа:')
        print_order_products(products_below_stock, MIN_STOCK)
        print()
    elif choice == '5':
        update_stock_from_input(DB_NAME)
        print()
    elif choice == '6':
        delete_product_from_input(DB_NAME)
        print()
    elif choice == '0':
        print('Программа завершена')
        break
    else:
        print('Ошибка: выберите пункт меню от 0 до 6')
        print()