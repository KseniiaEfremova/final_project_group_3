import mysql.connector
import logging
from mysql.connector import errorcode
from config import data

host, user, password = data["host"], data["user"], data["passwd"]
DB_NAME = 'game_users_db'


def connect_to_mysql_database(db_name):
    """
    Connects to a MySQL database using credentials from a JSON file.
    Returns:
        mysql.connector.MySQLConnection: A MySQL database connection object.
    Raises:
        mysql.connector.Error: If there is an error during the database connection process.
    """
    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        return db_connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        raise e
    except ValueError as e:
        print(f"ValueError: {e}")
        raise e
    except Exception as e:
        # Catch unexpected exceptions, log them, and raise to crash the program
        logging.exception(f"Unexpected error occurred: {e}")
        raise e


def get_cursor_and_connection(db_name):
    db_connection = connect_to_mysql_database(db_name)
    cursor = db_connection.cursor()
    return cursor, db_connection


def create_database(db_name):
    try:
        cursor, _ = get_cursor_and_connection(db_name)
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))

    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def connect_to_database_or_create_if_not_exists(db_name):
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(db_name)
            print("Database {} created successfully.".format(db_name))
            db_connection.database = db_name
        else:
            print(err)
            exit(1)
    print(f"You are using {db_name} database.")


#  manipulating with user's data in DB

# adding new user
def insert_new_user(db_name, table_name, username, password):
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        print("Connected to DB: %s" % db_name)
        # insert user data into users table
        query = """INSERT INTO {} (username, password) VALUES ('{}', '{}')""".format(table_name, username, password)

        cursor.execute(query)
        db_connection.commit()
        cursor.close()

        # insert user's initial statistics in the game_statistics table
        user_id = get_user_id(db_name, table_name, username)
        update_user_statistics(db_name, "game_statistics", user_id)
        print(f"\nNew user '{username}' has been successfully added into the database!")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def update_user_statistics(db_name, table_name, user_id, points=0, life=3, level=1):
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        print("Connected to DB: %s" % db_name)

        query = """INSERT INTO {} (user_id, points, life, level) VALUES ('{}', '{}', '{}', '{}')""".format(table_name, user_id, points, life, level)

        cursor.execute(query)
        db_connection.commit()
        cursor.close()
        print(f"\nThe user's statistics has been successfully updated!")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def get_user_data(db_name, table_name, username):
    user_data = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        print("Connected to DB: %s" % db_name)
        query = """SELECT u.user_id, u.username, g.points, g.life, g.level 
        FROM {} as u 
        JOIN game_statistics as g
        ON u.user_id = g.user_id
        WHERE u.username = %s
        """.format(table_name)
        cursor.execute(query, (username,))
        user_data = cursor.fetchall()
        cursor.close()

    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return user_data


def get_user_id(db_name, table_name, username):
    user_id = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        print("Connected to DB: %s" % db_name)
        query = """SELECT user_id FROM {}
        WHERE username = %s
        """.format(table_name)
        cursor.execute(query, (username,))
        user_id = cursor.fetchall()
        cursor.close()

    except Exception as e:
        print(e)

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return user_id[0][0]
