### API тесты

## Установка зависимостей
pip install -r requirements.txt 

## Запуск тестов
pytest tests

## Генерация отчета
pytest tests --alluredir=allure_results 
allure serve allure_results

## Актуализировать requirements.txt
pip freeze > requirements.txt 
