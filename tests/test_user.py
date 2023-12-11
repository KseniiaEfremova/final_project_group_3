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
        self.db_name = "game_users_db"
        self.users_table = "users"
        self.statistics_table = "game_statistics"
        self.username = "test user"
        self.password = "Testtest123!"

    @patch('db.user.initial_user_statistics')
    @patch('db.user.get_user_id')
    def test_insert_new_user_success(self, mock_initial_user_stats, mock_user_id):
        with unittest.mock.patch(
            'db.db_utils.mysql.connector.connect',
                return_value=self.mock_connection):
            result = insert_new_user(self.db_name, self.statistics_table,
                                     self.username, self.password)
            expected_sql = (
                """INSERT INTO {} (username, password) VALUES ('{}', '{}')"""
                .format(self.statistics_table, self.username,
                        self.password)).replace("\n", "").replace(" ", "")

            actual_sql = self.mock_cursor.execute.call_args[0][0].replace("\n",
                                                                          "").replace(
                " ", "")

            self.assertIsNotNone(result)
            self.assertEqual(expected_sql, actual_sql)

    @patch('db.history.get_cursor_and_connection')
    def test_insert_new_user_exception(self, mock_get_cursor_and_connection):

        self.mock_cursor.execute.side_effect = Exception('Cannot create new user, try again later')

        mock_get_cursor_and_connection.return_value = (
            self.mock_cursor, self.mock_connection)

        result = insert_new_user(self.db_name, self.statistics_table,
                                     self.username, self.password)

        self.assertEqual(result, {'message': 'Cannot create new user, try again later'})
    @patch('db.user.get_user_id')
    def test_initial_user_statistics_success(self, mock_user_id):
        with unittest.mock.patch(
            'db.db_utils.mysql.connector.connect',
                return_value=self.mock_connection):

            initial_user_statistics(self.db_name, self.statistics_table, mock_user_id, points=0, life=90, level=1)

            expected_sql = """INSERT INTO {} (user_id, points, life, level) VALUES 
                ('{}', '{}', '{}', '{}')""".format(self.statistics_table,
                                                   mock_user_id, 0,
                                                    90, 1).replace(
                "\n", "").replace(" ", "")

            actual_sql = self.mock_cursor.execute.call_args[0][0].replace("\n",
                                                                          "").replace(
                " ", "")

            self.assertEqual(expected_sql, actual_sql)

    @patch('db.user.get_user_id')
    @patch('db.history.get_cursor_and_connection')
    def test_initial_users_statistics_exception(self, mock_user_id, mock_get_cursor_and_connection):

        self.mock_cursor.execute.side_effect = Exception('Cannot add initial user statistics, try again later')

        mock_get_cursor_and_connection.return_value = (
            self.mock_cursor, self.mock_connection)

        result =  initial_user_statistics(self.db_name, self.statistics_table, mock_user_id, points=0, life=90, level=1)

        self.assertEqual(result, {'message': 'Cannot add initial user statistics, try again later'})

    @patch('db.user.get_user_id')
    def test_update_user_statistics_success(self, mock_user_id):
        with unittest.mock.patch(
            'db.db_utils.mysql.connector.connect',
                return_value=self.mock_connection):

            update_user_statistics(self.db_name, self.statistics_table, 900, 68, 2, mock_user_id)

            expected_sql = """UPDATE {}
        SET points = {}, life = {}, level = {}
        WHERE user_id = {}""".format(self.statistics_table, 900, 68, 2, mock_user_id).replace(
                "\n", "").replace(" ", "")

            actual_sql = self.mock_cursor.execute.call_args[0][0].replace("\n",
                                                                          "").replace(
                " ", "")

            self.assertEqual(expected_sql, actual_sql)

    @patch('db.user.get_user_id')
    @patch('db.history.get_cursor_and_connection')
    def test_update_users_statistics_exception(self, mock_user_id, mock_get_cursor_and_connection):

        self.mock_cursor.execute.side_effect = Exception('Cannot update user statistics right now, please try again later')

        mock_get_cursor_and_connection.return_value = (
            self.mock_cursor, self.mock_connection)

        result =  update_user_statistics(self.db_name, self.statistics_table, 900, 68, 2, mock_user_id)
        self.assertEqual(result, {'message': 'Cannot update user statistics right now, please try again later'})