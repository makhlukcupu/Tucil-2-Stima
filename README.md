# Tucil-2-Stima

## i. Penjelasan singkat algoritma Decrease and Conquer yang diimplementasikan
	1. Membuat dictionary "banyakPrasyarat" dengan key setiap matkul(A) dan value berupa banyaknya Prasyarat dari matkul(A) tersebut
	2. Membuat dictionary "akuPrasyaratDari" dengan key setiap matkul(A) dan value berupa array yang berisi semua mata kuliah dimata A adalah prasyaratnya (data edge dari DAG)
	3. Pada setiap semester, diambil matkul yang tersisa 0 prasyarat. (conquer)
	4. Masing-masing value dari key didalam "banyakPrasyarat" dimana key-nya ada dalam "akuPrasyaratDari" dengan value dari matkul yang sudah diambil dikurangi 1 (menghapus edge) (decrease)
	5. Menghapus isi dari "banyakPrasyarat" yang sudah diambil (decrease)
	6. Ulangi step 3, 4, 5 sampai isi dari "banyakPrasyarat" kosong (semua matkul sudah diambil)

## ii. Requirement program dan instalasi tertentu bila ada
	-

## iii. Cara menggunakan program
	1. Copy isi file dari folder test ke file test.txt (replace isinya) yang berada di folder src
	2. run file 13519170.py dalam folder src

	Untuk masing masing fungsi, run saja drivernya (hanya satu case aja wkwkwk)

## iv. Author / identitas pembuat
	Nim: 13519170
	Nama: La Ode Rajuh Emoko
	Kelas: K4
	