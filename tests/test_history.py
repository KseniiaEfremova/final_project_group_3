import unittest
from unittest.mock import MagicMock, patch
from db.history import get_history_data


class TestHistory(unittest.TestCase):

    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor

    def test_get_history_data_success(self):
        with unittest.mock.patch(
            'db.db_utils.mysql.connector.connect',
                return_value=self.mock_connection):

            get_history_data()

            expected_sql = """SELECT u.username, g.points, g.life, g.level
                FROM users AS u
                JOIN game_statistics AS g ON u.user_id = g.user_id
                ORDER BY g.level DESC, g.points DESC
                LIMIT 8
            """.replace("\n", "").replace(" ", "")

            actual_sql = self.mock_cursor.execute.call_args[0][0].replace("\n",
                                                                          "").replace(
                " ", "")

            self.assertEqual(expected_sql, actual_sql)

    @patch('db.history.get_cursor_and_connection')
    def test_get_history_data_exception(self, mock_get_cursor_and_connection):

        self.mock_cursor.execute.side_effect = Exception('Cannot get history data right now, try again later')

        mock_get_cursor_and_connection.return_value = (
            self.mock_cursor, self.mock_connection)

        result = get_history_data()

        self.assertEqual(result, {'message': 'Cannot get history data right now, try again later'})