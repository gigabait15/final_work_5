import psycopg2
from POSTGRES import POSTGRES
import config


class DBManager:
    params = config

    @staticmethod
    def get_companies_and_vacancies_count():
        """Получает список всех компаний и
        количество вакансий у каждой компании."""
        with psycopg2.connect(DBManager.config(), database="hh_emp") as conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                query = """
                            SELECT name_emp, open_vacancies FROM employees
                            """
                cursor.execute(query)
                for item in cursor.fetchall():
                    print(f"название компании: {item[0]} \nколичество вакансий у компании - {item[1]}\n")
        conn.close()

    @staticmethod
    def get_all_vacancies():
        """Получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию."""
        with psycopg2.connect(DBManager.config(), database="hh_emp") as conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                query = """
                            SELECT employees.name_emp, vacancies.name_vac,
                            vacancies.salary, vacancies.url FROM vacancies 
                            INNER JOIN employees ON employees.employees_id = vacancies.employees_id
                            """
                cursor.execute(query)
                for item in cursor.fetchall():
                    print(f"Название компании : {item[0]}\nНазвание вакансии : {item[1]}\n"
                          f"Заработная плата - {item[2]} руб.\nссылка на вакансию :{item[3]}\n")
        conn.close()

    @staticmethod
    def get_avg_salary():
        """Получает среднюю зарплату по вакансиям."""
        with psycopg2.connect(DBManager.config(), database="hh_emp") as conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                query = """
                            SELECT AVG(salary) as average_salary FROM vacancies
                            """
                cursor.execute(query)
                result = cursor.fetchone()
                average_salary = int(result[0])
                print(f"Средняя зарплата: {average_salary} руб.")
        conn.close()

    @staticmethod
    def get_vacancies_with_higher_salary():
        """Получает список всех вакансий,
        у которых зарплата выше средней по всем вакансиям."""
        with psycopg2.connect(DBManager.config(), database="hh_emp") as conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                subquery = """
                                SELECT AVG(salary) as average_salary
                                FROM vacancies
                                """
                cursor.execute(subquery)
                result = cursor.fetchone()
                average_salary = int(result[0])

                query = """
                            SELECT vac_id, name_vac, url, salary
                            FROM vacancies
                            WHERE salary > %s
                            """
                cursor.execute(query, (average_salary,))
                results = cursor.fetchall()
                print(f"Список вакансий у которых зарплата выше {average_salary} руб.\n")
                for item in results:
                    print(f"Название вакансии: {item[1]}\nЗарплата- {item[3]}руб.\nссылка на вакансию: {item[2]}\n")
        conn.close()

    @staticmethod
    def get_vacancies_with_keyword():
        """Получает список всех вакансий,
        в названии которых содержатся переданные в метод слова, например “python”. """
        user_input = input("Введите название вакансии:")
        print()

        with psycopg2.connect(DBManager.config(), database="hh_emp") as conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                query = """
                                    SELECT vac_id, name_vac, url, salary
                                    FROM vacancies
                                    WHERE name_vac LIKE %s
                                    """
                search_keyword = f"%{user_input}%"
                cursor.execute(query, (search_keyword,))
                results = cursor.fetchall()
                print(f"Все вакансии по запросу - {user_input}\n")
                for item in results:
                    print(f"Название вакансии: {item[1]}\nСсылка на вакансию: "
                          f"{item[2]}\nЗарплата- {item[3]}руб.\n")

        conn.close()
