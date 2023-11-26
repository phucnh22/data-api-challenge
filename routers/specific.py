from pathlib import Path
import os
from fastapi import APIRouter, HTTPException
from processor.processing import DataProcessor, verify_country_codes

current_path = os.getcwd()
data_path = Path(current_path) / "data"
data = DataProcessor(data_path / "CO2-emissions.csv")

router = APIRouter()


@router.get('/top-10-percapita')
def top_10_percapita():
    """Get top 10 countries with highest Co2Emissions perCapita"""
    return data.get_top_X_from("Percapita")


@router.get('/top-10-le')
def top_10_le():
    """Get top 10 countries with highest LifeExpectancy"""
    return data.get_top_X_from("LifeExpectancy")


@router.get('/co2-yearly-change-from-list/{country_codes}')
def co2_yearly_change_from_list(country_codes: str):
    """Return CO2Emissions and YearlyChange given a list of country codes"""

    codes_list = verify_country_codes(country_codes)
    if not codes_list:
        raise HTTPException(status_code=404, detail="Country code not found")

    value_list = ['CO2Emissions', 'YearlyChange']
    response = {}
    for v in value_list:
        response[v] = data.get_value_of_list(v, codes_list)[v]
    return response


@router.get('/total-emission-from-list/{country_codes}')
def total_emission_from_list(country_codes: str):
    """Total of Emissions given a list of countries codes"""
    codes_list = verify_country_codes(country_codes)
    if not codes_list:
        raise HTTPException(status_code=404, detail="Country code not found")
    
    value = 'CO2Emissions'
    return data.get_sum_of_list(value, codes_list)


@router.get('/health')
def health_check():
    """Endpoint used for API health check"""
    return {"status": "Healthy"}
