from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до бази даних
client = MongoClient('localhost', 27017)
db = client['test']
collection = db['cats']

# Читання (Read)

# Функція для виведення всіх записів із колекції
def read_all():
    for document in collection.find():
        print(document)

# Функція для виведення інформації про кота за ім'ям
def read_by_name(name):
    document = collection.find_one({"name": name})
    if document:
        print(document)
    else:
        print("Кіт з ім'ям {} не знайдено".format(name))

# Оновлення (Update)

# Функція для оновлення віку кота за ім'ям
def update_age(name, new_age):
    result = collection.update_one(
        {"name": name},
        {"$set": {"age": new_age}}
    )
    if result.modified_count == 0:
        print("Кіт з ім'ям {} не знайдено".format(name))

# Функція для додавання нової характеристики до списку features кота за ім'ям
def add_feature(name, new_feature):
    result = collection.update_one(
        {"name": name},
        {"$push": {"features": new_feature}}
    )
    if result.modified_count == 0:
        print("Кіт з ім'ям {} не знайдено".format(name))

# Видалення (Delete)

# Функція для видалення запису з колекції за ім'ям тварини
def delete_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count == 0:
        print("Кіт з ім'ям {} не знайдено".format(name))

# Функція для видалення всіх записів із колекції
def delete_all():
    result = collection.delete_many({})
    print("{} записів видалено".format(result.deleted_count))
