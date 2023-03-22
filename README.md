# QA GURU Python 4 поток
### Задание 9



## Как запустить проект на Windows:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/wombatoff/qa_guru_python_4_9
cd qa_guru_python_4_9
```

Если не установлен ALLURE, то установить:

- Если не установлена Java - установить
- Отсюда https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/ забираем последнюю версию
- Пример2.20.1: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.20.1/
- Разархивируем в корень проекта, получаем папку allure-<номер версии>
- Переименовываем для удобства папку allure-<номер версии> в allure
- Запускать отчет можно из корня проекта командой (если папка с результатами в allure-result и она в корне проекта):
```
allure/bin/allure.bat serve
```


Создать и активировать виртуальное окружение:

```
python -m venv venv
source venv/Scripts/activate
```


Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Запуск теста

```
pytest
```


---

## Технологии проекта

- Python