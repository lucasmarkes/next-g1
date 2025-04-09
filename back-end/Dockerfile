FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY github_utils.py .
COPY models_github.py .
COPY pdf_repo_gerar.py .
COPY pdf_user_gerar.py .
COPY user_graph_commits.py .
COPY repo_graph_commits.py .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
