# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

### Установка скрипта

1. Скачайте репозиторий
2. Установите библиотеки командой
```commandline
pip install -r requirements.txt
```

### Запуск
1. Проделать шаги по установке
2. Запустите сайт командой
```commandline
python main.py
```
3. Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
4. Сайт должен выглядеть так:
![img.png](instruction_images/img.png)

### Работа с сайтом
Сайт заполняется позициями согласно Excel таблице.
В репозитории есть шаблонный excel файл `wine.xlsx`.\
Чтоб добавить новые продукты необходимо изменить этот файл или создать по его образцу новый и указать при вызове программы путь до него следующим образом:
```commandline
python main.py --path C:\Users\1\Desktop\your_file.xlsx
```
## Цели проекта

Код написан в учебных целях.
