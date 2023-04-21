from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def define_the_ending(num):
    last_digit = num % 10
    last_2_digits = num % 100
    if 10 < last_2_digits < 20 or 4 < last_digit < 10 or last_digit == 0:
        ending = 'лет'
    elif 1 < last_digit < 5:
        ending = 'года'
    else:
        ending = 'год'
    return ending


def count_years_of_work():
    import datetime
    present_year = datetime.date.today().year
    opening_year = 1920
    years_of_work = present_year - opening_year
    return years_of_work


def read_excel():
    import pandas
    import collections
    wines_inf = pandas.read_excel('wine.xlsx')\
        .fillna("")\
        .to_dict(orient='records')
    categories = collections.defaultdict(list)
    for wine in wines_inf:
        categories[wine['Категория']].append(wine)
    return categories


def update_years_of_work():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    years_of_work = count_years_of_work()
    wines_inf = read_excel()

    rendered_page = template.render(
        wines_inf=wines_inf,
        years_of_work=f'{years_of_work} {define_the_ending(years_of_work)}'
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


update_years_of_work()

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
