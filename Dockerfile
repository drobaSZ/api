# Вибираємо базовий образ
FROM python:3.9-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо всі файли в контейнер
COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Відкриваємо порт
EXPOSE 5000

# Запускаємо додаток
CMD ["python", "app.py"]
