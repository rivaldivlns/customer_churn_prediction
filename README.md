# Milestone 2 - Rivaldi Valensia

**Batch**: HCK-007

## Daftar Isi:

1. [# **i. Perkenalan**](##-i-perkenalan) 2. [### Conceptual Problems:](####-conceptual-problems:) 3. [# **ii. Import Libraries**](##-ii-import-libraries) 4. [# **iii. Data Loading**](##-iii-data-loading) 5. [# **iv. Exploratory Data Analysis (EDA)**](##-iv-exploratory-data-analysis-(eda)) 6. [## A. Problem Overview](###-a-problem-overview) 7. [## B. Data Understanding](###-b-data-understanding) 8. [## C. Data Cleaning](###-c-data-cleaning) 9. [### 1. Drop columns](####-1-drop-columns) 10. [### 2. Dataframe after data cleaning](####-2-dataframe-after-data-cleaning) 11. [## D. Data Visualization](###-d-data-visualization) 12. [### PLOT 1](####-plot-1) 13. [#### Distribution Churn](#####-distribution-churn) 14. [### PLOT 2](####-plot-2) 15. [#### Distribution Churn by Country](#####-distribution-churn-by-country) 16. [### PLOT 3](####-plot-3) 17. [#### Distribution Churn by Gender in France](#####-distribution-churn-by-gender-in-france) 18. [### PLOT 4](####-plot-4) 19. [#### Distribution Churn by Age in France](#####-distribution-churn-by-age-in-france) 20. [### PLOT 5](####-plot-5) 21. [#### Distribution Churn by Product Number in France](#####-distribution-churn-by-product-number-in-france) 22. [### PLOT 6](####-plot-6) 23. [#### Distribution Churn by Active Member in France](#####-distribution-churn-by-active-member-in-france) 24. [### PLOT 7](####-plot-7) 25. [#### Distribution Churn by Mean Balance in France](#####-distribution-churn-by-mean-balance-in-france) 26. [### PLOT 8](####-plot-8) 27. [#### Distribution Churn by Credit Card in France](#####-distribution-churn-by-credit-card-in-france) 28. [# **v. Feature Engineering**](##-v-feature-engineering) 29. [## A. Divide data into categories values and numeric values](###-a-divide-data-into-categories-values-and-numeric-values) 30. [## B. VIF](###-b-vif) 31. [## C. Cardinality](###-c-cardinality) 32. [## D. Heatmap Correlation](###-d-heatmap-correlation) 33. [## E. Feature Selection Using Phik Matrix](###-e-feature-selection-using-phik-matrix) 34. [## F. Split Data](###-f-split-data) 35. [### 1. X_train_num & X_test_num](####-1-x_train_num-&-x_test_num) 36. [### 2. X_train_cat & X_test_cat](####-2-x_train_cat-&-x_test_cat) 37. [## G. Skewness](###-g-skewness) 38. [#### i. Check Skewness](#####-i-check-skewness) 39. [#### ii. Plot Distribution of X_train_num](#####-ii-plot-distribution-of-x_train_num) 40. [#### iii. Count amount of outlier](#####-iii-count-amount-of-outlier) 41. [#### iv. Count percentage of outlier](#####-iv-count-percentage-of-outlier) 42. [## H. Preprocessing Using Pipeline](###-h-preprocessing-using-pipeline) 43. [## I. Imbalance Handling](###-i-imbalance-handling) 44. [# **vi. Model Definition**](##-vi-model-definition) 45. [## 1. Initialization Default Model](###-1-initialization-default-model) 46. [### A. K-Nearest Neighbours](####-a-k-nearest-neighbours) 47. [### B. SVM](####-b-svm) 48. [### C. Random Forest Classifier](####-c-random-forest-classifier) 49. [### D. Decision Tree](####-d-decision-tree) 50. [### E. ADABoosting](####-e-adaboosting) 51. [## 2. Classification Report](###-2-classification-report) 52. [##### **Saya memakai kelas positif(1) sebagai kelas churn dan kelas negatif(0) adalah kelas loyal. Dan saya memilih Recall untuk nilai evaluasi karena ingin mengurangi False Negative(FN). Pada kasus ini, False Negative berarti diprediksi loyal, aktual churn**](######-saya-memakai-kelas-positif(1)-sebagai-kelas-churn-dan-kelas-negatif(0)-adalah-kelas-loyal-dan-saya-memilih-recall-untuk-nilai-evaluasi-karena-ingin-mengurangi-false-negative(fn)-pada-kasus-ini,-false-negative-berarti-diprediksi-loyal,-aktual-churn) 53. [### D. Decision Tree Classifier](####-d-decision-tree-classifier) 54. [### E. ADABoost Classifier](####-e-adaboost-classifier) 55. [## 3. Cross Validation](###-3-cross-validation) 56. [# **vii. Model Training**](##-vii-model-training) 57. [### Hyperparameter Tuning](####-hyperparameter-tuning) 58. [# **viii. Model Evaluation**](##-viii-model-evaluation) 59. [# **ix. Final Pipeline**](##-ix-final-pipeline) 60. [# **x. Model Saving**](##-x-model-saving)

### # **i. Perkenalan**

Milestone 2

Nama : Rivaldi Valensia

Batch : HCK-007

Link Huggingface : https://huggingface.co/spaces/Rivaldi/bank_customer_churn_prediction

### ### Conceptual Problems:


1. Latar belakang bagging : Bagging digunakan untuk meningkatkan kekuatan model dengan memanfaatkan variasi kesalahan yang mungkin terjadi pada dataset yang sama.

Cara kerja :

- A. Buat banyak sampel acak dari dataset latihan dengan penggantian (bootstraping).

- B. Latih model pada setiap sampel acak ini secara terpisah.

- C. Gabungkan hasil prediksi dari semua model, misalnya, dengan mayoritas voting untuk klasifikasi.

2. Perbedaan cara kerja algoritma Random Forest dengan algoritma boosting yang Anda pilih !
- Komposisi Model:

Random Forest: Menggunakan banyak pohon keputusan yang berdiri sendiri dan menggabungkan hasil prediksi.

Adaboosting: Menggabungkan beberapa model lemah dengan memberi bobot lebih pada data yang salah diklasifikasikan.

- Pemberian Bobot pada Data:

Random Forest: Data memiliki bobot yang sama.

Adaboosting: Memberikan bobot lebih pada data yang sulit diklasifikasikan.


- Proses Pembelajaran:

Random Forest: Pembelajaran independen untuk setiap pohon.

Adaboosting: Pembelajaran iteratif, fokus pada kesalahan sebelumnya.


- Prediksi Akhir:

Random Forest: Hasil prediksi dari semua pohon digabungkan.

Adaboosting: Menggabungkan hasil prediksi dari model lemah dengan bobot.


3. Cross Validation adalah cara untuk menguji seberapa baik model mesin pembelajaran dengan menggunakan sebagian data pelatihan dan sebagian data pengujian secara bergantian. Ini membantu memastikan bahwa model tidak hanya baik pada data pelatihan, tetapi juga pada data yang belum pernah dilihat sebelumnya.





### # **ii. Import Libraries**

Bagian ini untuk mengimport library yang akan digunakan

### # **iii. Data Loading**

Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut.

### # **iv. Exploratory Data Analysis (EDA)**

Dataset yang telah diubah menjadi csv lalu di import menggunakan library pandas dan dijadikan suatu dataframe berbentuk tabel

### ## A. Problem Overview

Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

### ## B. Data Understanding

Problem Definition :
Customer churn adalah hilangnya pelanggan yang berpindah dari satu sektor ke pesaing lain dalam waktu tertentu. Industri perbankan yang termasuk kedalam sektor financial tentu menghadapi tantangan mengenai permasalahan churn ini. Customer churn ini tentu saja meresahkan apabila tidak ditangani karena akan beresiko dalam penurunan revenue perusahaan. Data customer bank yang berjumlah besar dapat dimanfaatkan untuk membangun model prediksi customer churn dengan menggunakan machine learning. Model prediksi yang dibangun dapat digunakan untuk strategi pelanggan guna meningkatkan customer retention.

Objectives :
- Mengurangi tingkat customer churn
- Membuat model prediksi
- Menganalisis ciri-ciri kemungkinan customer yang akan churn
- Mengukur kinerja model

### ## C. Data Cleaning

Langkah ini dilakukan guna memahami data dan pengecekan pola yang ada pada dataframe seperti pengecekan nama dan jumlah kolom, pengecekan missing value, pengecekan data duplikat dan lain-lain

### ### 1. Drop columns

Menampilkan 10 data teratas sesuai index dari dataframe

### ### 2. Dataframe after data cleaning

Menampilkan 10 data terakhir sesuai index dari dataframe

### ## D. Data Visualization

Menampilkan informasi dasar mengenai dataframe seperti nama kolom, tipe data dan lain-lain

### ### PLOT 1

Menampilkan ukuran tabel yang mempunyai 10000 baris dan 12 kolom

### #### Distribution Churn

Menampilkan nama kolom secara keseluruhan

### ### PLOT 2

**Keterangan nama kolom pada dataframe |**

| Nama Kolom                  | Keterangan                                                                   |
| --------------------------- | ---------------------------------------------------------------------------- |
| customer_id | Nomor identifikasi unik untuk setiap pelanggan |
| credit_score | Skor kredit pelanggan, yang mengindikasikan seberapa baik pelanggan memiliki catatan kredit |
| country | Negara tempat pelanggan tinggal atau terdaftar|
| gender | Jenis kelamin pelanggan (misalnya, pria atau wanita)|
| age | Usia nasabah |
| tenure | Jumlah tahun pelanggan telah menjadi nasabah bank|
| balance | Saldo akun pelanggan di bank|
| products_number | Jumlah produk atau layanan yang dimiliki oleh pelanggan di bank|
| credit_card | Indikator apakah pelanggan memiliki kartu kredit (ya/tidak)|
| active_member | Indikator apakah pelanggan adalah anggota aktif bank (ya/tidak)|
| estimated_salary | Estimasi gaji tahunan pelanggan|
| churn | Variabel target yang menunjukkan apakah pelanggan telah melakukan churn (pindah dari bank) atau tidak (0 untuk tidak churn, 1 untuk churn)|

### #### Distribution Churn by Country

Membagi dataframe berdasarkan tipe data pada kolomnya nya yaitu numerical dan categorical

### ### PLOT 3

Menampilkan jumlah kolom dan nama kolom secara keseluruhan yang bertipe data numerical

### #### Distribution Churn by Gender in France

Menampilkan jumlah kolom dan nama kolom secara keseluruhan yang bertipe data categorical.

### ### PLOT 4

Mengecek jumlah data yang terduplikasi pada dataframe. Tidak ada data duplikat

### #### Distribution Churn by Age in France

Tidak ada missing value

### ### PLOT 5

Mengecek ringkasan statistik seperti nilai rata-rata, nilai minimum dan maksimum pada data yang bertipe numerical

### #### Distribution Churn by Product Number in France

Menampilkan jumlah unik value yang ada di setiap kolom.

Kolom products_number, credit_card, active_member dan churn walaupun bertipe data numerical tetapi mempunyai sedikit unique values, maka kolom-kolom tersebut dianggap bertipe categorical karena tidak continues values.

### ### PLOT 6

Pada langkah ini akan dilakukan pembersihan data, guna menyiapkan data agar dapat digunakan untuk membuat model klasifikasi. Langkah yang akan dilakukan pada data cleaning seperti penghapusan kolom yang tidak terpakai.


### #### Distribution Churn by Active Member in France

Saya menghilangkan kolom customer_id karena tidak ada hubungannya dengan customer churn setelah itu membuat variabel baru untuk menyimpan hasil setelah menghapus kolom tersebut

### ### PLOT 7

Setelah data clean dilakukan, saya membuat dataframe baru untuk menyimpan hasil dari proses cleaning data tersebut

### #### Distribution Churn by Mean Balance in France

Terlihat bahwa customer retention lebih tinggi daripada customer churn. Namun tidak menutup kemungkinan bahwa kedepannya customer churn akan melebihi customer retention. Maka dari itu, kita akan melakukan visualisasi untuk menemukan pola apa yang berhubungan dari kolom-kolom yang ada dan mungkin saja menjadi alasan seorang customer untuk churn

### ### PLOT 8

Negara yang memiliki persentase tertinggi untuk customer churn adalah France dengan nilai 50%. Maka dari itu, saya ingin melakukan analisis berdasarkan visualisasi data yang berfokus pada negara France

### #### Distribution Churn by Credit Card in France

Di negara France, untuk tingkat customer churn tertinggi ada pada gender Female. Dan tingkat customer loyal tertinggi ada pada gender Male.

### # **v. Feature Engineering**

Pada umur 40 tahun keatas, tingkat churn pada customer meningkat

### ## A. Divide data into categories values and numeric values

Produk nomor 4 adalah produk yang sepi peminat. Produk 2 adalah produk yang berpotensi meningkatkan retention customer atau keloyalan customer sedangkan produk nomor 1 adalah produk yang berpotensi terhadap tingkat churn pada customer.

### ## B. VIF

Tingkat churn disebabkan juga oleh customer yang pasif untuk menggunakan layanan, karena customer tersebut pasif maka memperbesar peluang untuk churn atau keluar dari status nasabah nya.

### ## C. Cardinality

Rata-rata saldo pada customer churn lebih tinggi dibandingkan customer yang loyal. Maka dari itu, kita sebagai pihak bank wajib untuk mengurangi tingkat churn customer, karena apabila tingkat churn semakin tinggi maka semakin besar atau timpang rata-rata saldo customer churn dibandingkan customer loyal dan hal itu dapat menyebabkan bank merugi.

### ## D. Heatmap Correlation

Customer yang mempunyai kartu kredit mayoritas adalah customer loyal dan customer yang churn juga. Hanya ada sedikit customer yang tidak mempunyai kartu kredit, karena mayoritas customer sudah mempunyai kartu kredit

### ## E. Feature Selection Using Phik Matrix

Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

### ## F. Split Data

Langkah memisahkan data kategori dan data numerik agar dapat mengidentifikasi pola, tren, dan hubungan dalam data dengan lebih baik, yang selanjutnya akan membantu Anda membuat keputusan yang lebih baik dan membangun model yang lebih akurat. Memang, data dalam kolom bertipe integer, namun ada beberapa kolom yang memiliki unique values sedikit dan bisa dikatakan sebagai categories values

### ### 1. X_train_num & X_test_num

Menampilkan dataframe yang berisi kolom-kolom bertipe categorical

### ### 2. X_train_cat & X_test_cat

Menampilkan dataframe yang berisi kolom-kolom bertipe numerical

### ## G. Skewness

Langkah VIF (Variance Inflation Factor) digunakan untuk mengevaluasi tingkat multicollinearity (multikolinearitas) antara variabel-variabel independen dalam sebuah model

### #### i. Check Skewness

Terlihat nilai VIF pada 4 kolom tersebut rendah, berarti tidak ada multicollinearity pada kolom tersebut

### #### ii. Plot Distribution of X_train_num

Langkah ini dilakukan untuk mengukur jumlah nilai unik pada masing-masing kolom yang bertipe categorical

### #### iii. Count amount of outlier

Unique values pada beberapa kolom tersebut masih sedikit maka tidak perlu handling cardinality

### #### iv. Count percentage of outlier

Langkah ini dilakukan guna mencari hubungan korelasi antar kolom

### ## H. Preprocessing Using Pipeline

Hanya ada 3 kolom yang melewati threshold >0.1 atau <= -.01 yaitu kolom active_member, balance dan age. Sebenarnya kita bisa langsung menyeleksi kolom apa saja yang mempunyai korelasi kuat dengan churn, tetapi kita akan melakukan pengecekan lebih lanjut setelah ini untuk memastikan kolom apa saja yang benar-benar berkorelasi dengan churn.

### ## I. Imbalance Handling

Langkah ini merupakan proses seleksi kolom dan mengambil kolom yang memiliki korelasi diatas threshold yang ditentukan saja menggunakan phik_matrix

### # **vi. Model Definition**

Saya menggunakan seleksi fitur menggunakan korelasi phik_matrix karena phik_matrix memberikan alternatif perhitungan korelasi jika pada dataset terdapat kolom numerikal dan kategorikal

### ## 1. Initialization Default Model

Saya membuat threshold korelasi >0 untuk menyeleksi feature apa saja yang dibutuhkan dalam pembuatan model, setelah itu saya membuat dataframe untuk menyimpan hasil penyeleksian feature

### ### A. K-Nearest Neighbours

Pada langkah ini ditujukan untuk menghitung berapa nilai skewness, berapa jumlah dan persentase outlier, serta membuat plot untuk menggambarkan distribusi data pada X_train_numeric

### ### B. SVM

Kemiringan distribusi data dari variabel X_train_num dibawah 1, namun saya rasa masih perlu di handling agar distribusi data X_train_num semakin normal.

### ### C. Random Forest Classifier

Saya membuat plot visualisasi kolom X_train_num yang akan di handling skewness nya agar lebih jelas terlihat bagaimana kemiringan/distribusi data nya

### ### D. Decision Tree

Terdapat 8000 baris dan 8 kolom untuk X_train

### ### E. ADABoosting

Terdapat 2000 baris dan 8 kolom untuk X_test

### ## 2. Classification Report

Terdapat 8000 baris dan 1 kolom untuk y_train

### ##### **Saya memakai kelas positif(1) sebagai kelas churn dan kelas negatif(0) adalah kelas loyal. Dan saya memilih Recall untuk nilai evaluasi karena ingin mengurangi False Negative(FN). Pada kasus ini, False Negative berarti diprediksi loyal, aktual churn**

Terdapat 2000 baris dan 1 kolom untuk y_test

### ### D. Decision Tree Classifier

Saya ingin melihat ada berapa jumlah outlier pada masing-masing kolom dengan threshold 3 karena saya akan menggunakan Z-score/gaussian karena skewness <1. Terlihat ada 104 outlier pada kolom age, 8 outlier pada kolom credit_score dan kolom balance serta tenure bersih dari outlier

### ### E. ADABoost Classifier

Saya ingin melihat berapa persentase outlier dalam setiap kolom untuk menentukan cara handling outlier, apakah di capping atau di trimming. Jika persentase outlier kurang dari 5%, maka saya akan menggunakan metode trimming

### ## 3. Cross Validation

Menampilkan dataframe X_test_cat yang berjumlah 8000 baris dan 4 kolom

### # **vii. Model Training**

Berdasarkan hasil perhitungan, persentase outlier kolom age dan credit_score kurang dari 5%. Karena data latih saya hanya ada 8000 rows dan saya khawatir model saya akan jelek karena kekurangan data, maka saya menggunakan metode capping untuk handling outlier

### ### Hyperparameter Tuning

Proses ini dilakukan untuk otomatisasi langkah-langkah pemrosesan data sebelum melatih model. Penggunaan pipeline memudahkan manajemen dan mencegah kebocoran informasi saat evaluasi model.

### # **viii. Model Evaluation**

Saya membagi tipe data kategorikal menjadi beberapa jenis, yaitu ordinal_features dan categorical_features. Untuk ordinal_features dikhususkan untuk kolom products_number, country dan gender yang berisi beberapa unique values dan dihandling dengan OrdinalEncoder, sedangkan binary_features untuk kolom yang berisi 2 unique values saja yaitu active_member dan dihandling menggunakan OneHotEncoder. Saya juga membuat numeric_features yang berisi handling skewness dengan winsorizer dan method gaussian, serta scaling menggunakan standardscaler

### # **ix. Final Pipeline**

Pada langkah ini menggabungkan seluruh transformer dengan column transformer agar menjadi satu pipeline dengan nama variabel preprocessor

### # **x. Model Saving**

Pada langkah ini dilakukan pengaplikasian pipeline preprocessor pada data X_train
