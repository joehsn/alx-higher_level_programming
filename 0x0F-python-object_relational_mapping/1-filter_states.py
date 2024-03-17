#!/usr/bin/python3
"""
This script lists states starting with 'N' from the 'hbtn_0e_0_usa' database,
sorted by ascending 'id'.

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
        return connection
    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")
        exit(1)


def get_states_starting_with_n(cursor):
    """Retrieves states with names starting with 'N' sorted by 'id'.

   Args:
       cursor: A MySQLdb cursor object

   Returns:
       A list of tuples containing state data (id, name)
   """

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
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
    states = get_states_starting_with_n(cursor)
    print_states(states)
    connection.close()
