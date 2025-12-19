# Tugas_PCD_Sesi_11

Analisa Hasil Output Segmentasi Citra
1. Gambaran Umum Hasil

Berdasarkan hasil visualisasi, ditampilkan dua citra:

Citra Hasil Deteksi Tepi Sobel (kiri)
Menunjukkan kontur objek utama (tokoh humanoid) dalam bentuk garis-garis tepi berwarna terang di atas latar belakang gelap.

Hasil Segmentasi Threshold (T = 50) (kanan)
Menghasilkan citra hitam sepenuhnya, tanpa terlihat adanya objek atau tepi yang tersegmentasi.

2. Analisis Penyebab Hasil Segmentasi Kosong

Hasil segmentasi yang seluruhnya hitam menunjukkan bahwa tidak ada piksel yang memenuhi kriteria threshold (≥ 50). Hal ini disebabkan oleh beberapa faktor berikut:

a. Intensitas Piksel Citra Sobel Sangat Rendah

Citra hasil deteksi tepi Sobel pada gambar ini memiliki nilai intensitas yang dominan sangat kecil (gelap).

Garis tepi terlihat jelas secara visual, namun secara numerik nilai pikselnya berada di bawah threshold yang ditentukan.

b. Threshold Terlalu Tinggi

Nilai T = 50 ternyata tidak sesuai untuk karakteristik citra Sobel ini.

Akibatnya, semua piksel dianggap sebagai background (0), sehingga citra hasil threshold menjadi hitam seluruhnya.

c. Karakteristik Deteksi Tepi Sobel

Operator Sobel menghasilkan citra dengan:

Kontras tinggi secara visual

Tetapi rentang nilai intensitas sempit

Kondisi ini membuat basic thresholding sangat sensitif terhadap pemilihan nilai threshold.

3. Implikasi Terhadap Metode Basic Thresholding

Hasil ini menunjukkan bahwa:

✅ Basic thresholding sangat bergantung pada pemilihan nilai threshold
❌ Tidak adaptif terhadap distribusi intensitas citra
❌ Kurang robust untuk citra hasil edge detection tanpa normalisasi

Dengan kata lain, metode threshold sederhana tidak selalu langsung berhasil pada citra Sobel tanpa penyesuaian tambahan.

4. Solusi dan Perbaikan yang Dapat Dilakukan

Beberapa solusi yang dapat diterapkan untuk meningkatkan hasil segmentasi:

a. Menurunkan Nilai Threshold

Misalnya:

T = 10

T = 20

➡️ Akan membuat tepi objek mulai terlihat

b. Normalisasi Intensitas

Menyesuaikan nilai piksel ke rentang 0–255 sebelum thresholding agar distribusi lebih merata.

c. Menggunakan Metode Threshold yang Lebih Adaptif

Otsu Thresholding

Adaptive Thresholding

Metode ini lebih sesuai untuk citra dengan distribusi intensitas tidak merata seperti citra Sobel.

5. Kesimpulan

Dari hasil percobaan ini dapat disimpulkan bahwa:

Metode basic thresholding gagal mengekstraksi objek pada citra Sobel dengan threshold T = 50.

Hal ini disebabkan oleh nilai intensitas tepi yang berada di bawah nilai threshold.

Pemilihan threshold yang tepat atau penggunaan metode threshold adaptif sangat diperlukan untuk memperoleh hasil segmentasi yang optimal.
