# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3

# Создаем соединение с нашей базой данных
# В нашем примере у нас это просто файл базы
conn = sqlite3.connect('Chinook_Sqlite (1).sqlite')

# Создаем курсор - это специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

def query_artist(artist_name): #эта функция небезопасна
    query = f"SELECT * FROM artists WHERE Name = '{artist_name}'"
    return cursor.execute(query).fetchall()
def query_artist(artist_name): #эта функция безопасна
    query = "SELECT * FROM artists WHERE Name = ?"
    return cursor.execute(query, (artist_name,)).fetchall()

def find_user(username):
    query = f"SELECT * FROM users WHERE name = ?'"
    return cursor.execute(query, (username,)).fetchall()

def find_album(album_title):
    query = "SELECT * FROM albums WHERE title = ?"
    return cursor.execute(query, (album_title,)).fetchall()

def delete_record(record_id):
    query = f"DELETE FROM records WHERE id = ?"
    return cursor.execute(query, (record_id,)).fetchall()

#SQL- инъекция
def get_user_orders(user_id):
    query = f"SELECT * FROM Artist WHERE ArtistId = {user_id}"
    return cursor.execute(query).fetchall()

print(get_user_orders("5 UNION SELECT * FROM Artist"))
#с помощью UNION инъекции смогли получить данные всех артистов
#Оператор UNION позволяет извлечь данные из различных таблиц базы, выполняя дополнительные запросы SELECT
# и добавляя результаты в исходный запрос.

conn.close()