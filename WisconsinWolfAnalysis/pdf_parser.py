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
        tables = camelot.read_pdf(file_location, pages='all')
        # ,split_text = True)

        for i, table in enumerate(tables):
            df = table.df
            # df = df.iloc[1:]
            # try:
            #      df.columns = df.iloc[0]
            #      df = df[1:]
            #  except:
            #      pass
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
                                  "GoodData", f"table_{i+1}.csv"),
                                  index=False)
                    else:
                        merged_df = pd.concat(dfs, ignore_index=True)
                        csv_file = os.path.join(merged_data_dir,
                                                f"data_{cols}.csv")
                        merged_df.to_csv(csv_file, index=False)
            else:
                # Save the dataframe as a CSV file in the "BadData"
                # directory
                df.to_csv(os.path.join(pdf_folder, directory_name,
                          "BadData", f"table_{i+1}.csv"), index=False)


pdf_list = glob.glob('pdf/*.pdf')

pdf_parser(pdf_list, 'pdf')
