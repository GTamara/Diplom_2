# Diplom_2

## Установка зависимостей
pip install -r requirements.txt 

## Генерация отчета
pytest tests.py --alluredir=allure_results 
allure serve allure_results

## Актуализировать requirements.txt
pip freeze > requirements.txt 
