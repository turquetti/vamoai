from model.github import GithubModel

class GithubRequest():
    def __init__(self):
        self.pagina = 1
        self.model = GithubModel()
    
    def search(self, termo, retorna_tipo):
        retorna_objeto = []

        if retorna_tipo == 'csv':
            retorna_obj = self.model.search_as_csv(termo, self.pagina)
        
        elif retorna_tipo == 'json':
            retorna_obj = self.model.search_as_json(termo, self.pagina)
        
        self.pagina += 1

        return retorna_obj