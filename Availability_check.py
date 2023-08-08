import psycopg2


class Availability:

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
    def database_exists(database_name="hh_emp"):
        """Проверка на наличие БД"""
        params = Availability.config()
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT datname FROM pg_database WHERE datname = %s;", (database_name,))
                return cursor.fetchone() is not None

    @staticmethod
    def data_in_table(table_name):
        """Проверка на наличие данных в таблицах """
        params = Availability.config()
        with psycopg2.connect(**params) as conn:
            conn.execute(f"SELECT COUNT(*) FROM {table_name};")
            return conn.fetchone()[0] > 0