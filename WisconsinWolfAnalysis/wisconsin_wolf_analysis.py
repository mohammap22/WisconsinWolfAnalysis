"""
Primary Script for Analyzing the Impact of Wolves in Wisconsin
"""
import glob
import re

import pandas as pd

from data.data_processing import (pdf_parser,
                                  data_extractor,
                                  combine_csv_files)


def run_data_extraction_and_combination():
    '''
    This program extracts data from the parsed pdfs, and the yearly
    chronic wasting disease data and combines it into .csv files that
    can easily be ingested an analyzed in the statistical analysis
    module.
    '''

    # Combined all of the yearly deer chronic wasting disease files into one
    # csv by calculating a yearly total on tested and positive deer regardless
    # of location.
    cwd_csv_files = glob.glob('./csv/deer_chronic_wasting_disease/*.csv')
    cwd_list = []

    for file in cwd_csv_files:
        file_year = re.search(r"[1-2][0-9]{3}", file)
        df_temp = pd.read_csv(file)
        num_tested_samples = df_temp['# Analyzed'].sum()
        num_positive = df_temp['Positive for CWD'].sum()
        percent_positive = num_positive/num_tested_samples * 100
        cwd_list.append([file_year[0], num_tested_samples, num_positive,
                         percent_positive])

    cwd_df = pd.DataFrame(cwd_list)
    cwd_df.columns = ['year', 'number of samples', 'CWD Positive',
                      'Percent CWD Positive']
    cwd_df.to_csv('./csv/deer_chronic_wasting_disease_by_year.csv',
                  index=False)

    # Run the data extractor to pull data from the parsed pdfs and combine it
    # into a single csv file for each requested parameter.
    data_extractor(pdf_list, './pdf', 'Cattle Killed', 'cattle killed',
                   'csv/cattle_killed_by_year.csv')
    data_extractor(pdf_list, '../pdf/', 'Statewide', 'observations',
                   'csv/wolf_observations_by_year.csv')

    # Run the csv combiner to combine data from multiple csv files to prepare
    # it to be ingested and analyzed by the statistical tests.
    combine_csv_files('csv/wolf_population_by_year.csv', 'wolf population',
                      'csv/deer_population_by_year.csv', 'deer population',
                      'pdf/wolf_and_deer_pop.csv')
    combine_csv_files('csv/wolf_population_by_year.csv', 'wolf population',
                      'csv/cattle_killed_by_year.csv', 'cattle killed',
                      'pdf/wolf_pop_cattle_killed.csv')
    combine_csv_files('csv/wolf_population_by_year.csv', 'wolf population',
                      'csv/deer_chronic_wasting_disease_by_year.csv',
                      'CWD Positive', 'pdf/wolf_pop_cwd_positive.csv')
    combine_csv_files('csv/wolf_population_by_year.csv', 'wolf population',
                      'csv/deer_harvest_by_year.csv', 'deer harvest',
                      'pdf/wolf_pop_deer_harvest.csv')
    combine_csv_files('csv/wolf_population_by_year.csv', 'wolf population',
                      'csv/dogs_killed_by_year.csv', 'dogs killed',
                      'pdf/wolf_pop_dogs_killed.csv')
    combine_csv_files('csv/wolf_population_by_year.csv', 'wolf population',
                      'csv/hunter_observed_deer_by_year.csv', 'hunter survey',
                      'pdf/wolf_pop_hunter_observations.csv')
    combine_csv_files('csv/wolf_population_by_year.csv', 'wolf population',
                      'csv/wolf_investigations_by_year.csv', 'investigations',
                      'pdf/wolf_pop_investigations.csv')
    combine_csv_files('csv/wolf_population_by_year.csv', 'wolf population',
                      'csv/wolf_observations_by_year.csv', 'observations',
                      'pdf/wolf_pop_observations.csv')


if __name__ == '__main__':

    PARSE_PDFS = False
    UPDATE_DATA = False

    pdf_list = glob.glob('pdf/*.pdf')

    if PARSE_PDFS:
        pdf_parser(pdf_list, 'pdf', show_warnings=False)

    if UPDATE_DATA:
        run_data_extraction_and_combination()
