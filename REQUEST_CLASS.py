import json
import requests


class Emp:
    Llist = []

    @staticmethod
    def get_info_employers():
        """
        Функция для подключения к api.hh.ru и получения данных о работодателях
        """
        count = 0
        while True:
            response = requests.get(f'https://api.hh.ru/employers?page={count}').json()
            items = response.get("items", [])

            if not items:
                break

            for item in items:
                if item['open_vacancies'] >= 10:
                    info = dict(id=item['id'], name=item['name'], alternate_url=item['alternate_url'],
                                open_vacancies=item['open_vacancies'])
                    if len(Emp.Llist) >= 10:
                        break
                    else:
                        Emp.Llist.append(info)
            count += 1

    @staticmethod
    def json_dump(item=None):
        """
        Функция для сохранения полученных данных в json формате
        """
        if item is None:
            item = Emp.Llist
        with open(f'Employers.json', 'w', encoding="utf-8") as file:
            json.dump({"items": item}, file, ensure_ascii=False, indent=2)


class VAC:
    Llist = []

    @staticmethod
    def open_emp():
        """
        Функция для открытия json файла с данными о работодателях
        """
        with open('Employers.json', 'r', encoding="utf-8") as file:
            f = json.load(file)
            return f

    @staticmethod
    def get_open_vacancies():
        """
        Функция для подключения к api.hh.ru и получения данных о вакансиях от работодателей
        """
        data = VAC.open_emp()
        for index, item in enumerate(data['items']):
            employer_id = item['id']

            while index < 10:
                response = requests.get(f"https://api.hh.ru/vacancies/?employer_id={employer_id}").json()
                items = response.get("items", [])

                if not items:
                    break

                for item in items:
                    info = dict(id_emp=employer_id, id=item['id'], name=item['name'],
                                url=item['alternate_url'], salary_from=item['salary']['from'],
                                salary_to=item['salary']['to'], currency=item['salary']['currency'])

                    VAC.Llist.append(info)
        return VAC.Llist

    @staticmethod
    def json_dump(item=None):
        """
        Функция для сохранения полученных данных в json формате
        """
        if item is None:
            item = VAC.Llist
        with open(f'Vacancies.json', 'w', encoding="utf-8") as file:
            json.dump({"items": item}, file, ensure_ascii=False, indent=2)





