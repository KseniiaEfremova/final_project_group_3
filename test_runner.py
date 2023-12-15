import os
import unittest
import coverage


def run_tests():
    """
    Runs the unit tests for the project and generates a coverage report.

    This function changes the current working directory to the script's directory,
    discovers and runs unit tests in the 'tests' directory, and generates a coverage report.

    Returns:
        unittest.TextTestResult: The result of running the unit tests.
    """
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)
    tests_directory = os.path.join(script_directory, 'tests')

    cov = coverage.Coverage()
    cov.start()

    loader = unittest.TestLoader()
    suite = loader.discover(tests_directory)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    cov.stop()
    cov.report()

    return result


if __name__ == '__main__':
    run_tests()
