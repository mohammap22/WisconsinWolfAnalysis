import unittest
from unittest import mock
from stats_wrapper import wrapper

if __name__ == '__main__':
    unittest.main()

#Define a class in which the tests will run
class Testwrapper(unittest.TestCase):
    #Smoke test
    def test_wrap_smoke(self): 
        wrapper()
        self.assertTrue(False)
    
    #------test user input --------
    def test_user_input(self):
        with self.assertRaises(ValueError):
            #Give bad user input