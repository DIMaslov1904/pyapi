# backend/seed_data.py
"""
Скрипт для заполнения базы данных тестовыми данными.
Создает пользователей для демонстрации работы приложения.
"""

from src.database import SessionLocal, init_db
from src.users.models import User


def create_users(db):
    """
    Создает пользователей.

    Args:
        db: Сессия SQLAlchemy

    Returns:
        dict: Словарь созданных пользователей list['username']
    """

    users_data = [
        {"username": "DIMaslov", "email": "dimaslov@gmail.com", "password": 123456, "name": "Dima", "last_name": "Maslov"},
        {"username": "admin", "email": "admin@gmail.com", "password": 123456, "name": "Admin", "last_name": "Admin"},
    ]

    categories_data = [
        {"name": "Electronics", "slug": "electronics"},
        {"name": "Fashion", "slug": "fashion"},
        {"name": "Clothing", "slug": "clothing"},
        {"name": "Books", "slug": "books"},
        {"name": "Home & Garden", "slug": "home-garden"},
    ]

    new_users = []
    for user in users_data:
        new_user = User(**user)
        db.add(new_user)
        new_users.append(new_user)

    db.commit()

    # Обновляем объекты после commit для получения ID
    for user in new_users:
        db.refresh(user)

    return new_users


def seed_database():
    """
    Главная функция для заполнения базы данных.
    Создает таблицы, категории и товары.
    """
    print("🚀 Начало заполнения базы данных...")

    # Инициализируем БД (создаем таблицы)
    init_db()
    print("✅ Созданные таблицы базы данных")

    # Создаем сессию
    db = SessionLocal()

    try:
        # Проверяем, не заполнена ли уже БД
        existing_users = db.query(User).count()
        if existing_users > 0:
            print("⚠️ База данных уже содержит данные. Пропускаем начальное значение.")
            return

        # Создаем пользователей
        print("📁 Создание пользователей...")
        users = create_users(db)
        print(f"✅ Создано {len(users)} пользователей")

        print("🎉 Заполнение базы данных завершено успешно!")

    except Exception as e:
        print(f"❌ Ошибка при заполнении: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()