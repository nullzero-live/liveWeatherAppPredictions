import pytest
import responses
from ..api import (get_request, query_time_series, 
                         convert_time_series_binary_response_to_df, query_api)
from datetime import datetime
import isodate
import requests

# Initialize common fixture data
@pytest.fixture
def common_data():
    return {
        'coordinate_list': ['37.7749,-122.4194'],
        'startdate': datetime(2022, 1, 1),
        'enddate': datetime(2022, 1, 2),
        'interval': isodate.parse_duration('PT1H'),
        'parameters': ['temperature_2m', 'humidity_2m'],
        'username': 'test_user',
        'password': 'test_pass',
        'api_base_url': 'http://api.example.com/'
    }

# Testing get_request with a mocked 200 OK response
@responses.activate
def test_get_request_successful():
    responses.add(responses.GET, 'http://api.example.com/test', status=200)
    response = get_request('http://api.example.com/test')
    assert response.status_code == 200

# Other test cases for get_request would involve SSL and Proxy errors

@responses.activate
def test_query_time_series_successful(common_data):
    responses.add(
        responses.GET,
        'your_constructed_url_here_based_on_template',
        status=200,
        content_type='application/octet-stream'
    )
    # The URL here should be constructed based on your template
    df = query_time_series(**common_data)
    assert not df.empty

# Advanced: Testing unsuccessful API query due to 400 Bad Request
@responses.activate
def test_query_time_series_bad_request(common_data):
    responses.add(responses.GET, 'your_constructed_url_here', status=400)
    with pytest.raises(requests.exceptions.HTTPError):
        query_time_series(**common_data)

# Advanced: Testing convert_time_series_binary_response_to_df
def test_convert_time_series_binary_response_to_df():
    # Mock binary input and expected DataFrame output
    bin_input = b'your_mock_binary_data'
    coordinate_list = common_data['coordinate_list']
    parameters = common_data['parameters']
    df = convert_time_series_binary_response_to_df(bin_input, coordinate_list, parameters)
    assert not df.empty  # Add more checks

# Advanced: Testing query_api with mocked GET request
@responses.activate
def test_query_api_get_request_successful():
    responses.add(responses.GET, 'http://api.example.com/test', status=200)
    response = query_api('http://api.example.com/test', 'test_user', 'test_pass')
    assert response.status_code == 200

# Run pytest to execute all your tests
