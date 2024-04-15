# Урок 2. Работа с моделями
## Задание
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию. 


запуск:
cd django_projects
    Set-ExecutionPolicy Unrestricted -Scope Process
    .venv\Scripts\activate.ps1 
cd project1   
    python manage.py runserver
    python manage.py migrate  

    python manage.py customer_create aaa sss@cvc.com +79898098 fsdfsdf  
    python manage.py product_create название описание 4567.89 124       
    python manage.py fakeData 10 5 20
    manage.py order_create 4 4 5 1






