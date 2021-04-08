import requests

class GithubModel():
    def __init__(self):
        self.url = 'https://jobs.github.com/positions.json'

    def procura_json(self, termo, pagina):
        resposta = self.chamar(termo, pagina)
        return resposta.json()

    def chamar(self, termo, pagina):
        return requests.get(f'{self.url}?page={pagina}&search={termo}')