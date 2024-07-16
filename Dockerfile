FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV API_KEY="YOUR_API_KEY"

CMD ["python", "app.py"]
