import sqlite3

CREATE_BEANS_TABLE = "CREATE TABLE IF not exists beans (id INTEGER PRIMARY KEY, name TEXT, method text, rating INTEGER, price INTEGER);"

INSERT_BEAN = "INSERT INTO beans (name, method, rating, price) VALUES (?, ?, ?, ?);"

GET_ALL_BEANS = "SELECT * FROM beans;"

GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"

GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * from beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;
"""

DELETE_BEAN = "DELETE FROM beans WHERE name = ?;"

MODIFY_BEAN = "UPDATE beans SET name = ?, method = ?, rating = ? , price = ? WHERE name = ?;"



def connect():
    return sqlite3.connect('data_db.db')

def create_table(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection, name, method, rating, price):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating, price))

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()

def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()

def get_best_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()

def delete_bean(connection, name):
    with connection:
        connection.execute(DELETE_BEAN, (name,))

def modify_bean(connection, name, method, rating):
    with connection:
        connection.execute(MODIFY_BEAN, (name, method, rating, price))

