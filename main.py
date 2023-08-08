from User_work import User_work as ur
from POSTGRES import POSTGRES as pos
from Availability_check import Availability as av


if __name__ == "__main__":
    table_name = ["employees", "vacancies"]
    if av.database_exists():
        pass
    else:
        pos.create_database()
        pos.add_info()

    if av.data_in_table(table_name[0]):
        pass
    else:
        pos.add_info_emp()
    if av.data_in_table(table_name[1]):
        pass
    else:
        pos.add_info_vac()
    ur.run()
