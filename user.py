#  manipulating with user's data in DB
from db_utils import get_cursor_and_connection
import re
import hashlib

DB_NAME = "game_users_db"
users_table = "users"


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


def update_user_statistics(db_name, table_name, user_id, points=0, life=90, level=1):
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
    if not user_id:
        return
    return user_id[0][0]


def is_valid_username(username: str) -> bool:
    # Check if the username meets the criteria
    # Between 3 and 20 characters
    # Contains only letters, numbers, and underscores
    return re.match("^[a-zA-Z0-9_]{3,20}$", username) is not None


def is_valid_password(password: str) -> bool:
    # Check if the password meets the criteria
    # At least 8 characters long
    # Contains at least one uppercase letter
    # Contains at least one lowercase letter
    # Contains at least one digit
    # Contains at least one special character (e.g., !@#$%^&*)
    return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            re.search("[!@#$%^&*]", password) is not None
    )


def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256 algorithm with a salt.
    """
    # Use a static salt for hashing
    salt = "weqcrh378451#&*$3i4ycn24utyvn6y34y!(@*74"

    # Hash the password using SHA-256
    hashed_password = hashlib.sha256((password + ":" + salt).encode('utf-8')).hexdigest()
    return hashed_password


def check_username_and_password(input_username: str, input_password: str) -> tuple or None:
    """
    Checks if the provided username and password are valid.

    Parameters:
    - input_username (str): The input username.
    - input_password (str): The input password.

    Returns:
    - Tuple[str, str] or None: A tuple containing the valid username and password,
      or None if either the username or password is invalid.
    """
    if not is_valid_username(input_username) or not is_valid_password(input_password):
        return None
    return input_username, input_password


def is_user_exist_in_db(db_name: str, table_name: str, username: str) -> bool:
    """Checks if a user with the given username exists in the specified database table."""
    if get_user_id(db_name, table_name, username) is None:
        return False
    return True


def add_valid_user_data_to_db(username: str, password: str):
    """Adds valid user data to the specified database if the user does not already exist."""
    if is_user_exist_in_db(DB_NAME, users_table, username):
        # User already exists, return None
        return None

    # User does not exist, proceed with adding user data to the database
    hashed_password = hash_password(password)
    insert_new_user(DB_NAME, users_table, username, hashed_password)
