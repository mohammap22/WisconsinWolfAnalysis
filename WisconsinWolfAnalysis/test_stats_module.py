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

    def test_correlation_file_format(self):
        """Input file is csv"""
        with self.assertRaises(TypeError):
            hypothesis_function_one('./pdf/WolfReport2017.pdf')

    def test_correlation_three_columns(self):
        """Dataframe has 3 columns"""
        with self.assertRaises(TypeError):
            hypothesis_function_one(
                'pdf/test_files/two_col_wolf_and_deer_pop.csv')

    def test_correlation_other_cols_numeric(self):
        """Second and third columns are numeric"""
        with self.assertRaises(TypeError):
            hypothesis_function_one(
                'pdf/test_files/wolf_and_deer_pop_non_num.csv')
    
    def test_correlation_enough_entries(self):
        """Data frame has at least 2 rows"""
        with self.assertRaises(TypeError):
            hypothesis_function_one(
                'pdf/test_files/wolf_and_deer_pop_one_row.csv')
    
    def test_correlation_no_nulls(self):
        """Data frame has no null values"""
        with self.assertRaises(ValueError):
            hypothesis_function_one(
                'pdf/test_files/wolf_and_deer_pop_nulls.csv')

    '''def test_correlation_of_one(self):
        """This test verifies that we get a pearsons correlation of 
        1 given exactly the same data in x and y
        
        THIS TEST LIKELY NEEDS TO BE UPDATED AS I UNDERSTAND HOW
        PEARSONR WORKS"""
        self.assertAlmostEqual(hypothesis_function_one(
            'pdf/test_files/wolf_and_deer_pop_one.csv'),1)'''


if __name__ == '__main__':
    unittest.main()