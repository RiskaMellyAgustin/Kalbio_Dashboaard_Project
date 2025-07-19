# Project Title: `MSTD Dashboard Project`
---
Company: PT Kalbio Global Medika

Start Date: 2025-06-25

End Date: 2025-07-31

Objective: Membangun dashboard interaktif yang menyajikan informasi real-time terkait yield produksi dan titik-titik terjadinya yield loss di setiap batch (proses yg terjadi saat ini), untuk membantu MSTD dalam melakukan analisis performa dan pengambilan keputusan berbasis data.

---
## Struktur & Branch

Setiap orang memiliki branch masing-masing:

| Nama     | Branch         | Tugas                        |
|----------|----------------|------------------------------------|
| Alysia     | quality_analyst     | 1. Menentukan aturan validasi data di setiap tahap (input, ETL, DB); 2. Membangun sistem validasi otomatis (range, format, field wajib, dll); 3. Mendesain sistem notifikasi otomatis saat terjadi error validasi (log, alert, popup, atau email); 4. Berkolaborasi dengan ETL dan Integrator untuk memastikan validasi berjalan sesuai rencana     |
| Jeny     | automated_pipeline     | 1. Membangun pipeline otomatis menggunakan Python, cron job, atau Airflow; 2. Menangani data kosong atau error pada saat ingest; 3. Memproses staging dan memasukkan data ke dalam database; 4. Membuat logging proses dan menampilkan pop up pada web jika terjadi kegagalan      |
| Rut     | dashboard_visualization     | 1. Membangun dashboard interaktif (misal menggunakan pychart, dsb); 2. Mengambil data dari database untuk keperluan visualisasi; 3. Menyediakan fitur filter (minggu, kategori aktivitas); 4. Menyediakan fitur ekspor data ke format CSV dan PDF; 5. Mendokumentasikan fitur dashboard  |
| Riska     | quality_analyst      | 1. Menentukan aturan validasi data di setiap tahap (input, ETL, DB); 2. Membangun sistem validasi otomatis (range, format, field wajib, dll); 3. Mendesain sistem notifikasi otomatis saat terjadi error validasi (log, alert, popup, atau email); 4. Berkolaborasi dengan ETL dan Integrator untuk memastikan validasi berjalan sesuai rencana   |
| Valencia    | database_administrator   | 1. Merancang skema database relasional (master data & transaksi); 2. Menyusun skrip backup rutin dan restore database; 3. Memantau konektivitas database ke ETL dan Dashboard; 4. Mendukung fitur ekspor data     |

---

## Cara Mulai
### 1. Clone Repositori
```bash
git clone https://github.com/RiskaMellyAgustin/Kalbio_Dashboaard_Project
cd Kalbio_Dashboaard_Project
```

### 2. Checkout ke Branch Kalian
```bash
git checkout nama-branch
```
contoh: `git checkout etl`

### 3. Update dan Push
Setelah selesai mengedit atau menambahkan file:
```bash
git add .
git commit -m "Deskripsi perubahan singkat"
git push origin nama-branch
```

---

## Integrasi ke main
Semua pekerjaan akan digabung ke branch main melalui `Pull Request` (PR):
- Buka GitHub
- Buat PR dari branch kalian ke main
- PR akan di-merge

---

## Branch main
- Jangan push langsung ke `main`
- Semua update harus melalui `Pull Request` (PR)
- `main` hanya berisi kode yang sudah stabil dan teruji

---


## Struktur Folder 'main'
```bash
kalbio_dashboard_project/
├── backend/                          # Semua logika backend (Django)
│   ├── kalbio_dashboard/            # Main Django project folder
│   │   ├── settings.py              # Setting project: DB, apps, static, dll
│   │   ├── urls.py                  # Routing utama
│   │   └── wsgi.py / asgi.py        # Web server interface
│   │
│   ├── yieldapp/                    # App utama: logika yield dashboard
│   │   ├── models.py                # Struktur tabel (ORM)
│   │   ├── views.py                 # Fungsi view untuk dashboard, upload, dll
│   │   ├── urls.py                  # Routing app yield
│   │   ├── forms.py                 # Form upload CSV
│   │   ├── admin.py                 # Admin panel
│   │   ├── services/                # ⬇ Semua logika bisnis di sini
│   │   │   ├── calculator.py        # Rumus yield, loss, dll
│   │   │   ├── cleaning.py          # Script cleaning data CSV
│   │   │   ├── parser.py            # (opsional) parsing struktur file
│   │   │   └── oracle_api_client.py # ⬅ Kirim data ke API Oracle (mock/test)
│   │   ├── templates/
│   │   │   └── yieldapp/
│   │   │       ├── login.html             # Login page
│   │   │       ├── upload.html            # Upload CSV
│   │   │       ├── dashboard_operator.html    # ⬅ Halaman dashboard operator
│   │   │       ├── dashboard_mstd.html        # ⬅ Halaman dashboard MSTD
│   │   │       ├── dashboard_qc.html          # ⬅ Halaman dashboard QC (opsional)
│   │   │       └── detail_batch.html          # Detail info batch & grafik
│   │   └── static/
│   │       └── yieldapp/
│   │           ├── css/
│   │           ├── js/
│   │           └── img/
│   │
│   └── manage.py
├── .gitignore
├── requirements.txt                 # Library Python & Django
└── README.md                        # Dokumentasi project
---
##Optional
│
├── integration/                     # Folder untuk mock/simulasi API eksternal
│   └── oracle_mock_api/             # Simulasi FastAPI untuk Oracle
│       ├── main.py                  # FastAPI server (endpoint API Oracle)
│       ├── schemas.py               # Struktur request/response
│       └── database.py              # (opsional) jika mau simpan hasil dummy
│
├── frontend/                        # Optional: frontend terpisah (React/Vue/etc)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── utils/
│   └── dist/
│
├── media/                           # CSV yang diupload (via FileField)
```

---

## Tips
- Jangan commit file data besar (gunakan .gitignore)
- Update requirements.txt jika menambah library Python baru.

---
