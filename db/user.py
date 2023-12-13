from db.db_utils import get_cursor_and_connection
import re
import hashlib

DB_NAME = "game_users_db"
users_table = "users"
statistics_table = "game_statistics"


def insert_new_user(db_name, table_name, username, password):
    """
    Inserts a new user into the specified database table.

    Args:
        db_name (str): The name of the database.
        table_name (str): The name of the table in the database.
        username (str): The username of the new user.
        password (str): The hashed password of the new user.

    Returns:
        list: A list of tuples representing the result of the insertion.

    Raises:
        Exception: If there is an error during the user insertion process.
    """
    db_connection = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)

        query = ("""INSERT INTO {} (username, password) VALUES ('{}', '{}')"""
                 .format(table_name, username, password))

        cursor.execute(query)
        db_connection.commit()
        result = cursor.fetchall()
        cursor.close()

        user_id = get_user_id(db_name, table_name, username)
        initial_user_statistics(db_name, statistics_table, user_id)

    except Exception:
        return {'message': 'Cannot create new user, try again later'}

    finally:
        if db_connection:
            db_connection.close()
    return result


def initial_user_statistics(db_name, table_name, user_id, points=0, life=90, level=1):
    """
    Inserts initial statistics for a new user into the specified database table.

    Args:
        db_name (str): The name of the database.
        table_name (str): The name of the table in the database.
        user_id (int): The user ID for which the statistics are inserted.
        points (int): The initial points for the user.
        life (int): The initial life for the user.
        level (int): The initial level for the user.

    Returns:
        list: A list of tuples representing the result of the insertion.

    Raises:
        Exception: If there is an error during the statistics insertion process.
    """
    db_connection = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)

        query = """INSERT INTO {} (user_id, points, life, level) VALUES 
        ('{}', '{}', '{}', '{}')""".format(table_name, user_id, points,
                                           life, level)
        
        cursor.execute(query)
        db_connection.commit()
        result = cursor.fetchall()
        cursor.close()

    except Exception:
        return {'message': 'Cannot add initial user statistics, try again later'}

    finally:
        if db_connection:
            db_connection.close()

    return result


def update_user_statistics(db_name, table_name, points, life, level, user_id):
    """
    Updates the statistics for a user in the specified database table.

    Args:
        db_name (str): The name of the database.
        table_name (str): The name of the table in the database.
        points (int): The updated points for the user.
        life (int): The updated life for the user.
        level (int): The updated level for the user.
        user_id (int): The user ID for which the statistics are updated.

    Raises:
        Exception: If there is an error during the statistics update process.
    """
    db_connection = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)

        query = """UPDATE {}
        SET points = {}, life = {}, level = {}
        WHERE user_id = {}""".format(table_name, points, life, level, user_id)
        
        cursor.execute(query)
        db_connection.commit()
        cursor.close()

    except Exception:
        return {'message': 'Cannot update user statistics right now, please try again later'}

    finally:
        if db_connection:
            db_connection.close()


def get_user_data(db_name, table_name, username):
    """
    Retrieves user data from the specified database table.

    Args:
        db_name (str): The name of the database.
        table_name (str): The name of the table in the database.
        username (str): The username for which the data is retrieved.

    Returns:
        list: A list of tuples containing user data (user_id, username, points, life, level).

    Raises:
        Exception: If there is an error during the user data retrieval process.
    """
    db_connection = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)

        query = """SELECT u.user_id, u.username, g.points, g.life, g.level 
        FROM {} as u 
        JOIN game_statistics as g
        ON u.user_id = g.user_id
        WHERE u.username = %s
        """.format(table_name)

        cursor.execute(query, (username,))
        user_data = cursor.fetchall()
        cursor.close()

    except Exception:
        return {'message': 'Cannot get user data, please try again later'}

    finally:
        if db_connection:
            db_connection.close()

    return user_data


