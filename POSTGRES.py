import json
import os
import psycopg2
from REQUEST_CLASS import Emp, VAC


class POSTGRES:
    script_file = 'queries.sql'
    json_file_emp = 'Employers.json'
    json_file_vac = 'Vacancies.json'

    @staticmethod
    def config():
        """Возвращает параметры подключения к PostgresSQL"""
        return {
            'user': 'postgres',
            'password': '1703',
            'host': 'localhost',
            'port': '5432',
        }


    @staticmethod
    def create_database() -> None:
        """Создает новую базу данных."""
        params = POSTGRES.config()
        with psycopg2.connect(**params) as conn:
            conn.autocommit = True

            with conn.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE hh_emp;")
        conn.close()

    @staticmethod
    def add_info():
        """Создание таблиц """
        params = POSTGRES.config()
        with psycopg2.connect(**params, database="hh_emp") as conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                with open(POSTGRES.script_file, 'r') as file:
                    sql_statements = file.read()
                    queries = sql_statements.split(';')

                    for query in queries:
                        if query.strip():
                            cursor.execute(query)
        conn.close()

    @staticmethod
    def add_info_emp():
        """Заполняем таблицу employees данными"""
        if not os.path.isfile(POSTGRES.json_file_emp):
            Emp.get_info_employers()
            Emp.json_dump()
        else:
            params = POSTGRES.config()
            with psycopg2.connect(**params, database="hh_emp") as conn:
                conn.autocommit = True
                with conn.cursor() as cursor:
                    with open(POSTGRES.json_file_emp, 'r', encoding='utf-8') as file:
                        employees_data = json.load(file)

                        for employee in employees_data["items"]:
                            cursor.execute("INSERT INTO employees (employees_id, name_emp, url, open_vacancies) "
                                           "VALUES (%s, %s, %s, %s)",
                                           (employee["id"], employee["name"], employee["alternate_url"],
                                            employee["open_vacancies"])
                                           )
            conn.close()

    @staticmethod
    def add_info_vac():
        """Заполняем таблицу vacancies данными"""
        if not os.path.isfile(POSTGRES.json_file_vac):
            VAC.get_open_vacancies()
            VAC.json_dump()
        else:
            params = POSTGRES.config()
            with psycopg2.connect(**params, database="hh_emp") as conn:
                conn.autocommit = True
                with conn.cursor() as cursor:
                    with open(POSTGRES.json_file_vac, 'r', encoding='utf-8') as file:
                        vacancies_data = json.load(file)

                        for vac in vacancies_data["items"]:
                            # блок try-except для обработки ошибки возникающей при повторе ключа vac["id_emp"]
                            try:
                                cursor.execute("INSERT INTO vacancies ("
                                               "vac_id, name_vac, url, salary, employees_id) "
                                               "VALUES (%s, %s, %s, %s, %s) ",
                                               (vac["id"], vac["name"], vac["url"],
                                                vac["salary"], vac["id_emp"])
                                               )
                            except psycopg2.errors.UniqueViolation:
                                pass
            conn.close()
