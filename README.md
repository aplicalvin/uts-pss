# Proyek CRUD Flask & Docker Compose

Aplikasi ini adalah implementasi CRUD sederhana untuk User dan Produk menggunakan Flask, MySQL, dan Docker Compose.

## Arsitektur

Aplikasi ini terdiri dari dua service yang diatur oleh `docker-compose.yml`:
1.  `web`: Container aplikasi Flask (dibangun dari `Dockerfile`).
2.  `db`: Container database MySQL (menggunakan image resmi `mysql:8.0`).

Data database disimpan secara persisten menggunakan Docker Volume bernama `db_data`.

## Cara Menjalankan

**Prasyarat:**
* Docker
* Docker Compose

**Langkah-langkah:**

1.  Clone repositori ini.
2.  Buka terminal di folder utama proyek.
3.  Jalankan perintah berikut:

    ```bash
    docker-compose up -d
    ```
4.  Aplikasi akan berjalan dan bisa diakses di [http://localhost:5000](http://localhost:5000).

**Untuk Menghentikan Aplikasi:**
```bash
docker-compose down