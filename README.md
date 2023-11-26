# data-api-challenge

This is a simple REST API built with Python and FastAPI that returns some data about the air we breathe in

## Specific API Endpoints

### Top 10 Countries with highest Co2Emissions perCapita:

```http
GET /top-10-percapita
```

Returns a json of top 10 Countries with their CO2 Emissions perCapita

```console
curl http://localhost:8080/top-10-percapita -H "Accept: application/json"
```
Response:

```json
{
  "Percapita": {
    "Qatar": 37.29,
    "Montenegro": 25.9,
    "Kuwait": 25.65,
    "Trinidad and Tobago": 25.39,
    "United Arab Emirates": 23.37,
    "Oman": 19.61,
    "Canada": 18.58,
    "Brunei": 18.28,
    "Luxembourg": 17.51,
    "Bahrain": 17.15
  }
}
```

### Top 10 Countries with highest LifeExpectancy:

```http
GET /top-10-le
```

Returns a json of top 10 Countries with their CO2 Emissions perCapita

```console
curl http://localhost:8080/top-10-le -H "Accept: application/json"
```
Response:

```json
{
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
```

### Return CO2Emissions and YearlyChange given a list of country codes

The country_codes are in 3 Alpha-3 format and separated by comma (%2C)

```http
GET /co2-yearly-change-from-list/{country_codes}
```

Return CO2Emissions and YearlyChange given a list of country codes

```console
curl http://localhost:8080/co2-yearly-change-from-list/can%2Clux%2Cest -H "Accept: application/json"
```
Response:

```json
{
  "CO2Emissions": {
    "CAN": 675918610,
    "EST": 22402414,
    "LUX": 10144632
  },
  "YearlyChange": {
    "CAN": -1,
    "EST": 1.01,
    "LUX": 3.45
  }
}
```

### Return total of Emissions given a list of countries codes

The country_codes are in 3 Alpha-3 format and separated by comma (%2C)

```http
GET /total-emission-from-list/{country_codes}
```

Return total of Emissions

```console
curl http://localhost:8080/total-emission-from-list/can%2Clux%2Cest -H "Accept: application/json"
```
Response:

```json
{
  "CO2Emissions": 708465656
}
```
### Health check

```http
GET /health
```

Returns the health status of the running API

```console
curl http://localhost:8080/health -H "Accept: application/json"
```
Response:

```json
{
  "status": "Healthy"
}
```