def get_user_id(db_name, table_name, username):
    """
    Retrieves the user ID for a given username from the specified database table.

    Args:
        db_name (str): The name of the database.
        table_name (str): The name of the table in the database.
        username (str): The username for which the user ID is retrieved.

    Returns:
        int or None: The user ID if the username is found; otherwise, None.

    Raises:
        Exception: If there is an error during the user ID retrieval process.
    """
    db_connection = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)

        query = """SELECT user_id FROM {}
        WHERE username = %s
        """.format(table_name)
        cursor.execute(query, (username,))
        user_id = cursor.fetchall()
        cursor.close()

    except Exception:
        return {'message': 'Cannot retrieve user id, please try again later'}

    finally:
        if db_connection:
            db_connection.close()

    if not user_id:
        return
    return user_id[0][0]


def is_valid_username(username):
    """
    Checks if a username is valid based on certain criteria:
        Between 3 and 20 characters
        Contains only letters, numbers, and underscores

    Args:
        username (str): The username to be checked.

    Returns:
        bool: True if the username is valid; otherwise, False.
    """
    return re.match("^[a-zA-Z0-9_]{3,20}$", username) is not None


def is_valid_password(password):
    """
    Checks if a password is valid based on certain criteria:
        At least 8 characters long
        Contains at least one uppercase letter
        Contains at least one lowercase letter
        Contains at least one digit
        Contains at least one special character (e.g., !@#$%^&*)

    Args:
        password (str): The password to be checked.

    Returns:
        bool: True if the password is valid; otherwise, False.
    """
    return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            re.search("[!@#$%^&*]", password) is not None
    )


def hash_password(password):
    """
    Hashes a password using SHA-256 algorithm with a salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    salt = "weqcrh378451#&*$3i4ycn24utyvn6y34y!(@*74"

    hashed_password = hashlib.sha256((password + ":" + salt).encode('utf-8')).hexdigest()
    return hashed_password


def check_username_and_password(input_username, input_password):
    """
    Checks if the provided username and password are valid.

    Args:
        input_username (str): The input username.
        input_password (str): The input password.

    Returns:
        Tuple[str, str] or None: A tuple containing the valid username and password,
          or None if either the username or password is invalid.
    """
    if not is_valid_username(input_username) or not is_valid_password(input_password):
        return None
    return input_username, input_password


def is_user_exist_in_db(db_name, table_name, username):
    """
    Checks if a user with the given username exists in the specified database table.

    Args:
        db_name (str): The name of the database.
        table_name (str): The name of the table in the database.
        username (str): The username to check.

    Returns:
        bool: True if the user exists; otherwise, False.
    """
    if get_user_id(db_name, table_name, username) is None:
        return False
    return True


def add_valid_user_data_to_db(username, password):
    """
    Adds valid user data to the specified database if the user does not already exist.

    Args:
        username (str): The username of the user to be added.
        password (str): The password of the user to be added.

    Returns:
        None: If the user already exists.
        list: A list of tuples representing the result of the insertion.

    Raises:
        Exception: If there is an error during the user data addition process.
    """
    if is_user_exist_in_db(DB_NAME, users_table, username):
        return None

    hashed_password = hash_password(password)
    user = insert_new_user(DB_NAME, users_table, username, hashed_password)
    return user


def get_password_by_username(db_name, table_name, username):
    """
    Retrieve the hashed password for a given username from the database.

    Args:
        db_name (str): The name of the database.
        table_name (str): The name of the table in the database.
        username (str): The username for which the password is retrieved.

    Returns:
        Optional[str]: The hashed password if the username is found; otherwise, None.

    Raises:
        Exception: If there is an error during the password retrieval process.
    """
    user_id = None
    db_connection = None
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)

        query = """SELECT password FROM {}
        WHERE username = %s
        """.format(table_name)
        cursor.execute(query, (username,))
        user_id = cursor.fetchall()
        cursor.close()

    except Exception:
        return {'message': 'Cannot get password for this username, try again later'}

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    if not user_id:
        return
    return user_id[0][0]


def check_passwords(input_password, stored_password):
    """
    Check if the input password matches the stored hashed password.

    Args:
        input_password (str): The user-provided password.
        stored_password (str): The hashed password stored in the database.

    Returns:
        bool: True if the passwords match; otherwise, False.
    """
    hashed_input_password = hash_password(input_password)
    return hashed_input_password == stored_password
