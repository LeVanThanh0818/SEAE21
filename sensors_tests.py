# try to check commit 2022.09.23

import sensors_main
import unittest

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
<<<<<<< HEAD
=======
    

>>>>>>> b9b531994565224ee4cc998e832a77e64ee852a9
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

if __name__ == '__main__':
    unittest.main()