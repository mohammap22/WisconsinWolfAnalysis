"""MODULE DOCSTRING GOES HERE"""

import unittest
from unittest import mock
from stats_module import hypothesis_function_one

class UnitTests(unittest.TestCase):
    """
    This class contains the unit tests for the stats module. When run,
    it executes the unit test functions below.
    This class also relies on the unittest module and TestCase class
    """

    @mock.patch('stats_module.input', create = True)
    def test_correlation_file_format(self, mocked_input):
        """This test verifies the file input into the correlation
        function is a csv"""
        mocked_input = './pdf/WolfReport2017.pdf'
        with self.assertRaises(TypeError):
            hypothesis_function_one()

    def test_correlation_three_columns(self, mocked_input):
        """This test verifies that the dataframe has 3 columns"""
        mocked_input = 'pdf/test_files/two_col_wolf_and_deer_pop.csv'
        with self.assertRaises(TypeError):
            hypothesis_function_one()

    def test_correlation_other_cols_numeric(self, mocked_input):
        """This test verifies that the second and third columns of the
        dataframe are numeric types so the correlation analysis can be
        run on them"""
        mocked_input = 'pdf/test_files/wolf_and_deer_pop_non_num.csv'
        with self.assertRaises(TypeError):
            hypothesis_function_one()
    
    def test_correlation_enough_entries(self, mocked_input):
        """This test verifies that the user has at least 2 rows in
        their data frame"""
        with self.assertRaises(TypeError):
            mocked_input = 'pdf/test_files/wolf_and_deer_pop_one_row.csv'
            hypothesis_function_one()
    
    def test_correlation_no_nulls(self, mocked_input):
        """This test verifies that no values in the data frame are
        null"""
        mocked_input = 'pdf/test_files/wolf_and_deer_pop_nulls.csv'
        with self.assertRaises(ValueError):
            hypothesis_function_one()

    def test_correlation_of_one(self, mocked_input):
        """This test verifies that we get a pearsons correlation of 
        1 given exactly the same data in x and y
        
        THIS TEST LIKELY NEEDS TO BE UPDATED AS I UNDERSTAND HOW
        PEARSONR WORKS"""
        mocked_input = 'pdf/test_files/wolf_and_deer_pop_one.csv'
        self.assertAlmostEqual(hypothesis_function_one(),1)


if __name__ == '__main__':
    unittest.main()