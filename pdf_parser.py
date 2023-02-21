"""
os library to create files
camelot library to parse PDF documents
pandas to create dataframes
"""
import os
import camelot
import pandas as pd


def process_pdfs(files_list):
    """
    Takes in a list of file locations
    Parses through them for dataframes and
    creates CSV files based upon how useful
    the dataset could be 
    """
    good = 0 
    bad = 0  
    for file_location in files_list:
        # Create a new directory based on the file name
        file_name = os.path.basename(file_location)
        directory_name = os.path.splitext(file_name)[0]
        os.makedirs(directory_name, exist_ok=True)

        # Create GoodData and BadData subdirectories in the new directory
        os.makedirs(os.path.join(directory_name, "GoodData"), exist_ok=True)
        os.makedirs(os.path.join(directory_name, "BadData"), exist_ok=True)

        # Load the PDF file into camelot and create dataframes
        tables = camelot.read_pdf(file_location,split_text = True, pages='all')
        for i, table in enumerate(tables):
            df = table.df
        
            # Analyze the dataframe to see if it has useful values            
            has_useful_values = False
            for column in df.columns:
                column_values = df[column].values
                for value in column_values:
                    if isinstance(value, int) or (isinstance(value, str) and value.strip() != ''):
                        has_useful_values = True
                        break
                if has_useful_values:
                    break
            # Move the dataframe into the appropriate folder based on whether it has useful values                
            if has_useful_values:
                good += 1 
                df.to_csv(os.path.join(directory_name, "GoodData", f"table_{i+1}.csv"), index=False)
            else:
                df.to_csv(os.path.join(directory_name, "BadData", f"table_{i+1}.csv"), index=False)
                bad += 1
    print(f"Total dataframes created: {good + bad}")
    print(f"Total good dataframes: {good}")
    print(f"Total bad dataframes: {bad}")

process_pdfs(["Wisconsin_Gray_Wolf_Report_2022.pdf"])
