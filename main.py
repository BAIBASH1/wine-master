from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import collections
import datetime
import argparse


def define_the_ending(num):
    last_digit = num % 10
    last_2_digits = num % 100
    if 10 < last_2_digits < 20 or 4 < last_digit < 10 or not last_digit:
        ending = 'лет'
    elif 1 < last_digit < 5:
        ending = 'года'
    else:
        ending = 'год'
    return ending


def count_years_of_work():
    present_year = datetime.date.today().year
    opening_year = 1920
    years_of_work = present_year - opening_year
    return years_of_work


def read_excel(path):
    wines = pandas.read_excel(path)\
        .fillna("")\
        .to_dict(orient='records')
    categories = collections.defaultdict(list)
    for wine in wines:
        categories[wine['Категория']].append(wine)
    return categories


def update_index_html(path):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    years_of_work = count_years_of_work()
    categories_of_wine = read_excel(path)

    rendered_page = template.render(
        categories_of_wine=categories_of_wine,
        years_of_work=f'{years_of_work} {define_the_ending(years_of_work)}'
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    parser = argparse.ArgumentParser(
        description='Программа согласно данным обновляет'
                    ' файл "index.html" (если нет, создает) .'
    )
    parser.add_argument(
        '--path',
        default='wine.xlsx',
        help='Укажите путь до файла excell с информацией о продуктах.'
             ' Если не указать, программа дефолтно возьмет информацию'
             ' из файла wine.xlsx, который лежит'
             ' в одной директории с основым кодом.'
    )
    args = parser.parse_args()
    update_index_html(args.path)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
