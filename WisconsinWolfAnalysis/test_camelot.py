# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:30:56 2023

@author: kltor
"""
import pandas as pd
import unittest

import camelot


class TestKnn(unittest.TestCase):

    def camelot_smoke_test(self):
        data = camelot.read_pdf('pdf/Deer Health - Disease.pdf', pages='all')
        expected_result = pd.DataFrame[['', '', '', '', '', ''],
                                       ['', '', '', '', '', '']]
        self.assertAlmostEqual(data, expected_result, 1e-08)


if __name__ == '__main__':
    unittest.main()
