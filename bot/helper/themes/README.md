Tema Khusus * * * 🛠

- Tutorial Tutorial tentang cara membuat Tema Khusus Anda.
- _mari kita Mulai dengan Utilitas._

### * Persyaratan :*
1. Editor Lokal atau Gunakan [github.dev](https://github.dev)
2. Contoh Berkas: Periksa [wzml_minimal.py](https://github.com/weebzone/WZML-X/blob/master/bot/helper/themes/wzml_minimal.py)


#### * Langkah 1: * Buka Editor Kosong dan Tempel Kode wzml_minimal.py dan beri nama itu wzml_custom.py
Anda bisa memberikan custom sesuai pilihan Anda, seperti wzml_futuristic.py, dll

#### * Langkah 2: * Mulailah dengan Mengedit dan Membuat Desain Akhir Anda ✨ ️ 
- _hal-hal yang Perlu Diingat saat Mengedit :_
  - Jangan Mengubah Nama Di Dalam { } (Kurung ke-2)
  - Jangan Mengubah Nama Variabel seperti ST_BN1_NAME, dll
  - Jangan Mengubah nama Kelas WZMLStyle
  - Jangan Gunakan string-f seperti f"{var}"
* Pengeditan Sampel :*
kelas WZMLStyle: # Jangan Ubah Ini
    ST_BN1_NAME = '{sb1n}'
    # Anda dapat Mengubah seperti di Bawah ini !! -->
    ST_BN1_NAME = "It's {sb1n} ❤ ️" # Gunakan tanda kutip ganda, saat menggunakan tanda kutip tunggal di dalamnya

#### * Langkah 3: * Sekarang, Buka [init.py] () dan Edit seperti yang ditunjukkan di bawah ini dan Simpan
AVL_THEMES = {"minimal": wzml_minimal," emoji": wzml_emoji," futuristik": wzml_futuristik} # Anda dapat menambahkan Lebih Banyak ...
# Tambahkan Nilai Dict Terakhir, seperti yang ditunjukkan, name: filename (sama seperti yang diberikan pada Langkah 1)
# Nama dapat berupa Pilihan apa pun untuk Memanggil Nama Tema
---

_sudah selesai, Sekarang Anda telah Berhasil Membuat Tema Anda Sendiri !_