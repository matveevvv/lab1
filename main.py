import pandas as pd
import os
import sys
import urllib.request
def download_file(url_file, filename):
    directoria = os.getcwd()  # Получаем текущий рабочий каталог
    pyt = os.path.join(directoria, filename)

    if not os.path.exists(pyt):
        # Файл не существует, скачиваем его
        urllib.request.urlretrieve(url_file, pyt)
        print(f'Файл успешно скачан: {pyt}')
    else:
        # Файл уже существует
        print(f'Файл уже существует: {pyt}')

filename = 'lab_pi_101.xlsx'
url_file = 'https://drive.google.com/uc?export=download&id=1Bo5Oili5dAvWDSzAZXjzgjS71IrmLWun'
download_file(url_file, filename)
dataframe = pd.read_excel(filename)
all_groups = dataframe['Группа'].unique()
print('Доступные группы:')
for gruppa in all_groups:
    print(gruppa)
vibor = input('Введите название группы ')
if vibor not in dataframe['Группа'].values:
    print(f'Ошибка: Группа с названием "{vibor}" не найдена.')
    sys.exit(1)
grupa = dataframe['Группа'] == vibor
marks = dataframe['Оценка'].count()
marks_grupa = dataframe['Группа'] == vibor
kolvo_marks_grupa=dataframe[marks_grupa]['Оценка'].count()
students_grupa = dataframe[marks_grupa]['Личный номер студента'].unique()
formi_control = dataframe[marks_grupa]['Уровень контроля'].unique()
Years = sorted(dataframe['Год'].unique())
print('В исходном датасете содержалось', marks, 'оценок, из них', kolvo_marks_grupa, 'оценок относятся к группе', vibor ,'\n В датасете находятся оценки', len(students_grupa), 'студентов со следующими личными номерами:', ', '.join(map(str,students_grupa)),'\n Используемые формы контроля:',', '.join(map(str,formi_control)),'\n Данные представлены по следующим учебным годам:',', '.join(map(str,Years)))
