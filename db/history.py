#  manipulating with user's data in DB
from db.db_utils import get_cursor_and_connection

DB_NAME = "game_users_db"
users_table = "users"
statistics_table = "game_statistics"

def get_history_data():
    cursor, db_connection = get_cursor_and_connection("game_users_db")
    try:
        query = """SELECT u.username, g.points, g.life, g.level
                    FROM users AS u
                    JOIN game_statistics AS g ON u.user_id = g.user_id
                    ORDER BY g.level DESC, g.points DESC
                    LIMIT 8
                """
        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        return {'message': 'Cannot get history data right now, try again later'}
    
    finally:
        cursor.close()
        db_connection.close()
