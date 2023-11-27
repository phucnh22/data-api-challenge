# data-api-challenge

This is a simple REST API built with Python and FastAPI that returns some data about the air we breathe in

## Generic API Endpoints

### Get top X countries according to specific index:

Get top X countries with highest index.

  -  `index` (string): Choose one of the available indexes CO2Emissions, YearlyChange, Percapita, Population, LifeExpectancy
  -  `top` (int): the amount of top countries to get

```console
curl -X 'GET' 'http://localhost:8080/top-values/?index=Population&top=5'
     -H 'accept: application/json'
```
Response:
```json
{
  "Population": {
    "China": 1414049351,
    "India": 1324517249,
    "United States": 323015995,
    "Indonesia": 261556381,
    "Brazil": 206163053
  }
}
```

### Get sum of specific index for a list of countries:

Sum of index given a list of countries code.

  -  `index` (string, required): Choose one of the available indexes CO2Emissions, YearlyChange, Percapita, Population, LifeExpectancy
  -  `country_codes ` (string, required): country_codes are in Alpha-3 format and separated by comma (e.g. "vnm,can")

```console
curl -X 'POST' \
  'http://localhost:8080/sum-values' -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "index": "Population",
  "country_codes": "vnm,can"
}'
```
Response:
```json
{"Population":130023366}
```

### Get values of specific index for a list of countries:

Return the index value given a list of country codes

  -  `index` (string, required): Choose one of the available indexes CO2Emissions, YearlyChange, Percapita, Population, LifeExpectancy
  -  `country_codes ` (string, required): country_codes are in Alpha-3 format and separated by comma (e.g. "vnm,can")

```console
curl -X 'POST' \
  'http://localhost:8080/get-values' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "index": "Percapita",
  "country_codes": "vnm,can"
}'
```
Response:
```json
{
  "CAN": 18.58,
  "VNM": 2.2
}
```

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

 - `country_codes` (string, required): The country_codes are in 3 Alpha-3 format and separated by comma

Return CO2Emissions and YearlyChange given a list of country codes

```console
curl -X 'POST' \
  'http://localhost:8080/co2-yearly-change-from-list' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "country_codes": "can,lux,est"
}'
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

 - `country_codes` (string, required): The country_codes are in 3 Alpha-3 format and separated by comma

Return total of Emissions

```console
curl -X 'POST' \
  'http://localhost:8080/total-emission-from-list' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "country_codes": "can,lux,est"
}'
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