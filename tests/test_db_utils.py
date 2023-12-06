import unittest
from unittest.mock import MagicMock
from db_utils import connect_to_mysql_database, get_cursor_and_connection, create_database, connect_to_database_or_create_if_not_exists


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