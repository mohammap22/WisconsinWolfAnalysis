"""
Importing os for file creation
Importion re for regex
importing glob for filesystem
Importing Pandas for dataframe parsing
Importing Camelot for PDF parsing
"""
import glob
import re
import os
import warnings

import pandas as pd

import camelot

# pylint: disable-msg=too-many-locals
# pylint: disable-msg=too-many-nested-blocks
# pylint: disable-msg=too-many-branches


def pdf_parser(pdf_files_list, pdf_folder, show_warnings=False):
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
        warnings.filterwarnings("ignore")
        tables = camelot.read_pdf(file_location, pages="all", flavor='stream',
                                  edge_tol=500,
                                  suppress_stdout=show_warnings)
        warnings.resetwarnings()

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


def data_extractor(pdf_file_list, pdf_folder, match_string, label,
                   output_file):
    '''
    For all PDF files in pdf_file_list within pdf_folder, this program
    will import all of the .csv files in GoodData and Merged_Data folders
    then look through each of them for a user-specified match_string. If
    the string is found, then the last two columns from that row will be
    added to an output dataframe. Those will be a value and year
    associated with that value. The output dataframe is processed to remove
    nans and to only keep the most recent row from each year.

    Parameters
    ----------
    pdf_file_list : LIST OF STRINGS
        A list of PDF files. Each file should have a folder in pdf_folder
        and within the folder for the file there should be subfolders for
        good data and merged data.
    pdf_folder : STRING
        The folder location where the PDFs and their associated data
        folders reside.
    match_string : STRING
        The row name to extact from the data.
    label : STRING
        A column label for the extracted parameter in the output dataframe.
    output_file : STRING
        A filepath and file name to write a csv to containing the extracted
        dataframe.

    Returns
    -------
    None.

    '''
    os.makedirs(os.path.join(pdf_folder, "CombinedData"), exist_ok=True)

    csv_path_list = []
    for pdf_file in pdf_file_list:
        pdf_good_data_csv_list = glob.glob(pdf_file[:-4] + '/GoodData/*.csv')
        pdf_merged_data_csv_list = glob.glob(pdf_file[:-4] +
                                             '/Merged_Data/*.csv')
        csv_path_list = csv_path_list + pdf_good_data_csv_list
        csv_path_list = csv_path_list + pdf_merged_data_csv_list

    df_list = []
    for csv_file_path in csv_path_list:
        df_list.append(pd.read_csv(csv_file_path))

    result_list = []
    for my_df in df_list:
        rows = my_df[(my_df == match_string).any(axis=1)]

        for i in range(len(rows)):
            year = rows.iat[i, -1]
            match_value = rows.iat[i, -2]
            if isinstance(match_value, str):
                match_value = match_value.replace(",", "")
                match_value = float(match_value)
            result_list.append([year, match_value])

    output_df = pd.DataFrame(result_list)
    output_df = output_df.drop_duplicates()
    output_df = output_df.dropna()
    output_df.columns = ['year', label]

    year_counts = output_df.year.value_counts()
    for i in range(0, len(year_counts)):
        selected_year = year_counts.index[i]
        num_to_remove = year_counts[selected_year] - 1
        removed_count = 0
        while removed_count < num_to_remove:
            output_df = output_df.drop(output_df[output_df.year ==
                                                 selected_year][0:1].index[0])
            removed_count = removed_count + 1

    output_df.to_csv(output_file, index=False)


def combine_csv_files(csv_file_1, column_name_1,
                      csv_file_2, column_name_2,
                      output_file):
    '''
    This program combines subsets of two csv files for trend analysis.
    It expects two csv files, each with a "year" column and some number
    of data columns. The user specifies one of these data columns from
    each file. For each year that is in both files, a row is added to a
    dataframe with the year, the corresponding value from the specified
    column in the first file, and the corresponding value from the
    specified column in the second file. This dataframe is then written
    to the user-specified output_file.

    Parameters
    ----------
    csv_file_1 : STR
        The first csv file from which data will be extracted
    column_name_1 : STR
        The column name in the first file to add to the combined file
    csv_file_2 : STR
        The second csv file from which data will be extracted
    column_name_2 : STR
        The column name in the second file to add to the combined file
    output_file : STR
        The file path and name for the output file.

    Raises
    ------
    TypeError
        A TypeError is raised if either of the files are not .csv files.
    ValueError
        A ValueError is raised if either of the .csv files does not contain
        a column labeled "year" or the user specified column name for that
        file.

    Returns
    -------
    None.

    '''

    if csv_file_1[-4:] != '.csv':
        raise TypeError(csv_file_1 + ' must be a csv')
    df_1 = pd.read_csv(csv_file_1)

    if csv_file_2[-4:] != '.csv':
        raise TypeError(csv_file_2 + ' must be a csv')
    df_2 = pd.read_csv(csv_file_2)

    if 'year' in df_1.columns:
        csv_1_years = df_1.year.tolist()
    else:
        raise ValueError(csv_file_1 + ' does not contain a "year" column')

    if 'year' in df_2.columns:
        csv_2_years = df_2.year.tolist()
    else:
        raise ValueError(csv_file_2 + ' does not contain a "year" column')

    if column_name_1 not in df_1.columns:
        raise ValueError(csv_file_1 + 'does not contain a ' +
                         column_name_1 + ' column')

    if column_name_2 not in df_2.columns:
        raise ValueError(csv_file_2 + 'does not contain a ' +
                         column_name_2 + ' column')

    combined_list = []
    for year in csv_1_years:
        if year in csv_2_years:
            csv_1_value = df_1[df_1.year == year][column_name_1].values[0]
            csv_2_value = df_2[df_2.year == year][column_name_2].values[0]

            combined_list.append([year, csv_1_value, csv_2_value])

    output_df = pd.DataFrame(combined_list)
    output_df.columns = ['year', column_name_1, column_name_2]

    output_df.to_csv(output_file, index=False)
