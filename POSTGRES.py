import psycopg2
import configparser
from config import config


class POSTGRES:
    script_file = 'queries.sql'
    json_file_emp = 'Employers.json'
    json_file_vac = 'Vacancies.json'
    db_name = 'HH_emp'

    @staticmethod
    def create_database() -> None:
        """Создает новую базу данных."""
        params = config()
        conn = psycopg2.connect(
            host=params['host'],
            user=params['user'],
            password=params['password'],
            port=params['port']
        )
        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {POSTGRES.db_name};")
            print(f"База данных '{POSTGRES.db_name}' успешно создана.")
