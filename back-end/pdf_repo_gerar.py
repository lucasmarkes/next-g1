from fpdf import FPDF
from requests import request
from github_utils import get_github_data

def gerar_pdf_repo(owner: str, repo: str) -> str:
    repo_data = get_github_data(owner, repo, "")
    contributors = get_github_data(owner, repo, "/contributors")
    languages = get_github_data(owner, repo, "/languages")


    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, f"Relatório do Repositório: {repo}", ln=True, align="C")

    pdf.set_font("Arial", "", 10)
    pdf.ln(10)
    pdf.cell(200, 10, f" Estrelas: {repo_data.get('stargazers_count', 'N/A')}", ln=True)
    pdf.cell(200, 10, f" Forks: {repo_data.get('forks_count', 'N/A')}", ln=True)
    pdf.cell(200, 10, f" Watchers: {repo_data.get('watchers_count', 'N/A')}", ln=True)
    pdf.cell(200, 10, f" Tamanho: {repo_data.get('size', 'N/A')} KB", ln=True)
    pdf.cell(200, 10, f" Última atualização: {repo_data.get('updated_at', 'N/A')}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "", 12)

    if isinstance(contributors, dict) and "message" in contributors:
        pdf.cell(200, 10, " Contribuidores:", ln=True)
        pdf.cell(200, 10, "Erro ao obter contribuidores: Repositório muito grande.", ln=True)
    else:
        pdf.cell(200, 10, " Top 10 Contribuidores:", ln=True)
        pdf.set_font("Arial", "", 10)
        for contributor in contributors[:10]:
            login = contributor.get("login", "Desconhecido")
            contributions = contributor.get("contributions", 0)
            pdf.cell(200, 10, f"- {login} ({contributions} commits)", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, " Linguagens Utilizadas:", ln=True)
    pdf.set_font("Arial", "", 10)
    for lang, lines in languages.items():
        pdf.cell(200, 10, f"- {lang}: {lines} linhas", ln=True)

    pdf.ln(10)
    pdf.multi_cell(0, 10, "Este relatório foi gerado automaticamente com base nas informações públicas do GitHub.")

    nome_arquivo = f"relatorio_repositorio_{repo}.pdf"
    pdf.output(nome_arquivo)
    return nome_arquivo

