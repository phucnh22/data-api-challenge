from processor.processing import DataProcessor
from . import FIXTURES_DIR

def test_top_10(expected_top_10_life_expectancy):
    data = DataProcessor(FIXTURES_DIR / "CO2-emissions.csv")
    result = data.get_top_10_from("LifeExpectancy")
    assert result == expected_top_10_life_expectancy

def test_get_value_from_list(expected_CO2_emission):
    data = DataProcessor(FIXTURES_DIR / "CO2-emissions.csv")
    result = data.get_value_of_list("CO2Emissions", ["CAN", "VNM"])
    assert result == expected_CO2_emission

def test_get_sum_from_list(expected_CO2_emission_sum):
    data = DataProcessor(FIXTURES_DIR / "CO2-emissions.csv")
    result = data.get_sum_of_list("CO2Emissions", ["CAN", "VNM"])
    assert result == expected_CO2_emission_sum