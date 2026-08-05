FROM python:3.12-slim

# Αποφυγή buffering στα logs (πολύ σημαντικό στο Render, αλλιώς
# δεν βλέπεις print()/logging live)
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Πρώτα requirements για να εκμεταλλευόμαστε το Docker layer cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Μετά όλα τα υπόλοιπα αρχεία
COPY . .

# Fake/placeholder port — το Render το αντικαθιστά με το πραγματικό
# μέσω της env var PORT, αλλά το EXPOSE πρέπει να υπάρχει
EXPOSE 10000

CMD ["python", "main.py"]
