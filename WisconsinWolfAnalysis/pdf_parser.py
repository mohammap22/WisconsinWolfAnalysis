"""
Importing os for file creation
Importion re for regex
importing glob for filesystem
Importing Pandas for dataframe parsing
Importing Camelot for PDF parsing
"""
import os
import re
import glob
import pandas as pd
import camelot

# pylint: disable-msg=too-many-locals
# pylint: disable-msg=too-many-nested-blocks
# pylint: disable-msg=too-many-branches
def pdf_parser(pdf_files_list, pdf_folder):
    """
    Extracts data tables from a list of PDF files. For each file, it
    creates a folder in the pdf_folder directory. Within that folder for
    each file, folders are created for good, bad, and merged data files,
    and the tables extracted from the PDF are saved into the good folder
    if they contain data or the bad folder if they are empty.
    Inputs:
    :pdf_files_list - a list of files from which data will be extracted
    :pdf_folder - a folder location to save the output files.
    Ouputs:
    :nothing is returned by this function, but it will create folders
    and data files of the data in the pdfs that are ind pdf_file_list
    """

    dataframes = {}

    for file_location in pdf_files_list:
        # Create a new directory based on the file name
        file_name = os.path.basename(file_location)
        print(file_name)
        pdf_report_year = re.search(r"[1-2][0-9]{3}", file_name)
        directory_name = os.path.splitext(file_name)[0]
        os.makedirs(os.path.join(pdf_folder, directory_name), exist_ok=True)

        os.makedirs(os.path.join(pdf_folder, directory_name,
                                 "GoodData"), exist_ok=True)
        os.makedirs(os.path.join(pdf_folder, directory_name,
                                 "BadData"), exist_ok=True)
        merged_data_dir = os.path.join(pdf_folder, directory_name,
                                       "Merged_Data")
        os.makedirs(merged_data_dir, exist_ok=True)
        tables = camelot.read_pdf(
            file_location, pages="all", flavor='stream', edge_tol=500)

        for i, table in enumerate(tables):
            given_df = table.df.applymap(is_sentence)

            non_empty_row_idx = 0
            for row_idx, row in enumerate(given_df.values):
                if not all(cell == '' for cell in row):
                    non_empty_row_idx = row_idx
                    break
            column_names = given_df.iloc[non_empty_row_idx]
            given_df = given_df.iloc[non_empty_row_idx +
                                     1:].reset_index(drop=True)
            given_df.columns = column_names

            non_null_cols = given_df.columns[given_df.notnull().any()].tolist()

            file_name = make_file_names(non_null_cols)

            has_useful_values = False
            for column in given_df.columns:
                column_values = given_df[column].values
                for value in column_values:
                    if isinstance(value, int) or (isinstance(value, str)
                                                  and value.strip() != ''):
                        has_useful_values = True
                        break

            if pdf_report_year[0] is not None:
                given_df['PDF_Year'] = int(pdf_report_year[0])

            if has_useful_values:
                cols = tuple(given_df.columns)
                if cols not in dataframes:
                    dataframes[cols] = []
                dataframes[cols].append(given_df)

                for cols, dfs, in dataframes.items():
                    if len(dfs) == 1:
                        given_df = dfs[0]
                        # Save the dataframe as a CSV file
                        # in the "GoodData" directory
                        given_df.to_csv(os.path.join(
                            pdf_folder, directory_name, "GoodData",
                            file_name + str(i) + '.csv'), index=False)
                    else:
                        merged_df = pd.concat(dfs, ignore_index=True)
                        col_names = ""
                        for col in cols:
                            col_names = col_names + col
                        # col_names = {cols}
                        col_names = col_names.replace("%", "percent")
                        col_names = col_names.replace("#", "number")
                        col_names = col_names.replace("w/", "with")
                        csv_file = os.path.join(merged_data_dir,
                                                "data_" + col_names + ".csv")
                        merged_df.to_csv(csv_file, index=False)
            else:
                # Save the dataframe as a CSV file in the "BadData"
                # directory
                given_df.to_csv(os.path.join(
                    pdf_folder, directory_name, "BadData", file_name
                    + str(i) + '.csv'), index=False)

def make_file_names(cols):
    """
    Replaces bad names for
    columns
    """
    file_name = '_'.join(cols)
    file_name = file_name.replace("%", "percent")
    file_name = file_name.replace("#", "number")
    file_name = file_name.replace("w/", "with")
    return file_name


def is_sentence(cell):
    """
    Detects if a certain cell is a
    sentance or not
    """
    if isinstance(cell, str) and cell.endswith('.'):
        return ''
    if isinstance(cell, str) and len(cell) > 50:
        return ''
    return cell


def data_merger(pdf_file_list, pdf_folder, match_string):
    """
    Merging dataframes based upon
    the column names inside the
    'CombinedData' directory
    """
    os.makedirs(os.path.join(pdf_folder, "CombinedData"), exist_ok=True)

    csv_path_list = []
    for pdf_file in pdf_file_list:
        #pdf_good_data_csv_path = pdf_file[:-4]+'/GoodData/*.csv'
        pdf_good_data_csv_list = glob.glob(pdf_file[:-4]+'GoodData/*.csv')
        #pdf_merged_data_csv_path = pdf_file[:-4]+'/Merged_Data/*.csv'
        pdf_merged_data_csv_list = glob.glob(pdf_file[:-4]+'/Merged_Data/*.csv')
        csv_path_list = csv_path_list + pdf_good_data_csv_list
        csv_path_list = csv_path_list + pdf_merged_data_csv_list

    df_list = []
    for csv_file_path in csv_path_list:
        #given_df = pd.read_csv(csv_file_path)
        df_list.append(pd.read_csv(csv_file_path))

    result_list = []
    for my_df in df_list:
        rows = my_df[(my_df == match_string).any(axis=1)]

        for i in range(len(rows)):
            year = rows.iat[i, -1]
            match_value = rows.iat[i, -2]
            if isinstance(match_value, str):
                match_value = match_value.replace(",", "")
                #match_value_num = float(match_value)
                match_value = float(match_value)
            result_list.append([year, match_value])

    output_df = pd.DataFrame(result_list)
    output_df = output_df.drop_duplicates()
    output_df = output_df.dropna()

    output_df.columns = ['Year', match_string]

    return output_df


PDF_LIST = glob.glob('pdf/*.pdf')

# pdf_parser(pdf_list, 'pdf/')

CATTLE_KILLED = data_merger(PDF_LIST, 'pdf/', 'Cattle Killed')

INVESTIGATIONS = data_merger(PDF_LIST, 'pdf/',
                             '# of Wolf related Investigations conducted:')

OBSERVATIONS = data_merger(PDF_LIST, 'pdf/', 'Statewide')
