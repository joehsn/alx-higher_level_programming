#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves all states from the
'states' table in ascending order by 'id', and prints them to the console.

Arguments:
    username: MySQL username
    password: MySQL password
    database: Database name
"""

import MySQLdb


def connect_to_database(username, password, database):
    """Connects to the MySQL database server.

    Args:
        username: MySQL username
        password: MySQL password
        database: Database name

    Returns:
        A MySQLdb connection object
    """

    try:
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306,
        )
    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")
        exit(1)

    return connection


def get_states(cursor):
    """Retrieves all states from the 'states' table sorted by 'id'.

    Args:
        cursor: A MySQLdb cursor object

    Returns:
        A list of tuples containing state data (id, name)
    """

    query = "SELECT * FROM states ORDER BY id ASC;"
    cursor.execute(query)
    return cursor.fetchall()


def print_states(states):
    """Prints states to the console in the specified format.

    Args:
        states: A list of tuples containing state data (id, name)
    """

    for state in states:
        print(state)


if __name__ == "__main__":
    username, password, database = input().split()
    connection = connect_to_database(username, password, database)
    cursor = connection.cursor()
    states = get_states(cursor)
    print_states(states)
    connection.close()
