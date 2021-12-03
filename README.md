# download-photos-
Программа скачивает фоторгафии с сайтов SpaceX и Nasa и размещает их в телеграм канале с заданным интервалом.

### Как установить

Для корректной работы необходимо создать файл .env со следующими данными:
```
TOKEN=токен_api_nasa
TG_TOKEN=токен_телеграм_бота
sleep=86400
chat_id=ссылка_на_канал_тг
```
где:
 TOKEN - ваш токен api с сайта наса, который необходимо получить на странице https://api.nasa.gov/ .  
 TG_TOKEN - токен телеграм бота, который выдаст BotFather при создании бота.  
 sleep - задержка между публикациями постов в телеграм канале в секундах, по умолчанию - сутки.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Запуск

```
C:\progect>python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
