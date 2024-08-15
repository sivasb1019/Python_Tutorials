from email import header

import requests

'''url = 'https://www.ibm.com/'
r = req.get(url)
h = r.headers
print(r.status_code)
print(r.request.headers)
print(r.request.body)
print(h)
print(h['date'])
print(h['Content-Type'])
print(r.encoding)
print(r.text[0:10])'''

# Get request
'''
url_get = "http://httpbin.org/get"
payload = {"name": "Joseph", "ID": "123"}
r = requests.get(url_get, params=payload)
print(r.url)
print(r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])
'''

# Post requests

url_post = "http://httpbin.org/post"
payload = {"name": "Joseph", "ID": "123"}
r = requests.post(url_post, params=payload)
print(r.url)
print(r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])