import os
import requests
from fpdf import FPDF
from dotenv import load_dotenv
from datetime import datetime

# === Carrega token ===
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"}

def baixar_avatar(url, caminho="avatar.png"):
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(caminho, "wb") as f:
            f.write(resp.content)
    return caminho

def gerar_relatorio_usuario(usuario):
    user_url = f"https://api.github.com/users/{usuario}"
    repos_url = f"https://api.github.com/users/{usuario}/repos?per_page=100"

    user_resp = requests.get(user_url, headers=HEADERS)
    repos_resp = requests.get(repos_url, headers=HEADERS)

    if user_resp.status_code != 200:
        print("Erro ao buscar usuário:", user_resp.json().get("message"))
        return

    user = user_resp.json()
    repos = repos_resp.json()
    avatar = baixar_avatar(user["avatar_url"])

    total_commits = 0
    total_branches = 0
    total_stars = 0
    total_forks = 0
    total_prs_open = 0
    total_prs_closed = 0
    total_linguagens = {}

    for repo in repos:
        repo_name = repo["name"]
        owner = repo["owner"]["login"]

        # Commits (até 100)
        commits_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits?per_page=100"
        commits_resp = requests.get(commits_url, headers=HEADERS)
        if commits_resp.status_code == 200:
            total_commits += len(commits_resp.json())

        # Branches
        branches_url = f"https://api.github.com/repos/{owner}/{repo_name}/branches"
        branches_resp = requests.get(branches_url, headers=HEADERS)
        if branches_resp.status_code == 200:
            total_branches += len(branches_resp.json())

        # Pull Requests abertas
        pulls_open_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls?state=open&per_page=100"
        pulls_open_resp = requests.get(pulls_open_url, headers=HEADERS)
        if pulls_open_resp.status_code == 200:
            total_prs_open += len(pulls_open_resp.json())

        # Pull Requests fechadas
        pulls_closed_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls?state=closed&per_page=100"
        pulls_closed_resp = requests.get(pulls_closed_url, headers=HEADERS)
        if pulls_closed_resp.status_code == 200:
            total_prs_closed += len(pulls_closed_resp.json())

        # Estrelas e forks
        total_stars += repo.get("stargazers_count", 0)
        total_forks += repo.get("forks_count", 0)

        # Linguagens
        languages_url = f"https://api.github.com/repos/{owner}/{repo_name}/languages"
        languages_resp = requests.get(languages_url, headers=HEADERS)
        if languages_resp.status_code == 200:
            langs = languages_resp.json()
            for lang, bytes_qtd in langs.items():
                total_linguagens[lang] = total_linguagens.get(lang, 0) + bytes_qtd

    # Top linguagens por porcentagem
    linguagens_ordenadas = sorted(total_linguagens.items(), key=lambda x: x[1], reverse=True)
    soma_total = sum(total_linguagens.values())
    top_5_linguagens = linguagens_ordenadas[:5]

    # === Criar PDF ===
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", size=14)
    pdf.set_title(f"Relatório GitHub - {usuario}")
    pdf.cell(200, 10, f" Relatório GitHub - @{usuario}", ln=True, align="C")
    pdf.ln(5)

    # Avatar
    if os.path.exists(avatar):
        pdf.image(avatar, x=160, y=15, w=30)
        pdf.ln(10)

    # Informações básicas
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f" Nome: {user.get('name', 'N/A')}", ln=True)
    pdf.cell(200, 10, f" Login: {user.get('login', 'N/A')}", ln=True)
    pdf.cell(200, 10, f" Localização: {user.get('location', 'N/A')}", ln=True)
    pdf.cell(200, 10, f" Criado em: {datetime.strptime(user['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d/%m/%Y')}", ln=True)

    # Estatísticas
    pdf.ln(10)
    pdf.cell(200, 10, " Estatísticas do GitHub:", ln=True)
    pdf.cell(200, 10, f"- Seguidores: {user.get('followers', 0)}", ln=True)
    pdf.cell(200, 10, f"- Estrelas recebidas: {total_stars}", ln=True)
    pdf.cell(200, 10, f"- Forks: {total_forks}", ln=True)
    pdf.cell(200, 10, f"- Repositórios públicos: {user.get('public_repos', 0)}", ln=True)
    pdf.cell(200, 10, f"- Commits (estimados): {total_commits}", ln=True)
    pdf.cell(200, 10, f"- Pull Requests (abertas): {total_prs_open}", ln=True)
    pdf.cell(200, 10, f"- Pull Requests (fechadas): {total_prs_closed}", ln=True)
    pdf.cell(200, 10, f"- Branches: {total_branches}", ln=True)

    # Linguagens
    pdf.ln(10)
    pdf.cell(200, 10, " Linguagens utilizadas (Top 5 por porcentagem):", ln=True)
    if top_5_linguagens and soma_total > 0:
        for lang, size in top_5_linguagens:
            porcentagem = (size / soma_total) * 100
            pdf.cell(200, 10, f"- {lang}: {porcentagem:.1f}%", ln=True)
    else:
        pdf.cell(200, 10, "- Nenhuma linguagem identificada.", ln=True)

    # Rodapé
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 5, "NOTA: Este relatório foi gerado automaticamente com base nas informações públicas do GitHub. Considere as limitações da REST API do GitHub ao analisar as estatísticas acima.")

    # Salvando arquivo
    nome_arquivo = f"relatorio_usuario_{usuario}.pdf"
    pdf.output(nome_arquivo)
    print(f" PDF gerado: {nome_arquivo}")

# === EXECUTAR ===
gerar_relatorio_usuario("torvalds")
