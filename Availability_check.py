import psycopg2
import config


class Availability:
    params = config

    @staticmethod
    def database_exists(database_name="hh_emp"):
        """Проверка на наличие БД"""
        with psycopg2.connect(Availability.config()) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT datname FROM pg_database WHERE datname = %s;", (database_name,))
                return cursor.fetchone() is not None
        conn.close()

    @staticmethod
    def data_in_table(table_name):
        """Проверка на наличие данных в таблицах """
        with psycopg2.connect(Availability.config()) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
                return conn.fetchone()[0] > 0
        conn.close()
