import unittest
from unittest.mock import MagicMock
from db.history import get_history_data


class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor

    def test_get_history_data(self):
        with unittest.mock.patch(
            'db_utils.mysql.connector.connect',
                return_value=self.mock_connection):

            get_history_data()
            expected_sql = """SELECT u.username, g.points, g.life, g.level
                FROM users AS u
                JOIN game_statistics AS g ON u.user_id = g.user_id
                ORDER BY g.level DESC, g.points DESC
                LIMIT 8
            """

            self.mock_cursor.execute.assert_called_once_with(expected_sql)

