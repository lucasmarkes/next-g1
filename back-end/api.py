import requests 
   
class Commits:
    def __init__(self, login: str, repos: str):
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
