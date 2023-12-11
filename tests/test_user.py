# import unittest
# from unittest.mock import MagicMock
# from user import insert_new_user, initial_user_statistics
#
#
# class TestDatabaseConnection(unittest.TestCase):
#
#     def setUp(self):
#         self.mock_connection = MagicMock()
#         self.mock_cursor = MagicMock()
#         self.mock_connection.cursor.return_value = self.mock_cursor
#
#
#     def test_insert_new_user(self):
#         with unittest.mock.patch(
#             'db_utils.mysql.connector.connect',
#                 return_value=self.mock_connection):
#             db_name = "test_db"
#             table_name = "test_users"
#             username = "Test User"
#             password = "Testtest123!"
#
#             insert_new_user(db_name, table_name, username, password)
#             expected_sql = """INSERT INTO {} (username, password) VALUES ('{}', '{}')""".format(table_name, username, password)
#
#             self.mock_cursor.execute.assert_called_once_with(expected_sql)
#
#     def test_initial_user_statistics(self):
#         with unittest.mock.patch(
#                 'db_utils.mysql.connector.connect',
#                 return_value=self.mock_connection):
#             db_name = "test_db"
#             table_name = "test_users"
#             user_id = 123
#             points = 0
#             life = 90
#             level = 1
#
#             initial_user_statistics(db_name, table_name, user_id)
#
#             expected_sql = """INSERT INTO {} (user_id, points, life, level) VALUES ('{}', '{}', '{}', '{}')""".format(
#                 table_name, user_id, points, life, level)
#
#             self.mock_cursor.execute.assert_called_once_with(expected_sql)