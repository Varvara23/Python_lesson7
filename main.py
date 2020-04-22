import datetime
from docxtpl import DocxTemplate
import csv
import json
import time


def read_data(file_name):
    dict_k = {}
    f = open(file_name)
    list_data = f.read().split('\n')
    for line in list_data:
        key = line.split(':')[0]
        value = line.split(':')[1]
        dict_k[key] = value
    f.close()
    return dict_k


# 3) Автоматически сгенерировать отчет о машине в формате doc
def from_template(file_data, template):
    template = DocxTemplate(template)
    context = read_data(file_data)
    template.render(context)
    template.save('report_' + str(datetime.datetime.now().date()) + '.docx')


start_time = time.time()
from_template('auto.txt','report.docx')
end_time = time.time()
print("Время, затраченное на генерацию отчета docx: {} секунд".format(end_time-start_time))


# 4) Создать csv файл с данными о машине
def generate_csv(file_data, file_csv):
    dict_data = read_data(file_data)
    fieldnames = list(dict_data.keys())

    with open(file_csv, 'w') as f:
        writer = csv.DictWriter(f,delimiter='$',fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(dict_data)


start_time = time.time()
generate_csv('auto.txt','auto.csv')
end_time = time.time()
print("Время, затраченное на генерацию отчета csv: {} секунд".format(end_time-start_time))


# 5) Создать json файл с данными о машине
def generate_json(file_data, file_json):
    with open(file_json, 'w') as f:
        dict_data = read_data(file_data)
        json.dump(dict_data, f)


start_time = time.time()
generate_json('auto.txt','auto.json')
end_time = time.time()
print("Время, затраченное на генерацию отчета json: {} секунд".format(end_time-start_time))