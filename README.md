# 📊 Student Data Score CLI

Aplikasi **Command Line Interface (CLI)** sederhana menggunakan **Python** untuk mengelola data nilai siswa. Proyek ini menerapkan operasi dasar **CRUD (Create, Read, Update, Delete)** dan menampilkan data dalam bentuk tabel yang rapi menggunakan library `tabulate`.

---

## 🚀 Fitur

* 📖 Menampilkan seluruh data siswa
* 🔍 Menampilkan data siswa berdasarkan **Student ID**
* ➕ Menambahkan data siswa baru
* ✏️ Memperbarui data siswa (per kolom atau semua kolom)
* 🗑️ Menghapus data siswa
* ✅ Validasi agar **Student ID** dan **Email** tidak duplikat
* 📋 Tampilan tabel menggunakan format `fancy_grid`

---

## 🧑‍💻 Teknologi yang Digunakan

* **Python 3**
* **tabulate**

---

## 📦 Instalasi

1. Clone repository:

```bash
git clone https://github.com/username/student-data-score-cli.git
cd student-data-score-cli
```

2. Pastikan Python sudah terinstal:

```bash
python --version
```

3. Install dependency yang dibutuhkan:

```bash
pip install tabulate
```

---

## ▶️ Cara Menjalankan Program

Jalankan program melalui terminal / command prompt:

```bash
python student_data.py
```

---

## 🧭 Menu Aplikasi

### Menu Utama

```
1. Read all data
2. Create new data
3. Update existing data
4. Delete existing data
5. Exit
```

### Menu Read

* Menampilkan semua data siswa
* Menampilkan data siswa berdasarkan ID

### Menu Create

* Menambahkan data siswa baru

### Menu Update

* Mengubah data siswa tertentu
* Mengubah seluruh data siswa

### Menu Delete

* Menghapus data siswa berdasarkan ID

---

## 🗂️ Struktur Data

Setiap data siswa disimpan dalam bentuk dictionary di dalam list:

```python
{
    "student_id": int,
    "name": str,
    "class": str,
    "gender": str,
    "age": int,
    "email": str,
    "score": int
}
```

---

## ⚠️ Catatan

* Data disimpan **sementara (in-memory)**, sehingga akan hilang saat program dihentikan.
* Program ini cocok untuk **latihan dasar Python**, struktur data, dan logika CRUD.

---

## 🔮 Pengembangan Selanjutnya

* Menyimpan data ke file (**JSON / CSV**)
* Menambahkan validasi input yang lebih lengkap
* Menambahkan fitur pencarian berdasarkan nama atau email
* Mengembangkan versi **GUI** atau **Web**

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran.

---

## ✍️ Author

Dibuat sebagai proyek latihan pemrograman Python.
