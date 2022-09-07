
import pandas as pd
import numpy as np
import logging

class MissingValue:
    def __init__(self):
        logging.basicConfig(filename='../logfile.log', filemode='a',
                            encoding='utf-8', level=logging.DEBUG)
        
    def missing_values_table(self,df:pd.DataFrame):
        ''' return a DataFrame of Total missing values'''
        total = df.isnull().sum()

        # Percentage of missing values
        mis_val_perc = 100 * df.isnull().sum() / len(df)

        # dtype of missing values
        dtype_mis_val= df.dtypes

        # Make a table with the results
        mis_val_table = pd.concat(
            [total, mis_val_perc, dtype_mis_val], axis=1)

        # Rename the columns
        mis_val_table_ren_col = mis_val_table.rename(
            columns={0: 'Missing Values', 1: '% of Total Values', 2: 'Dtype'})

        # Sort the table by percentage of missing descending
        mis_val_table_ren_col = mis_val_table_ren_col[
            mis_val_table_ren_col.iloc[:, 1] != 0].sort_values(
            "% of Total Values", ascending=False).round(1)

        # Print some summary information
     
        logging.info("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
                         "There are " + str(mis_val_table_ren_col.shape[0]) +
                         " columns that have missing values.")

        # Return the dataframe with missing information
        return mis_val_table_ren_col

    def val_miss_percntage(self,df:pd.DataFrame):

        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        return totalCells, missingCount, totalMissing