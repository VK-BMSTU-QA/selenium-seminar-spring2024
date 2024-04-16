### Дима Белозеров

---
### Креды

Перед запуском тестов необходимо внести свои креды в `.env` файл.

### Запуск

Необходимо перейти в нужную директорию:

```cd Selenium/code```

Установить зависимости:

```pip install -r requirements.txt```

Команда для запуска тестов через Chrome:

```pytest test_login.py --browser='chrome' --url='https://park.vk.company/'```
