import requests

r = requests.get('http://localhost:8080/')

print(r.status_code)
print(r.text)
