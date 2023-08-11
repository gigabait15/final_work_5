import configparser


def config(filename='config.ini', section='postgresql'):
    """Чтение параметров подключения из .ini файла"""
    parser = configparser.ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        params = parser.items(section)
        return dict(params)
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

