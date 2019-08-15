import requests


response = requests.get('https://api.github.com')
response.raise_for_status()

print(response.content)  # content in bytes
response.encoding = 'utf-8'  # optional
print(response.text)  # content in string using UTF-8, actually it is serialized JSON

print(response.json())  # vraci slovnik

# headers - access to metadata
print(response.headers)  # vraci dict like object, hodnoty jsou pristupne pres key
print(response.headers['Date'])  # case-insensitive, lze zadat i date, content-type apod.

# customization of GET
response = requests.get('https://api.github.com/search/repositories',
                        params={'q': 'requests+language:python'},
                        headers={'Accept': 'application/vnd.github.v3.text-match+json'})
"""
params muze byt dict nebo list of tuples: params=[('q', 'requests+language:python')]
nebo bytes: params=b'q=requests+language:python'
Accept header tells the server what content type is required. The value is special GitHub Accept header, content is
in special JSON format
"""

json_response = response.json()
repository = json_response['items'][0]
print('Repository name: {}'.format(repository['name']))
print('Repository description: {}'.format(repository['description']))
print('RText matches: {}'.format(repository['text_matches']))

# httpbin.org is a we which accepts requests and responds with data about the requests
print(requests.post('https://httpbin.org/post', data={'key': 'value'}))  # vse vraci Response 200
print(requests.put('https://httpbin.org/put', data={'key': 'value'}))
print(requests.delete('https://httpbin.org/delete'))  # class 'requests.models.Response'
print(requests.head('https://httpbin.org/get'))
print(requests.patch('https://httpbin.org/patch', data={'key': 'value'}))
print(requests.options('https://httpbin.org/get'))
# for each method I can inspect their responses
response = requests.head('https://httpbin.org/get')
print(response.headers['content-type'])

response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])
# headers,response bodies,status codes, and more are returned in the Response for each method

"""
POST, PUT, PATCH pass their data through the message body rather than through parameters in the query string
the data should be passed to data parameter - dict, list of tuples, bytes or file-like object
"""
print(requests.post('https://httpbin.org/post', data={'key': 'value'}))  # class 'requests.models.Response'
print(requests.post('https://httpbin.org/post', data=[('key', 'value')]))

# pro poslani JSON dat je json parameter. Kdyz se JSON data posilaji pres json, tak requests prida spravny header
response = requests.post('https://httpbin.org/post', json={'key': 'value'})
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])

# making a request, the Request lib prepares it before sending it to the destination server
# viewing the PreparedRequest by accessing .request
response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response.request.headers['content-type'])
print(response.request.url)
print(response.request.body)

# SSL encryption - for sensitive data, Requests does that by default
print(requests.get('https://api.github.com', verify=False))  # disableing SSL Ceritificate verification


# PERFORMANCE
# 1. timeouts
"""
making a request to an external service, the system will wait upon the response before moving on. If the applucation
waits too long for that response, user experience could suffer or background jobs could hang.
By defalt, Requests will wait indefinitely - it's necessary to specify a timeout duration to prevent this.
"""
print(requests.get('https://api.github.com', timeout=1.5))  # the request will timeout after 1.5 sec
# tuple - timeout for establishing the connection to the server, timeout for waitinf for a responce after the connection
print(requests.get('https://api.github.com', timeout=(2, 5)))

# Timeout exception can be handeled
try:
    response = requests.get('https://api.github.com', timeout=1)
except requests.exceptions.Timeout:
    print('The request timed out.')
else:
    print('The request did not timed out.')

# 2. Session Object
"""
functions like get(), put() are high level request and the hide what's going on under the hood (details about how
connections are managed etc.).
Underneath there is a class Session - it can be used to fine-tune control over how requests are made or improve the
performance of my requests 
Session Object allowd to persist certain parameters across requests, cookies.
When making several requests to the same host,the underlying TCP connection will be reused rather than establishing a 
new one, which can result in significant performance increase. 
"""
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)

# can be used to provide default data to the request methods - by providing data to the properties on Session Object
s = requests.Session()
s.auth = ('user', 'password')
s.headers.update({'x-test': 'true'})
s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})  # both x-test and x-test2 are sent


# 3. Max Retries - for retrying failed requests - Requests doesn't do it by default
# implement Transport Adapter
github_adapter = requests.adapters.HTTPAdapter(max_retries=3)
session = requests.Session()
# use github_adapter for all requests to endpoints thatstart with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except requests.exceptions.ConnectionError:
    print(requests.exceptions.ConnectionError)
