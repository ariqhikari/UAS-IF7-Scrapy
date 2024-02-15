# Tugas UAS IF-7 Scrapy

## Anggota Kelompok

| NIM      | Nama                    |
| -------- | ----------------------- |
| 10122238 | TITAN EL HAQI           |
| 10122241 | MARSYA AWLIYA SABRINA   |
| 10122254 | ARIQ HIKARI HIDAYAT     |
| 10122257 | M.GHAZY AL H.H          |
| 10122260 | ADISYA AINUN FATIHAH    |
| 10122264 | MUHAMMAD NAUFAL GHIFARI |

## Panduan clone repository untuk Collaborator

1. Clone repository ini

```bash
git clone https://github.com/ariqhikari/UAS-IF7-Scrapy.git
```

2. Masuk ke folder UAS-IF7-Scrapy

```bash
cd UAS-IF7-Scrapy
```

# Panduan push code ke github

1. Pindah ke branch yang sudah disediakan sesuai dengan nama kalian, dengan list branch sebagai berikut:<br>
   > main, titan, marsya, ariq, ghazy, adisya, naufal

```bash
# sesuaikan dengan nama kalian, disini contoh akan masuk ke branch ariq
git checkout ariq
```

2. Lakukan pull code terlebih dahulu saat ingin memulai sesuatu

```bash
git pull origin main
```

3. Silahkan melakukan perubahan code apapun
4. Jika sudah menyelesaikan perubahan code dan akan melakukan push ke repository github, maka lakukan

```bash
git add .
```

5. Lakukan commit untuk memberi tahu pesan perubahannya

```bash
git commit -m "tulis pesan disini"
```

6. Lakukan perintah push ke repository github

```bash
# sesuaikan dengan nama kalian, disini contoh akan push code ke branch ariq
git push origin ariq
```

## Cara menjalankan program secara local

1. Install _dependencies_

```bash
pip install -r requirements.txt
```

2. Jalankan program Streamlit

```bash
streamlit run main.py
```
