import unittest
import os
import shutil
from pdf_parser import pdf_parser


class TestPdfParser(unittest.TestCase):
    """Test suite for pdf_parser function"""
    
    def test_file_creation(self):
        """
        Given a list with one PDF file
        When pdf_parser is called
        Then it should create one file with three subfolders:
        GoodData, BadData, and MergedData
        each folder should contain at least one csv 
        no other file type should exist 
        """
        pdf_files_list = ["pdf/Wisconsin_Gray_Wolf_Report_2022.pdf"]
        pdf_parser(pdf_files_list,".")

        # Assert that the file and directories were created as expected
        self.assertTrue(os.path.exists("Wisconsin_Gray_Wolf_Report_2022"))
        self.assertTrue(os.path.exists("Wisconsin_Gray_Wolf_Report_2022/GoodData"))
        self.assertTrue(os.path.exists("Wisconsin_Gray_Wolf_Report_2022/BadData"))
        self.assertTrue(os.path.exists("Wisconsin_Gray_Wolf_Report_2022/Merged_Data"))

        # Assert that the subfolders contain CSV files
        good_data_files = os.listdir("Wisconsin_Gray_Wolf_Report_2022/GoodData")
        bad_data_files = os.listdir("Wisconsin_Gray_Wolf_Report_2022/BadData")
        merged_data_files = os.listdir("Wisconsin_Gray_Wolf_Report_2022/Merged_Data")
        self.assertTrue(len(good_data_files) >= 1)
        self.assertTrue(len(bad_data_files) >= 1)
        self.assertTrue(len(merged_data_files) >= 1)

        # Assert that there are no files other than CSV files in the subfolders
        for file in good_data_files:
            self.assertTrue(file.endswith(".csv"))
        for file in bad_data_files:
            self.assertTrue(file.endswith(".csv"))
        for file in merged_data_files:
            self.assertTrue(file.endswith(".csv"))
        
        #Delete file tree
        shutil.rmtree("Wisconsin_Gray_Wolf_Report_2022")

if __name__ == '__main__':
    unittest.main()
