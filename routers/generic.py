from pathlib import Path
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from processor.processing import DataProcessor, verify_country_codes

current_path = os.getcwd()
data_path = Path(current_path) / "data"
data = DataProcessor(data_path / "CO2-emissions.csv")

router = APIRouter()

class QueryBody(BaseModel):
    index: str
    country_codes: str

@router.get('/top-values/')
def top_values(index: str, top: int):
    """Get top X countries with highest index. Available indexes are:

    CO2Emissions, YearlyChange, Percapita, Population, LifeExpectancy
    """
    return data.get_top_X_from(value_col=index,top=top)

@router.post('/sum-values')
def sum_values(query: QueryBody):
    """Sum of index given a list of countries code. Available indexes are:

    CO2Emissions, YearlyChange, Percapita, Population, LifeExpectancy
    """

    codes_list = verify_country_codes(query.country_codes)
    if not codes_list:
        raise HTTPException(status_code=404, detail="Country code not found")
    
    return data.get_sum_of_list(query.index, codes_list)

@router.post('/get-values')
def get_values(query: QueryBody):
    """Return the index value given a list of country codes. Available indexes are:

    CO2Emissions, YearlyChange, Percapita, Population, LifeExpectancy
    """

    codes_list = verify_country_codes(query.country_codes)
    if not codes_list:
        raise HTTPException(status_code=404, detail="Country code not found")

    return data.get_value_of_list(query.index, codes_list)[query.index]
