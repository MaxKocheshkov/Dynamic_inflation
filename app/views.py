from django.shortcuts import render
import csv
from app.settings import RUSSIAN_INFLATION_CSV


def inflation_view(request):
    template_name = 'inflation.html'
    headers = []
    rows = []
    with open(RUSSIAN_INFLATION_CSV, encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            headers.append(row.keys())
            rows.append(row.values())
    return render(request, template_name,
                  context={'headers': headers, 'columns': rows})
