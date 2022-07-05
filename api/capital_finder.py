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
        '''
        The capital of Chile is Santiago
        '''
        if len(capital) > 1:
            url = 'https://restcountries.com/v3.1/capital/'
            r = requests.get(url + capital)
            data = r.json()
            for c_data in data:
                capital_name = c_data['capital'][0]
                country_name = c_data['name']['common']
                message = str(capital_name + ' is the capital of ' + country_name)
        elif len(country) > 1:
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()
            for c_data in data:
                capital_name = c_data['name']['common']
                country_name = c_data['capital'][0]
                message = f'The capital of {capital_name} is {country_name}'
        else:
            '''
             Santiago is the capital of Chile
            '''
            message = "Please provide capital or country"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return


# response = requests.get('https://restcountries.com/v3.1/capital/Amman')
# print(f'Response status code: {response.status_code}')
# print(f'Response header: {response.headers}')
# print(f'Response body : {json.dumps(response.json(), indent=4)}')
# print('*'*50)
#
#
# response = requests.get('https://restcountries.com/v3.1/name/jordan')
# print(f'Response status code: {response.status_code}')
# print(f'Response header: {response.headers}')
# print(f'Response body : {json.dumps(response.json(), indent=4)}')

