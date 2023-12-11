import unittest
from unittest.mock import MagicMock
from db.db_utils import connect_to_mysql_database, get_cursor_and_connection, create_database, connect_to_database_or_create_if_not_exists


class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor

    def test_connect_to_mysql_database(self):
        try:
            with unittest.mock.patch(
                    'db_utils.mysql.connector.connect',
                    return_value=self.mock_connection):
                db_connection = connect_to_mysql_database('test_db')
                self.assertIsNotNone(
                    db_connection)
                db_connection.close()
        except Exception as e:
            self.fail(f"Failed to connect to the database: {e}")

    def test_get_cursor_and_connection(self):
        try:
            with unittest.mock.patch('db_utils.mysql.connector.connect', return_value=self.mock_connection):
                cursor, db_connection = get_cursor_and_connection('test_db')
                self.assertIsNotNone(cursor)
                self.assertIsNotNone(db_connection)
                cursor.close()
                db_connection.close()
        except Exception as e:
            self.fail(f"Failed to get cursor and connection: {e}")

    def test_create_database(self):
        try:
            with unittest.mock.patch(
                'db_utils.mysql.connector.connect',
                    return_value=self.mock_connection):

                db_name = 'test_db'

                create_database(db_name)

                expected_sql = "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name)
                self.mock_cursor.execute.assert_called_once_with(expected_sql)
        except Exception as e:
            self.fail("Failed creating database: {}".format(e))

    def test_connect_to_database_or_create_if_not_exists(self):
        try:
            with unittest.mock.patch(
                'db_utils.mysql.connector.connect',
                    return_value=self.mock_connection):

                db_name = 'test_db'

                connect_to_database_or_create_if_not_exists(db_name)

                expected_sql = "USE {}".format(db_name)
                self.mock_cursor.execute.assert_called_once_with(expected_sql)
        except Exception as e:
            self.fail("Database {} does not exist.".format(db_name))

