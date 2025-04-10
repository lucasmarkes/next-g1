FROM python:3.10


WORKDIR /Beatriz-ma-branch


# Copia os arquivos necessários
COPY requirements.txt .
COPY main_back.py .
COPY user_requests.py .
COPY repo_requests.py .
COPY models_github.py .
COPY repo_graph_commits.py . 
COPY user_graph_commits.py .
COPY pdf_user_gerar.py .
COPY pdf_repo_gerar.py .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt


# Expõe a porta que o uvicorn vai usar
EXPOSE 8000


# Executa o servidor com o novo arquivo main_back
CMD ["uvicorn", "main_back:app", "--host", "0.0.0.0", "--port", "8000"]
