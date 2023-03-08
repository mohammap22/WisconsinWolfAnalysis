"""
unittest for testing
os to create and remove files
shuttil to remove file trees
pdf_parser is function being tested
"""
import unittest
import os
import shutil
from pdf_parser import pdf_parser


class TestPdfParser(unittest.TestCase):
    """Test suite for pdf_parser function"""

    @classmethod
    def setUpClass(cls):
        """Set up pdf parser and data"""
        cls.pdf_files_list = ["pdf/WolfReport2021.pdf",
                              "pdf/WolfReport2022.pdf"]
        pdf_parser(cls.pdf_files_list, ".")

    @classmethod
    def tearDownClass(cls):
        """Clean up test data"""
        shutil.rmtree("WolfReport2022")

    def test_directory_creation(self):
        """
        Given a list with one PDF file
        When pdf_parser is called
        Then it should create one directory with the same name as the PDF file
        """
        self.assertTrue(os.path.exists("WolfReport2022"))

    def test_good_data_creation(self):
        """
        Given a list with one PDF file
        When pdf_parser is called
        Then it should create a subdirectory "GoodData" in the directory
        And the subdirectory should contain at least one CSV file
        """
        self.assertTrue(os.path.exists("WolfReport2022/" +
                                       "GoodData"))
        good_data_files = os.listdir("WolfReport2022/" +
                                     "GoodData")
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
        self.assertTrue(os.path.exists("WolfReport2022/" +
                                       "BadData"))
        bad_data_files = os.listdir("WolfReport2022/" +
                                    "BadData")
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
        self.assertTrue(os.path.exists("WolfReport2022/" +
                                       "Merged_Data"))
        merged_data_files = os.listdir("WolfReport2022/" +
                                       "Merged_Data")
        print(merged_data_files)
        self.assertTrue(len(merged_data_files) >= 1)
        for file in merged_data_files:
            self.assertTrue(file.endswith(".csv"))


if __name__ == '__main__':
    unittest.main()
