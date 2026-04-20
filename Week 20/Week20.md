# Review Week 19 - Evaluasi Hasil Siswa

Berikut pembahasan singkat hasil kerjaan Week 19 dari folder Submission. Penilaian hanya untuk fungsi JavaScript sesuai tugas pada template; HTML dan CSS tidak dinilai.

## Bobot Penilaian (Total 100%)

| Tugas | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| Bobot | 8%   | 14% | 16%  | 20%  | 14%  | 14%  | 14%  |

## Rekap Nilai (Berdasarkan Bobot)

| Nama          | T1  | T2  | T3  | T4  | T5  | T6  | T7  | Total |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Justin Arland | 90  | 85  | 85  | 70  | 50  | 85  | 80  | 77.8  |
| Nathan Hans   | 80  | 75  | 40  | 30  | 30  | 30  | 70  | 47.5  |
| Raffael Teng  | 40  | 20  | 20  | 20  | 20  | 20  | 20  | 21.6  |

## Justin Arland

**Yang sudah oke**

- Tugas 1, 2, 3, 6, dan 7 berjalan sesuai konsep dasar (event, DOM, array warna, update teks).

**Catatan perbaikan**

- Tugas 5 (toggle konten) masih bermasalah. Di dalam event klik, konten selalu diset `display = "none"`, jadi tidak bisa benar-benar toggle. Ada blok `if` di luar event yang seharusnya ada di dalam event klik.
- Tugas 4 validasi form: pesan error hanya `"error"`, kurang jelas untuk user. Lebih baik tampilkan "Nama wajib diisi" / "Email wajib diisi".
- Tugas 7: saat input kosong, sebaiknya tampilkan teks default, bukan string kosong.

**Perbaikan**

- Pindahkan logika toggle ke dalam event klik, gunakan `classList.toggle("show")` agar konsisten dengan CSS.
- Tampilkan pesan validasi yang jelas.

## Nathan Hans

**Yang sudah oke**

- Tugas 1 dan 2 sudah mengarah benar (event + update angka).

**Catatan perbaikan**

- Tugas 3: variabel `color.length` salah, seharusnya `colors.length`. Ini bikin error dan warna tidak jalan.
- Tugas 5: `hidden-content-box` tidak ada di HTML, ID yang benar `hidden-content`.
- Tugas 4, 6 belum selesai (masih komentar / placeholder).
- Ada elemen HTML tambahan di luar container (button dan script terpisah), jadi sulit dibaca. Catatan ini di luar penilaian.

**Saran cepat**

- Rapikan struktur HTML: semua task tetap di dalam container.
- Pastikan ID di JS sama persis dengan ID di HTML.
- Selesaikan task yang masih kosong sebelum lanjut ke styling.

## Raffael Teng

**Yang sudah oke**

- Sudah mencoba mengerjakan tugas satu per satu, terlihat usaha untuk memahami tiap bagian.

**Catatan perbaikan besar**

- Banyak HTML dan JS yang belum valid: tag tidak tertutup, ada teks acak di dalam script, dan penulisan atribut salah (contoh: `id` ditulis di dalam isi tag, bukan sebagai atribut). Catatan ini di luar penilaian.
- Tugas 2, 3, 4, 5, 6 belum jalan karena variabel / ID tidak sesuai dan logika masih kosong.
- Ada potongan kode yang bukan sintaks JS (`"Array colors" = 1`, `alert(berhasil)`, `(show).hiddenContent.toggle`). Ini bikin file error total sehingga bagian lain tidak jalan.

**Saran cepat**

- Mulai ulang dari template kosong, isi satu tugas dulu sampai berjalan, lalu lanjut ke tugas berikutnya.
- Cek console browser untuk melihat error pertama yang menghentikan script.

---

## Kenapa cuma 3?

Sudah ada beberapa yang mengirim jawaban tapi tidak menambahkan Nama - Kelas.
padahal sudah diberitahukan untuk menambahkan Nama - Kelas karena beberapa kontak yang hilang. Jika namamu tidak ada di Submission maka tidak mendapatkan nilai.
