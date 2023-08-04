--- установка параметров для текущей сессии
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET default_tablespace = '';

SET default_with_oids = false;

--- удаляем таблицы, если они существуют
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS vacancies;

--- создаем таблицы со столбцами
--- таблица employees
CREATE TABLE employees (
    employees_id INT PRIMARY KEY,
    name_emp VARCHAR(100) NOT NULL,
    url VARCHAR(100) NOT NULL,
    open_vacancies INT NOT NULL
);
--- таблица  vacancies
CREATE TABLE vacancies (
    vac_id INT PRIMARY KEY,
    name_vac VARCHAR(100) NOT NULL,
    url VARCHAR(100) NOT NULL,
    salary INT NOT NULL,
    employees_id INT,
    FOREIGN KEY (employees_id) REFERENCES employees(employees_id)
)
