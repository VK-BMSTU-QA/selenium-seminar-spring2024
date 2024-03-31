# selenium-seminar-spring2024



# Запуск тестов

## В файл creds.ymal ввести данные для авторизации
```yaml
username: 'username'
password: 'password'
```

Ввести следующие команды
```
    cd Selenium/code/
    pip install -r requirements.txt
    pytest test_login.py --url='https://park.vk.company/'
```
