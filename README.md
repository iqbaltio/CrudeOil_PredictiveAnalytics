# Laporan Submission Pertama - Crude Oil Predictive Analytics
---

## Domain Proyek
Domain yang dipilih untuk proyek machine learning kali ini ada pada sektor keuangan dengan judul Crude Oil Predictive Analytics.

### Latar Belakang
Dunia saat ini mengalami krisis energi dan itu menjadi salah satu faktor harga-harga bahan pangan maupun nonpangan maka dari itu judul ini saya angkat dan menggunakan data yang terkait. Data yang saya angkat adalah dataset harga saham minyak mentah yang ada pada yahoo finance. Ada dua jenis pasar saham didunia ini, yaitu  pasar saham ekuitas yang berupa saham atau sebuah surat berharga kemudian ada pasar saham komoditas yang bisa berupa emas, tembaga nikel kemudian selain dari logam mulia tersebut komoditas juga mencakup seperti gandum, gula, kopi, dan lain-lainnya.

Investor yang memilih berinvestasi terhadap suatu saham tentu saja memiliki tujuan, salah satu tujuan para investor berinvestasi terhadap instrumen saham adalah menerima dividen yang dijanjikan oleh sebuah perusahaan tempat dimana berinvestasi yang dihasilkan dari keuntungan perusahaan tersebut. Selain dari dividen tentu saja para investor mengincar Capital Gain, dimana capital gain adalah selisih antara nilai beli dan jual yang dapat memberikan banyak keuntungan. Tentu saja berinvestasi kepada instrumen saham mengalami perkembangan dari waktu ke waktu yang dimana dulu kita harus ke pasar bursa untuk membeli sebuah lot, sekarang kita bisa membeli sebuah saham hanya dengan menekan tombol di handphone kita. Untuk mempermudah menebak harga suatu saham kita bisa menggunakan teknik forecasting.

Teknik forecasting adalah teknik yang menggunakan data yang sudah ada atau data masa lalu untuk menebak data atau keadaan yang akan terjadi di masa mendatang. Dengan menggunakan data yang telah ada di masa lalu pasti akan terbentuk suatu pola dan kecendurangan data, yang kemudian dapat kita formulasikan dalam suatu rumus yang dapat memprediksi data yang akan datang.

## Business Understanding

### Problem Statements
Merujuk latar belakang yang sudah dipaparkan sebelumnya, bisa kita simpulkan bahwa permasalahan yang diangkat adalah :
- Bagaimana cara memprediksi harga saham minyak mentah di masa yang akan datang ?
- Bagaimana cara membantu membuat keputusan yang baik?

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

Dataset ini memiliki kolom seperti dataset price stok pada umumnya yaitu 8 kolom ["Date","Open","High","Low","Close","Volume","Dividend","Stock Splits"]. Pada saat ini dataset yang digunakan tak menggandung *missing value*, lalu penjelasan terkait setiap kolom sebagai berikut :
- Date : Tanggal perdagangan berlangsung
- Open : Harga pembukaan pada tanggal perdangangan berlangsung
- High : Harga tertinggi pada tanggal perdangangan berlangsung
- Low : Harga terendah pada tanggal perdangangan berlangsung
- Close : Harga terakhir pada saat perdangan pada hari itu di tutup
- Volume : Volume transaksi yang terjadi pada tanggal perdagangan berlangsung
- Dividend : pembagian keuntungan yang diberikan perusahaan atau emiten kepada pemegang saham
- Stock Splits : pemecahan nilai nominal saham sehingga nilai nominal saham menjadi lebih rendah yang dampaknya adalah meningkatkan jumlah saham beredar suatu perusahaan

## Exploratory Data Analysis

Sebelum kita mengolah data kita alangkah baiknya kita mengekplorasi dataset kita untuk mencari korelasi, outlier, unvariate dan multivariate analisis dalam dataset kita. 

- Penanganan outlier
<br>Visualisasi data yang kita miliki

