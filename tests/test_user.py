import unittest
from unittest.mock import MagicMock, patch
from db.user import *


class TestUser(unittest.TestCase):

    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_get_cursor_and_connection = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor
        self.mock_get_cursor_and_connection.return_value = (
        self.mock_cursor, self.mock_connection)
        self.db_name = "test_db"
        self.table_name = "test_table"
        self.username = "test user"
        self.password = "Testtest123!"

    def test_insert_new_user_success(self):

        result = insert_new_user(self.db_name, self.table_name, self.username, self.password)

        expected_sql = """INSERT INTO {} (username, password) VALUES ('{}', '{}')""".format(self.table_name, self.username, self.password).replace("\n", "").replace(" ", "")
        "INSERTINTOtest_table(username,password)VALUES('testuser','Testtest123!'".replace("\n",
                 "").replace(
            " ", "")
        self.assertIsNotNone(result)
        self.assertEqual(expected_sql, )

    # @patch('db.history.get_cursor_and_connection')
    # def test_get_history_data_exception(self, mock_get_cursor_and_connection):
	#
    #     self.mock_cursor.execute.side_effect = Exception('Cannot get history data right now, try again later')
	#
    #     mock_get_cursor_and_connection.return_value = (
    #         self.mock_cursor, self.mock_connection)
	#
    #     result = get_history_data()
	#
    #     self.assertEqual(result, {'message': 'Cannot get history data right now, try again later'})