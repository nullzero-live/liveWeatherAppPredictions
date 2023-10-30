# test_weather_api.py
import pytest
import responses
from ..api import query_station_timeseries  # Replace with your actual import

# Use pytest fixture for common setup
@pytest.fixture
def setup_common():
    return {
        'startdate': '2022-01-01T00:00Z',
        'enddate': '2022-01-02T00:00Z',
        'interval': 'PT1H',
        'parameters': ['temperature_2m', 'precipitation_sum'],
        'username': 'your_username',
        'password': 'your_password',
        'API_BASE_URL': 'http://api.meteomatics.com/'
    }

@responses.activate 
def test_query_station_timeseries_success(setup_common):
    # Mock the API response
    responses.add(
        responses.GET,
        f"{setup_common['API_BASE_URL']}/query_station_ts",  # Update this based on your function logic
        json={'your_expected': 'json_response'},
        status=200
    )

    # Call your function
    result = query_station_timeseries(
        startdate=setup_common['startdate'],
        enddate=setup_common['enddate'],
        interval=setup_common['interval'],
        parameters=setup_common['parameters'],
        username=setup_common['username'],
        password=setup_common['password'],
        API_BASE_URL=setup_common['API_BASE_URL']
    )

    
    assert result is not None
    assert 'temperature_2m' in result.columns
    assert 'precipitation_sum' in result.columns

    @responses.activate
def test_unauthorized_access(setup_common):
    responses.add(
        responses.GET,
        f"{setup_common['API_BASE_URL']}your_expected_endpoint",
        status=401
    )
    with pytest.raises(requests.exceptions.HTTPError):
        query_station_timeseries(
            # ... (pass the arguments)
        )

@responses.activate
def test_rate_limiting(setup_common):
    responses.add(
        responses.GET,
        f"{setup_common['API_BASE_URL']}your_expected_endpoint",
        status=429
    )
    with pytest.raises(requests.exceptions.HTTPError):
        query_station_timeseries(
            # ... (pass the arguments)
        )

@responses.activate
def test_invalid_parameter(setup_common):
    responses.add(
        responses.GET,
        f"{setup_common['API_BASE_URL']}your_expected_endpoint",
        status=400
    )
    with pytest.raises(requests.exceptions.HTTPError):
        query_station_timeseries(
            # ... (pass invalid parameters)
        )

@responses.activate
def test_api_timeout(setup_common):
    responses.add(
        responses.GET,
        f"{setup_common['API_BASE_URL']}your_expected_endpoint",
        status=408
    )
    with pytest.raises(requests.exceptions.HTTPError):
        query_station_timeseries(
            # ... (pass the arguments)
        )

def test_invalid_date_range(setup_common):
    with pytest.raises(ValueError):
        query_station_timeseries(
            startdate='2022-01-02T00:00Z',
            enddate='2022-01-01T00:00Z',
            # ... (rest of the arguments)
        )

def test_empty_parameters(setup_common):
    with pytest.raises(ValueError):
        query_station_timeseries(
            parameters=None,
            # ... (rest of the arguments)
        )

@responses.activate
def test_partial_data(setup_common):
    responses.add(
        responses.GET,
        f"{setup_common['API_BASE_URL']}your_expected_endpoint",
        json={'partial': 'data'},
        status=200
    )
    result = query_station_timeseries(
        # ... (pass the arguments)
    )
    # assert conditions that validate partial data
    assert 'temperature_2m' not in result.columns


