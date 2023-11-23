# Gambaran

Sistem Sewa Sepeda Bersama mewakili generasi baru layanan sewa sepeda di mana seluruh proses, mulai dari keanggotaan hingga penyewaan dan pengembalian sepeda, telah diotomatisasi. Sistem ini memungkinkan pengguna dengan mudah menyewa sepeda dari lokasi tertentu dan mengembalikannya ke lokasi lain yang ditentukan. Saat ini, ada lebih dari 500 program berbagi sepeda di seluruh dunia, yang terdiri dari lebih dari 500 ribu sepeda. Sistem-sistem ini memainkan peran penting dalam menangani masalah keuangan, lalu lintas, lingkungan, dan kesehatan.

Tujuan utama dari dibangunnya algoritma ini adalah untuk membantu memberikan insight sebagai alternatif pengambilan keputusan manajemen supply sepeda kepada perusahaan penyedia jasa.

# About the Data

Source: Capital Bikeshare Analytic Report  [link](https://www.kaggle.com/datasets/marklvl/bike-sharing-dataset)
Periode: Januari 2011 hingga Desember 2012

# Features:
dteday: Tanggal
season: Musim 
yr: Tahun
mnth: Bulan 
hr: Jam
holiday: Hari libur atau bukan (diekstrak dari Jadwal Libur)
weathersit:
1: Cerah, Beberapa awan, Sebagian berawan, Sebagian berawan
2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Beberapa awan, Kabut
3: Salju ringan, Hujan ringan + Badai petir + Awan bertebaran, Hujan ringan + Awan bertebaran
4: Hujan Lebat + Pallet Es + Badai Petir + Kabut, Salju + Kabut
temp: Temperatur ternormalisasi dalam Celsius. Nilai ini dihasilkan melalui rumus (t-t_min)/(t_max-t_min), dengan t_min=-8, t_max=+39 (hanya dalam skala per jam)
atemp: Temperatur terasa ternormalisasi dalam Celsius. Nilai ini dihasilkan melalui rumus (t-t_min)/(t_max-t_min), dengan t_min=-16, t_max=+50 (hanya dalam skala per jam)
hum: Kelembaban ternormalisasi. Nilai ini dibagi oleh 100 (maksimum)
casual: Jumlah pengguna kasual
registered: Jumlah pengguna terdaftar

cnt: count of total rental bikes including both casual and registered

# Modelling Process

Model prediktif yang diimplementasikan dalam proyek ini didasarkan pada analisis regresi. Cross-validation digunakan untuk memastikan kekokohan model dan mengidentifikasi model terbaik.

Model Winner: CatBoost

Setelah eksperimen dan evaluasi yang teliti, algoritma CatBoost dipilih sebagai model final untuk memprediksi jumlah sewa sepeda. CatBoost sangat baik dalam menangani variabel kategori, mengotomatisasi penanganan nilai yang hilang, dan memberikan pelatihan yang efisien dengan regularisasi bawaan untuk mencegah overfitting.


# Streamlit API
Algoritma ini telah diintegrasikan kepada API streamlit yang dapat diaccess melalui link dibawah ini:

[Bike Sharing Predictor](https://bikesharingpredictor.streamlit.app/)

to access app = http://localhost:8501/