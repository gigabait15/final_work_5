from DBManager import DBManager as dbm


class User_work:
    @staticmethod
    def display_menu():
        """Функция выбора пользователем дальнейших действий"""
        print("=== Меню просмотра ===")
        print("1. Получить список всех компаний и "
              "количество вакансий у каждой компании")
        print("2. Получить список всех вакансий с указанием названия компании,"
              "названия вакансии и зарплаты и ссылки на вакансию")
        print("3. Получить среднюю зарплату по вакансиям")
        print("4. Получить список всех вакансий, "
              "у которых зарплата выше средней по всем вакансиям")
        print("5. Получить список всех вакансий, "
              "в названии которых содержатся переданные слова")
        print("0. Выход")

    @staticmethod
    def run():
        while True:
            User_work.display_menu()
            choice = int(input("Введите ваш выбор: "))

            if choice == 0:
                print("Выход...")
                break

            elif choice == 1:
                print("Список компаний и количество вакансий у каждой")
                dbm.get_companies_and_vacancies_count()

            elif choice == 2:
                print("Список компаний и данные вакансий у данных компаний")
                dbm.get_all_vacancies()

            elif choice == 3:
                dbm.get_avg_salary()

            elif choice == 4:
                dbm.get_vacancies_with_higher_salary()

            elif choice == 5:
                dbm.get_vacancies_with_keyword()
