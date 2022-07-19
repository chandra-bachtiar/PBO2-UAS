# Kelompok 7 - Aplikasi Pendataan Lowongan Kerja 

Aplikasi dibuat untuk memenuhi tugas Ujian Akhir Semester Pemrograman Berbasis Objek 2. 

## Persiapan

* Download dan Install [Visual Studio Code](https://code.visualstudio.com/) atau code editor lainnya
* Download dan Install [Python](https://www.python.org)
* Download dan Install [PosgreSQL](https://www.postgresql.org)
* Download dan Install [QtDesigner](https://build-system.fman.io/qt-designer-download)

Setelah selesai semua dilanjutkan dengan menginstall package pyqt5 dan psycopg2 dengan [pip](https://pip.pypa.io/en/stable/).

```bash
pip install pyqt5
```
dan
```bash
pip install psycopg2
```

## Konfigurasi Database

Pembuatan Database
```sql
CREATE DATABASE loker;
```
Pembuatan Table users
```sql
CREATE TABLE IF NOT EXISTS public.users
(
    iduser bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 999999 CACHE 1 ),
    username character varying(100) COLLATE pg_catalog."default" NOT NULL,
    password character varying(100) COLLATE pg_catalog."default" NOT NULL,
    nama character varying(200) COLLATE pg_catalog."default" NOT NULL,
    email character varying(200) COLLATE pg_catalog."default" NOT NULL,
    role character varying(20) COLLATE pg_catalog."default" NOT NULL,
    tgl_didirikan date,
    tgl_lahir date,
    alamat character varying(500) COLLATE pg_catalog."default",
    pendidikan character varying(100) COLLATE pg_catalog."default",
    nama_sekolah character varying(200) COLLATE pg_catalog."default",
    jenis_perusahaan character varying(100) COLLATE pg_catalog."default",
    tempat_lahir character varying(200) COLLATE pg_catalog."default",
    CONSTRAINT user_pkey PRIMARY KEY (iduser),
    CONSTRAINT "user" UNIQUE (username)
)
```
Pembuatan Table master_loker
```sql
CREATE TABLE IF NOT EXISTS public.master_loker
(
    "idLoker" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 99999 CACHE 1 ),
    "idPerusahaan" bigint NOT NULL,
    "Posisi" character varying(200) COLLATE pg_catalog."default" NOT NULL,
    "Gaji" numeric NOT NULL,
    "Pendidikan" character varying(200) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT master_loker_pkey PRIMARY KEY ("idLoker"),
    CONSTRAINT iduser FOREIGN KEY ("idPerusahaan")
        REFERENCES public.users (iduser) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)
```
pembuatan table detail_loker
```sql
CREATE TABLE IF NOT EXISTS public.detail_loker
(
    "idLoker" bigint NOT NULL,
    "idPelamar" bigint NOT NULL,
    status character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "idDetail" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 99999 CACHE 1 ),
    CONSTRAINT detail_loker_pkey PRIMARY KEY ("idDetail"),
    CONSTRAINT idloker FOREIGN KEY ("idLoker")
        REFERENCES public.master_loker ("idLoker") MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT iduser FOREIGN KEY ("idPelamar")
        REFERENCES public.users (iduser) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)
```

## Penggunaan
### Setelah semua selesai anda bisa menjalankan file main.py 

ERD dan Alur Aplikasi bisa di lihat di PDF Berikut :
[Detail Aplikasi.pdf](https://github.com/chandra-bachtiar/PBO2-UAS/files/9143850/Detail.Aplikasi.pdf)



# Kelompok
## Chandra Bachtiar
## Marisa Naofa
## Lani
## Panca Raharja
