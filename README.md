# TugasKripto_Mareta-Surya-Tananjaya_24051204006_RSA
Implementasi Algoritma RSA dari Scratch (Python)

## Deskripsi Proyek
    Repository ini berisi implementasi algoritma kriptografi asimetris RSA (Rivest, Shamir, Adleman) yang dibuat dari awal (from scratch) tanpa menggunakan library enkripsi instan seperti : `import rsa` dan `from cryptography import ...`

Seluruh proses matematis seperti :
- Greatest Common Divisor (GCD)
- Extended Euclidean Algorithm
- Modular Inverse
- Modular Exponentiation
diimplementasikan secara manual untuk menunjukkan pemahaman konsep kriptografi secara mendalam.

Proyek ini dibuat untuk memenuhi tugas mata kuliah Keamanan Data dan Informasi.

## Pengantar Teori RSA
    RSA dikembangkan pada tahun 1977 oleh : Ron Rivest, Adi Shamir, dan Leonard Adleman . RSA merupakan algoritma kriptografi asimetris, yang berarti menggunakan dua kunci berbeda : Public Key digunakan untuk enkripsi dan Private Key digunakan untuk dekripsi.

## Konsep Matematis yang Digunakan
Implementasi ini menggunakan beberapa konsep matematika penting :
1. Faktorisasi bilangan prima
2. Aritmetika modular
3. Fungsi Totient Euler :
   φ(n) = (p − 1)(q − 1)
4. Extended Euclidean Algorithm  
   Digunakan untuk mencari invers modular.

5. Modular Exponentiation (Square and Multiply)  
   Digunakan untuk menghitung perpangkatan besar secara efisien.

## Struktur Program dan Penjelasan Step-by-Step
Program dibagi menjadi 5 bagian utama:

1.Fungsi Matematika Dasar
    `gcd(a, b)`  
    Menghitung Greatest Common Divisor (FPB) menggunakan algoritma Euclid.
    Digunakan untuk memastikan bahwa :
    gcd(e, φ(n)) = 1		Artinya e relatif prima terhadap φ(n).
    
    `extended_euclidean(a, b)`Digunakan untuk menyelesaikan persamaan :
    ax + by = gcd(a, b)	Fungsi ini digunakan untuk mencari invers modular.	
    `mod_inverse(e, phi)`
    Mencari nilai `d` sehingga :
    d × e ≡ 1 (mod φ(n))	Jika gcd(e, φ(n)) ≠ 1 maka invers modular tidak ada.
    
    `modular_exponentiation(base, exponent, modulus)`
    Menghitung : (base^exponent) mod modulus
    Menggunakan metode Square and Multiply agar efisien dan tidak menghasilkan angka sangat besar.
    Ini adalah komponen penting dalam enkripsi dan dekripsi RSA.

2.Key Generation (Pembangkitan Kunci)
  Langkah-langkah dalam program :
  1) Pilih dua bilangan prima (Bilangan kecil digunakan hanya untuk demonstrasi.)
     p = 61
     q = 53
  2) Hitung Modulus 
     n = p × q 	Nilai n akan menjadi bagian dari public dan private key.
  3) Hitung Totient Euler
     φ(n) = (p − 1)(q − 1)
  4) Pilih nilai e
     Syarat :
     1 < e < φ(n)
     gcd(e, φ(n)) = 1
  
     Dalam program e=17
  5) Hitung nilai d
     Menggunakan invers modular :
     d × e ≡ 1 (mod φ(n))
      
     Hasil :
     Public Key = (e, n)
     Private Key = (d, n)

3.Proses Enkripsi
  Rumus enkripsi 
  C = M^e mod n
  
  Langkah-langkah dalam program :
  1)	Ubah setiap karakter plaintext menjadi ASCII :
  m = ord(char)
  2)	Hitung ciphertext :
  c = modular_exponentiation(m, e, n)
  3)	Simpan dalam list ciphertext.
  Contoh:
  '9' → 57 → 1175

4.Proses Deskripsi
  Rumus dekripsi:
  M = C^d mod n
  Langkah-langkah dalam program :
  1)	Ambil setiap nilai ciphertext
  2)	Hitunng :
  m = modular_exponentiation(c, d, n)
  3)	Ubah kembali ke karakter :
  chr(m)
  Hasil plaintext akan kembali seperti semula.

5.Cara Menjalankan Program
  1) Pastikan Python Terinstal
  2) Jalankan Program
  3) Masukkan Pesan 
  4) Ketika program berhasil dijalankan maka akan menampilkan :
    - Tahap Key Generation
    - Proses Enkripsi per karakter
    - Ciphertext
    - Proses Dekripsi
    - Hasil akhir plaintext kembali

6.Analisis Keamanan
  Kelebihan ;
  - Menggunakan sistem public key
  - Aman untuk distribusi kunci
  - Digunakan luas dalam HTTPS dan SSL/TLS
  - Aman jika menggunakan kunci ≥ 2048 bit
  
  Kelemahan :
  - Lebih lambat dibanding kriptografi simetris
  - Tidak efisien untuk data berukuran besar
  - Rentan terhadap komputer kuantum di masa depan
  - Tidak aman jika menggunakan bilangan kecil
