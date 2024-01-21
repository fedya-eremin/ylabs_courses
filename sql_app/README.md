# YLABS HW1

Первая домашняя работа для интенсивов YLABS

## Инструкция по запуску на Linux (использовался Arch Linux)
1. По необходимости надо инициализировать кластер Postgres. Это делается командой:
    
    ```bash
    su - postgres -c "initdb -D '/var/lib/postgres/data'"
    ```

2. Далее необходимо от пользователя postgres (```su - postgres```) выполнить команды ```createdb <имя базы>``` и ```createuser --interactive```. Локально и пользователь, и база были созданы с именем ylabs.

3. Запуск

   3.1 Для запуска сервера Postgres использовалась команда
   ```bash
   su - postgres -c "pg_ctl -D /var/lib/postgres/data start"
   ```
   В других дистрибутивах pg_ctl может заменять pg_ctlcluster с соответсвующими аргументами.

   3.2 Для установки python зависимостей необходимо использовать: 
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   3.3 Секретные данные (DB_NAME, DB_USER, DB_PASSWORD и DB_HOST (вместе с портом)) необходимо разместить в файле .env в директории sql_app

   3.4 Для запуска api-сервера необходимо использовать команду
   ```bash
    uvicorn sql_app.main:app --reload
   ```

## Результат прохождения тестов (так же в папке postman_results):
