
# Тесты на проверку параметра Name при создании нового набора в Яндекс.Прилавок с помощью API Яндекс.Прилавок.

-   Для запуска тестов должны быть установлены пакеты pytest и requests
-   Запуск всех тестов выполянется командой pytest
-   Все URL запросов хранятся в файле configuration.py
-   Все тела запросов хранятся в файле data.py
-   Все вспомогательные запросы для прохождения автотестов хранятся в файле sender_stand_request.py
-   Все автотесты хранятся в файле create_kit_name_kit_test.py

## Результаты тестов
|test|test type| Objective|Result|
|-----|-----|-----------------|-----------------------------|
|1|positive| 1 letter  |Passed |
|2|positive| 511 letters |Passed |
|3|negative| no letters |FAILED|
|4|negative| 512 letters |FAILED|
|5|positive| EN letters |Passed |
|6|positive| RU letters |Passed |
|7|positive| spec symbols |Passed |
|8|positive| space allowed |Passed |
|9|positive| numbers allowed |Passed |
|10|negative| no name |FAILED|
|11|negative| wrong parameter |FAILED|



