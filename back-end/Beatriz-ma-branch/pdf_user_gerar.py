import os
from fpdf import FPDF
from github_utils import baixar_avatar, buscar_estatisticas
from datetime import datetime
from fpdf import FPDF


def gerar_pdf_usuario(usuario: str) -> str:

    stats = buscar_estatisticas(usuario)
    avatar = baixar_avatar(stats.avatar_url)

    stats = buscar_estatisticas(usuario)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", size=14)

    if avatar and os.path.exists(avatar):
        pdf.image(avatar, x=160, y=15, w=30)

    pdf.set_title(f"Relatório GitHub - {usuario}")
    pdf.cell(200, 10, f" Relatório GitHub - @{usuario}", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f" Nome: {stats.nome}", ln=True)
    pdf.cell(200, 10, f" Login: {stats.login}", ln=True)
    pdf.cell(200, 10, f" Localização: {stats.localizacao}", ln=True)
    pdf.cell(200, 10, f" Criado em: {stats.criado_em}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, " Estatísticas:", ln=True)
    pdf.cell(200, 10, f"- Seguidores: {stats.seguidores}", ln=True)
    pdf.cell(200, 10, f"- Repositórios públicos: {stats.public_repos}", ln=True)
    pdf.cell(200, 10, f"- Commits: {stats.commits}", ln=True)
    pdf.cell(200, 10, f"- PRs abertas: {stats.prs_abertas}", ln=True)
    pdf.cell(200, 10, f"- PRs fechadas: {stats.prs_fechadas}", ln=True)
    pdf.cell(200, 10, f"- Branches: {stats.branches}", ln=True)
    pdf.cell(200, 10, f"- Estrelas: {stats.estrelas}", ln=True)
    pdf.cell(200, 10, f"- Forks: {stats.forks}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, " Linguagens utilizadas (Top 5):", ln=True)
    if stats.linguagens:
        for lang in stats.linguagens:
            pdf.cell(200, 10, f"- {lang.linguagem}: {lang.porcentagem:.1f}%", ln=True)
    else:
        pdf.cell(200, 10, "- Nenhuma linguagem identificada.", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 5, "Este relatório foi gerado automaticamente com base nas informações públicas do GitHub.")

    nome_arquivo = f"relatorio_usuario_{usuario}.pdf"
    pdf.output(nome_arquivo)
    return nome_arquivo
