# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik:Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit) 
Nama: Khusnatun Lina Fitri  
NIM: 230202762  
Kelas: 5IKRB
---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.  
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).  
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.  
---

## 2. Dasar Teori
a. Langkah 1-Aritmetika Modular
```
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))
```
Hasilnya
```
7 + 5 mod 12 = 0
7 * 5 mod 12 = 11
7^128 mod 13 = 3
```
b. Langkah 2-GCD dan Algoritma Euclidean
```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))
```
Hasilnya
```
gcd(54, 24) = 6
```
Langkah 3 — Extended Euclidean Algorithm
```
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4
```
Hasilnya
```
Invers 3 mod 11 = 4
```
Langkah 4 — Logaritma Diskrit (Discrete Log)
```
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
```
Hasilnya
```
3^x ≡ 4 (mod 7), x = 4
```
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Chrome
---

## 4. Langkah Percobaan
1. Membuat file dengan nama aritmatika_modular.py di folder `praktikum/week3-modmath/src/`.
2. Membuat file dengan nama gcd-dan-algoritma-euclidean.py di folder `praktikum/week3-modmath/src/`.
3. Membuat file dengan nama extended-euclidean-algorithm.py di folder `praktikum/week3-modmath/src/`.
4. Membuat file dengan nama logaritma-diskrit.py di folder `praktikum/week3-modmath/src/`.
5. Menyalin kode program dari panduan praktikum.
6. Menjalankan program dengan perintah sesuai nama file.
---

## 5. Source Code
a. Langkah 1-Aritmetika Modular
```
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))
```
b. Langkah 2-GCD dan Algoritma Euclidean
```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))
```
Langkah 3 — Extended Euclidean Algorithm
```
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4
```
Langkah 4 — Logaritma Diskrit (Discrete Log)
```
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
```
---

## 6. Hasil dan Pembahasan
Hasil eksekusi Langkah 1-Aritmetika Modular

![Hasil Eksekusi](screenshots/hasil%20langkah1.png)

Hasil eksekusi Langkah 2-GCD dan Algoritma Euclidean

![Hasil Eksekusi](screenshots/hasil%20langkah%202.png)

Hasil eksekusi Langkah 3 — Extended Euclidean Algorithm

![Hasil Eksekusi](screenshots/hasil%20langkah%203.png)

Hasil eksekusi Langkah 4 — Logaritma Diskrit (Discrete Log)

![Hasil Eksekusi](screenshots/hasil%20langkah%204.png)

Pembahasan : 
Semua percobaan berhasil tanpa eror, dan hasil keluaran sesuia dengan teori dasar kriptografi.

---


---

## 7. Jawaban Pertanyaan
Jawab pertanyaan diskusi yang diberikan pada modul.  

### Pertanyaan 1 : Apa peran aritmetika modular dalam kriptografi modern?
Aritmetika modular memiliki peran yang sangat penting dalam kriptografi modern karena menjadi dasar utama berbagai sistem keamanan digital seperti RSA dan Diffie-Hellman. Fungsinya adalah menjaga setiap hasil operasi matematika tetap berada dalam batas tertentu (antara 0 sampai n-1), sehingga pproses enkripsi dan dekripsi dapat dilakukan secara efisien. 
Selain itu,operasi seperti perpangkatan modular juga mudah dikerjakan, tetappi sulit untuk dibalik, yang menjadikan kunci utama dalam keamanan data.
### Pertanyaan 2 : Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
### Pertanyaan 3 : Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?


---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka

---

## 10. Commit Log
```
commit week3-moodmath-gcd
Author: Khusnatun Lina Fitri <husnatunlinafitri@gmail.com>
Date:   2025-01-16

    week3-moodmath-gcd: implementasi Modular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)  dan laporan.
```
