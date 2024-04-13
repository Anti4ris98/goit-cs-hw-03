from faker import Faker
import psycopg2
import random

# З'єднання з базою даних PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1324",
    host="localhost"
)

# Створення курсора
cur = conn.cursor()

# Ініціалізація Faker
fake = Faker()

# Заповнення таблиці users
for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Отримання списку користувачів та статусів для використання при заповненні таблиці tasks
cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

# Заповнення таблиці tasks
for _ in range(20):
    title = fake.sentence()
    description = fake.text()
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

# Збереження змін у базі даних
conn.commit()

# Закриття курсора та з'єднання
cur.close()
conn.close()
