# vk-extract-phones-from-group-conversations
Скрипт, с помощью которого владельцы сообществ смогут собрать ФИ людей, которые писали в ЛС сообщества, а так же 
номера телефонов, которые они оставили в сообщениях.

## Установка и использование

Для запуска скрипта необходимо установить poetry.  
Как использовать:
1. Добавляем API ключ в переменную окружения VK_API_TOKEN `export VK_API_TOKEN={TOKEN}`
2. Запускаем скрипт через poetry `poetry run extract-phones`
3. После успешного завершения в директории проекта появится файл report.csv

## Особенности работы, которые нужно учитывать

* Скрипт кэширует все ответы от VK, складывает их в директорию cache в корне проекта. Следует изучить этот механизм перед 
использованием.
* В ТЗ было требование приводить все номера к формату 79999999999. Если вам это не нужно, следует избавиться от этого механизма.


