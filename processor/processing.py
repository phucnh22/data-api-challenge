'''Submodule contains public functions to handle file data'''
import re
import pandas as pd
from pathlib import Path

class DataProcessor:
    def __init__(self, source):
        self.df = self._load_data(source)
    
    def _load_data(self, path_to_file: Path) -> pd.DataFrame:
        """Load data from a tsv file and return a pandas dataframe"""
        return pd.read_csv(path_to_file)

    def get_top_10_from(self, value_col: str, id_col: str = 'Country') -> dict:
        result_df = self.df.nlargest(10, value_col)[[value_col, id_col]]
        return result_df.set_index(id_col).to_dict()

    def get_value_of_list(self, value_col: str, list_country_codes: [str]) -> dict:
        list_country_codes = [x.upper() for x in list_country_codes]
        result_df = self.df[self.df['Code'].isin(list_country_codes)][[value_col, 'Code']]
        return result_df.set_index('Code').to_dict()

    def get_sum_of_list(self, value_col: str, list_country_codes: [str]) -> dict:
        list_country_codes = [x.upper() for x in list_country_codes]
        result_df = self.df[self.df['Code'].isin(list_country_codes)][value_col].sum().item()
        return {value_col: result_df}
