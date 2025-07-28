
DROP DATABASE IF EXISTS kddDividendos;
CREATE DATABASE kddDividendos;
USE kddDividendos;


-- Tabla para los datos crudos obtenidos de la API:
CREATE TABLE dividendos_raw (
	symbol TEXT,
    ex_dividend_date TEXT,
    declaration_date TEXT,
    record_date TEXT,
    payment_date TEXT,
    amount REAL
);


-- Tabla para los datos transformados:
CREATE TABLE dividendos_transformados (
	symbol TEXT,
    ano INTEGER,
    dividend_avg REAL,
    dividend_growth REAL,
    dividend_yield REAL,
    payout_ratio REAL
);









