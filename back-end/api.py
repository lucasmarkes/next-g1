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
    


if __name__ == '__main__':
    meu_git = APIGit("freitasthiiago")
    print(meu_git)
