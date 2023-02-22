# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:31:46 2023

@author: Kevin Torrico
"""

# Tabula package installation instructions can be found here:
# https://pypi.org/project/tabula-py/

import tabula

# print(tabula.environment_info())

wolf_pdf_path = "WolfReport/Wisconsin_Gray_Wolf_Report_2022.pdf"
wolf_report_data = tabula.read_pdf(wolf_pdf_path, pages="all",
                                   stream=True, silent=True)
print(wolf_report_data[0])


deer_pdf_path = "DeerHarvest/Marquette_Deer_Metric_Report.pdf"
deer_report_data = tabula.read_pdf(deer_pdf_path, pages="all",
                                   lattice=True, silent=True)
print(deer_report_data[0])
