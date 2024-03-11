import requests

r = requests.get('http://localhost:8080/alt')

print(r.status_code)
print(r.text)
