
# WZML

Panduan untuk membuat dan men-deploy aplikasi WZML di Heroku.

## Create and Deploy

1. Buat aplikasi Heroku baru di wilayah US:
```shell
heroku create --region us APP_NAME
```

2. Tambahkan remote Heroku ke repositori Git lokal:
```shell
heroku git:remote -a APP_NAME
```

3. Atur stack Heroku ke container:
```shell
heroku stack:set container
```

4. Tambahkan semua file ke Git:
```shell
git add . -f
```

5. Commit perubahan:
```shell
git commit -m "HK Setup"
```

6. Push ke Heroku:
```shell
git push heroku main --force
```

7. Lihat log aplikasi:
```shell
heroku logs -t
```

## Delete and Restart

### Delete
Untuk menghapus aplikasi:
```shell
heroku apps:destroy NAME_APPS
```

### Restart
Untuk me-restart aplikasi:
```shell
heroku restart
```

## Konfigurasi Opsional

Anda dapat mengunggah konfigurasi Anda sebagai secret di https://gist.github.com/

Untuk mengatur variabel Heroku:
```shell
heroku config:set CONFIG_FILE_URL=url_gist.github_disini
```

## Catatan

- Ganti `APP_NAME` dengan nama aplikasi Heroku Anda.
- Ganti `NAME_APPS` dengan nama aplikasi yang ingin Anda hapus.
- Pastikan untuk mengganti `url_gist.github_disini` dengan URL Gist GitHub Anda yang sebenarnya.


