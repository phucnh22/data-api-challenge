"""Pytest configuration file"""
import pandas as pd
import pytest

@pytest.fixture(scope='module')
def expected_top_10_life_expectancy() -> pd.DataFrame:
    data = {
        "LifeExpectancy": {
            "Hong Kong": 84.277,
            "Japan": 84.09,
            "Macao": 83.854,
            "Cayman Islands": 83.48,
            "Switzerland": 83.31,
            "Spain": 83.145,
            "Singapore": 83.083,
            "Italy": 83.008,
            "Australia": 82.959,
            "Iceland": 82.601
        }
    }
    return data

@pytest.fixture(scope='module')
def expected_CO2_emission() -> pd.DataFrame:
    return {
        "CO2Emissions": {
            "CAN": 675918610,
            "VNM": 206042140
        }
    }

@pytest.fixture(scope='module')
def expected_CO2_emission_sum() -> pd.DataFrame:
    return {"CO2Emissions": 881960750}

