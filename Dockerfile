# 1. Gunakan base image Python
FROM python:3.9-slim

# 2. Set direktori kerja di dalam container
WORKDIR /app

# 3. Copy file requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy sisa kode aplikasi ke dalam container
COPY . .

# 5. Perintah untuk menjalankan aplikasi saat container startup
# Kita gunakan "flask run" karena Gunicorn/Waitress tidak ada di requirements
# host=0.0.0.0 agar bisa diakses dari luar container
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]