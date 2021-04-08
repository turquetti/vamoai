import requests

requisicao = requests.post('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
resp = requisicao.json()

print(requisicao.status_code)
