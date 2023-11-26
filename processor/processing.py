'''Submodule contains public functions to handle file data'''
from typing import List
import pandas as pd
from pathlib import Path
from processor.vars import Country


class DataProcessor:
    def __init__(self, source):
        self.df = self._load_data(source)
    
    def _load_data(self, path_to_file: Path) -> pd.DataFrame:
        """Load data from a tsv file and return a pandas dataframe"""
        return pd.read_csv(path_to_file)

    def get_top_X_from(self, value_col: str, id_col: str = 'Country', top: int = 10) -> dict:
        result_df = self.df.nlargest(top, value_col)[[value_col, id_col]]
        return result_df.set_index(id_col).to_dict()

    def get_value_of_list(self, value_col: str, list_country_codes: List[str]) -> dict:
        list_country_codes = [x.upper() for x in list_country_codes]
        result_df = self.df[self.df['Code'].isin(list_country_codes)][[value_col, 'Code']]
        return result_df.set_index('Code').to_dict()

    def get_sum_of_list(self, value_col: str, list_country_codes: List[str]) -> dict:
        list_country_codes = [x.upper() for x in list_country_codes]
        result_df = self.df[self.df['Code'].isin(list_country_codes)][value_col].sum().item()
        return {value_col: result_df}


def verify_country_codes(country_codes: str) -> List[str]:
    """Given a string of country codes separated by comma, this function
    will verify if the country codes are valid and return a list of codes
    respectively"""
    codes_list = country_codes.split(',')
    for country in codes_list:
        if country.upper() not in Country._member_names_:
            return False
    return codes_list
    