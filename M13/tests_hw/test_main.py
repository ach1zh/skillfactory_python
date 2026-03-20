import unittest
from unittest.mock import patch, Mock
from M13.src_hw.main import get_weather 

class TestGetWeather(unittest.TestCase):

    @patch('M13.src_hw.main.requests.get')    
    def test_get_weather_success(self, mock_get):
        
        mock_response = Mock()        
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'current': {
                'temperature': 20,
                'weather_descriptions': ['Sunny']
            }
        }

        mock_get.return_value = mock_response
        temperature, description = get_weather('dummy_api_key', 'London')

        print(mock_response().temperature)
        print(mock_response().description)

        self.assertEqual(temperature, 20)
        self.assertEqual(description, 'Sunny')
    
    @patch('M13.src_hw.main.requests.get')
    def test_get_weather__failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            get_weather('dummy_api_key', 'UnknownCity')
        self.assertTrue('Error while fetching weather data' in str(context.exception))    
    
if __name__ == '__main__':
    unittest.main()