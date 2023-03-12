"""
unittest for testing
os to create and remove files
shuttil to remove file trees
pdf_parser and combine_csv_files are function being tested
"""
import os
import shutil
import unittest

import pandas as pd

from Data.data_processing import pdf_parser, combine_csv_files


class TestPdfParser(unittest.TestCase):
    """Test suite for pdf_parser function"""

    @classmethod
    def setUpClass(cls):
        """Set up pdf parser and data"""
        cls.pdf_files_list = ["test_files/data_test_files/WolfReport2021.pdf",
                              "test_files/data_test_files/WolfReport2022.pdf"]
        pdf_parser(cls.pdf_files_list, "test_files/data_test_files",
                   show_warnings=False)

    @classmethod
    def tearDownClass(cls):
        """Clean up test data"""
        shutil.rmtree("test_files/data_test_files/WolfReport2022")
        shutil.rmtree("test_files/data_test_files/WolfReport2021")

    def test_directory_creation(self):
        """
        Given a list with one PDF file
        When pdf_parser is called
        Then it should create one directory with the same name as the PDF file
        """
        self.assertTrue(os.path.exists("test_files/data_test_files/" +
                                       "WolfReport2022"))

    def test_good_data_creation(self):
        """
        Given a list with one PDF file
        When pdf_parser is called
        Then it should create a subdirectory "GoodData" in the directory
        And the subdirectory should contain at least one CSV file
        """
        self.assertTrue(os.path.exists("test_files/data_test_files/" +
                                       "WolfReport2022/GoodData"))
        good_data_files = os.listdir("test_files/data_test_files/" +
                                     "WolfReport2022/GoodData")
        self.assertTrue(len(good_data_files) >= 1)
        for file in good_data_files:
            self.assertTrue(file.endswith(".csv"))

    def test_bad_data_creation(self):
        """
        Given a list with one PDF file
        When pdf_parser is called
        Then it should create a subdirectory "BadData" in the directory
        And the subdirectory should contain at least one CSV file
        """
        self.assertTrue(os.path.exists("test_files/data_test_files/" +
                                       "WolfReport2022/BadData"))
        bad_data_files = os.listdir("test_files/data_test_files/" +
                                    "WolfReport2022/BadData")
        self.assertTrue(len(bad_data_files) >= 1)
        for file in bad_data_files:
            self.assertTrue(file.endswith(".csv"))

    def test_merged_data_creation(self):
        """
        Given a list with one PDF file
        When pdf_parser is called
        Then it should create a subdirectory "MergedData" in the directory
        And the subdirectory should contain at least one CSV file
        """
        self.assertTrue(os.path.exists("test_files/data_test_files/" +
                                       "WolfReport2022/Merged_Data"))
        merged_data_files = os.listdir("test_files/data_test_files/" +
                                       "WolfReport2022/Merged_Data")
        print(merged_data_files)
        self.assertTrue(len(merged_data_files) >= 1)
        for file in merged_data_files:
            self.assertTrue(file.endswith(".csv"))


class TestCombineCsvFiles(unittest.TestCase):
    '''
    Test suite for combine_csv_files
    '''

    def test_bad_file_name_1(self):
        '''
        This test case ensures that a TypeError is raised if
        combine_csv_files is called with an invalid file name for
        the first csv file.
        '''
        with self.assertRaises(TypeError):
            combine_csv_files('bad_file_name',
                              'wolf population',
                              'test_files/data_test_files/' +
                              'deer_population_by_year.csv',
                              'deer population',
                              'test_files/data_test_files/' +
                              'test_out.csv')

    def test_bad_file_name_2(self):
        '''
        This test case ensures that a TypeError is raised if
        combine_csv_files is called with an invalid file name for
        the second csv file.
        '''
        with self.assertRaises(TypeError):
            combine_csv_files('test_files/data_test_files/' +
                              'wolf_population_by_year.csv',
                              'wolf population',
                              'test_files/data_test_files/' +
                              'missing_file',
                              'deer population',
                              'test_files/data_test_files/' +
                              'test_out.csv')

    def test_no_year_file_1(self):
        '''
        This test case ensures that a ValueError is raised if
        combine_csv_files is called and the first file does not contain
        a column labeled "year"
        '''
        with self.assertRaises(ValueError):
            combine_csv_files('test_files/data_test_files/missing_year.csv',
                              'wolf population',
                              'test_files/data_test_files/' +
                              'deer_population_by_year.csv',
                              'deer population',
                              'test_files/data_test_files/' +
                              'test_out.csv')

    def test_no_year_file_2(self):
        '''
        This test case ensures that a ValueError is raised if
        combine_csv_files is called and the second file does not contain
        a column labeled "year"
        '''
        with self.assertRaises(ValueError):
            combine_csv_files('test_files/data_test_files/' +
                              'wolf_population_by_year.csv',
                              'wolf population',
                              'test_files/data_test_files/missing_year.csv',
                              'deer population',
                              'test_files/data_test_files/' +
                              'test_out.csv')

    def test_missing_column_name_1(self):
        '''
        This test case ensures that a ValueError is raised if
        combine_csv_files is called and the user-provided column name is
        not in the first .csv file.
        '''
        with self.assertRaises(ValueError):
            combine_csv_files('test_files/data_test_files/' +
                              'wolf_population_by_year.csv',
                              'bad column',
                              'test_files/data_test_files/' +
                              'deer_population_by_year.csv',
                              'deer population',
                              'test_files/data_test_files/' +
                              'test_out.csv')

    def test_missing_column_name_2(self):
        '''
        This test case ensures that a ValueError is raised if
        combine_csv_files is called and the user-provided column name is
        not in the second .csv file.
        '''
        with self.assertRaises(ValueError):
            combine_csv_files('test_files/data_test_files/' +
                              'wolf_population_by_year.csv',
                              'wolf population',
                              'test_files/data_test_files/' +
                              'deer_population_by_year.csv',
                              'bad column',
                              'test_files/data_test_files/' +
                              'test_out.csv')

    def test_year_reduction(self):
        '''
        This checks to make sure only matching years from both files
        are included in the output file by checking a new result
        against an expected values dataframe.
        '''
        combine_csv_files('test_files/data_test_files/' +
                          'wolf_population_by_year.csv',
                          'wolf population',
                          'test_files/data_test_files/' +
                          'deer_population_by_year.csv',
                          'deer population',
                          'test_files/data_test_files/' +
                          'test_out.csv')

        result = pd.read_csv('test_files/data_test_files/test_out.csv')

        key = pd.read_csv('test_files/data_test_files/' +
                          'wolf_and_deer_pop_KEY.csv')
        check_equal = key.equals(result)
        self.assertTrue(check_equal,
                        msg="Result does not equal the expected result")


if __name__ == '__main__':
    unittest.main()
