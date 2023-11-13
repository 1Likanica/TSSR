# БТ. Заказ от Федерации Спортивного Туризма России (ФСТР)
Когда турист поднимется на перевал, он сфотографирует его и внесёт нужную информацию с помощью мобильного приложения:
- координаты объекта и его высоту;
- название объекта;
- несколько фотографий;
- информацию о пользователе, который передал данные о перевале:
- имя пользователя (ФИО строкой);
- почта;
- телефон.
После этого турист нажмёт кнопку «Отправить» в мобильном приложении. Мобильное приложение вызовет метод submitData твоего REST API.

# Описание реализации.
В рамках данного проекта создана база данных, написаны классы по работе с БД и реализованы следующие методы для Rest API:
1. Метод POST submitData (http://127.0.0.1:8000/submitData/). <br>
Метод submitData принимает JSON в теле запроса с информацией о перевале. Предоставленный пример такого JSON-а:
```
{
    "beauty_title": "пер. ",
    "title": "Пхия",
    "other_titles": "Триев",
    "connect": "", // что соединяет, текстовое поле
 
    "add_time": "2021-09-22 13:18:13",
    "user": {
        "email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
            "name": "Василий",
            "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
    "coords":{
        "latitude": "45.3842",
        "longitude": "7.1525",
        "height": "1200"}

    //Категория трудности. В разное время года перевал может иметь разную категорию трудности
    level:{
        "winter": "", 
        "summer": "1А",
        "autumn": "1А",
        "spring": ""},
    
    images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
}
```
Результат метода: JSON
- **status** — код HTTP, целое число:
    - 500 — ошибка при выполнении операции;
    - 400 — Bad Request (при нехватке полей);
    - 200 — успех.
- **message** — строка:
    - Причина ошибки (если она была);
    - Отправлено успешно;
    - Если отправка успешна, дополнительно возвращается id вставленной записи.
- **id** — идентификатор, который был присвоен объекту при добавлении в базу данных.


*Примеры:*
- { "status": 500, "message": "Ошибка подключения к базе данных","id": null}
- { "status": 200, "message": null, "id": 42 }


*Выполенные в спринте-1 задачи:*
- Создание базы данных.
- Создание класса по работе с данными (добавление новых значений в таблицу перевалов).
- Написание REST API, вызывающего метод из класса по работе с данными.