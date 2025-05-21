# Tes MBTI Interaktif dengan Streamlit

Aplikasi web sederhana untuk tes kepribadian MBTI menggunakan Streamlit.  
Menampilkan pertanyaan secara bertahap, menyimpan jawaban dengan session state, dan menampilkan hasil tipe MBTI lengkap dengan grafik interaktif.

---

## Fitur

- Total 20 pertanyaan MBTI, masing-masing dengan 2 pilihan jawaban.
- Pembagian soal dalam beberapa halaman, 5 pertanyaan per halaman.
- Navigasi soal menggunakan tombol **Sebelumnya** dan **Selanjutnya**.
- Jawaban disimpan di `st.session_state` agar tidak hilang saat berpindah halaman.
- Setelah menyelesaikan semua halaman, hasil MBTI ditampilkan di halaman hasil.
- Menampilkan tipe MBTI seperti `ESTJ`, `INFP`, dll.
- Ringkasan deskripsi singkat tipe MBTI berdasarkan hasil.
- Visualisasi skor dimensi MBTI dalam bentuk grafik bar interaktif menggunakan Plotly.

---

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Install dependensi:
   ```bash
   pip install streamlit pandas plotly
   ```
3. Simpan kode Python ke file, misal `app.py`.
4. Jalankan aplikasi dengan:
   ```bash
   streamlit run app.py
   ```
5. Buka browser dan akses `http://localhost:8501`.

---

## Struktur Kode

- **Pertanyaan:** Disimpan dalam list dengan format `(pertanyaan, [pilihan1, pilihan2])`.
- **Session State:** Menyimpan halaman saat ini dan jawaban pengguna dalam dictionary.
- **Navigasi:** Tombol untuk pindah halaman soal dan mengontrol flow.
- **Perhitungan Hasil:** Menghitung skor tiap dimensi MBTI berdasarkan jawaban.
- **Output:** Menampilkan hasil tipe MBTI, deskripsi singkat, dan grafik bar Plotly.

---

## Penjelasan MBTI

Tipe MBTI terdiri dari kombinasi 4 dimensi berikut:

- **E** (Ekstrovert) vs **I** (Introvert)
- **S** (Sensing) vs **N** (Intuition)
- **T** (Thinking) vs **F** (Feeling)
- **J** (Judging) vs **P** (Perceiving)

Setiap jawaban mengindikasikan kecenderungan ke salah satu sisi dimensi, dan hasilnya dirangkum untuk menentukan tipe akhir.

---

## Contoh Output

- Tipe MBTI: misal `INFJ`
- Deskripsi singkat karakteristik tipe
- Grafik bar menampilkan skor setiap dimensi, contohnya:
  - E vs I: 12 : 8
  - S vs N: 5 : 15
  - dll.

---

## Lisensi

Proyek ini open-source dan bebas digunakan untuk tujuan belajar dan pengembangan.
