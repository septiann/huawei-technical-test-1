# Huawei Technical Test - 1

Aplikasi ini digunakan untuk mendapatkan informasi cuaca terkini berdasarkan nama kota dari Open Weather Map.

## Requirements

- Python: 3.11.5
- Django 5.0.7
- Requests Library

## Installation

- Clone Repo
```
git clone https://github.com/septiann/huawei-technical-test-1.git
cd huawei-technical-test-1
```

- Install dependency
```
pip install django requests
```

- Configuration
```
Gunakan API key dari Open Weather Map dan tambahkan ke weather_app/views.py di variabel api_key.
```

- Running Server
```
python manage.py runserver
```

## Functions
```
weather/views.py
```
Terdapat function view untuk halaman utama Aplikasi ini.

Fungsi ini akan menangani method POST dari form input yang terdapat di halaman utama. Form input akan mengirimkan data berupa string ke dalam function dan melakukan request ke API Open Weather Map untuk mendapatkan data cuaca, dan merender HTML ketika informasi kota dan cuaca berhasil didapatkan.

```
Parameters:
- request (HTTPRequest):
Objek HTTPRequest yang berisi request dari form yang didapat dari halaman utama

Returns:
- HTTPResponse:
Halaman HTML yang dirender.
```
