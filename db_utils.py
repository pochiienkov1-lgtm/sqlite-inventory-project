import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def get_db_path(db_name):
    return BASE_DIR / db_name


def get_connection(db_name):
    db_path = get_db_path(db_name)

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def read_products(db_name):
    connection = get_connection(db_name)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM products
    """)
    
    products = cursor.fetchall()

    connection.close()

    return products


def get_products_below_stock(db_name, min_stock):
    connection = get_connection(db_name)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM products
    WHERE stock < ?
    """, (min_stock,))

    products = cursor.fetchall()

    connection.close()

    return products


def add_product(db_name, name, stock, price):
    connection = get_connection(db_name)
    
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO products (name, stock, price)
    VALUES (?, ?, ?)
    """, (name, stock, price))


    connection.commit()
    connection.close()


def find_product_by_name(db_name, name):
    connection = get_connection(db_name)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM products
    WHERE name = ?
    """, (name,))

    product = cursor.fetchone()

    connection.close()

    return product


def update_product_stock(db_name, name, new_stock):
    connection = get_connection(db_name)

    cursor = connection.cursor()

    cursor.execute("""
    UPDATE products
    SET stock = ?
    WHERE name = ?
    """, (new_stock, name))

    connection.commit()
    connection.close()


def delete_product(db_name, name):
    connection = get_connection(db_name)

    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM products
    WHERE name = ?
    """, (name, ))

    connection.commit()
    connection.close()