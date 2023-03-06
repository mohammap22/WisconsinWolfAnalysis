"""Module docstring goes here"""

import unittest
import pandas as pd
import camelot


class TestKnn(unittest.TestCase):
    "class docstring goes here"

    def camelot_smoke_test(self):
        """function docstring goes here"""
        data = camelot.read_pdf('pdf/Deer Health - Disease.pdf', pages='all')
        expected_result = pd.DataFrame[['', '', '', '', '', ''],
                                       ['', '', '', '', '', '']]
        self.assertAlmostEqual(data, expected_result, 1e-08)


if __name__ == '__main__':
    unittest.main()
