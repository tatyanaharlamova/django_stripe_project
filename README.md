# 🛒 **ПРОЕКТ DJANGO-STRIPE**

Этот проект представляет собой бэкенд на Django с интеграцией Stripe API для обработки платежей. 
Проект включает в себя:

- **Модель Item** для хранения информации о товарах.
- **API** для создания платежных сессий Stripe.
- **Простую HTML-страницу** для отображения информации о товаре и кнопки "Buy".
- **Поддержку Docker и PostgreSQL**.

---

## 🚀 **Установка и запуск**

*Клонирование репозитория*:
```bash
git clone git@github.com:tatyanaharlamova/django_stripe_project.git
cd django_stripe_project

*Установка переменных окружения*:

Переименуйте файл .env.sample в .env, внесите свои переременные

*Запуск Docker*:
```bash
docker-compose up --build

*Примените миграции*:
```bash
docker-compose exec web python manage.py migrate

*Для доступа в админ-панель создайте суперпользователя*:
```bash
docker-compose exec web python manage.py createsuperuser

*Откройте браузер и перейдите по адресу*:

Главная страница: http://localhost:8000/
Админка: http://localhost:8000/admin/
