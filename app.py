#  manipulating with user's data in DB
from db_utils import get_cursor_and_connection


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
