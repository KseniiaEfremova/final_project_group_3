from db.db_utils import get_cursor_and_connection

DB_NAME = "game_users_db"
users_table = "users"
statistics_table = "game_statistics"


def get_history_data():
    """
    Retrieves historical game statistics data for the top 8 players.

    Returns:
        list: A list of tuples containing historical data for each player.
              Each tuple includes the username, points, life, and level.
              The list is ordered by level and points in descending order.
    
    Raises:
        Exception: If there is an error retrieving data from the database.
    """
    cursor, db_connection = get_cursor_and_connection(DB_NAME)
    try:
        query = """SELECT u.username, g.points, g.life, g.level
                    FROM users AS u
                    JOIN game_statistics AS g ON u.user_id = g.user_id
                    ORDER BY g.level DESC, g.points DESC
                    LIMIT 8
                """
        cursor.execute(query)
        return cursor.fetchall()

    except Exception:
        return {'message': 'Cannot get history data right now, try again later'}
    
    finally:
        if db_connection:
            cursor.close()
            db_connection.close()
