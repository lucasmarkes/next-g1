import os
import requests
from fpdf import FPDF
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

# Configurações do repositório: dados da consulta
owner = "goldbergyoni"  # Dono do repositório
repo = "javascript-testing-best-practices"      # Nome do repositório
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Função para fazer requisições
def get_github_data(endpoint):
    url = f"https://api.github.com/repos/{owner}/{repo}{endpoint}"
    response = requests.get(url, headers=headers)
    return response.json()

# Coletando estatísticas principais
repo_data = get_github_data("")
contributors = get_github_data("/contributors")
languages = get_github_data("/languages")
commit_activity = get_github_data("/stats/commit_activity")

# Criando o relatório em PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, f"Relatório do Repositório: {repo}", ln=True, align="C")

# Adicionando dados principais
pdf.set_font("Arial", "", 10)
pdf.ln(10)
pdf.cell(200, 10, f" Estrelas: {repo_data.get('stargazers_count', 'N/A')}", ln=True)
pdf.cell(200, 10, f" Forks: {repo_data.get('forks_count', 'N/A')}", ln=True)
pdf.cell(200, 10, f" Watchers: {repo_data.get('watchers_count', 'N/A')}", ln=True)
pdf.cell(200, 10, f" Tamanho: {repo_data.get('size', 'N/A')} KB", ln=True)
pdf.cell(200, 10, f" Última atualização: {repo_data.get('updated_at', 'N/A')}", ln=True)

# Adicionando informações de contribuidores
pdf.ln(10)
pdf.set_font("Arial", "", 12)

# Verificar contributors
if isinstance(contributors, dict) and "message" in contributors:
    pdf.cell(200, 10, " Contribuidores:", ln=True)
    pdf.cell(200, 10, "Erro ao obter contribuidores: Repositório muito grande.", ln=True)
else:
    pdf.cell(200, 10, " Top 10 Contribuidores:", ln=True)
    pdf.set_font("Arial", "", 10)

    for contributor in contributors[:10]:  # Pegando os 10 primeiros
        login = contributor.get("login", "Desconhecido")
        contributions = contributor.get("contributions", 0)
        pdf.cell(200, 10, f"- {login} ({contributions} commits)", ln=True)

# Adicionando linguagens usadas
pdf.ln(10)
pdf.set_font("Arial", "", 12)
pdf.cell(200, 10, " Linguagens Utilizadas:", ln=True)
pdf.set_font("Arial", "", 10)
for lang, lines in languages.items():
    pdf.cell(200, 10, f"- {lang}: {lines} linhas", ln=True)

pdf.ln(10)
pdf.multi_cell(0, 10, "Este relatório foi gerado automaticamente com base nas informações públicas do GitHub.")

# Salvando PDF
nome_arquivo = f"relatorio_repositorio_{repo}.pdf"
pdf.output(nome_arquivo)
print(f" PDF gerado: {nome_arquivo}")