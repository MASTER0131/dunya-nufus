FROM python:3.9-slim
WORKDIR /app
# Önce bağımlılıkları yükleyelim
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Sonra kodları kopyalayalım
COPY . .
# Uygulamayı başlatalım
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]