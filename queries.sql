CREATE TABLE employees (
    employees_id INT PRIMARY KEY,
    name_emp VARCHAR(100) NOT NULL,
    url VARCHAR(100) NOT NULL,
    open_vacancies INT NOT NULL
);
CREATE TABLE vacancies (
    vac_id INT PRIMARY KEY,
    name_vac VARCHAR(100) NOT NULL,
    url VARCHAR(100) NOT NULL,
    salary INT NOT NULL,
    employees_id INT,
    FOREIGN KEY (employees_id) REFERENCES employees(employees_id)
);
