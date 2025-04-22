from fpdf import FPDF
from user_requests import buscar_estatisticas, buscar_usuario, baixar_avatar

def gerar_pdf_user(usuario: str,nome_arquivo: str = "") -> str:

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", size=14)
    pdf.set_title(f"Relatório GitHub - {usuario}")
    pdf.cell(200, 10, f" Relatório GitHub - @{usuario}", ln=True, align="C")
    pdf.ln(10)
   
    # Coleta os dados usando as funções definidas
    info_usuario = buscar_usuario(usuario)
    stats = buscar_estatisticas(usuario)

    # Baixar avatar
    avatar_path = baixar_avatar(info_usuario.get("avatar_url", ""))
   
    # Avatar no canto superior direito
    if avatar_path:
        pdf.image(avatar_path, x=160, y=20, w=30)
        pdf.ln(10)

    # Informações do usuário
    pdf.set_font("Arial", "", 12)
    for chave in ["nome", "login", "localizacao", "criado_em"]:
        valor = info_usuario.get(chave, "N/A")
        pdf.cell(0, 8, f"{chave.capitalize().replace('_', ' ')}: {valor}", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"Seguidores: {stats.seguidores}", ln=True)
    pdf.cell(200, 10, f"Repositórios públicos: {stats.public_repos}", ln=True)
    pdf.cell(200, 10, f"Commits totais: {stats.commits}", ln=True)
    pdf.cell(200, 10, f"Branches totais: {stats.branches}", ln=True)
    pdf.cell(200, 10, f"Pull Requests totais: {stats.prs_total}", ln=True)
    pdf.cell(200, 10, f"Forks totais: {stats.forks}", ln=True)
    pdf.cell(200, 10, f"Estrelas totais: {stats.estrelas}", ln=True)


    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, "Top Linguagens (máximo:10):", ln=True)
    pdf.set_font("Arial", "", 10)
    for linguagem in stats.linguagens:
        pdf.cell(200, 10, f"- {linguagem.linguagem}: {linguagem.porcentagem:.2f}%", ln=True)


    pdf.ln(10)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, "Repositórios públicos (máximo: 10):", ln=True)
    pdf.set_font("Arial", "", 10)
    for nome in stats.repositorios:
        pdf.cell(200, 10, f"- {nome}", ln=True)


    pdf.ln(10)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(200,10, "NOTA")
    pdf.set_font("Arial", "", 10)
    pdf.cell(200, 10, "As estattísticas são coletadas somente a partir das informações públicas do GitHub", ln=True)
    pdf.cell(200, 10, "Considere também que há limites de requisições permitidas ou suportadas pela API", ln=True)
    pdf.cell(200, 10, "Equipe RetrospectGit agradece a sua visita!", ln=True)


    if not nome_arquivo:
        nome_arquivo = f"relatorio_{usuario}.pdf"
    
    pdf.output(nome_arquivo)
    return nome_arquivo
