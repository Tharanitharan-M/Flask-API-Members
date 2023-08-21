import sqlite3
from flask import g

def connect_db():
    """
    Connect to the SQLite database and configure row factory for returning rows as dictionaries.
    """
    sql = sqlite3.connect('members.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    """
    Get the database connection from the application context (g), and create a new connection if it doesn't exist.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
