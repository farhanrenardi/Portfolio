# Panduan Pengembangan Portofolio Web (Copilot Instructions)

## 1. Konteks Proyek & Identitas Pengembang
- **Nama Pengembang:** Farhan Faiq Renardi
- **Profil:** Lulusan Teknik Industri, Data Analyst, dan Aspiring Data Scientist.
- **Tujuan:** Membuat website portofolio statis (Static Website) yang profesional, responsif, dan ringan untuk di-deploy ke GitHub Pages.
- **File Referensi Utama (Wajib Dibaca):** - `CV_Farhan Faiq_Engineer.pdf` (Untuk pengalaman kerja, skill teknis, dan proyek ML).
  - `Portfolio_Farhan Faiq Renardi.pdf` (Untuk deskripsi proyek Dashboard dan Sistem Informasi).

## 2. Tech Stack yang Digunakan
- **Frontend Utama:** HTML5 Semantic, CSS3.
- **Framework CSS:** Bootstrap 5 (via CDN) untuk tata letak yang cepat dan *mobile-responsive*.
- **JavaScript:** Vanilla JS (hanya jika diperlukan untuk fungsionalitas UI sederhana seperti *slider*).
- **Batasan Penting:** JANGAN gunakan bahasa *backend* (PHP, Python, Node.js, atau database SQL) karena web ini akan di-hosting secara statis di GitHub Pages.

## 3. Struktur Halaman (Satu Halaman / Single Page Application style)
Website harus terdiri dari bagian-bagian berikut secara berurutan:

### A. Hero Section
- Tampilkan nama "Farhan Faiq Renardi".
- Tampilkan *tagline*: "Aspiring Data Scientist | Industrial Engineering Graduate".
- Masukkan ringkasan profil dari CV (berpengalaman dalam *machine learning*, *data pipelines*, dsb).
- Sediakan tombol CTA (Call to Action) menuju LinkedIn dan Email.

### B. Pengalaman Profesional (Professional Experience)
- Ambil data dari CV.
- Tampilkan peran sebagai Data Analyst di Telkom Indonesia dan Semen Indonesia Group.
- Gunakan format *list* atau *timeline* yang rapi.

### C. Galeri Proyek (Projects) - *Aturan Khusus Visualisasi*
Bagi proyek menjadi 3 kategori utama dengan aturan tampilan yang berbeda:
1. **Data Analytics & Dashboards (Power BI):** - Proyek: *Financial Overview*, *Sourcing Monitoring*, *Weekly Price Monitoring*.
   - **Aturan UI:** Gunakan tag `<video controls>` untuk menampilkan demo interaktif (jangan gunakan *iframe*).
2. **Machine Learning Projects:**
   - Proyek: *Male Pattern Baldness Classification*, *Employee Profile Match-Up Optimization*.
   - **Aturan UI:** Gunakan format *Card*. Berikan tombol eksternal (contoh: "Coba Demo di Hugging Face" atau "Lihat Kode di GitHub").
3. **Information Systems:**
   - Proyek: *Logistics Information System for CV Qirana Furniture*.
   - **Aturan UI:** Gunakan komponen `Bootstrap Carousel` (Slider) untuk menampilkan multiple *screenshot* antarmuka sistem.

### D. Technical Skills & Organisasi
- Tampilkan *skills* (Programming, ML, Data Analytics, Web) menggunakan sistem *badges* atau *tags* Bootstrap agar modern.
- Masukkan pengalaman kepanitiaan/organisasi dari CV secara singkat.

### E. Footer
- *Copyright* tahun berjalan dan tautan sosial media (LinkedIn, GitHub).

## 4. Aturan Penulisan Kode (Coding Standards)
- **Bahasa Komentar:** Gunakan Bahasa Indonesia atau Inggris yang jelas untuk setiap *section*.
- **Aksesibilitas:** Selalu gunakan atribut `alt` pada gambar dan aria-label pada tombol.
- **Struktur Folder Asumsi:**
  - `/images/` (untuk aset foto/screenshot)
  - `/videos/` (untuk demo dashboard)