import requests 

class APIGit:
    def __init__(self, login):
        self.login = login
        self.name = ''
        self.id = ''

        self.buscar_git()

    def buscar_git(self):
        resposta = requests.get(f"https://api.github.com/users/{self.login}")
        dados = resposta.json()
        self.name = dados.get('name', '')
        self.id = dados.get('id', '')

        def __repr__(self):
        return f"Login: {self.login}, Name: {self.name}, ID: {self.id}"

    
class Commits:
    def __init__(self, login, repos):
        self.login = login
        self.repos = repos

        self.get_commits()
    def get_commits(self):
        resposta = requests.get(f"https://api.github.com/repos/{self.login}/{self.repos}/commits")
        dados = resposta.json()
        return {'commits': len(dados)}






if __name__ == '__main__':
    meu_git = Commits("lucasmarkes", "next-exercicios")
    print(meu_git)
