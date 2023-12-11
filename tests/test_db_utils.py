import unittest
from unittest.mock import MagicMock, patch
import mysql.connector
import logging
from mysql.connector import errorcode
from db.db_utils import connect_to_mysql_database, get_cursor_and_connection, create_database, connect_to_database_or_create_if_not_exists


class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor

    def test_connect_to_mysql_database_success(self):
        with unittest.mock.patch(
            'db.db_utils.mysql.connector.connect',
                return_value=self.mock_connection):
            db_connection = connect_to_mysql_database('test_db')

            self.assertIsNotNone(db_connection)

    @patch('db.db_utils.mysql.connector.connect')
    def test_connect_to_mysql_database(self, mock_connect):
        mock_connect.side_effect = mysql.connector.Error('Error connecting to the database')

        with self.assertRaises(mysql.connector.Error):
            connect_to_mysql_database('test_db')

        mock_connect.side_effect = ValueError('Invalid input value')

        with self.assertRaises(ValueError):
            connect_to_mysql_database('test_db')

        mock_connect.side_effect = Exception('Some unexpected error occurred')

        with self.assertRaises(Exception):
            connect_to_mysql_database('test_db')

    def test_get_cursor_and_connection(self):
        with unittest.mock.patch('db.db_utils.mysql.connector.connect',
                                 return_value=self.mock_connection):
            cursor, db_connection = get_cursor_and_connection('test_db')

            self.assertIsNotNone(cursor)
            self.assertIsNotNone(db_connection)



    def test_create_database(self):
        with unittest.mock.patch(
            'db.db_utils.mysql.connector.connect',
                return_value=self.mock_connection):

            db_name = 'test_db'

            create_database(db_name)

            expected_sql = "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name)

            self.mock_cursor.execute.assert_called_once_with(expected_sql)

    def test_connect_to_database_or_create_if_not_exists(self):
        with unittest.mock.patch(
            'db.db_utils.mysql.connector.connect',
                return_value=self.mock_connection):

            db_name = 'test_db'

            connect_to_database_or_create_if_not_exists(db_name)

            expected_sql = "USE {}".format(db_name)

            self.mock_cursor.execute.assert_called_once_with(expected_sql)


