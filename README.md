# Laporan Submission Pertama - Crude Oil Predictive
---

## Domain Proyek
Domain yang dipilih untuk proyek machine learning kali ini ada pada sektor keuangan dengan judul Crude Oil Predictive Analytics

### Latar Belakang
Dunia saat ini mengalami krisis energi dan itu menjadi salah satu faktor harga-harga bahan pangan maupun nonpangan maka dari itu judul ini saya angkat dan menggunakan data yang terkait. Data yang saya angkat adalah dataset harga saham minyak mentah yang ada pada yahoo finance. Ada dua jenis pasar saham didunia ini, yaitu  pasar saham ekuitas yang berupa saham atau sebuah surat berharga kemudian ada pasar saham komoditas yang bisa berupa emas, tembaga nikel kemudian selain dari logam mulia tersebut komoditas juga mencakup seperti gandum, gula, kopi, dan lain-lainnya.

Investor yang memilih berinvestasi terhadap suatu saham tentu saja memiliki tujuan, salah satu tujuan para investor berinvestasi terhadap instrumen saham adalah menerima dividen yang dijanjikan oleh sebuah perusahaan tempat dimana berinvestasi yang dihasilkan dari keuntungan perusahaan tersebut. Selain dari dividen tentu saja para investor mengincar Capital Gain, dimana capital gain adalah selisih antara nilai beli dan jual yang dapat memberikan banyak keuntungan. Tentu saja berinvestasi kepada instrumen saham mengalami perkembangan dari waktu ke waktu yang dimana dulu kita harus ke pasar bursa untuk membeli sebuah lot, sekarang kita bisa membeli sebuah saham hanya dengan menekan tombol di handphone kita. Untuk mempermudah menebak harga suatu saham kita bisa menggunakan teknik forecasting.

Teknik forecasting adalah teknik yang menggunakan data yang sudah ada atau data masa lalu untuk menebak data atau keadaan yang akan terjadi di masa mendatang. Dengan menggunakan data yang telah ada di masa lalu pasti akan terbentuk suatu pola dan kecendurangan data, yang kemudian dapat kita formulasikan dalam suatu rumus yang dapat memprediksi data yang akan datang.

## Business Understanding

### Problem Statements
Merujuk latar belakang yang sudah dipaparkan sebelumnya, bisa kita simpulkan bahwa permasalahan yang diangkat adalah :
- Bagaimana cara memprediksi harga saham minyak mentah di masa yang akan datang ?

### Goals
Tujuan dari pembuatan proyek ini adalah :
- Dapat memprediksi harga saham minyak mentah di masa yang akan datang menggunakan *machine Learning*
- Membantu investor/pembeli membuat keputusan yang lebih baik disaat akan membeli saham minyak mentah

### Solution Statements
Solusi yang dilakukan untuk mencapai tujuan dari proyek ini adalah sebagai berikut :

- Melakukan analisa dan pengolahan data yang bertujuan untuk dapat diproses menjadi data yang memberi pengetahuan bagi investor dan pengolahan data dilakukan agar bisa divisualisasikan agar mudah dipahami, dimengerti, ditelaah oleh investor. Berikut pengolahan yang dilakukan :
  - Menghapus nilai yang menggandung *missing value* dan kolom yang tidak akan digunakan
  - Menangani outlier yang ada pada dataset dengan metode IQR
  - Menormalisasi data
  - Membuat model yang berguna untuk melakukan prediksi
  
- Algoritma yang digunakan dalam membuat model untuk prediksi:
  - *K-Nearest Neighbors*
  - *Random Forest Regression*
  - *Gradient Boosting Regression*

- Menggunakan *Hyperparameter* dan *GridSearch* untuk membantu dalam memilih parameter terbaik yang akan digunakan pada prediksi

### Data Understanding

Dataset yang digunakan pada proyek kali ini adalah : [Crude Oil Nov 22 (CL=F)](https://finance.yahoo.com/quote/CL%3DF/history?p=CL%3DF)

Dataset ini memiliki kolom seperti dataset price stok pada umumnya yaitu 7 kolom ["Date","Open","High","Low","Close","Adj Close","Volume"]. Pada saat ini dataset yang digunakan tak menggandung *missing value*, lalu penjelasan terkait setiap kolom sebagai berikut :
- Date : Tanggal perdagangan berlangsung
- Open : Harga pembukaan pada tanggal perdangangan berlangsung
- High : Harga tertinggi pada tanggal perdangangan berlangsung
- Low : Harga terendah pada tanggal perdangangan berlangsung
- Close : Harga terakhir pada saat perdangan pada hari itu di tutup
- Adj Close : Harga penutupan pada hari tersebut setelah disesuaikan
- Volume : Volume transaksi yang terjadi pada tanggal perdagangan berlangsung

## Exploratory Data Analysis

Sebelum kita mengolah data kita alangkah baiknya kita mengekplorasi dataset kita untuk mencari korelasi, outlier, unvariate dan multivariate analisis dalam dataset kita. 

- Penanganan outlier
<br>Visualisasi data yang kita miliki
<image src="https://raw.githubusercontent.com/iqbaltio/CrudeOil_PredictiveAnalytics/master/images/output_with_outlier.png" width=600/>
<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><em>Gambar 1. sebelum metode IQR dijalankan</em></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl>
