import csv
from pprint import pprint
from django.shortcuts import render
from django.conf import settings


class InflationData():

    def __init__(self, elem):
        self.year = int(elem['Год'])
        self.summ = elem['Суммарная']

        self.data = []
        for key in elem.keys():
            if elem[key] == '':
                elem[key] = 999
            else:
                elem[key] = float(elem[key])

        self.data.append(elem['Янв'])
        self.data.append(elem['Фев'])
        self.data.append(elem['Мар'])
        self.data.append(elem['Апр'])
        self.data.append(elem['Май'])
        self.data.append(elem['Июн'])
        self.data.append(elem['Июл'])
        self.data.append(elem['Авг'])
        self.data.append(elem['Сен'])
        self.data.append(elem['Окт'])
        self.data.append(elem['Ноя'])
        self.data.append(elem['Дек'])


def get_data(file_path):
    class_content = []

    with open(file_path, newline='\n', encoding='utf-8') as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=";")

        for elem in file_reader:
            class_content.append(InflationData(elem))

    return class_content


CONTENT = get_data(settings.INFLATION_RUSSIA_CSV)


def inflation_view(request):
    template_name = 'app/inflation.html'

    context = {"table": CONTENT}

    for elem in CONTENT:
        print(elem.year)
        print(elem.summ)
        print(elem.data)

    return render(request, template_name, context)

