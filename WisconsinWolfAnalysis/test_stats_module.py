"""MODULE DOCSTRING GOES HERE"""

import unittest
#from unittest import mock
from stats_module import *

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

    #Logan's Stuff:
    #-----IO---------
    # def test_proportion_file_format(self):
    #     """Input file is csv"""
    #     with self.assertRaises(TypeError):
    #         hypothesis_function_three('./pdf/WolfReport2017.pdf')
    
    # def test_proportion_other_cols_numeric(self):
    #     """Columns are numeric"""
    #     with self.assertRaises(TypeError):
    #         hypothesis_function_three(
    #             'pdf/test_files/prop_of_wolves_non_numeric.csv')
    
    # def test_proportion_enough_entries(self):
    #     """DataFrame has at least 2 rows"""
    #     with self.assertRaises(ValueError):
    #         hypothesis_function_three(
    #             'pdf/test_files/prop_of_wolves_one_row.csv')
    
    # def test_proportion_enough_cols(self):
    #     """DataFrame has at least 3 columns"""
    #     with self.assertRaises(ValueError):
    #         hypothesis_function_three('prop_of_wolves_two_col.csv')
    
    # def test_proportion_no_nulls(self):
    #     """DataFrame has no null values"""
    #     with self.assertRaises(ValueError):
    #         hypothesis_function_three(
    #             'pdf/test_files/prop_of_wolves_nulls.csv')
    
    # #------- Stats --------
    # #That the total # obs in a row is always >= cells in other cols
    # def test_proportion_total_at_least_observed(self):
    #     """The 2nd (total observations) is >= corresponding observed with
    #     characteristic of interest"""
    #     with self.assertRaises(ValueError):
    #         hypothesis_function_three('prop_of_wolves_pop_issue.csv')
    

if __name__ == '__main__':
    unittest.main()