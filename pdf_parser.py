import os
import camelot
import pandas as pd

def pdf_parser(pdf_files_list):
    dataframes = {}

    for file_location in pdf_files_list:
        # Create a new directory based on the file name
        file_name = os.path.basename(file_location)
        print(file_name)
        directory_name = os.path.splitext(file_name)[0]
        os.makedirs(directory_name, exist_ok=True)

        os.makedirs(os.path.join(directory_name, "GoodData"), exist_ok=True)
        os.makedirs(os.path.join(directory_name, "BadData"), exist_ok=True)
        merged_data_dir = os.path.join(directory_name, "Merged_Data")
        os.makedirs(merged_data_dir, exist_ok=True)
        tables = camelot.read_pdf(file_location,pages = 'all') #,split_text = True)
        for i, table in enumerate(tables):
            df = table.df
          # df = df.iloc[1:]
          #  try:
          #      df.columns = df.iloc[0]
          #      df = df[1:]
          #  except:
          #      pass
            has_useful_values = False
            for column in df.columns:
                column_values = df[column].values
                for value in column_values:
                    if isinstance(value, int) or (isinstance(value, str) and value.strip() != ''):
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
                        # Save the dataframe as a CSV file in the "GoodData" directory
                        df.to_csv(os.path.join(directory_name, "GoodData", f"table_{i+1}.csv"), index=False)
                    else:
                        merged_df = pd.concat(dfs, ignore_index=True)
                        csv_file = os.path.join(merged_data_dir, f"data_{cols}.csv")
                        merged_df.to_csv(csv_file, index=False)
            else:
                # Save the dataframe as a CSV file in the "BadData" directory
                df.to_csv(os.path.join(directory_name, "BadData", f"table_{i+1}.csv"), index=False)


pdfs = ["Wisconsin_Gray_Wolf_Report_2022.pdf","Wisconsin_Gray_Wolf_2020_2021_Final.pdf"]
pdf_parser(pdfs)



