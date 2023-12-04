import os
import unittest


def run_tests():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    tests_directory = os.path.join(script_directory, 'tests')
    loader = unittest.TestLoader()
    suite = loader.discover(tests_directory)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return result


if __name__ == '__main__':
    test_result = run_tests()