![output_with_outlier](https://user-images.githubusercontent.com/77862455/193956128-eb0ee208-d042-4460-a6cd-0d37437575b5.png)

<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><em>Gambar 1. sebelum metode IQR dijalankan</em></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl>

<br>Berikut visualisasi data yang sudah menerapkan metode IQR dengan menghapus data diluar IQR yaitu antara 25% dan 75%

![output_without_outlier](https://user-images.githubusercontent.com/77862455/193956899-b33b2ebc-17ae-42dd-a8f4-e9e9fc371d2f.png)

<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><em>Gambar 2. sesudah metode IQR dijalankan</em></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl><br>

- Unvariate Analysis
<br>Fitur yang akan diprediksi pada kasus ini terfokus kepada fitur 'Close','High','Open','Low'
![output_unvariate](https://user-images.githubusercontent.com/77862455/193957070-4ee206d4-af5a-415a-9323-cea6f6eb6e3e.png)

<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><em>Gambar 3. Univariate Analysis</em></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl><br>

- Multivariate Analysis
<br>Dapat kita simpulkan bahwa fitur 'Close' memiliki terkaitan antara fitur 'Open', 'Low', 'High'
![output_multivariate](https://user-images.githubusercontent.com/77862455/193957101-082743a4-e604-46c9-ae94-f40ff5a1324a.png)

<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><em>Gambar 4. multivariate Analysis</em></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl><br>

- Corellation Matrix
<br>Memvisualisasikan korelasi yang ada dengan menggunakan heatmap, pada data ini semua saling berkorelasi
![output_corellation_matrix](https://user-images.githubusercontent.com/77862455/193957140-12303b4d-ad1c-4208-8140-39273fe96b12.png)

<dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><dl><dd><em>Gambar 5. Corellation Matrix</em></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl></dd></dl><br>

## Data Prepareration

Sebelum kita melakukan modeling kita perlu melakukan beberapa langkah untuk mempersiapkan data, yaitu: 
### Melakuakan penanganan *Missing Value*
Pada dataset saya kali ini tidak memiliki *Missing Value* sehingga kita tidak perlu menghapus apapun

### Melakukan pembagi dataset
Kita akan membagi dataset kita menjadi train data dan test data sehingga sistem bisa menggunakan train data menjadi training model dan test data sebagai data yang memvalidasi akurat atau tidaknya. Rasio yang digunakan adalah 8:2, 8 train data dan 2 test data

### Menghapus kolom yang tak digunakan
Disini saya menghapus kolom dividens dan stock split karena saya tidak memerlukan kolom tersebut.

## Modeling
Model yang akan digunakan proyek kali ini yaitu *Gradient Boosting*, *K-Nearest Neighbors*, dan *Random Forest*.

### Gradient Boosting
*Gradient Boosting* adalah sebuah algoritma pada machine learning yang menggunakan teknik *ensembel learning* dari *decision tree* untuk meprediksi nilai. *Gradient Boosting* mampu menangani data dan pattern yang kompleks. Untuk parameter yang digunakan pada model ini ada 3 yaitu:
  - *learning_rate* : salah satu parameter training untuk menghitung nilai koreksi bobot pada waktu proses training, biasanya berada pada range 0 hingga 1, disini saya menggunakan nilai 0.01 untuk nilai *learning_rate* saya
  - *n_estimators* : Jumlah tahapan yang akan dilakukan, disini saya menggunakan nilai 1000 untuk nilai *n_estimators* saya
  - *criterion* : untuk menentukan kualitas dari pembagian data, disini saya menggunakan *friedman_mse* untuk *criterion* saya

#### Kelebihan
  - Hasil pemodelan lebih akurat
  - Stabil
#### Kekurangan
  - Waktu pemrosesan yang cukup lama
  - Tingkat kesulitan yang tinggi dalam pemilihan model

### K-Nearest Neighbors
*K-Nearest Neighbors* adalah sebuah algoritma pada *machine learning* yang bekerja dengan mengklasifikasikan data baru menggunakan kesamaan fitur untuk memprediksi nilai dari setiap data yang baru. Dengan kata lain, setiap data baru diberi nilai berdasarkan seberapa mirip titik tersebut dalam sebuah set pelatihan. Untuk parameter yang digunakan pada model ini ada 1 yaitu :
  - *n_neighbors* : Jumlah tetangga untuk yang diperlukan untuk menentukan letak data baru, disini saya menggunakan nilai 4 untuk nilai *n_neighbors* saya

#### Kelebihan
  - Mudah diimplementasikan
  - Efektif terhadap data yang besar
#### Kekurangan
  - Perlu menentukan nilai parameter K
  - Rentan terhadap variabel yang tidak informatif

### Random Forest
*Random Forest* adalah sebuah algoritma pada *machine learning* yang bekerja menggunakan teknik *ensembel learning* untuk memprediksi suatu nilai. *Random Forest* dapat bekerja secara bersamaan dalam satu waktu, sehingga tingkat keberhasilan menjadi lebih tinggi. Untuk parameter yang digunakan pada model ini ada 2 yaitu :
  - *n_estimators* : Jumlah tahapan yang akan dilakukan, disini saya menggunakan nilai 75 untuk nilai *n_estimators* saya
  - *criterion* : untuk menentukan kualitas dari pembagian data, disini saya menggunakan *absolute_error* untuk *criterion* saya

#### Kelebihan
  - Dapat mengatasi training data yang besar secara efisien
  - Dapat menangani *missing values*
#### Kekurangan
  - Kompleksitas yang tinggi
  - Waktu pemrosesan yang lama

Berdasarkan data diatas serta pada tahap modeling dan evaluasi, menurut saya ketiga algoritma bekerja cukup baik dalam memprediksi.

## Evaluation
Untuk evaluasi pada machine learning model ini, metrik yang saya gunakan adalah mean squared error (mse). Dimana metrik ini menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi.

![mean-squared-error](https://user-images.githubusercontent.com/77862455/193958219-167cf28a-52d3-49d3-b90d-35505a8beedf.png)

<br>

### Berikut adalah hasil mse dari beberapa model yang dipakai :
| Model                 	| Train    	| Test     	|
|-----------------------	|----------	|----------	|
| *Gradient Boosting* 	| 1626774.206643 	| 2385916015.821763 	|
| *K-Nearest Neighbor*       	| 902175794.013505 	| 3794621316.670325 	|
| *Random Forest*       | 166434.387352 | 2386956827.095893 |

### Berikut adalah hasil akurasi dari beberapa model yang dipakai :
| Model                 	| Accuracy(%)   	|
|-----------------------	|----------	|
| *Gradient Boosting* 	| 99.921065 	|
| *Random Forest*        	| 99.921031 	|
| *K-Nearest Neighbor*      | 99.874460 |

### Kesimpulan

Kesimpulan dari proyek ini adalah :
- Model terbaik yang digunakan adalah *Gradient Boosting* dibandingkan *Random Forest*  dengan akurasi 99.921065%
- Hasil Prediksi akan lebih akurat jika data lebih banyak

### Daftar Pustaka

- G. Sismanoglu, M. A. Onde, F. Kocer and O. K. Sahingoz, "Deep Learning Based Forecasting in Stock Market with Big Data Analytics," 2019 Scientific Meeting on Electrical-Electronics & Biomedical Engineering and Computer Science (EBBT), 2019, pp. 1-4, doi: 10.1109/EBBT.2019.8741818.

- Matthias Feurer and Frank Hutter. Hyperparameter optimization. In: AutoML: Methods, Systems, Challenges, pages 3–38.

- “Saham - PT bursa efek Indonesia.” [Online]. Available: https://www.idx.co.id/produk/saham/.

- "Dividen Saham: Arti, Contoh, dan Cara Menghitungnya."[Online]. Available: https://www.cermati.com/artikel/dividen-saham-arti-contoh-dan-cara-menghitungnya.

- "stock split."[Online]. Available: https://www.bareksa.com/kamus/s/stock-split.

- M. M. Kumbure, C. Lohrmann, P. Luukka, and J. Porras, “Machine learning techniques and data for stock market forecasting: A literature review,” Expert Systems with Applications, vol. 197, p. 116659, 2022. 
