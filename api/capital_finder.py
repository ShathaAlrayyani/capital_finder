from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
# import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global message
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        country = ''
        capital = ''
        if 'capital' in dic:
            capital = dic['capital']
        if 'country' in dic:
            country = dic['country']
        if len(capital) > 1:
            url = 'https://restcountries.com/v3.1/capital/'
            req = requests.get(url + capital)
            data = req.json()
            for c_data in data:
                cap_name = c_data['capital'][0]
                country_name = c_data['name']['common']
                message = f'{cap_name} is the capital of {country_name}'
        elif len(country) > 1:
            url = 'https://restcountries.com/v3.1/name/'
            req = requests.get(url + country)
            data = req.json()
            for c_data in data:
                cap_name = c_data['name']['common']
                country_name = c_data['capital'][0]
                message = f'The capital of {cap_name} is {country_name}'
        else:
            message = "Please provide capital or country"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return


# To get the body of a json file we import json then we write the following :
#
# response = requests.get('https://restcountries.com/v3.1/capital/Amman')
# print(f'Response status code: {response.status_code}')
# print(f'Response header: {response.headers}')
# print(f'Response body : {json.dumps(response.json(), indent=4)}')
# print('*'*50)
#
#
# response = requests.get('https://restcountries.com/v3.1/name/Japan')
# print(f'Response status code: {response.status_code}')
# print(f'Response header: {response.headers}')
# print(f'Response body : {json.dumps(response.json(), indent=4)}')

