
# Proyek CRUD Flask & Docker Compose

Aplikasi ini merupakan implementasi **CRUD (Create, Read, Update, Delete)** sederhana untuk **User** dan **Produk** sebagai pemenuhan Ujian Tengah Semester mata kuliah **Pemrograman Sisi Server**.

`Calvin Samuel Simbolon - A11.2023.14880`

<p align="center">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</p>

## 🗺️ Arsitektur Aplikasi

Aplikasi ini terdiri dari dua _service_ utama yang diatur melalui file [`docker-compose.yml`](docker-compose.yml):

1.  **`web`** → Kontainer aplikasi **Flask** yang dibangun dari [`Dockerfile`](Dockerfile).
2.  **`db`** → Kontainer **MySQL 8.0** menggunakan _official image_ dari Docker Hub.

> 💾 Data database disimpan secara persisten menggunakan **Docker Volume** bernama `db_data` agar data tidak hilang saat kontainer dimatikan.

## ✨ Fitur Aplikasi

* Fungsionalitas **CRUD** penuh (Create, Read, Update, Delete) untuk **User**.
* Fungsionalitas **CRUD** penuh (Create, Read, Update, Delete) untuk **Produk**.
* Tampilan UI sederhana dengan *form* terpisah untuk *create* dan *update*.
* Persistensi data menggunakan **Docker Volume**.
* *Single-command setup* menggunakan **Docker Compose**.

## 📂 Struktur Folder

Proyek ini menggunakan struktur sederhana dengan satu file `app.py` sebagai intinya.

```

.
├── app.py             \# \<-- File utama Flask (Model, View, Controller)
├── templates/
│   ├── layout.html    \# \<-- Template dasar (menu navigasi)
│   ├── dashboard.html \# \<-- Halaman utama
│   ├── users.html     \# \<-- Halaman CRUD User
│   └── products.html  \# \<-- Halaman CRUD Product
├── Dockerfile         \# \<-- Resep untuk membangun image 'web'
├── docker-compose.yml \# \<-- File orkestrasi untuk 'web' dan 'db'
├── requirements.txt   \# \<-- Daftar library Python (Flask, SQLAlchemy, dll.)
└── README.md

````

## ⚙️ Persyaratan

Pastikan Anda sudah menginstal:

* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/) (biasanya sudah termasuk dalam Docker Desktop)

## 🚀 Cara Menjalankan Aplikasi

1.  **Clone repositori ini**
    ```bash
    git clone https://github.com/aplicalvin/uts-pss
    cd uts-pss
    ```

2.  **Jalankan Docker Compose**
    Perintah ini akan membangun *image* dan menjalankan kontainer `web` dan `db` di *background* (`-d`).
    ```bash
    docker compose up -d --build
    ```
    *(Flag `--build` hanya diperlukan saat pertama kali atau jika ada perubahan pada `Dockerfile`/`requirements.txt`)*

3.  **Akses Aplikasi**
    Tunggu sekitar 10-15 detik hingga database siap, lalu buka browser Anda:
    👉 **[http://localhost:5000](http://localhost:5000)**

4.  **Menghentikan Aplikasi**
    Perintah ini akan menghentikan dan menghapus kontainer yang sedang berjalan.
    ```bash
    docker compose down
    ```

## 📜 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
````