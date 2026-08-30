# Review Week 20 - Evaluasi Hasil Siswa

Berikut pembahasan singkat hasil kerjaan Week 20 dari folder Submission. Penilaian hanya untuk fungsi JavaScript sesuai tugas pada template; HTML dan CSS tidak dinilai.

## Bobot Penilaian (Total 50%)

| Tugas | 1    | 2    | 3    | 4    | 5   | 6   | 7    | 8    | 9   | 10   | 11   | 12  | 13   | 14  | 15   |
| ----- | ---- | ---- | ---- | ---- | --- | --- | ---- | ---- | --- | ---- | ---- | --- | ---- | --- | ---- |
| Bobot | 3.5% | 3.5% | 3.5% | 3.5% | 3%  | 4%  | 3.5% | 3.5% | 3%  | 3.5% | 3.5% | 3%  | 3.5% | 3%  | 3.5% |

## Rekap Nilai (Skala 100)

| Nama        | T1  | T2  | T3  | T4  | T5  | T6  | T7  | T8  | T9  | T10 | T11 | T12 | T13 | T14 | T15 | Total |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| Jonathan7   | 85  | 90  | 90  | 80  | 90  | 85  | 85  | 90  | 90  | 80  | 90  | 90  | 90  | 90  | 30  | 85.1  |
| NathanHans7 | 0   | 0   | 0   | 0   | 85  | 0   | 0   | 70  | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 10.0  |
| Lemuel7     | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0.0   |

## Jonathan Kls 7

**Yang sudah oke**

- Tugas 1-14 umumnya berjalan dan sesuai konsep (kalkulator, to-do, search, counter, validasi, timer, dll).

**Catatan perbaikan**

- Tugas 1: tombol titik (`data-dot`) belum ditangani, jadi input desimal tidak bisa.
- Tugas 3: data produk tidak lengkap (tidak ada `Webcam`).
- Tugas 4: accordion hanya 3 item, seharusnya 4.
- Tugas 15: handler tidak dipasang (fungsi buka FAQ tidak dipanggil) dan hanya 3 item, sehingga FAQ tidak bisa dibuka.

**Perbaikan**

- Tambahkan handler `data-dot`, lengkapi data list, tambah item accordion/FAQ menjadi 4, dan panggil `bukaFaq()` setelah membuat konten.

## NathanHans Kls 7

**Yang sudah oke**

- Tugas 5 (counter step) berjalan.
- Tugas 8 (timer) sudah ada start/pause/reset dasar.

**Catatan perbaikan**

- Tugas lain masih kosong.
- Timer tidak menghentikan interval saat mencapai 00:00 sehingga bisa berjalan ke negatif.
- Reset hanya mengubah tampilan ke `00:00` tanpa set ulang state countdown.

**Saran cepat**

- Lengkapi tugas yang belum dikerjakan, dan tambahkan pengecekan stop saat waktu habis.

## Lemuel Kls 7

**Catatan perbaikan besar**

- Ada sintaks yang tidak valid pada Tugas 5 (`function if`), sehingga seluruh script gagal jalan.
- Tugas lain masih berupa template atau kosong.

**Saran cepat**

- Hapus kode yang tidak valid, mulai dari tugas paling mudah (misalnya T1 atau T2), dan cek error pertama di console.

---
