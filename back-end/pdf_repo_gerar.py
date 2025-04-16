from fpdf import FPDF
from repo_requests import info_repositorio


def gerar_pdf_repo(owner: str, repo: str) -> str:
    info = info_repositorio(owner, repo)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, f"Relatório do Repositório: {repo}", ln=True, align="C")

    pdf.set_font("Arial", "", 10)
    pdf.ln(10)
    pdf.cell(200, 10, f" Estrelas: {info.estrelas}", ln=True)
    pdf.cell(200, 10, f" Forks: {info.forks}", ln=True)
    pdf.cell(200, 10, f" Watchers: {info.watchers}", ln=True)
    pdf.cell(200, 10, f" Tamanho: {info.tamanho}", ln=True)
    pdf.cell(200, 10, f" Última atualização: {info.ultima_atualizacao}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, " Contribuidores (máximo: 10):", ln=True)
    pdf.set_font("Arial", "", 10)
    for contribuidor in info.contribuidores:
        pdf.cell(200, 10, contribuidor, ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, " Linguagens Utilizadas (máximo: 10):", ln=True)
    pdf.set_font("Arial", "", 10)
    for linguagem in info.linguagens_repo:
        pdf.cell(200, 10, linguagem, ln=True)

    pdf.ln(10)
    pdf.multi_cell(0, 10, "Este relatório foi gerado automaticamente com base nas informações públicas do GitHub. Considere os limites de requisições permitidas")

    nome_arquivo = f"relatorio_repositorio_{repo}.pdf"
    pdf.output(nome_arquivo)
    return nome_arquivo
