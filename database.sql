CREATE DATABASE loker;

-- Language: sql
-- Path: database.sql

-- TABLE users

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

TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.users OWNER to postgres;

-- TABLE MASTER_LOKER

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

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.master_loker OWNER to postgres;

-- TABLE DETAIL_LOKER

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

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.detail_loker OWNER to postgres;