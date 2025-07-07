# FastAPI SRE App

## Ringkasan

Proyek ini adalah aplikasi FastAPI yang dirancang untuk praktik Site Reliability Engineering (SRE). Stack utama:
- **FastAPI** (backend API)
- **Uvicorn** (ASGI server)
- **Prometheus** (monitoring)
- **Grafana** (visualisasi monitoring)
- **UptimeRobot** (monitoring uptime)
- **GitHub Actions** (CI/CD)

Tujuan: Menyediakan API yang mudah di-deploy, terpantau, dan siap untuk pengembangan berkelanjutan.

---

## Setup Lokal

### Prasyarat
- Python 3.9+
- Git
- pip

### Langkah Instalasi

1. **Clone repository:**
  ```bash
  git clone https://github.com/eka0789/fastapi-sre-app.git
  cd fastapi-sre-app
  ```
  > Ganti `username` dengan nama pengguna GitHub yang sesuai jika berbeda.

2. **Buat virtual environment (opsional tapi direkomendasikan):**
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows
  ```

3. **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

4. **Jalankan aplikasi:**
  ```bash
  uvicorn app.main:app --reload
  ```

5. **Akses API:**
  - Buka browser ke [http://localhost:8000/docs](http://localhost:8000/docs) untuk dokumentasi Swagger.

---

## Monitoring & Observability

- **Prometheus** dan **Grafana** dapat di-setup menggunakan docker-compose (lihat file `docker-compose.yml` jika tersedia).
- **UptimeRobot** dapat dikonfigurasi untuk memonitor endpoint health API.

---

## CI/CD

- Pipeline otomatis menggunakan **GitHub Actions** (lihat `.github/workflows/deploy.yml`).

---

## Kontribusi

Silakan fork repo ini dan buat pull request untuk kontribusi.