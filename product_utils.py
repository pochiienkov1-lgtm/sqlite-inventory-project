def calculate_product_value(product):
    value = product['stock'] * product['price']

    return value


def get_stock_status(product):
    if product['stock'] == 0:
        return "Нет товара"
    elif 1 <= product['stock'] <= 9:
        return "Критически мало"
    elif 10 <= product['stock'] <= 50:
        return "Норма"
    else:
        return "Много"


def print_products(products, empty_message="Список товаров пуст."):
    if not products:
        print(empty_message)
        return
     
    for product in products:
        
        product_id = product['id']
        name = product['name']
        stock = product['stock']
        price = product['price']
        value = calculate_product_value(product)
        status = get_stock_status(product)

        print(f'Порядковый номер: {product_id}')
        print(f'Товар: {name}')
        print(f'Остаток: {stock}')
        print(f'Цена: {price}')
        print(f'Стоимость: {value}')
        print(f'Статус: {status}')
        print('--------------------')


def print_order_products(order_products, min_stock):
    if not order_products:
        print('Товаров для дозаказа нет.')
        return
    
    for product in order_products:
        product_id = product['id']
        name = product['name']
        stock = product['stock']
        price = product['price']
        value = calculate_product_value(product)
        status = get_stock_status(product)
        order_quantity = min_stock - stock

        print(f'Порядковый номер: {product_id}')
        print(f'Товар: {name}')
        print(f'Остаток: {stock}')
        print(f'Цена: {price}')
        print(f'Стоимость: {value}')
        print(f'Статус: {status}')
        print(f'Нужно дозаказать: {order_quantity}')
        print('--------------------')