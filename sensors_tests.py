# try to check commit 2022.09.23

import sensors_main
import unittest
from unittest.mock import patch # needed for the example integration test case
import sys # needed for setting the command line parameters for test cases

# Unit tests implemented with Python's built-in unittest
# need to be classes, so here we use TestSensors class
# for the tests.
class TestSensors(unittest.TestCase):

    # The test case test_check_limits1 that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    
    # The test case test_check_limits2 that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect. To be implemented.
    def test_check_limits2(self):
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, False)
        
    # Placeholder for the test case test_check_limits3. To be designed
    # and implemented.
    # The test case test_check_limits3 that tests the check_limits
    # with incorrect inputs (lower limit 10 and higher limit 10) and
    # expects the method to return False, since the limits are
    # incorrect. To be implemented.
    def test_check_limits3(self):
        limits = [10, 10]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, False) 


    ##### for Case 1- 3  

    def test_check_limits1(self):
        limits = [18, 24]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)

    def test_check_limits2(self):
        limits = [20, 18]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, False)

    def test_check_limits3(self):
        limits = [15, 15]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, False) 

    def test_check_limits_2_iterms1(self):
        limits = [15]
        result = sensors_main.check_limits_2_iterms(limits)
        self.assertTrue(result, False) 

    def test_check_limits_2_iterms2(self):
        limits = [10,12]
        result = sensors_main.check_limits_2_iterms(limits)
        self.assertTrue(result, True) 

    ##### for Case 1- 3 



    # Placeholder for the test case test_check_limits_2_iterm1. 
    # To be designed and implemented.
    # The test case test_check_limits_2_iterm1 that tests 
    # the test_check_limits_2_iterm1
    # with incorrect inputs (1 iterm in limits) and
    # expects the method to return False, since the limits are
    # incorrect. To be implemented.
    def test_check_limits_2_iterms1(self):
        limits = [10]
        result = sensors_main.check_limits_2_iterms(limits)
        self.assertTrue(result, False) 

    # Placeholder for the test case test_check_limits_2_iterm2. 
    # To be designed and implemented.
    # The test case test_check_limits_2_iterm1 that tests 
    # the test_check_limits_2_iterm1
    # with incorrect inputs (1 iterm in limits) and
    # expects the method to return False, since the limits are
    # incorrect. To be implemented.
    def test_check_limits_2_iterms2(self):
        limits = [2,10]
        result = sensors_main.check_limits_2_iterms(limits)
        self.assertTrue(result, True) 

    #######################################
    # Example of an integration test case #
    #######################################

    # The test case test_check_limits_integration1 that tests
    # the check_limits from main.

    # Redirect console output to sys.stdout in order to
    # check it from the test cases (here, from the example
    # integration test case). Notice the use of mock_print
    # as a parameter of the test case function.
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [22], [18]]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

    
    # The test case test_check_limits_integration2 that tests
    # the check_limits from main.

    # Redirect console output to sys.stdout in order to
    # check it from the test cases (here, from the example
    # integration test case). Notice the use of mock_print
    # as a parameter of the test case function.
    @patch('builtins.print')
    def test_check_limits_integration2(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [10], [10]]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

    
    # The test case test_check_limits_integration3 that tests
    # the check_limits from main.

    # Redirect console output to sys.stdout in order to
    # check it from the test cases (here, from the example
    # integration test case). Notice the use of mock_print
    # as a parameter of the test case function.
    @patch('builtins.print')
    def test_check_limits_integration3(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [22], [18]]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

        # If you want to see what is in mock_print, you can use the following
        # (requires that there is import sys as this module has because this
        # test case sets the command line arguments that are in sys.argv)
        # sys.stdout.write(str(mock_print.call_args) + "\n")
        # sys.stdout.write(str(mock_print.call_args_list) + "\n")

    
    ##### For case 1-3


    @patch('builtins.print')
    def test_check_limits_integration4(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [20], [18]]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")
    

    @patch('builtins.print')
    def test_check_limits_integration5(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [15], [15]]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

    @patch('builtins.print')
    def test_check_limits_integration6(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [18], [24]]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")
    @patch('builtins.print')
    def test_check_limits_integration7(self, mock_print):
        # set command line parameters, since they are where main gets the
        # min and max temperature settings
        sys.argv = [["sensors_main.py"], [18], []]

        # call main with the command line parameters set up
        sensors_main.main()

        # check that the console output is the expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")
    ##### For case 1-3

if __name__ == '__main__':
    unittest.main()