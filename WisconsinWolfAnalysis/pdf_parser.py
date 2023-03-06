import os
import camelot
import glob
import pandas as pd


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
        directory_name = os.path.splitext(file_name)[0]
        os.makedirs(os.path.join(pdf_folder, directory_name), exist_ok=True)

        os.makedirs(os.path.join(pdf_folder, directory_name,
                                 "GoodData"), exist_ok=True)
        os.makedirs(os.path.join(pdf_folder, directory_name,
                                 "BadData"), exist_ok=True)
        merged_data_dir = os.path.join(pdf_folder, directory_name,
                                       "Merged_Data")
        os.makedirs(merged_data_dir, exist_ok=True)
        tables = camelot.read_pdf(file_location, pages="all", flavor='stream',
                                  edge_tol=500)

        for i, table in enumerate(tables):
            df = table.df.applymap(is_sentence)

            non_empty_row_idx = 0
            for row_idx, row in enumerate(df.values):
                if not all(cell == '' for cell in row):
                    non_empty_row_idx = row_idx
                    break
            column_names = df.iloc[non_empty_row_idx]
            df = df.iloc[non_empty_row_idx+1:].reset_index(drop=True)
            df.columns = column_names

            non_null_cols = df.columns[df.notnull().any()].tolist()
            file_name = '_'.join(non_null_cols)
            file_name = file_name.replace("%", "percent")
            file_name = file_name.replace("#", "number")
            file_name = file_name.replace("w/", "with")

            has_useful_values = False
            for column in df.columns:
                column_values = df[column].values
                for value in column_values:
                    if isinstance(value, int) or (isinstance(value, str)
                                                  and value.strip() != ''):
                        has_useful_values = True
                        break
            if has_useful_values:
                cols = tuple(df.columns)
                if cols not in dataframes:
                    dataframes[cols] = []
                dataframes[cols].append(df)

                for cols, dfs, in dataframes.items():
                    if len(dfs) == 1:
                        df = dfs[0]
                        # Save the dataframe as a CSV file
                        # in the "GoodData" directory
                        df.to_csv(os.path.join(pdf_folder, directory_name,
                                  "GoodData", file_name + str(i) + '.csv'),
                                  index=False)
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
                df.to_csv(os.path.join(pdf_folder, directory_name,
                          "BadData", file_name + str(i) + '.csv'), index=False)


def is_sentence(cell):
    if isinstance(cell, str) and cell.endswith('.'):
        return ''
    if isinstance(cell, str) and len(cell) > 50:
        return ''
    else:
        return cell


pdf_list = glob.glob('pdf/*.pdf')

pdf_parser(pdf_list, 'pdf/')
