import sqlite3

# Создание класса для представления альбома
class Album:
    def __init__(self, album_id, title, artist_id):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    def __repr__(self):
        return f"Album(id={self.album_id}, title='{self.title}', artist_id={self.artist_id})"

# Функция для подключения к базе данных
def get_connection(db_file):
    return sqlite3.connect(db_file)

# CRUD операции для альбомов

# 1. Создание (Create)
def create_album(connection, title, artist_id):
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Album (Title, ArtistId) VALUES (?,?)""", (title, artist_id))
    cursor.fetchall()

# 2. Чтение (Read)
def read_albums(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM Album""")
    reads = cursor.fetchall()
    for read in reads:
        print(read)

# 3. Обновление (Update)
def update_album(connection, album_id, new_title):
    cursor = connection.cursor()
    cursor.execute("""UPDATE Album SET Title=? WHERE AlbumId=?""", (new_title,album_id))

# 4. Удаление (Delete)
def delete_album(connection, album_id):
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM Album WHERE AlbumId = ?""", album_id)
    cursor.fetchall()

