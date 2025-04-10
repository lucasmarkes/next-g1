FROM python:3.10

WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt .
COPY app.py .
COPY user_requests.py .
COPY repo_requests.py .
COPY models_github.py .
COPY repo_graph_commits.py . 
COPY user_graph_commits.py .
COPY pdf_user_gerar.py .
COPY pdf_repo_gerar.py .
COPY .env .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt


# Expõe a porta que o uvicorn vai usar
EXPOSE 8000


# Executa o servidor com o novo arquivo main_back
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
